# Requests

Posting JSON data

```python
cookies = { 'name': 'value' }
headers =  { 'header': 'value' }
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload, cookies=cookies, headers=headers)
```
