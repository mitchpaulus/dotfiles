# NuGet

## Packaging for GitHub

Authentication: Use the Personal Access Tokens. Can set those up going
to: Settings -> Developer Settings -> Personal Access Tokens.

These are set up per user, not per repository.

Needed three things:

1. Additional items in .csproj. `RepositoryUrl` does not have the .git added.

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>netcoreapp3.1</TargetFramework>
    <RootNamespace>andover_dmp</RootNamespace>

    <PackageId>CCLLC.AndoverDmp</PackageId>
    <Version>0.1.0</Version>
    <Authors>Mitchell T. Paulus</Authors>
    <Company>Command Commissioning, LLC</Company>
    <PackageDescription>Library and console application for reading Andover .dmp files.</PackageDescription>
    <RepositoryUrl>https://github.com/Command-Commissioning/andover-dmp</RepositoryUrl>
  </PropertyGroup>

</Project>
```

2. Nuget.Config file. On many of the blogs and documentation, it says to
   put the PAT in the packageSourceCredentials tag, however, I found
   that this does not work. Really it should go into the `apikeys` tag,
   or specified on the command line. All this file is doing is setting
   the location of the 'source', which is then used on the command line
   in step 3.

   Maybe don't need that `<clear />` item?

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <packageSources>
        <clear />
        <add key="github" value="https://nuget.pkg.github.com/Command-Commissioning/index.json" />
    </packageSources>
</configuration>
```

3. Run command like:

```sh
dotnet nuget push "bin/Release/CCLLC.AndoverDmp.0.1.0.nupkg" --api-key ghp_asdfasdfasdfasdfasdf  --source github
```


## Packaging Local

1. Get nuget.exe CLI - Note this is different than using `dotnet nuget`.
   Some of the same functionality, but they aren't necessarily the same.

2. `nuget.exe add Lib.0.5.0.nupkg -Source  C:\Users\mpaulus\Nuget`


## Exception looking for dll on `pack`

Apparently having `GeneratePackageOnBuild` breaks everything on the CLI.
<https://github.com/dotnet/sdk/issues/10335>
