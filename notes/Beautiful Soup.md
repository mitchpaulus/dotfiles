```python
# pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')

# Search recursively
soup.find_all('a')

# find is basically find_all with limit=1

tag['my_attr']  # Get attribute value

'myclass' in tag['class']  # Check if class exists

soup.find_all(class_='myclass')  # Find all with class 'myclass', '_' is to avoid conflict with Python keyword

tag.contents # Get all children of tag


```
