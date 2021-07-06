# Requests

Posting JSON data

```python
cookies = { 'name': 'value' }
headers =  { 'header': 'value' }
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

# JSON Post
r = requests.post(url, json=payload, cookies=cookies, headers=headers)

# application/x-www-form-urlencoded
data = { 'key': 'value', 'list key': ['val1', 'val2'] }
r = requests.post(url, data=payload, cookies=cookies, headers=headers)

# Get request
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
```

