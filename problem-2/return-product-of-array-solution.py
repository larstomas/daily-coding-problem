
from time import process_time

# Funktion för att mäta tiden en annan funktion tar att exikvera
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


def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


repetitions = 1

print(products(list_of_numbers_1))
print (measureTime(products, repetitions, list_of_numbers_1) * 1000, 'ms')
print()

print(products(list_of_numbers_2))
print (measureTime(products, repetitions, list_of_numbers_2) * 1000, 'ms')
print()

print(products(list_of_numbers_3))
print (measureTime(products, repetitions, list_of_numbers_3) * 1000, 'ms')
print()

print (measureTime(products, repetitions, list_of_numbers_4) * 1000, 'ms')
print()


# Anwser when [1, 2, 3, 4, 5]: [120, 60, 40, 30, 24]
# Anwser when [3, 2, 1]: [2, 3, 6]
