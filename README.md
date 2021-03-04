# fruit-db-search-engine :pineapple:

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/fruit-db-search-engine/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/fruit-db-search-engine?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/fruit-db-search-engine?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/fruit-db-search-engine?style=for-the-badge)

[![repl](https://repl.it/badge/github/KennyOliver/fruit-db-search-engine)](https://repl.it/@KennyOliver/fruit-db-search-engine)

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
