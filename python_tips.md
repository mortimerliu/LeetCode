# Python Tips<!-- omit from toc -->

- [Flat list of list](#flat-list-of-list)
- [Update a key in dict if it doesn't exist](#update-a-key-in-dict-if-it-doesnt-exist)

## [Flat list of list](https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists)

```python
flat_list = [item for sublist in l for item in sublist]
```

## [Update a key in dict if it doesn't exist](https://stackoverflow.com/questions/42315072/python-update-a-key-in-dict-if-it-doesnt-exist)

```python
d = {'key1': 'one'}
d.setdefault('key1', 'some-unused-value')
# 'one'
d # d has not changed because the key already existed
# {'key1': 'one'}
d.setdefault('key2', 'two')
# 'two'
d
# {'key1': 'one', 'key2': 'two'}
```
