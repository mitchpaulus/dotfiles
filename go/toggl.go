package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
    "time"
    "encoding/json"
    "math"
    "strings"
    "bytes"
    "strconv"
    "runtime"
)

const toggl_err = `Toggl API error`


type TogglTimeEntry struct {
    ID                int64      `json:"id"`
    WorkspaceID       int64      `json:"workspace_id"`
    ProjectID         *int64     `json:"project_id"`  // Use pointer, since it can be null
    TaskID            *int64     `json:"task_id"`     // Use pointer, since it can be null
    Billable          bool       `json:"billable"`
    Start             time.Time  `json:"start"`
    Stop              *time.Time `json:"stop"`   // Use pointer, since it can be null
    Duration          int64      `json:"duration"`
    Description       string     `json:"description"`
    Tags              []string   `json:"tags"`
    TagIDs            []int64    `json:"tag_ids"`
    Duronly           bool       `json:"duronly"`
    At                time.Time  `json:"at"`
    ServerDeletedAt   *time.Time `json:"server_deleted_at"`  // Use pointer, since it can be null
    UserID            int64      `json:"user_id"`
    UID               int64      `json:"uid"`
    WID               int64      `json:"wid"`
}

type TogglWorkspace struct {
    Name string `json:"name"`
    Id int64 `json:"id"`
}

type TogglProject struct {
    ID int64 `json:"id"`
    Name string `json:"name"`
    WorkspaceId int64 `json:"workspace_id"`
}

// Name	Type	Description
// active	boolean	Whether the project is active or archived
// auto_estimates	boolean	Whether estimates are based on task hours, optional, premium feature
// billable	boolean	Whether the project is set as billable, optional, premium feature
// cid	integer	Client ID, legacy
// client_id	integer	Client ID, optional
// client_name	string	Client name, optional
// color	string	Project color
// currency	string	Project currency, optional, premium feature
// end_date	string	End date of a project timeframe
// estimated_hours	integer	Estimated hours, optional, premium feature
// fixed_fee	number	Project fixed fee, optional, premium feature
// is_private	boolean	Whether the project is private or not
// is_shared	boolean	Shared
// name	string	Project name
// rate	number	Hourly rate, optional, premium feature
// rate_change_mode	string	Rate change mode, optional, premium feature. Can be "start-today", "override-current", "override-all"
// recurring	boolean	Project is recurring, optional, premium feature
// recurring_parameters	object	Project recurring parameters, optional, premium feature
// start_date	string	Start date of a project timeframe
// template	boolean	Project is template, optional, premium feature
// template_id	integer	Template ID, optional

type TogglProjectPost struct {
    Name string `json:"name"`
    ClientName string `json:"client_name,omitempty"`
    WorkspaceId int64 `json:"workspace_id"`
    Active bool `json:"active"`
}


type TogglTimeEntryPost struct {

// name	type	description
// billable	boolean	Whether the time entry is marked as billable, optional, default false
// created_with	string	Must be provided when creating a time entry and should identify the service/application used to create it
// description	string	Time entry description, optional
// duration	integer	Time entry duration. For running entries should be negative, preferable -1
// duronly	boolean	Deprecated: Used to create a time entry with a duration but without a stop time. This parameter can be ignored.
// pid	integer	Project ID, legacy field
// project_id	integer	Project ID, optional
// shared_with_user_ids	Array of integer	List of user IDs to share this time entry with
// start	string	Start time in UTC, required for creation. Format: 2006-01-02T15:04:05Z
// start_date	string	If provided during creation, the date part will take precedence over the date part of "start". Format: 2006-11-07
// stop	string	Stop time in UTC, can be omitted if it's still running or created with "duration". If "stop" and "duration" are provided, values must be consistent (start + duration == stop)
// tag_action	string	Can be "add" or "delete". Used when updating an existing time entry
// tag_ids	Array of integer	IDs of tags to add/remove
// tags	Array of string	Names of tags to add/remove. If name does not exist as tag, one will be created automatically
// task_id	integer	Task ID, optional
// tid	integer	Task ID, legacy field
// uid	integer	Time Entry creator ID, legacy field
// user_id	integer	Time Entry creator ID, if omitted will use the requester user ID
// wid	integer	Workspace ID, legacy field
// workspace_id	integer	Workspace ID, required

    CreatedWith string `json:"created_with"`
    Description string `json:"description"`
    Duration int64 `json:"duration"`
    ProjectId int64 `json:"project_id"`
    Start string `json:"start"`
    WorkspaceId int64 `json:"workspace_id"`
}

// Name	Type	Description
// api_token	string	will be omitted if empty
// at	string	-
// authorization_updated_at	string	AuthorizationUpdatedAt timestamp when the authorization user session object was last updated.
// beginning_of_week	integer	-
// clients	Array of object	Clients, null if with_related_data was not set to true or if the user does not have any clients
// country_id	integer	-
// created_at	string	-
// default_workspace_id	integer	-
// email	string	-
// fullname	string	-
// has_password	boolean	-
// id	integer	-
// image_url	string	-
// intercom_hash	string	will be omitted if empty
// oauth_providers	Array of string	-
// openid_email	string	-
// openid_enabled	boolean	-
// options	object	will be omitted if empty
// projects	Array of object	Projects, null if with_related_data was not set to true or if the user does not have any projects
// tags	Array of object	Tags, null if with_related_data was not set to true, or if the user does not have any tags
// tasks	Array of object	Tasks, null if with_related_data was not set to true or if the user does not have any tasks
// time_entries	Array of object	TimeEntries, null if with_related_data was not set to true or if the user does not have any time entries
// timezone	string	-
// updated_at	string	-
// workspaces	Array of object	Workspaces, null if with_related_data was not set to true or if the user does not have any workspaces

// All I care about for now is the default_workspace_id
type TogglMeGet struct {
    DefaultWorkspaceId int64 `json:"default_workspace_id"`
}



func main() {

    // Try getting the "PATH" environment variable
    token, exists := os.LookupEnv("TOGGL_TOKEN")
    if !exists {
        // Print to stderr
        fmt.Fprintf(os.Stderr, "TOGGL_TOKEN environment variable not set\n")
        os.Exit(1)
    }

    not_tracking_text, exists := os.LookupEnv("TOGGL_NOT_TRACKING")
    if !exists {
        not_tracking_text = "Not tracking"
    }

    var tsMonth int = -1
    var tsPeriod int = -1

    command := "current"
    i := 1 // Oth index is the program name

    for i < len(os.Args) {

        if os.Args[i] == "current" {
            command = "current"
        } else if os.Args[i] == "stop" {
            command = "stop"
        } else if os.Args[i] == "help" || os.Args[i] == "--help" || os.Args[i] == "-h" {
            fmt.Print("Usage:\n")
            fmt.Print(" toggl current\n")
            fmt.Print(" toggl stop\n")
            fmt.Print(" toggl ts [<Month num> <Month period>]\n")
            fmt.Print(" toggl ws\n")
            fmt.Print(" toggl lunch\n")
            fmt.Print(" toggl break\n")
            fmt.Print(" toggl start <Project Name> <Description>\n")
            fmt.Print(" toggl newproj [Project Name] [Client]\n")
            os.Exit(0)
        } else if os.Args[i] == "ts" {
            command = "ts"

            // If there are more arguments, it's assumed to be the month and period
            if i + 2 < len(os.Args) {
                var err error
                tsMonth, err = strconv.Atoi(os.Args[i+1])

                if err != nil {
                    fmt.Fprintf(os.Stderr, "Invalid month: %s\n", os.Args[i+1])
                    os.Exit(1)
                }
                if tsMonth < 1 || tsMonth > 12 {
                    fmt.Fprintf(os.Stderr, "Invalid month: %d\n", tsMonth)
                    os.Exit(1)
                }

                tsPeriod, err = strconv.Atoi(os.Args[i+2])
                if err != nil {
                    fmt.Fprintf(os.Stderr, "Invalid period: %s\n", os.Args[i+2])
                    os.Exit(1)
                }
                if tsPeriod != 1 && tsPeriod != 2 {
                    fmt.Fprintf(os.Stderr, "Invalid period: %d\n", tsPeriod)
                    os.Exit(1)
                }

                i += 2
            }

        } else if os.Args[i] == "ws" {
            command = "ws"
        } else if (os.Args[i] == "lunch") {
            // Start lunch timer
            command = "lunch"
        } else if (os.Args[i] == "break") {
            command = "break"
        } else if os.Args[i] == "start" {
            // Start a new time entry
            // Check for project name
            if i + 2 >= len(os.Args) {
                fmt.Fprintf(os.Stderr, "Missing project name and description\n")
                os.Exit(1)
            }

            // Start the timer
            startTimer(os.Args[i+1], os.Args[i+2], token)
            os.Exit(0)

        } else if os.Args[i] == "newproj" {
            command = "newproj"

            var client string
            var newProjectName string

            if i + 2 < len(os.Args) {
                client = strings.TrimSpace(os.Args[i+2])
                newProjectName = strings.TrimSpace(os.Args[i+1])
                // Strip lead/trail whitespace

            } else if i + 1 < len(os.Args) {
                newProjectName = strings.TrimSpace(os.Args[i+1])
            } else {
                // Prompt for project name and client
                fmt.Print("Enter project name: ")
                fmt.Scanln(&newProjectName)
                newProjectName = strings.TrimSpace(newProjectName)
            }

            // Check whether the project name already exists
            projects, err := get_projects(token)
            if err != nil {
                fmt.Fprintf(os.Stderr, toggl_err)
                os.Exit(1)
            }

            for _, project := range projects {
                if strings.EqualFold(project.Name, newProjectName) {
                    fmt.Fprintf(os.Stderr, "Project %s already exists\n", newProjectName)
                    os.Exit(1)
                }
            }

            // Create the new project in the default workspace
            // https://api.track.toggl.com/api/v9/me
            defaultWorkspaceId := getMe(token).DefaultWorkspaceId

            fmt.Fprintf(os.Stderr, "Creating project '%s' in workspace %d\n", newProjectName, defaultWorkspaceId)

            TogglProjectPost := TogglProjectPost{
                Name: newProjectName,
                ClientName: client,
                WorkspaceId: defaultWorkspaceId,
                Active: true,
            }

            err = PostProject(TogglProjectPost, token)
            if err != nil {
                fmt.Fprintf(os.Stderr, toggl_err)
                os.Exit(1)
            }

            fmt.Printf("Project '%s' created\n", newProjectName)
            os.Exit(0)
        } else if os.Args[i] == "projects" {
            // Print all projects
            command = "projects"
        } else {
            // Print to stderr
            fmt.Fprintf(os.Stderr, "Unknown command: %s\n", os.Args[i])
            os.Exit(1)
        }

        // fmt.Println(os.Args[i])
        i++
    }


    if command == "ws" {
        // Get the workspaces for currrent user
        // https://engineering.toggl.com/docs/api/me#get-workspaces

        workspaces, err := getWorkspaces(token)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Print the workspaces to stdout
        for _, ws := range workspaces {
            fmt.Printf("%d\t%s\n", ws.Id, ws.Name)
        }

        os.Exit(0)
    } else if command == "lunch" {
        startTimer("Lunch", "Lunch", token)
        os.Exit(0)
    } else if command == "break" {
        startTimer("Office/Admin", "Break", token)
        os.Exit(0)
    } else if command == "projects" {
        // Get the projects for the current user
        projects, err := get_projects(token)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Print the projects to stdout
        for _, project := range projects {
            fmt.Printf(project.Name + "\n")
        }
    }

    // If the command is "current", check whether there an override file.
    // This is used in my status line, and when the internet goes out, it's a bad experience.
    // Check for presence of file ~/.config/toggl/off.
    if runtime.GOOS == "linux" {
        homeDir, exists := os.LookupEnv("HOME")
        if !exists {
            fmt.Fprintf(os.Stderr, "HOME variable doesn't exist?\n")
            os.Exit(1)
        }

        _, err := os.Stat(homeDir + "/.config/toggl/off")

        if err == nil {
            fmt.Printf("Toggl current off\n")
            os.Exit(0)
        }
    }

    // Else command is either "current" or "stop", need to get the current time entry for both
    req, err := http.NewRequest(http.MethodGet, "https://api.track.toggl.com/api/v9/me/time_entries/current", nil)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in building new request.\n")
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }
    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in client.Do '%v'\n", err)
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    defer resp.Body.Close()
    body, err := io.ReadAll(resp.Body)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in reading body '%v'\n", err)
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    body_text := string(body)

    if command == "current" {
        if body_text == "null" {
            fmt.Println(not_tracking_text)
            os.Exit(0)
        }

        // Parse as TooglTimeEntry
        var t TogglTimeEntry
        err = json.Unmarshal(body, &t)
        if err != nil {
            // Print to sdterr
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Print the description and elapsed time
        elapsed := time.Since(t.Start)

        // Print as Description (XX mins)
        fmt.Printf("%s (%d mins)\n", t.Description, int(elapsed.Minutes()))

    } else if command == "stop" {

        if body_text == "null" {
            // Do nothing..
            os.Exit(0)
        }

        // Parse as TooglTimeEntry
        var t TogglTimeEntry
        err = json.Unmarshal(body, &t)
        if err != nil {
            // Print to sdterr
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Stop the time entry (PATCH)
        // https://api.track.toggl.com/api/v9/workspaces/{workspace_id}/time_entries/{time_entry_id}/stop
        req, err := http.NewRequest(http.MethodPatch, fmt.Sprintf("https://api.track.toggl.com/api/v9/workspaces/%d/time_entries/%d/stop", t.WorkspaceID, t.ID), nil)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }
        req.Header.Set("Content-Type", "application/json; charset=utf-8")
        req.SetBasicAuth(token, "api_token")

        client := &http.Client{}
        resp, err := client.Do(req)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Check the response code
        if resp.StatusCode != 200 {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }
    } else if command == "ts" {
        // Our billing periods are always 1st through 15th, and 16th through end of month
        // URL: https://api.track.toggl.com/api/v9/me/time_entries

        // Get the current date/time local.
        now := time.Now()

        year := now.Year()
        month := int(now.Month())
        day := now.Day()

        if tsMonth != -1 {
            month = tsMonth
            if tsMonth > month {
                year -= 1
            }
        }

        if tsPeriod != -1 {
            if tsPeriod == 1 {
                day = 1
            } else {
                day = 16
            }
        }

        // Check whether the date of the month is before or after the 15th
        // Need to get start and end dates in YYYY-MM-DD format.
        // Assume end_date is inclusive
        var start_date string
        var end_date string

        if day <= 15 {
            // Start date is 1st of the month
            start_date = fmt.Sprintf("%d-%02d-%02d", year, month, 1)
            end_date = fmt.Sprintf("%d-%02d-%02d", year, month, 15)
        } else {
            // Start date is 16th of the month
            start_date = fmt.Sprintf("%d-%02d-%02d", year, month, 16)
            last_day := daysInMonth(year, int(month))
            end_date = fmt.Sprintf("%d-%02d-%02d", year, month, last_day)
        }

        // Get the time entries for the current billing period
        req, err := http.NewRequest(http.MethodGet, fmt.Sprintf("https://api.track.toggl.com/api/v9/me/time_entries?start_date=%s&end_date=%s", start_date, end_date), nil)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        req.Header.Set("Content-Type", "application/json; charset=utf-8")
        req.SetBasicAuth(token, "api_token")

        client := &http.Client{}
        resp, err := client.Do(req)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        defer resp.Body.Close()
        body, err := io.ReadAll(resp.Body)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Parse as slice of TooglTimeEntry
        var t []TogglTimeEntry
        err = json.Unmarshal(body, &t)
        if err != nil {
            // Print to sdterr
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Load Central Time Zone
        loc, err := time.LoadLocation("America/Chicago")
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        projects, err := get_projects(token)
        // project_map, err := get_projects(token)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Create a map of project IDs to project names
        project_map := make(map[int64]string)
        for _, project := range projects {
            project_map[project.ID] = project.Name
        }

        // Print the entries to stdout, tab delimited
        // Fields: description, project_id, duration (hrs), start, stop

        // Print header
        fmt.Printf("Description\tProject\tDuration (rounded)\tDuration (exact)\tStart Date\tStart Time\tStop Time\n")

        for _, entry := range t {
            dur_in_hours := float64(entry.Duration) / 3600.0

            // Round to nearest 15 minutes (0.25 hours)
            dur_in_hours_rounded := math.Round(dur_in_hours*4) / 4

            local_start := entry.Start.In(loc)
            var local_stop time.Time

            if entry.Stop == nil {
                local_stop = time.Now().In(loc)
            } else {
                local_stop = entry.Stop.In(loc)
            }

            var proj_name string
            if entry.ProjectID == nil{
                proj_name = "No project"
            } else {
                var ok bool
                proj_name, ok = project_map[*entry.ProjectID]
                if !ok {
                    proj_name = "No project"
                }
            }

            fields := []string{entry.Description,
                                proj_name,
                                fmt.Sprintf("%.2f", dur_in_hours_rounded),
                                fmt.Sprintf("%.2f", dur_in_hours),
                                local_start.Format("1/2"),
                                local_start.Format("3:04 PM"),
                                local_stop.Format("3:04 PM")}

            fmt.Printf(strings.Join(fields, "\t") + "\n")
        }
    }
}


func get_projects(token string) ([]TogglProject, error) {
    // https://api.track.toggl.com/api/v9/me/projects
    req, err := http.NewRequest(http.MethodGet, "https://api.track.toggl.com/api/v9/me/projects", nil)
    if err != nil {
        return nil, err
    }

    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }

    defer resp.Body.Close()
    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    body_text := string(body)

    // Parse as slice of TooglProject
    var t []TogglProject
    err = json.Unmarshal([]byte(body_text), &t)
    if err != nil {
        return nil, err
    }

    return t, nil
}

func getWorkspaces(token string) ([]TogglWorkspace, error) {
    // https://api.track.toggl.com/api/v9/me/workspaces
    req, err := http.NewRequest(http.MethodGet, "https://api.track.toggl.com/api/v9/me/workspaces", nil)
    if err != nil {
        return nil, err
    }

    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }

    defer resp.Body.Close()
    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    // Parse as slice of TogglWorkspace
    var t []TogglWorkspace
    err = json.Unmarshal(body, &t)
    if err != nil {
        return nil, err
    }

    return t, nil
}

func daysInMonth(year int, month int) int {
    switch month {
    case 1, 3, 5, 7, 8, 10, 12:
        return 31
    case 4, 6, 9, 11:
        return 30
    case 2:
        if year%4 == 0 && (year%100 != 0 || year%400 == 0) {
            return 29
        } else {
            return 28
        }
    default:
        return 0
    }
}

func PostProject(project TogglProjectPost, token string) error {
    // POST body
    postBytes, err := json.Marshal(project)
    if err != nil {
        return err
    }

    // https://api.track.toggl.com/api/v9/workspaces/{workspace_id}/projects
    req, err := http.NewRequest(http.MethodPost, fmt.Sprintf("https://api.track.toggl.com/api/v9/workspaces/%d/projects", project.WorkspaceId), bytes.NewBuffer(postBytes))
    if err != nil {
        return err
    }

    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return err
    }

    // Check the response code
    if resp.StatusCode != 200 {
        // Get reason for failure
        body, err := io.ReadAll(resp.Body)
        if err != nil {
            return fmt.Errorf("Could not read response body for %s\n", project.Name)
        }

        return fmt.Errorf("Error in POST request for %s. Reason: %s\n", project.Name, body)
    }

    return nil
}

func getMe(token string) TogglMeGet {
    // https://api.track.toggl.com/api/v9/me
    req, err := http.NewRequest(http.MethodGet, "https://api.track.toggl.com/api/v9/me", nil)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Could not build request for https://api.track.toggl.com/api/v9/me")
        os.Exit(1)
    }

    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Could not get response for https://api.track.toggl.com/api/v9/me")
        os.Exit(1)
    }

    defer resp.Body.Close()
    body, err := io.ReadAll(resp.Body)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Could not read response body for https://api.track.toggl.com/api/v9/me")
        os.Exit(1)
    }

    // Parse as TogglMeGet
    var t TogglMeGet
    err = json.Unmarshal(body, &t)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Could not unmarshal response body for https://api.track.toggl.com/api/v9/me")
        os.Exit(1)
    }

    return t
}

func startTimer(projectName string, description string, token string)  {
    // Look for project with name "projectName", case-insensitive
    projects, err := get_projects(token)
    if err != nil {
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    // Check if project with name "project" exists
    var projectId int64
    var togglProject TogglProject
    for _, project := range projects {
        if strings.EqualFold(project.Name, projectName) {
            projectId = project.ID
            togglProject = project
            break
        }
    }

    if projectId == 0 {
        fmt.Fprintf(os.Stderr, "Project %s not found\n", projectName)
        // Print all available projects, sorted
        fmt.Fprintf(os.Stderr, "Available projects:\n")
        for _, project := range projects {
            fmt.Fprintf(os.Stderr, "%s\n", project.Name)
        }

        os.Exit(1)
    }

    // Print project Id to STDERR
    fmt.Fprintf(os.Stderr, "%s project ID: %d\n", projectName, projectId)

    workspaceId := togglProject.WorkspaceId

    // Start timer for project
    // https://api.track.toggl.com/api/v9/workspaces/{workspace_id}/time_entries
    TogglProjectPost := TogglTimeEntryPost{
        CreatedWith: "toggl_cli",
        Description: description,
        Duration: -1,
        ProjectId: projectId,
        Start: time.Now().UTC().Format("2006-01-02T15:04:05Z"),
        WorkspaceId: workspaceId,
    }

    postBytes, err := json.Marshal(TogglProjectPost)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in marshalling TogglProjectPost\n")
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    req, err := http.NewRequest(http.MethodPost, fmt.Sprintf("https://api.track.toggl.com/api/v9/workspaces/%d/time_entries", workspaceId), bytes.NewBuffer(postBytes))
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in building new request.\n")
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in POST request for %s\n", projectName)
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    // Check the response code
    if resp.StatusCode != 200 {
        fmt.Fprintf(os.Stderr, "Error in POST request for %s\n", projectName)
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }
}
