# CLI

Environment variables:

- `B2_APPLICATION_KEY_ID`
- `B2_APPLICATION_KEY`

```
b2 ls BUCKET_NAME path/to/prefix
b2 upload-file BUCKET_NAME local-file-name remote-file-name
b2 download-file B2_URI local-file-name

B2_URI = b2://BUCKET_NAME/remote-file-name
```

## Pricing

- $6/TB/Month (or $0.60/100 GB/Month)
- Class 'A' transactions, free
- Class 'B' transactions, $0.004/10,000 with 2,500 free per day
- Class 'C' transactions, $0.004/1,000 with 2,500 free per day

Class B:

- `b2_download_file_by_id`
- `b2_download_file_by_name`
- `b2_get_file_info`

Class C:

- `b2_authorize_account`
- `b2_copy_file`
- `b2_copy_part`
- `b2_create_bucket`
- `b2_create_key`
- `b2_get_download_authorization`
- `b2_list_buckets`
- `b2_list_file_names`
- `b2_list_file_versions`
- `b2_list_keys`
- `b2_list_parts`
- `b2_list_unfinished_large_files`
- `b2_update_bucket`
