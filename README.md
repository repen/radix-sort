### Radix Sort Python
In computer science, radix sort is a non-comparative sorting algorithm. 
It avoids comparison by creating and distributing elements into buckets 
according to their radix.

```
import random
from functools import reduce
def len_number(num):
    c = 0
    while num:
        num //= 10
        c += 1
    return c

def radix_sort(array):
    shift = 1
    for x in range(len_number(max(array))):
        result = [[] for _ in range(10)] # [[], [], [], [], [], [], [], [], [], []]
        numbers = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for e, num in enumerate(numbers):
            for arr in array:
                if num == arr % (shift * 10) // shift:
                    result[e].append(arr)
        ============
        First iteration
            result => [[], [], [312, 752], [333], [404, 954], [135, 245], [], [127, 377], [588], []]
            reduce(result) =>  [312, 752, 333, 404, 954, 135, 245, 127, 377, 588]
        ============
        array = reduce(lambda x,y: x+y, result)
        shift = shift * 10

    return array

if __name__ == '__main__':
    result = radix_sort([312, 333, 135, 404, 954, 127, 377, 245, 588, 752])
    print(result) # [127, 135, 245, 312, 333, 377, 404, 588, 752, 954]
```

