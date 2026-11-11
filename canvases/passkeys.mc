{
  "version": 1,
  "grid": 8.0,
  "preamble": "",
  "page": "f5f94af5",
  "pages": [
    {
      "id": "f5f94af5",
      "name": "Page 1",
      "view": {
        "x": -916.2178955078125,
        "y": -4.0540313720703125,
        "zoom": 0.826446533203125
      },
      "nodes": [
        {
          "id": "aa7c7949",
          "type": "typst",
          "x": 208.0,
          "y": 128.0,
          "width": 320.0,
          "height": null,
          "source": "- Passkey is public/private key pair\n  - Public key goes to website\n  - Private key with you\n\n\n"
        },
        {
          "id": "805c0299",
          "type": "typst",
          "x": 560.0,
          "y": 136.0,
          "width": 768.0,
          "height": null,
          "source": "A YubiKey has several separate apps\n\nA YubiKey 5 runs several independent apps:\n- FIDO2 / U2F: the WebAuthn and passkey part\n- PIV: smart-card certificates, with a few fixed slots\n- OpenPGP: GPG keys\n- OATH: TOTP codes, read through the Yubico Authenticator app\n- OTP: the long string it types when you touch it\n\nPasskeys only use the FIDO2 app.\n\nFIDO2 has two kinds of credentials\n\n1. Non-discoverable credentials (this is the \"single key\" idea)\n\nThe YubiKey holds one secret master key that never leaves the device. When you register with a site, the key derives a unique key pair for that site from the master secret plus some random data. The random data goes to the website as the \"credential ID.\" At login the site sends the ID back, and the YubiKey recomputes the private key on the spot.\n\n- Nothing is stored on the key per site, so the number of these is unlimited.\n- The site has to tell the key which credential to use, so you type your username first.\n- Classic \"use a security key as 2FA\" setups (older U2F-style) usually work this way.\n\n2. Discoverable credentials (true passkeys)\n\nThe private key and some account info (site, username) are stored on the YubiKey itself. That lets the key answer \"which accounts do you have for this site?\" without the site telling it anything, which is what makes username-less \"Sign in with a passkey\" work.\n\n- These take up storage slots.\n- YubiKey 5 with firmware before 5.7: 25 slots. Firmware 5.7 or later: 100 slots. Firmware can't be upgraded, so the number your key shipped with is permanent.\n\nWhen a site says \"passkey,\" it almost always means a discoverable credential, so it uses a slot."
        },
        {
          "id": "6773df7e",
          "type": "typst",
          "x": 608.0,
          "y": -48.0,
          "width": 472.0,
          "height": null,
          "source": "TPM (Trusted Platform Module)\n\nThe TPM is a tiny, isolated processor that can:\n- generate cryptographic keys,\n- store or protect them so they can't be exported,\n- do signing operations internally."
        },
        {
          "id": "1beb0ec1",
          "type": "typst",
          "x": 1384.0,
          "y": 32.0,
          "width": 320.0,
          "height": null,
          "source": "FIDO (Fast IDentity Online)\n\nopen industry association launched in February 2013 whose stated mission is to develop and promote authentication standards that \"help reduce the world’s over-reliance on passwords\"."
        },
        {
          "id": "4b92a35b",
          "type": "typst",
          "x": -928.0,
          "y": -168.0,
          "width": 1024.0,
          "height": null,
          "source": "You're right, I mixed two things together. To be precise:\n\n- #strong[The challenge] really is just random bytes. The server\n  generates it and nothing else goes in it.\n- #strong[What gets signed] is more than the challenge: a bundle that\n  contains the challenge plus the domain, flags and a counter.\n\n== The specs\n<the-specs>\nThe whole system is called #strong[FIDO2], and it's made of two specs:\n\n#figure(\n  align(center)[#table(\n    columns: (25.43%, 9.25%, 65.32%),\n    align: (auto,auto,auto,),\n    table.header([Spec], [Who publishes it], [Covers],),\n    table.hline(),\n    [#strong[WebAuthn] (Web Authentication)], [W3C], [The JavaScript API\n    between the #strong[website and the browser], plus the data formats\n    and server verification rules],\n    [#strong[CTAP2] (Client to Authenticator Protocol)], [FIDO\n    Alliance], [How the #strong[browser/OS talks to the authenticator]\n    (YubiKey over USB/NFC/BLE, the platform authenticator, a phone)],\n  )]\n  , kind: table\n  )\n\n- WebAuthn: https:/\\/www.w3.org/TR/webauthn-3/ (Level 3; Level 2 is the\n  older stable Recommendation)\n- CTAP: https:/\\/fidoalliance.org/specifications/ (CTAP 2.1 / 2.2)\n\nThe spec calls the login flow an #strong[authentication ceremony] and\nthe signup flow a #strong[registration ceremony].\n\n== Login, in full detail\n<login-in-full-detail>\n=== Step 1: Server → browser\n<step-1-server-browser>\nThe server generates a random challenge, stores it with your session,\nand sends options to the page's JavaScript:\n\n```js\nnavigator.credentials.get({\n  publicKey: {\n    challenge: <32 random bytes>,\n    rpId: \"example.com\",             // \"Relying Party\" = the website\n    allowCredentials: [ ... ],       // credential IDs (empty for username-less passkeys)\n    userVerification: \"required\",    // demand PIN/biometric, not just a touch\n    timeout: 60000\n  }\n})\n```\n\n=== Step 2: The browser builds `clientDataJSON`\n<step-2-the-browser-builds-clientdatajson>\nThe #strong[browser] creates this itself. The website can't control the\n`origin` field:\n\n```json\n{\n  \"type\": \"webauthn.get\",\n  \"challenge\": \"k3J9x...Qz7\",\n  \"origin\": \"https://example.com\",\n  \"crossOrigin\": false\n}\n```\n\nThe browser also checks that `rpId` is valid for the page's actual\ndomain. A page on `evil.com` can't ask for `rpId: \"google.com\"`.\n\nIt then hashes this: `clientDataHash = SHA-256(clientDataJSON)`.\n\n=== Step 3: Browser → authenticator (CTAP2)\n<step-3-browser-authenticator-ctap2>\nThe browser sends the authenticator an `authenticatorGetAssertion`\ncommand containing: - `rpId` - `clientDataHash` (the authenticator only\ngets the hash, not the JSON) - the allow list of credential IDs, if any\n\\- options such as \"user verification required\"\n\n=== Step 4: The authenticator does its work\n<step-4-the-authenticator-does-its-work>\n+ Finds a credential for that `rpId`. For a discoverable passkey it\n  looks up its stored slots. For a non-discoverable one it re-derives or\n  unwraps the key from the credential ID.\n+ Checks #strong[user presence] (touch) and/or #strong[user\n  verification] (PIN or biometric).\n+ Builds #strong[`authenticatorData`], a compact binary structure:\n\n#figure(\n  align(center)[#table(\n    columns: (8.53%, 6.2%, 85.27%),\n    align: (auto,auto,auto,),\n    table.header([Field], [Size], [Contents],),\n    table.hline(),\n    [`rpIdHash`], [32 bytes], [SHA-256 of `\"example.com\"`],\n    [`flags`], [1 byte], [bits for UP (user present), UV (user\n    verified), BE/BS (backup-eligible / backed up, i.e.~synced passkey),\n    etc.],\n    [`signCount`], [4 bytes], [counter that goes up with each use (helps\n    detect cloned keys; synced passkeys often leave it at 0)],\n    [extensions], [optional], [extra data],\n  )]\n  , kind: table\n  )\n\n#block[\n#set enum(numbering: \"1.\", start: 4)\n+ #strong[Signs the concatenation of the two:]\n\n  ```\n  signature = Sign(privateKey, authenticatorData || clientDataHash)\n  ```\n\n  This is the bundle I mentioned. Through `clientDataHash` it covers the\n  challenge, origin and type, and through `authenticatorData` it covers\n  the rpId hash, flags and counter.\n\n+ Returns the credential ID, `authenticatorData`, `signature` and\n  `userHandle` (the user ID the site assigned at registration).\n]\n\n=== Step 5: Browser → server\n<step-5-browser-server>\nThe JavaScript gets back a `PublicKeyCredential` object and posts it to\nthe server: credential ID, `clientDataJSON` (the full JSON this time),\n`authenticatorData`, `signature`, `userHandle`.\n\n=== Step 6: The server verifies (WebAuthn §7.2)\n<step-6-the-server-verifies-webauthn-7.2>\n+ Look up the stored public key by credential ID.\n+ Parse `clientDataJSON` and check:\n  - `type == \"webauthn.get\"`\n  - `challenge` equals the one it issued for this session, and it hasn't\n    been used before\n  - `origin` is its own origin\n+ Check that `rpIdHash` in `authenticatorData` equals SHA-256 of its own\n  rpId.\n+ Check the flags: UP is set, and UV is set if it required verification.\n+ Compute `SHA-256(clientDataJSON)` itself, then #strong[verify the\n  signature] over `authenticatorData || hash` with the stored public\n  key.\n+ Check `signCount` is greater than the last value seen (if it's\n  non-zero), and save the new value.\n\nIf everything passes, you're logged in.\n\n== Registration is similar\n<registration-is-similar>\n`navigator.credentials.create()` follows the same pattern, with three\ndifferences: - The server also sends user info (`user.id`, name) and\nacceptable algorithms. Common ones are ES256 (`-7`), EdDSA (`-8`) and\nRS256 (`-257`), identified by COSE numbers. - The authenticator\n#strong[generates a new key pair] and returns the public key and\ncredential ID inside `authenticatorData`. - It can include an optional\n#strong[attestation] statement, signed with a key baked in at the\nfactory. This proves to the server what kind of device it is, e.g.~\"this\nis a genuine YubiKey 5 NFC.\" Most sites don't ask for it.\n\n== To see it in practice\n<to-see-it-in-practice>\n- #strong[https:/\\/webauthn.io]: a demo site where you can register and\n  log in with your YubiKey and look at the raw request and response.\n- #strong[https:/\\/webauthn.guide]: a readable walkthrough of the same\n  flow.\n- Chrome DevTools has a #strong[WebAuthn] panel (⋮ → More tools →\n  WebAuthn) that emulates authenticators and shows credentials.\n"
        },
        {
          "id": "6de21c7e",
          "type": "typst",
          "x": 1856.0,
          "y": 24.0,
          "width": 800.0,
          "height": null,
          "source": "There was a FIDO 1.0, though people rarely call it \"FIDO1.\" FIDO2 is the\nsecond generation of the FIDO Alliance's standards.\n\n== FIDO Alliance\n<fido-alliance>\nFIDO stands for #strong[Fast IDentity Online]. The alliance was founded\nin 2012 by PayPal, Lenovo, Nok Nok Labs and a few others, and Google,\nYubico, Microsoft and Apple joined later. Its goal from the start was to\nreplace or strengthen passwords using public-key cryptography.\n\n== FIDO 1.0 (December 2014): two separate specs\n<fido-1.0-december-2014-two-separate-specs>\n\n#strong[U2F (Universal 2nd Factor)] \n- Came mainly from #strong[Google and Yubico], which is why YubiKeys were among the first devices.\n- A #strong[second factor only]: you still typed your password, then touched the key.\n- Used the same challenge-signing idea, including origin binding against phishing.\n- Credentials were non-discoverable, so a key could have unlimited registrations and needed no storage.\n- Browser support was patchy. Chrome had its own API, and other browsers took years or never fully supported it.\n- Google rolled it out to all its employees and reported essentially no successful phishing of those accounts afterward.\n\n#strong[UAF (Universal Authentication Framework)] \n- Came mainly from #strong[Nok Nok Labs].\n- #strong[Passwordless]: you unlocked a key on your phone with a fingerprint or PIN.\n- Required a FIDO client built into the app or OS, not the browser.\n- Mostly used in some banking and payment apps (Samsung Pay, some Asian banks). It never caught on for the web.\n\nSo FIDO 1.0 split the job: U2F was \"a key as a second factor,\" UAF was\n\"passwordless on your phone,\" and neither was a native part of the web\nplatform.\n\n== FIDO2 (2018): the two ideas merged and standardized\n<fido2-2018-the-two-ideas-merged-and-standardized>\n\nFIDO2 combined both ideas into one system:\n\n- #strong[WebAuthn] was submitted to the W3C in 2015 and became a W3C Recommendation in March \\2019.\n  It gave every major browser one standard JavaScript API. This was the biggest change.\n- #strong[CTAP2] added passwordless login, PINs,\n  biometrics and #strong[discoverable (resident) credentials], which are the slots on your YubiKey. \n- #strong[CTAP1] is the #strong[old U2F protocol, renamed]. It was kept so existing U2F keys still work with WebAuthn.\n\n== \"Passkeys\" (2022)\n<passkeys-2022>\n\n\"Passkey\" isn't a new protocol. In May 2022, Apple, Google and Microsoft\njointly committed to support #strong[discoverable FIDO2 credentials,\nsynced across devices], and they gave those credentials a friendly name.\nUnder the hood a passkey is still WebAuthn plus CTAP2.\n\n== Timeline\n<timeline>\n#figure(\n  align(center)[#table(\n    columns: (11.25%, 88.75%),\n    align: (auto,auto,),\n    table.header([Year], [Event],),\n    table.hline(),\n    [2012], [FIDO Alliance founded],\n    [2014], [FIDO 1.0: #strong[U2F] (2nd-factor keys) and #strong[UAF]\n    (passwordless mobile)],\n    [2018--2019], [#strong[FIDO2]: WebAuthn (W3C) + CTAP2; U2F becomes\n    CTAP1],\n    [2022], [Apple/Google/Microsoft announce #strong[passkeys] (synced\n    FIDO2 credentials)],\n  )]\n  , kind: table\n  )\n\nYour YubiKey 5 NFC supports both generations. The \"U2F\" and \"FIDO2\"\nentries in Yubico Authenticator or `ykman info` are those two layers.\n"
        }
      ]
    }
  ]
}
