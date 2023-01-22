# GitHub Actions

Events -> Workflows -> Jobs -> Steps -> Actions

- By default, a workflow with multiple jobs runs in parallel.

- Steps:
  - Either an action or shell command

  - Actions:
    - Portable building block, from community or custom made.


```
Steps - Step[]

Step :
  name
  uses | run
```


## Deploying Release on tag

<https://github.com/softprops/action-gh-release>

```yaml
name: release
on:
  push:
    tags:
      - "v*"

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        name: Checkout Repo

      - name: Setup .NET
        uses: actions/setup-dotnet@v2
        with:
          dotnet-version: 6.0.x

      - name: Build
        run: dotnet build

      - name: Publish
        run: |
          cd CCLLCDataSync
          ls -la
          dotnet publish --no-self-contained -r win-x64 -o publish -c Release -p:DebugType=None -p:PublishSingleFile=true

      - name: GH Release
        uses: softprops/action-gh-release@v0.1.14
        with:
          files: CCLLCDataSync/publish/CCLLCDataSync.exe
```

Another action: <https://github.com/ncipollo/release-action>


## Passing on environment variables

Can use the `$GITHUB_PATH` variable which is a file path you can write to.
