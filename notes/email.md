# Email

## Schema.org

You can add special interaction with the email client in Gmail (and Outlook too I think) using special syntax from Schema.org.

Example from GitHub:

```
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"><p></p>
<p>Sample issue </p>

<p
style="font-size:small;-webkit-text-size-adjust:none;color:#666;">—<br>You
are receiving this because you authored the thread.<br>Reply to this
email directly, <a href="https://SampleDomainissues/1">view it on GitHub Enterprise</a>, or <a href="https://github.tamu.edu/notifications/unsubscribe-auth/AAAAAZAYLV5CNE4I4XZVBELTJQ3BXANCNFSM3PDG">unsubscribe</a>.
<img src="https://github.tamu.edu/notifications/beacon/AAAAAZBHDL435MLP4UIJNUDTJQ3BXA5CNFSM3PDGVRRW63LNMVXHIX3UPFYGLLCJONZXKZKDN5WW2ZLOOSVGG33NNVSW45C7NFSM24XO.gif" height="1" width="1" alt="">
</p>
<script type="application/ld+json">[
{
"@context": "http://schema.org",
"@type": "EmailMessage",
"potentialAction": {
"@type": "ViewAction",
"target": "https://SampleDomain/issues/1"
"url": "https://SampleDomain/issues/1",
"name": "View Issue"
},
"description": "View this Issue on GitHub Enterprise",
"publisher": {
"@type": "Organization",
"name": "GitHub",
"url": "https://github.com"
}
}
]</script>
```


## IMAP vs POP3

IMAP: Internet Mail Access Protocol. More modern than POP3. 2-Way.

POP3: Post Office Protocol 3. 1 Way.


## Office 365 IMAP

[Source](https://www.getmailbird.com/setup/access-office365-via-imap-smtp#gmail)

- Office365 IMAP Server: outlook.office365.com
- IMAP port: 993
- IMAP Security: SSL
- IMAP Username: "Your full email address"
- IMAP password: "Your Office365 password"

## CLI Clients to Try

- Neomutt
- [aerc](https://aerc-mail.org/)
- [sup](https://sup-heliotrope.github.io/)
- [notmuch](https://notmuchmail.org/)

## Message Format

See RFC 5322.

<https://datatracker.ietf.org/doc/html/rfc5322>

## CLI Tools

Assume `maildir` format. Each message is a file in a directory.
Maildir:
    - `tmp`
    - `new`
    - `cur`

## Email Services

- Proton

## Maildir

<https://cr.yp.to/proto/maildir.html>

## Content Types

multipart/alternative	Different representations of the same content	Show one (usually HTML)
multipart/mixed	Bundle of unrelated parts	Show all, offer downloads
multipart/related	Related parts for rendering together (e.g. inline images)	Render as a unit (HTML + resources)

From <https://mimekit.net/docs/html/Frequently-Asked-Questions.htm>

MIME is a tree structure of parts.
There are multiparts which contain other parts (even other multiparts).
There are message parts which contain messages. And finally, there are leaf-node parts which contain content.

There are a few common message structures:

The message contains only a text/plain or text/html part (easy, just use that).

The message contains a multipart/alternative which will typically look a bit like this:

multipart/alternative
  text/plain
  text/html

Same as above, but the html part is inside a multipart/related so that it can embed images:

multipart/alternative
  text/plain
  multipart/related
    text/html
    image/jpeg
    image/png

The message contains a textual body part as well as some attachments:

multipart/mixed
  text/plain
  application/octet-stream
  application/zip

The same as above, but with the first part replaced with either #2 or #3 To illustrate:

multipart/mixed
  multipart/alternative
    text/plain
    text/html
  application/octet-stream
  application/zip

Or:

multipart/mixed
  multipart/alternative
    text/plain
    multipart/related
      text/html
      image/jpeg
      image/png
  application/octet-stream
  application/zip
