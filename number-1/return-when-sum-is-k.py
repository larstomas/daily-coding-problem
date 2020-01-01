list_of_numbers = [10, 15, 3, 7]
k = 17

print(len(list_of_numbers))

def two_sum(list_of_numbers, k):
    k_friends = []  # A k_friend
    for num in list_of_numbers:
        if num in k_friends:
            print("True, numbers: " + str(num) + " " + str(k - num))
            return True
        k_friends.append(k - num)
    return False


print(two_sum(list_of_numbers, k))
