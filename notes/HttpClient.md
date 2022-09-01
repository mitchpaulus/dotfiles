# `HttpClient`

- Is `IDisposable`, but shouldn't be disposed.

- Simplest best practice is to:
  - Make single instance
  - Directly set the `SocketsHttpHandler.PooledConnectionTimeout` property like:

    ```C#
    SocketsHttpHandler socketsHttpHandler = new SocketsHttpHandler();
    socketsHttpHandler.PooledConnectionLifetime = TimeSpan.FromMinutes(1);
    _httpClient = new HttpClient(socketsHttpHandler);
    ```

If in a bind, may look into this NuGet package for a stand alone `HttpClientFactory`.
<https://www.nuget.org/packages/Arnath.StandaloneHttpClientFactory>
