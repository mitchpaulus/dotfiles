{
  "version": 1,
  "grid": 8.0,
  "preamble": "",
  "page": "ef14c219",
  "pages": [
    {
      "id": "ef14c219",
      "name": "Page 1",
      "view": {
        "x": 698.7130737304688,
        "y": 42.082542419433594,
        "zoom": 0.5557869076728821
      },
      "nodes": [
        {
          "id": "fba6f0df",
          "type": "typst",
          "x": -144.0,
          "y": 64.0,
          "width": 488.0,
          "height": null,
          "source": "#link(\"https://www.rfc-editor.org/rfc/rfc1122.html\")[RFC 1122 Requirements for Internet Hosts - Communication Layers - October 1989]\n\n2 concepts:\n\n- Physical network interface\n- Logical network interface. Multiple logical interfaces could correspond to one physical interface\n\nFrom MS:\n\n#emph[A network interface is the point where two pieces of network equipment or protocol layers connect.]"
        },
        {
          "id": "8677368c",
          "type": "typst",
          "x": 440.0,
          "y": 80.0,
          "width": 480.0,
          "height": null,
          "source": "1989 — RFC 1122: Explicitly defines physical and logical network interfaces, edited by Robert Braden.\n\n1993 — RFC 1573: Establishes an expanded interfaces management model.\n\n2000 — RFC 2863: Refines the interface management model, authored by Keith McCloghrie and Frank Kastenholz."
        },
        {
          "id": "2d5b1075",
          "type": "typst",
          "x": -440.0,
          "y": 384.0,
          "width": 760.0,
          "height": null,
          "source": "RFC 1122 Terminology\n\n#strong[Segment]: A segment is the unit of end-to-end transmission in the\nTCP protocol.  A segment consists of a TCP header followed\n              by application data.  A segment is transmitted by\n              encapsulation inside an IP datagram.\n\n#strong[Message]: In this description of the lower-layer protocols, a\n              message is the unit of transmission in a transport layer\n              protocol.  In particular, a TCP segment is a message.  A\n              message consists of a transport protocol header followed\n              by application protocol data.  To be transmitted end-to-\n              end through the Internet, a message must be encapsulated\n              inside a datagram.\n\n  #strong[IP Datagram]: An IP datagram is the unit of end-to-end transmission in\n              the IP protocol.  An IP datagram consists of an IP header\n              followed by transport layer data, i.e., of an IP header\n              followed by a message.\n\n              In the description of the internet layer (Section 3), the\n              unqualified term \"datagram\" should be understood to refer\n              to an IP datagram.\n\n#strong[Packet]: A packet is the unit of data passed across the interface\n              between the internet layer and the link layer.  It\n              includes an IP header and data.  A packet may be a\n              complete IP datagram or a fragment of an IP datagram.\n\n#strong[Frame]: A frame is the unit of transmission in a link layer\n              protocol, and consists of a link-layer header followed by\n              a packet.\n\n#strong[Connected Network]: A network to which a host is interfaced is often known as\n            the \"local network\" or the \"subnetwork\" relative to that\n              host.  However, these terms can cause confusion, and\n              therefore we use the term \"connected network\" in this\n              document.\n\n#strong[Multihomed]: A host is said to be multihomed if it has multiple IP\n              addresses.  For a discussion of multihoming, see Section\n              3.3.4 below.\n\n#strong[Physical network interface]: This is a physical interface to a connected network and\n              has a (possibly unique) link-layer address.  Multiple\n              physical network interfaces on a single host may share the\n              same link-layer address, but the address must be unique\n              for different hosts on the same physical network.\n\n#strong[Logical [network] interface]\n              We define a logical [network] interface to be a logical\n              path, distinguished by a unique IP address, to a connected\n              network.  See Section 3.3.4."
        },
        {
          "id": "d174ca39",
          "type": "typst",
          "x": 456.0,
          "y": 376.0,
          "width": 472.0,
          "height": null,
          "source": "Boundaries\n\n- Application: Socket API\n- OS networking stack: TCP/UDP/IP/routing\n- Network interface abstraction: Identitiy, state, link operations\n- Driver or virtual implementation\n- Physical hardware or software path"
        },
        {
          "id": "ca177a35",
          "type": "typst",
          "x": 464.0,
          "y": 656.0,
          "width": 480.0,
          "height": null,
          "source": "```C\n// linux/include/linux/netdevice.h\nstruct net_device {\r\n    char name[IFNAMSIZ];  // eth0\r\n    int ifindex;\r\n    unsigned int mtu;\r\n    unsigned int flags;\r\n\r\n    const struct net_device_ops *netdev_ops;\r\n\r\n    /* Many additional fields */\r\n};\n```"
        },
        {
          "id": "0158bbef",
          "type": "typst",
          "x": 960.0,
          "y": 368.0,
          "width": 320.0,
          "height": null,
          "source": "Node: A device participating in the network.\n\nLink: The medium or communication facility connecting nodes.\n\nInterface: A node's attachment to that link.\n\nLink Layer: The protocols governing communication over that link."
        },
        {
          "id": "97861a9d",
          "type": "typst",
          "x": 1304.0,
          "y": 368.0,
          "width": 320.0,
          "height": null,
          "source": "- App Layer: SMTP\n- Transport Layer: TCP/UDP\n- Internet Layer: IP\n- Link Layer: MAC?"
        },
        {
          "id": "ff9ef479",
          "type": "typst",
          "x": 984.0,
          "y": 648.0,
          "width": 648.0,
          "height": null,
          "source": "The terms frame, packet, datagram, message, and segment are\nillustrated by the following schematic diagrams:\n\n```\nA. Transmission on connected network:\n_________________________________________________\n| LL hdr | IP hdr |         (data)              |\n|________|________|_____________________________|\n\n  <---------- Frame ----------------------------->\n          <----------Packet -------------------->\n\n\nB. Before IP fragmentation or after IP reassembly:\n          ________________________________________\n          | IP hdr | transport| Application Data |\n          |________|____hdr___|__________________|\n\n          <--------  Datagram ------------------>\n                    <-------- Message ----------->\n  or, for TCP:\n          ________________________________________\n          | IP hdr |  TCP hdr | Application Data |\n          |________|__________|__________________|\n\n          <--------  Datagram ------------------>\n                    <-------- Segment ----------->\n```\n\n"
        }
      ]
    }
  ]
}
