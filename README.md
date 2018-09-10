# TCC

Simple Library for splitting an array into given number of chunks. If the input array cannot be divided equally, the
final chunk is going to store the remainder.

## Getting started

### Installation
Install the package using pip ```pip install [repository path on disk]```

## Running the tests
Run ```pytest```

## Basic Usage
```python
import tcc

array = [1,2,3,4,5]
chunks = 3

result = tcc.split_array(array, chunks)
# result = [[1,2],[3,4],[5]]
```
