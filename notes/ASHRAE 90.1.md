Available schedules from 90.1

Assembly
Health
Light Manufacturing
Office
Parking Garage
Restaurant
Retail
School
Warehouse
Laboratory


Piping System Design Max Flow Rate

Table 6.5.4.6 - 2013, same in 2022

Over 14" nominal pipe size:

Hours/Year       | Type     | Velocity ft/s
-----------------|----------|--------------
<2000            | Other    | 8.5
<2000            | Variable | 13
2000 < x <= 4400 | Other    | 6.5
2000 < x <= 4400 | Variable | 9.5
>4400            | Other    | 5
>4400            | Variable | 7.5


# 2016 and beyond

Baseline is a fixed "pseudo-2004" standard.
Now there is a "Building performance factor" which is basically the factor that a building using whatever current version of standard will hit as compared to 2004.
Makes the baseline building items not change from revision year to revision year, allowing automation.

<https://chatgpt.com/c/691b3faf-bb74-8327-8981-d937e729e389>

- <https://www.energy.gov/eere/buildings/articles/building-energy-modeling-101-inherent-performance-rating-use-case>


## Fan Power Limitation

```
BHP <= CFMs * 0.0013 + A
A = PD * CFMd / 4131
```


0.0013 hp/CFM at 70% total efficiency is 5.772 in. wc.

For System 6 parallel fan power boxes, 0.35 W/cfm at 70% efficiency is 2.084 inH2O.
