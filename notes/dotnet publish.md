```
dotnet publish -r <runtime> -o dir -c Release -p:DebugType=None --self-contained -p:PublishSingleFile=true
// or
<PublishSingleFile>true</PublishSingleFile>
```

Official file describing the [runtimes](https://github.com/dotnet/runtime/blob/main/src/libraries/Microsoft.NETCore.Platforms/src/runtime.json).
[help page](https://docs.microsoft.com/en-us/dotnet/core/rid-catalog)

Most common:

- win-x64
- win-x86
- win-arm
- win-arm64
- linux-x64
- linux-musl-x64
- linux-arm
- linux-arm64
- osx-x64

