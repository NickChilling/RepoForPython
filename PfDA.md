

# Python for Data Analysis

[TOC]

## Some features of `ipython`

### Tab completion

### `?`

anything plus a `?` in `ipython` , will give you the annotation of that .

### `%run`

run `.py` file in `ipython`, just like run it in the `power shell`

use `%run -i ` to give a script access to the defined namespace in `ipython`

`%load` imports a script into a code cell

![1532005959533](C:\Users\zanzh\RepoForPython\assets\1532005959533.png)

### `%matplotlib`

In the `ipython` shell, running `%matplotlib` sets up the integration so you can create multiple plot windows without interfering with the console session

### Ternary expression

`value = true-expr if condition else false-expr`



## `Numpy`

### Basics

all the elements must be the same type

```python
>>> data.shape # dimension of data
(2,3)
>>> data.dtype # type of data
dtype('float64')
```

like dictionaries closed by `{}` ,lists closed by `[]`, arrays is closed by `([])`

```python
np.zeros((3,6)) # pass a tuple into it to output a 3*6 matrix 
```

![1532009920870](C:\Users\zanzh\RepoForPython\assets\1532009920870.png)

### Datatypes

```python
arr1 = np.array([1,2,3],dtype=np.float64) # initialize

arr2 = arr1.astype(np.int64) # transform

```

