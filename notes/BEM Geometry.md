# Floor plan layout process

1. Breakdown floor plan into rectangles using something like Bluebeam
2. Get 1-D list of y's and x's. Two y's and two x's for each rectangle
3. Cluster the y's and x's
4. Build mapping from actual y to new cluster mean
5. Transform each rectangle into new discrete cluster coordinates
6. Print to SVG using something like `idf_surface_draw.py` from Repo below
6. Merge desired adjacent rectangles into new polygons


# References

- <https://github.com/mitchpaulus/surface-matching>
