
from time import process_time

def measureTime(method, n, *args):
    start = process_time()
    for _ in range(n):
        method(*args)
    end = process_time()
    return (end - start) / n

###
list_of_numbers_1 = [1, 2, 3, 4, 5]
list_of_numbers_2 = [3, 2, 1]
list_of_numbers_3 = [10, 15, 3, 7]
list_of_numbers_4 = list(range(1, 1001))


def array_product_mod(list_of_numbers):
    array_product = 1
    list_of_products = []

    for num in list_of_numbers:
        array_product *= num

    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] != 0:
            list_of_products.append(array_product // list_of_numbers[i])
        else:
            print("Error divition by zero")

    return list_of_products


def array_product_mod_non_division(list_of_numbers):
    list_of_products = []
    list_range = range(len(list_of_numbers))

    for i in list_range:
        array_product = 1
        if list_of_numbers[i] != 0:
            for j in list_range:
                if j != i:
                    array_product *= list_of_numbers[j]
            list_of_products.append(array_product)
        else:
            print("Error divition by zero")

    return list_of_products


repetitions = 1

print(array_product_mod(list_of_numbers_1))
print (measureTime(array_product_mod, repetitions, list_of_numbers_1) * 1000, 'ms')
print(array_product_mod_non_division(list_of_numbers_1))
print (measureTime(array_product_mod_non_division, repetitions, list_of_numbers_1) * 1000, 'ms')
print()

print(array_product_mod(list_of_numbers_2))
print (measureTime(array_product_mod, repetitions, list_of_numbers_2) * 1000, 'ms')
print(array_product_mod_non_division(list_of_numbers_2))
print (measureTime(array_product_mod_non_division, repetitions, list_of_numbers_2) * 1000, 'ms')
print()

print(array_product_mod(list_of_numbers_3))
print (measureTime(array_product_mod, repetitions, list_of_numbers_3) * 1000, 'ms')
print(array_product_mod_non_division(list_of_numbers_3))
print (measureTime(array_product_mod_non_division, repetitions, list_of_numbers_3) * 1000, 'ms')
print()

#print(array_product_mod(list_of_numbers_4))
print (measureTime(array_product_mod, repetitions, list_of_numbers_4) * 1000, 'ms')
#print(array_product_mod_non_division(list_of_numbers_4))
print (measureTime(array_product_mod_non_division, repetitions, list_of_numbers_4) * 1000, 'ms')
print()


# Anwser when [1, 2, 3, 4, 5]: [120, 60, 40, 30, 24]
# Anwser when [3, 2, 1]: [2, 3, 6]
