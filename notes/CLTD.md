# Cooling Load Temperature Difference


1. Get roof/wall number type from construction
2. Look up standard CLTD value from table

  - Walls: Appendix B -> Appendix C
  - Roofs: Table 8-1 -> Table 8-2

3. Correct for different indoor temperature or mean outdoor temperature

   CLTD_c = CLTD + (78 - Ti) + (Tm - 85)

4. Add correction for latitude and month (Table 8-4). Not used for conduction through glass
