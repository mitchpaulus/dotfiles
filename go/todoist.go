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
    // First check for TODOIST_TOKEN environment variable
    token, exists := os.LookupEnv("TODOIST_TOKEN")

    if !exists {
        // Print to stderr
        fmt.Fprint(os.Stderr, "TODOIST_TOKEN environment variable not set.\n")
        os.Exit(1)
    }

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
