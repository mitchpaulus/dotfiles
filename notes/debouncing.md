```c#
using System;
using System.Timers;

public class Debouncer
{
    private Timer _timer;
    private Action _action;

    public Debouncer(int interval)
    {
        _timer = new Timer(interval);
        _timer.Elapsed += HandleElapsed;
        _timer.AutoReset = false;  // Ensure the timer is only called once per interval
    }

    public void Debounce(Action action)
    {
        _action = action;
        _timer.Stop();  // Stop the previous timer
        _timer.Start(); // Start a new timer
    }

    private void HandleElapsed(object sender, ElapsedEventArgs e)
    {
        _action();
    }
}

public class Program
{
    public static void Main()
    {
        Debouncer debouncer = new Debouncer(1000); // Debounce interval of 1000 milliseconds (1 second)

        // Simulate rapid method calls
        for (int i = 0; i < 10; i++)
        {
            debouncer.Debounce(() => Console.WriteLine("Debounced Action!"));
            System.Threading.Thread.Sleep(200); // Sleep 200 ms between calls
        }
    }
}
```
