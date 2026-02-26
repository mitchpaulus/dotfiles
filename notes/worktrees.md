```sh
# Add a new worktree directory, checking out an existing branch
git worktree add ../my-feature my-feature

# Or create a new branch and check it out there
git worktree add -b my-feature ../my-feature origin/main

# See all worktrees attached to this repo
git worktree list

# Remove a linked worktree (after you’re done)
git worktree remove ../my-feature
```
