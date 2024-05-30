```python
# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

# Search recursively
soup.find_all('a')
```
