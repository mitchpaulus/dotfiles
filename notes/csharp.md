# C\#

- Repeat String: `new string('a', 12)`


## DateTime Formatting

<https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings>

```
d    = Day of month 1-31
dd   = Day of month 01-31
ddd  = Mon
dddd = Monday
h    = Hour, 1 to 12
hh   = Hour, 01 to 12
H    = Hour, 0 to 23
HH   = Hour, 00 to 23
m    = minute, 0 to 59
mm   = minute, 00 to 60
M    = month, 1 to 12
MM   = month, 01 to 12
MMM  = Abbreviated Month name, Jun
MMMM = Full Month Name, January
ss   = second, 00 to 59
tt   = AM/PM
```

## Numeric Formatting

```
F{num} : Fixed point, with number of digits.
```

## Time Zones

See [this blog on cross-platform time zone issues](https://devblogs.microsoft.com/dotnet/cross-platform-time-zones-with-net-core/)

```C#
TimeZoneInfo tzInfo = TimeZoneInfo.FindSystemTimeZoneById("Central Standard Time");
```

## Line Splitting

![From SO](https://stackoverflow.com/a/6873727/5932184)

```c#
    public static IEnumerable<string> SplitLines(this string text)
    {
        using StringReader sr = new StringReader(text);
        while (sr.ReadLine() is { } line)
        {
            yield return line;
        }
    }
```

## Emailing

```C#
using System.Net.Mail;

mailClient = new SMTPClient("mail.host.com");
mailClient.Credentials = new NetworkCredential("user", "pass");
MailMessage msg = new();
msg.From = new MailAddress("email@host.com");
msg.To.Add(to);
msg.Subject = subject;
msg.Body = message;
mailClient.Send(msg);
```

## IO

```
Directory.EnumerateFiles(string dir) -> List of full file paths.
```

## Structures for improved typing

<https://www.meziantou.net/use-structures-to-improve-the-readability-of-your-code.htm>
