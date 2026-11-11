# Networking

- Prefer `ip` over `ifconfig`. `ip` is meant to deprecate `ifconfig`.
- `ip` is part of the iproute2 project.

## ARP

- ARP is the Address Resolution Protocol (RFC 826)

## Difference between URI and URL?

[Post explains it all very well](https://danielmiessler.com/study/difference-between-uri-url/)

Quote from that post

> 1. A URI is an identifier of a specific resource. Like a page, or book, or a document.
> 2. A URL is special type of identifier that also tells you how to access it, such as HTTPs, FTP, etc. like https://www.google.com.
> 3. If the protocol (https, ftp, etc.) is either present or implied for a domain, you should call it a URL—even though it’s also a URI.

## Port Forwarding

Can take network requests send to public IP and then send them to a particular
device on the local network based on the port the network request came in on.

<https://www.youtube.com/watch?v=mLLKtO-qlNM>


## Tracking all web requests

`edge://net-export/`

## References

<https://fazamhd.com/mental-models/networking/>

## Local Networking

Suppose your computer is 192.168.1.10/24 and a controller is 192.168.1.20/24:

1. The computer uses its subnet mask to determine that the controller is local.
2. It broadcasts an ARP request: “Who has IP address 192.168.1.20?”
3. The controller replies with its Ethernet MAC address.
4. The computer sends an Ethernet frame addressed to that MAC address, with the IP packet inside it.
5. The Ethernet switch forwards the frame to the controller’s port.

The computer remembers the IP-to-MAC mapping for a while, so it doesn't need to ask for every packet.
The switch forwards Ethernet frames using MAC addresses; a router forwards IP packets between networks.

Router and gateway are closely related but describe different things:

- A router is a device or software that forwards IP packets between networks.
- A default gateway is the next-hop IP address your device uses when it has no more specific route to a destination.
  On a typical local network, this is the local IP address of a router.

For a destination outside your local network, your computer addresses the Ethernet frame to the gateway’s MAC address,
while the IP packet inside still carries the final destination’s IP address.
The router receives that frame and forwards the packet onward.

“Gateway” also has broader meanings, such as a device that translates between protocols.
In your computer’s Ethernet settings, though, it normally means the default router.
