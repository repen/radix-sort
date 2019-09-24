'''
    Radix sort on Python
    Me very helped debug with instrument "import pdb; pdb.set_trace()"
'''
import random
def len_number(num):
    c = 0
    while num:
        num //= 10
        c += 1
    return c

def normalize(array):
    new_array = []
    for e, arr in enumerate(array):
        for ar in arr:
            new_array.append(ar)
    return new_array

def radix_sort(array):
    shift = 1
    for x in range(len_number(max(array))):
        result = [[] for _ in range(10)]
        numbers = [x for x in range(10)]

        for e, num in enumerate(numbers):
            for arr in array:
                if num == arr % (shift * 10) // shift:
                    result[e].append(arr)
        array = normalize(result)
        shift = shift * 10

    return array

if __name__ == '__main__':
    # array = [random.randint(1,1000) for x in range(10)]
    array = [312, 333, 135, 404, 954, 127, 377, 245, 588, 752]
    result = radix_sort(array)
    print(array)
    print(result)
