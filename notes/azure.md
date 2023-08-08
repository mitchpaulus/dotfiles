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

```Powershell
$env:AZCOPY_CRED_TYPE = "Anonymous";
$env:AZCOPY_CONCURRENCY_VALUE = "AUTO";
./azcopy.exe copy "D:\att\dallas toll\104 Field Notes\2020-10-28_walk through pics\" "https://commandblobdata.blob.core.windows.net/datablob/Photo%20Video/Dallas%20Toll/?sv=2021-10-04&se=2023-08-10T19%3A11%3A02Z&sr=c&sp=rwl&sig=w36Uea6FFoXlFoo9DLuogOWclRE%2BD5HIdGjD7FooeXU%3D" --overwrite=prompt --from-to=LocalBlob --blob-type BlockBlob --follow-symlinks --check-length=true --put-md5 --follow-symlinks --disable-auto-decoding=false --recursive --log-level=INFO;
$env:AZCOPY_CRED_TYPE = "";
$env:AZCOPY_CONCURRENCY_VALUE = "";
```


```sh
# Copying file from local to blob
azcopy cp "/path/to/file.txt" "https://[account].blob.core.windows.net/[container]/[path/to/blob]"
azcopy cp "/path/to/dir" "https://[account].blob.core.windows.net/[container]/[path/to/directory]?[SAS]" --recursive=true

# Blob to local file
az storage blob download --account-name mystorageaccount --name myfile --container-name mycontainer --type block --file ./downloaded_file --auth-mode login
# Need at least `Storage Blob Data Reader` role for the storage account.

```


# `az` vs. `azcopy`

ChatGPT tells me that `az` can handle Azure AD-based authentication, while `azcopy` can't.

# Roles

<https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access?tabs=portal>

> To access blob data in the Azure portal with Azure AD credentials, a user must have the following role assignments:

> - A data access role, such as Storage Blob Data Reader or Storage Blob Data Contributor
> - The Azure Resource Manager Reader role, at a minimum
