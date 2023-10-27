```
public sealed class Singleton
{
    private static readonly Singleton _instance = new Singleton();

    // Private constructor to prevent instantiation from outside the class
    private Singleton() { }

    public static Singleton Instance
    {
        get
        {
            return _instance;
        }
    }

    public void DoSomething()
    {
        // Your code here
    }
}
```
