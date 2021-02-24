# fruit-database-search-engine :pineapple:

![image](https://www.codefactor.io/repository/github/KennyOliver/fruit-db-search-engine/badge?style=for-the-badge)

[![](https://repl.it/badge/github/KennyOliver/fruit-db-search-engine)](https://repl.it/@KennyOliver/fruit-db-search-engine)

Search a .txt database, holding names of fruits, in Python.
---
```python
import csv #NOT USED!
```
----
#### How to search a file:
```python
def file_search(query):
  file = open("file.xy",'r')
  for record in file:
    if query in record:
      print(record)
  file.close()
```
---
Kenny Oliver ©2021
