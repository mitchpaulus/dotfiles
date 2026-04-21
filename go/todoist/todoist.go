package main

// Simple CLI for Todoist

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"sort"
	"strings"
)

// Example task object:
/* { */
/* "creator_id": "2671355", */
/* "created_at": "2019-12-11T22:36:50.000000Z", */
/* "assignee_id": "2671362", */
/* "assigner_id": "2671355", */
/* "comment_count": 10, */
/* "is_completed": false, */
/* "content": "Buy Milk", */
/* "description": "", */
/* "due": { */
/* "date": "2016-09-01", */
/* "is_recurring": false, */
/* "datetime": "2016-09-01T12:00:00.000000Z", */
/* "string": "tomorrow at 12", */
/* "timezone": "Europe/Moscow" */
/* }, */
/* "duration": { */
/* "amount": 15, */
/* "unit": "minute" */
/* }, */
/* "id": "2995104339", */
/* "labels": ["Food", "Shopping"], */
/* "order": 1, */
/* "priority": 1, */
/* "project_id": "2203306141", */
/* "section_id": "7025", */
/* "parent_id": "2995104589", */
/* "url": "https://todoist.com/showTask?id=2995104339" */
/* } */

type Task struct {
	UserId         string   `json:"user_id"`
	Id             string   `json:"id"`
	ProjectId      string   `json:"project_id"`
	SectionId      string   `json:"section_id"`
	ParentId       string   `json:"parent_id"`
	AddedByUid     string   `json:"added_by_uid"`
	AssignedByUid  string   `json:"assigned_by_uid"`
	ResponsibleUid string   `json:"responsible_uid"`
	Labels         []string `json:"labels"`
	IsCollapsed    bool     `json:"is_collapsed"`
	Checked        bool     `json:"checked"`
	IsDeleted      bool     `json:"is_deleted"`
	AddedAt        string   `json:"added_at"`
	CompletedAt    string   `json:"completed_at"`
	CompletedByUid string   `json:"completed_by_uid"`
	UpdatedAt      string   `json:"updated_at"`
	Priority       int      `json:"priority"`
	ChildOrder     int      `json:"child_order"`
	Content        string   `json:"content"`
	Description    string   `json:"description"`
	NoteCount      int      `json:"note_count"`
	DayOrder       int      `json:"day_order"`
	GoalIds        []string `json:"goal_ids"`
}

type TaskPage struct {
	Results    []Task  `json:"results"`
	NextCursor *string `json:"next_cursor"`
}

type Project struct {
	Id         string `json:"id"`
	ChildOrder int    `json:"child_order"`
	Name       string `json:"name"`
	ParentId   string `json:"parent_id"`
	IsArchived bool   `json:"is_archived"`
	IsDeleted  bool   `json:"is_deleted"`
	Inbox      bool   `json:"inbox_project"`
}

type ProjectPage struct {
	Results    []Project `json:"results"`
	NextCursor *string   `json:"next_cursor"`
}

func main() {
	// Loop through arguments like while, looking for -h or --help
	var index int = 1

	command := "list"
	var description string

	for index < len(os.Args) {
		if os.Args[index] == "-h" || os.Args[index] == "--help" {
			fmt.Println("Usage: todoist")
			fmt.Println("       todoist projects")
			fmt.Println("       todoist add <DESCRIPTION>")
			os.Exit(0)
		} else if os.Args[index] == "add" || os.Args[index] == "a" {
			command = "add"

			// Get the next arguments as the description for the task, space separated
			// If the description is not provided, print an error message and exit
			if index+1 >= len(os.Args) {
				fmt.Fprint(os.Stderr, "Description required for add command.\n")
				os.Exit(1)
			} else {
				descriptionItems := os.Args[index+1:]
				// Join the description items with a space
				description = strings.Join(descriptionItems, " ")
			}
		} else if os.Args[index] == "projects" || os.Args[index] == "p" {
			command = "projects"
		}

		index++
	}

	// First check for TODOIST_TOKEN environment variable
	token, exists := os.LookupEnv("TODOIST_TOKEN")

	if !exists {
		// Print to stderr
		fmt.Fprint(os.Stderr, "TODOIST_TOKEN environment variable not set.\n")
		os.Exit(1)
	}

	if command == "list" {
		list(token)
	} else if command == "projects" {
		projects(token)
	} else if command == "add" {
		add(token, description)
	} else {
		// Should never reach here, print what invalid command was used
		fmt.Fprint(os.Stderr, "Invalid command: ", command, "\n")
	}
}

func list(token string) {
	tasks, err := fetchAllTasks(token)
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}

	// Print tasks that match project_id 2315202256
	// print content, project_id, and labels, tab separated
	// Order by child order (ascending)
	sort.Slice(tasks, func(i, j int) bool {
		if tasks[i].ChildOrder == tasks[j].ChildOrder {
			return tasks[i].Content < tasks[j].Content
		}
		return tasks[i].ChildOrder < tasks[j].ChildOrder
	})

	for _, task := range tasks {
		if task.ProjectId == "2315202256" {
			fmt.Printf("%s\t%s\n", task.Content, strings.Join(task.Labels, ","))
		}
	}
}

func fetchAllTasks(token string) ([]Task, error) {
	client := &http.Client{}
	tasks := make([]Task, 0)
	cursor := ""

	for {
		page, err := fetchTaskPage(client, token, cursor)
		if err != nil {
			return nil, err
		}

		tasks = append(tasks, page.Results...)

		if page.NextCursor == nil || *page.NextCursor == "" {
			break
		}

		cursor = *page.NextCursor
	}

	return tasks, nil
}

func fetchTaskPage(client *http.Client, token string, cursor string) (*TaskPage, error) {
	endpoint, err := url.Parse("https://api.todoist.com/api/v1/tasks")
	if err != nil {
		return nil, err
	}

	query := endpoint.Query()
	query.Set("limit", "200")
	if cursor != "" {
		query.Set("cursor", cursor)
	}
	endpoint.RawQuery = query.Encode()

	req, err := http.NewRequest(http.MethodGet, endpoint.String(), nil)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Authorization", "Bearer "+token)

	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("todoist tasks request failed: %s: %s", resp.Status, strings.TrimSpace(string(body)))
	}

	var page TaskPage
	if err := json.Unmarshal(body, &page); err != nil {
		return nil, err
	}

	return &page, nil
}

func projects(token string) {
	projects, err := fetchAllProjects(token)
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}

	sort.Slice(projects, func(i, j int) bool {
		if projects[i].ChildOrder == projects[j].ChildOrder {
			return projects[i].Name < projects[j].Name
		}
		return projects[i].ChildOrder < projects[j].ChildOrder
	})

	for _, project := range projects {
		if project.IsArchived || project.IsDeleted {
			continue
		}
		fmt.Printf("%s\t%s\n", project.Id, project.Name)
	}
}

func fetchAllProjects(token string) ([]Project, error) {
	client := &http.Client{}
	projects := make([]Project, 0)
	cursor := ""

	for {
		page, err := fetchProjectPage(client, token, cursor)
		if err != nil {
			return nil, err
		}

		projects = append(projects, page.Results...)

		if page.NextCursor == nil || *page.NextCursor == "" {
			break
		}

		cursor = *page.NextCursor
	}

	return projects, nil
}

func fetchProjectPage(client *http.Client, token string, cursor string) (*ProjectPage, error) {
	endpoint, err := url.Parse("https://api.todoist.com/api/v1/projects")
	if err != nil {
		return nil, err
	}

	query := endpoint.Query()
	query.Set("limit", "200")
	if cursor != "" {
		query.Set("cursor", cursor)
	}
	endpoint.RawQuery = query.Encode()

	req, err := http.NewRequest(http.MethodGet, endpoint.String(), nil)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Authorization", "Bearer "+token)

	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("todoist projects request failed: %s: %s", resp.Status, strings.TrimSpace(string(body)))
	}

	var page ProjectPage
	if err := json.Unmarshal(body, &page); err != nil {
		return nil, err
	}

	return &page, nil
}

func add(token string, description string) {
	// Add a task with the description provided
	// Example:
	// $ curl "https://api.todoist.com/api/v1/tasks" \
	// -X POST \
	// --data '{"content": "Buy Milk", "project_id": "6XGgm6PHrGgMpCFX"}' \
	// -H "Content-Type: application/json" \
	// -H "X-Request-Id: $(uuidgen)" \
	// -H "Authorization: Bearer $token"

	url := "https://api.todoist.com/api/v1/tasks"

	// Create a map with the task description
	task := map[string]string{
		"content":    description,
		"project_id": "2315202256",
	}

	// Convert the map to a JSON string
	taskJson, err := json.Marshal(task)
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}

	req, err := http.NewRequest(http.MethodPost, url, strings.NewReader(string(taskJson)))
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+token)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Fprint(os.Stderr, err)
		os.Exit(1)
	}

	if resp.StatusCode != http.StatusOK && resp.StatusCode != http.StatusCreated {
		fmt.Fprintf(os.Stderr, "todoist add request failed: %s: %s\n", resp.Status, strings.TrimSpace(string(body)))
		os.Exit(1)
	}

	message := fmt.Sprintf("Task '%s' successfully added.\n", description)
	fmt.Print(message)
}
