{
  "version": 1,
  "grid": 8.0,
  "preamble": "",
  "page": "bcc1b526",
  "pages": [
    {
      "id": "bcc1b526",
      "name": "Page 1",
      "view": {
        "x": -71.32353973388672,
        "y": -18.753196716308594,
        "zoom": 1.8360373973846436
      },
      "nodes": [
        {
          "id": "0a795f9d",
          "type": "typst",
          "x": 112.0,
          "y": 32.0,
          "width": 320.0,
          "height": null,
          "source": "= BACnet/IP\n\n- UDP protocol\n- client/server approach (devices like servers)\n- Default port 47808 (0xBAC0). "
        },
        {
          "id": "c719c796",
          "type": "typst",
          "x": 456.0,
          "y": 32.0,
          "width": 384.0,
          "height": null,
          "source": "= Application Datatypes, Application Tags\n\n- Tag Number Description\n- 0\tNULL\n- 1\tBoolean\n- 2\tUnsigned Integer (can be unsigned 8, 16, or 3)\n- 3\tSigned Integer\n- 4\tReal\n- 5\tDouble\n- 6\tOctet String\n- 7\tCharacter String\n- 8\tBit String\n- 9\tEnumerated\n- 10\tDate\n- 11\tTime\n- 12\tBACnetObjectIdentifier\n- 13\tReserved\n- 14\tReserved\n- 15\tReserved - Indicates that the following Octect contains an 8-bit Tag Number"
        },
        {
          "id": "acff26cc",
          "type": "typst",
          "x": 112.0,
          "y": 144.0,
          "width": 320.0,
          "height": null,
          "source": "= References\n\n- https://www.emqx.com/en/blog/bacnet-protocol-basic-concepts-structure-obejct-model-explained"
        },
        {
          "id": "ebfe7657",
          "type": "typst",
          "x": 864.0,
          "y": 32.0,
          "width": 480.0,
          "height": null,
          "source": "Stack\n\n- BACnet Application Layer (ReadProperty, WriteProperty, Who-Is, I-Am\n- BACnet Network Layer (NPDU) (BACnet network addressing and routing)\n- BVLC (BACnet Virtual Link Control)\n  - BVLC provides mechanisms for transporting BACnet messages over UDP/IP, including support for broadcasts across IP subnet boundaries.\n- UDP\n  - Typically destination port 47808 0xBAC0\n- IP/Ethernet\n  - IPv4 addressing and Layer 2 delivery\n"
        },
        {
          "id": "b0a85678",
          "type": "typst",
          "x": 864.0,
          "y": 336.0,
          "width": 496.0,
          "height": null,
          "source": "BVLC defines different message types, identified by a function code.\n\n#table(\ncolumns: (auto, auto, auto),\n[Function],[Hex code],[Purpose],\n[Original-Unicast-NPDU],[0x0A],[Send a BACnet message to one device],\n[Original-Broadcast-NPDU],[0x0B],[Broadcast a BACnet message locally],\n[Forwarded-NPDU],[0x04],[Forward a broadcast, typically through a BBMD],\n[Register-Foreign-Device],[0x05],[Register a remote BACnet/IP device with a BBMD],\n[Distribute-Broadcast-To-Network],[0x09],[Ask a BBMD to distribute a broadcast],\n[BVLC-Result],[0x00],[Report success or failure of certain BVLC operations],\n)"
        }
      ]
    }
  ]
}
