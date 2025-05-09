# Networking

- Prefer `ip` over `ifconfig`. `ip` is meant to deprecate `ifconfig`.
- `ip` is part of the iproute2 project.

## ARP

- ARP is the Address Resolution Protocol (RFC 826)

## Difference between URI and URL?

[Post explains it all very well](https://danielmiessler.com/study/difference-between-uri-url/)

Quote from that post

> 1. A URI is an identifier of a specific resource. Like a page, or book,
>    or a document.
> 2. A URL is special type of identifier that also tells you how to access
>    it, such as HTTPs, FTP, etc. like https://www.google.com.
> 3. If the protocol (https, ftp, etc.) is either present or implied for a
>    domain, you should call it a URL—even though it’s also a URI.

## Port Forwarding

Can take network requests send to public IP and then send them to a particular
device on the local network based on the port the network request came in on.

<https://www.youtube.com/watch?v=mLLKtO-qlNM>


## Tracking all web requests

`edge://net-export/`
