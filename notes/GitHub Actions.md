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

## Adding git tag

[Git tag object](https://docs.github.com/en/rest/git/tags?apiVersion=2022-11-28#create-a-tag-object)
[Create a reference](https://docs.github.com/en/rest/git/refs?apiVersion=2022-11-28#create-a-reference)

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/git/refs \
  -d '{"ref":"refs/heads/featureA","sha":"aa218f56b14c9653891f9e74264a383fa43fefbd"}'
```

[Permissions](https://docs.github.com/en/rest/overview/permissions-required-for-github-apps)

## Authentication

PAT:

```yaml
- uses: actions/checkout@v3
  with:
    token: ${{ secrets.PAT }}
    ssh-key: ${{ secrets.SSH_KEY }}
```

- [Trigger workflow from workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#triggering-a-workflow-from-a-workflow)
  - Can't use `GITHUB_TOKEN`, need PAT or SSH deploy key.

- `actions/checkout` only gets the single commit, not the full history.

## Debugging

- `shell: bash -x {0}` to see the commands being run.


## [Checkout multiple repos (private)](https://github.com/actions/checkout?tab=readme-ov-file#checkout-multiple-repos-private)

```yaml
- name: Checkout
  uses: actions/checkout@v4
  with:
    path: main

- name: Checkout private tools
  uses: actions/checkout@v4
  with:
    repository: my-org/my-private-tools
    token: ${{ secrets.GH_PAT }} # `GH_PAT` is a secret that contains your PAT
    path: my-tools
```


## Unable to access organization private repository with fine-grained token #40910

<https://github.com/orgs/community/discussions/40910>
