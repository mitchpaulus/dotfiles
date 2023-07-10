# Azure

## Storage Products

### Azure Files

Cloud file shares.

4 tiers:

1. Premium
2. Transaction optimized
3. Hot
4. Cool


### Blob Storage

Data storage prices pay-as-you-go | Premium      | Hot           | Cool         | Cold (preview) | Archive
----------------------------------|--------------|---------------|--------------|----------------|----------------
First 50 terabyte (TB) / month    | $0.15 per GB | $0.018 per GB | $0.01 per GB | $0.0036 per GB | $0.00099 per GB

Cool Storage
100 Gb = $1 / month.
1 Tb = $10 / month.

Operations and data transfer                                    | Premium | Hot    | Cool   | Cold (preview) | Archive
----------------------------------------------------------------|---------|--------|--------|----------------|--------
Write operations (per 10,000)1                                  | $0.0228 | $0.065 | $0.13  | $0.234         | $0.13
Read operations (per 10,000)2                                   | $0.0019 | $0.005 | $0.013 | $0.13          | $6.50
Iterative Read Operations (per 10,000)3                         | N/A     | $0.005 | $0.013 | $0.13          | $6.50
Iterative Write Operations (100’s)4                             | N/A     | $0.065 | $0.13  | $0.234         | $0.13
Data Retrieval (per GB)5                                        | Free    | Free   | $0.01  | $0.03          | $0.02
Data Write (per GB)                                             | Free    | Free   | Free   | Free           | Free
Index (GB/month)                                                | N/A     | $0.026 | N/A    | N/A            | N/A
All other Operations (per 10,000), except Delete, which is free | $0.0019 | $0.005 | $0.005 | $0.0052        | $0.005
