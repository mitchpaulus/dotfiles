# SkySpark Setup


## Deployment

- Get Files from <https://skyfoundry.com/downloads>
    - On main header, will see headings like `Doc`, `Forum`, and `Files`. If you have the right permissions, you will see: `Downloads`.
- Unzip
- Make all `bin` files executable
- Smoke test `skyspark -version`
- Run `bin/setup` (Shouldn't need `sudo` if in user directory)
    - Makes superuser `su` account
    - Set port
    - Copy license file
- Usually add the following `start.sh` file to the `bin` directory:

```
#!/bin/sh
./skyspark >stdout.log 2> stderr.log &
```


1. Add site:
  - commit(diff(null, { site, navName: "Site Name", tz: "Chicago", dis: "Site Name" }, {add}))

2. Add equipment
  - AHUs:
    - ["AHU A-1", "AHU B-1", "AHU B-2", "AHU B-3", "AHU C-1", "AHU C-2", "AHU C-3"].map(r => diff(null, { ahu, siteRef: read(site)->id, equip, dis: r, navName: r }, {add})).commit
  - VAVs:
    - diff(null, { vav, equip, siteRef: read(site)->id, dis: "VAV A-1", navName: "VAV A-1", equipRef: read(ahu and dis=="AHU Name" }, {add}).commit

Using my library, looks like:

```
ccllcskyspark.py -d 'http://domain.command-cx.com' --port 8090 -u user --password 'pass' eval vav.axon
```

3. Add Points

```
{
  point, his, sensor | cmd | sp
  hisMode: "sampled" | "cov" | "consumption"
  tz: "Chicago"
  kind: "Bool" | "Number" | "Str"
  siteRef: read(site)->id
  equipRef: read(equip and dis=="something")->id
  dis: "Point Name"
  navName: "Nav name"
}

```
