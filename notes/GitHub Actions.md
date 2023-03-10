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

## Don't trigger on tag push

<https://stackoverflow.com/a/71879890/5932184>

## .NET Template

```
# This workflow will build a .NET project
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-net

name: .NET

on:
  push:

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Setup .NET
      uses: actions/setup-dotnet@v3
      with:
        dotnet-version: 6.0.x
    - name: Restore dependencies
      run: dotnet restore
    - name: Build
      run: dotnet build --no-restore
    - name: Test
      run: dotnet test --no-build --verbosity normal
```

## NuGet

If using nuget.config, make sure to have all sources, including the normal nuget.org one (<https://stackoverflow.com/a/57855098/5932184>)

```
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="internal" value="URL_TO_INTERNAL_FEED" />
  </packageSources>
</configuration>
```

- [Reference environment secret](https://stackoverflow.com/a/66526312/5932184)
