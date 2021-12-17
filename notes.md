```python
# Checks the opposite
1 != 1
False
```
```python
1 == 1
True
```
```python
name = input('Your name: ')
Your name: Max
name != 'Chris'
True
```
```python
1 is 1
True
```
```python
data = [1, 1.5, 3.4]
test_data = [1, 1.5, 3.5]
# Check the value
data == test_data
True
---------
# Check the object
data is test_data
False
---------
# check data
1 in data
True
---------
# check data
2 in data
False
---------
2 not in data
True
---------
1 not == 1
error
```
```python
# and 
age = 29
if age > 20 and age < 30:
    print('Between 20 and 20')

# or 
if age < 30 or age > 60:
    print('Not between 30 and 60')

# both
if age > 20 and age < 30 or age > 60:
    print('Yes')
```

### Grouping conditionals

```python
name = 'Max'
age = 29 
if name == 'chris' and age > 20 or age < 30:
    print('Yes')
# Es yes porque no toma el condicional and
Yes

if name == 'chris' and (age > 20 or age < 30):
    print('Yes')
```