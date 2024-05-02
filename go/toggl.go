package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "time"
    "encoding/json"
    "math"
    "strings"
    "bytes"
    "strconv"
)


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

type TogglProjectPost struct {

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
            fmt.Print("Usage: toggl [current|stop]\n")
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
        } else {
            // Print to stderr
            fmt.Fprintf(os.Stderr, "Unknown command: %s\n", os.Args[i])
            os.Exit(1)
        }

        // fmt.Println(os.Args[i])
        i++
    }


    toggl_err := `Toggl API error`

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

        // Look for project with name "Lunch", case-insensitive
        projects, err := get_projects(token)
        if err != nil {
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Check if project with name "Lunch" exists
        var lunch_id int64
        var lunchProject TogglProject
        for _, project := range projects {
            if strings.ToLower(project.Name) == "lunch" {
                lunch_id = project.ID
                lunchProject = project
                break
            }
        }

        if lunch_id == 0 {
            fmt.Fprintf(os.Stderr, "Lunch project not found\n")
            os.Exit(1)
        }

        // Print lunch Id to STDERR
        fmt.Fprintf(os.Stderr, "Lunch project ID: %d\n", lunch_id)

        workspaceId := lunchProject.WorkspaceId

        // Start timer for lunch project
        // https://api.track.toggl.com/api/v9/workspaces/{workspace_id}/time_entries
        TogglProjectPost := TogglProjectPost{
            CreatedWith: "toggl_cli",
            Description: "Lunch",
            Duration: -1,
            ProjectId: lunch_id,
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
            fmt.Fprintf(os.Stderr, "Error in POST request for lunch\n")
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }

        // Check the response code
        if resp.StatusCode != 200 {
            fmt.Fprintf(os.Stderr, "Error in POST request for lunch\n")
            fmt.Fprintf(os.Stderr, toggl_err)
            os.Exit(1)
        }
        os.Exit(0)
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
        fmt.Fprintf(os.Stderr, "Error in client.Do\n")
        fmt.Fprintf(os.Stderr, toggl_err)
        os.Exit(1)
    }

    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Error in reading body\n")
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
        body, err := ioutil.ReadAll(resp.Body)
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
    body, err := ioutil.ReadAll(resp.Body)
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
    body, err := ioutil.ReadAll(resp.Body)
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
