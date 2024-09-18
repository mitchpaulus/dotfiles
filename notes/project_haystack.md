# Project Haystack

## Handling VFDs

See chapter on [Motors](https://project-haystack.org/doc/docHaystack/Motors).

Depending on units, use either `freq` for 0-60 Hz or `speed` for 0-100.

The `vfd` tag should usually be used on the `equip` record, not the
`point`.

Other tags: `fan`, `discharge` (for supply fan)

From docs:

> Fans may optionally be defined as either an equip or a point. If the
> fan motor is driven by a VFD then it is recommended to make the fan a
> sub-equip. However in many cases a simple fan in a terminal unit such
> as a vav is more easily modeled as just a point.

## Common tags

- `discharge`
- `temp`
- `sp` (setpoint)
- `sensor` (sensors)
- `cmd` (command)
