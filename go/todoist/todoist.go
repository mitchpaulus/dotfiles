package main

// Simple CLI for Todoist

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "strings"
    "sort"
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
    CreatorId string `json:"creator_id"`
    CreatedAt string `json:"created_at"`
    AssigneeId string `json:"assignee_id"`
    AssignerId string `json:"assigner_id"`
    CommentCount int `json:"comment_count"`
    IsCompleted bool `json:"is_completed"`
    Content string `json:"content"`
    Description string `json:"description"`
    Due struct {
        Date string `json:"date"`
        IsRecurring bool `json:"is_recurring"`
        Datetime string `json:"datetime"`
        String string `json:"string"`
        Timezone string `json:"timezone"`
    } `json:"due"`
    Duration struct {
        Amount int `json:"amount"`
        Unit string `json:"unit"`
    } `json:"duration"`
    Id string `json:"id"`
    Labels []string `json:"labels"`
    Order int `json:"order"`
    Priority int `json:"priority"`
    ProjectId string `json:"project_id"`
    SectionId string `json:"section_id"`
    ParentId string `json:"parent_id"`
    Url string `json:"url"`
}

func main() {
    // Loop through arguments like while, looking for -h or --help
    var index int = 1

    command := "list"
    var description string

    for index < len(os.Args) {
        if os.Args[index] == "-h" || os.Args[index] == "--help" {
            fmt.Println("Usage: todoist")
			fmt.Println("       todoist add <DESCRIPTION>")
            os.Exit(0)
        } else if os.Args[index] == "add" || os.Args[index] == "a" {
            command = "add"

            // Get the next arguments as the description for the task, space separated
            // If the description is not provided, print an error message and exit
            if index + 1 >= len(os.Args) {
                fmt.Fprint(os.Stderr, "Description required for add command.\n")
                os.Exit(1)
            } else {
                descriptionItems := os.Args[index + 1:]
                // Join the description items with a space
                description = strings.Join(descriptionItems, " ")
            }
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
    } else if command == "add" {
        add(token, description)
    } else {
        // Should never reach here, print what invalid command was used
        fmt.Fprint(os.Stderr, "Invalid command: ", command, "\n")
    }
}

func list(token string) {
    // Get active tasks from:
    // curl --silent -X GET \
    // https://api.todoist.com/rest/v2/tasks \
    // -H "Authorization: Bearer $TODOIST_TOKEN"

    url := "https://api.todoist.com/rest/v2/tasks"

    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    req.Header.Set("Authorization", "Bearer " + token)

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    // Parse JSON response
    var tasks []Task
    err = json.Unmarshal(body, &tasks)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    // Print tasks that match project_id 2315202256
    // print content, project_id, and labels, tab separated
    // Order by order number (ascending)
    sort.Slice(tasks, func(i, j int) bool {
        return tasks[i].Order < tasks[j].Order
    })

    for _, task := range tasks {
        if task.ProjectId == "2315202256" {
            fmt.Printf("%s\t%s\n", task.Content, strings.Join(task.Labels, ","))
        }
    }
}

func add(token string, description string) {
    // Add a task with the description provided
    // Example:
    // $ curl "https://api.todoist.com/rest/v2/tasks" \
    // -X POST \
    // --data '{"content": "Buy Milk", "due_string": "tomorrow at 12:00", "due_lang": "en", "priority": 4}' \
    // -H "Content-Type: application/json" \
    // -H "X-Request-Id: $(uuidgen)" \
    // -H "Authorization: Bearer $token"

    url := "https://api.todoist.com/rest/v2/tasks"

    // Create a map with the task description
    task := map[string]string{
        "content": description,
        "project_id": "2315202256",
    }

    // Convert the map to a JSON string
    taskJson, err := json.Marshal(task)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    req, _ := http.NewRequest(http.MethodPost, url, strings.NewReader(string(taskJson)))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("Authorization", "Bearer " + token)

    client := &http.Client{}
    _, err = client.Do(req)
    if err != nil {
        fmt.Fprint(os.Stderr, err)
        os.Exit(1)
    }

    message := fmt.Sprintf("Task '%s' successfully added.\n", description)
    fmt.Print(message)
}
