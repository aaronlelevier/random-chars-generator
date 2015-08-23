# random-chars-generator
Generate random characters or number easily

### Usage
```python
from randoms import Randoms

# give me a random integer with a length of 4
Randoms().integer(4)
```

### Motivation
This is a helper library mostly motivated by [Django](https://www.djangoproject.com/) 
to make this. Reasons to use this:

* A Model has a unique constraint on one of the fields. *i.e. number* or 
*guest name*. In this case you would need to generate a unique value easily, 
and **to have randomly harcoded unique values in tests is problematic**, 
hence the motivation for this simple library.


### Run tests
```
python tests.py
```
