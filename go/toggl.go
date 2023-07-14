package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "time"
    "encoding/json"
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

func main() {

    // Try getting the "PATH" environment variable
    token, exists := os.LookupEnv("TOGGL_TOKEN")

    if !exists {
        fmt.Println("TOGGL_TOKEN environment variable not set")
        os.Exit(1)
    }

    not_tracking_text, exists := os.LookupEnv("TOGGL_NOT_TRACKING")
    if !exists {
        not_tracking_text = "Not tracking"
    }

    toggl_err := `Toggl API error`

    req, err := http.NewRequest(http.MethodGet, "https://api.track.toggl.com/api/v9/me/time_entries/current", nil)
    if err != nil {
        print(toggl_err)
    }
    req.Header.Set("Content-Type", "application/json; charset=utf-8")
    req.SetBasicAuth(token, "api_token")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        print(toggl_err)
    }

    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        print(toggl_err)
    }

    body_text := string(body)

    if body_text == "null" {
        fmt.Println(not_tracking_text)
        os.Exit(0)
    }

    // Parse as TooglTimeEntry
    var t TogglTimeEntry
    err = json.Unmarshal(body, &t)
    if err != nil {
        print(toggl_err)
    }

    // Print the description
    fmt.Println(t.Description)
}
