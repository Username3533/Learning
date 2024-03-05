#work with lists

""" friends_names = ['richard', 'justin', 'tony']
print(type(friends_names))
print(f"I like that we are friends", {friends_names[0].title()})
print(f"I like that we are friends", {friends_names[1].title()})
print(f"I like that we are friends", {friends_names[2].title()})

friends_names.append(input("Do you have any other friends? : "))
print(friends_names) """

#guest_list = ["richard", "mark", "alan", "ryan"]

""" def announce_guests():
    for name in guest_list:
        print(f'{name}, you are invited to diner!')

announce_guests()

print(guest_list)
uninvited_guest = guest_list[-1]
guest_list.pop()
print(guest_list)
print(uninvited_guest)
guest_list.append("jack")
print(guest_list)

announce_guests()

print("\nSome more seats have opened up!")
guest_list.insert(0, "steven")

half_list = len(guest_list) / 2
print(half_list)
guest_list.insert(round(len(guest_list) / 2), "opingheimer")

guest_list.append("newton")

print(f"\n{guest_list}")

announce_guests()

print("\nI am sorry, things have changed, I can no only invite 2 people.")

def uninvite_guests():
    while len(guest_list) > 2:
        guest_list.pop()
    return guest_list

uninvite_guests()


print(guest_list)

announce_guests()

def uninvite_all():
    while len(guest_list) > 0:
        del guest_list[0]
    return guest_list

uninvite_all()

print(guest_list) """

""" print(guest_list)
print(sorted(guest_list))
print(guest_list)
 """
""" print(guest_list)
guest_list.reverse()
print(guest_list) """

#list comprehension

""" squares = [value**2 for value in range(1, 11)] #list comprehension for squares
print(squares)

#prints values but returns none for values if print used in comprehension
comprehension_test = [print(value) for value in range(1 , 21)] 
print(comprehension_test)

comprehension_test_odds = [print(value) for value in range(1 , 21, 2)]

cubes = [value**3 for value in range(1, 11)]
print(cubes[0 : 5]) #slice
copy_list = squares[:] #copy using slice

print(copy_list) """

""" test = [value*1 for value in range(1, 101)]
print(test)

for value in test:
    if value % 2 == 0:
        print(value)
    else:
        print("not even") """

""" #tuples

numbers = (1, 2, 3, 4, 6, 7, 8, 12, 31, 52)

print(numbers[0 : 4])

for number in numbers:
    print(number)
 """

#Compare 2 strings for common substrings algo - Dynamic O(n*m)
def longest_common_substring(string1, string2):
    m = len(string1)
    n = len(string2)

    # Initialize dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_index = 0

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    start_index = end_index - max_length
    substring = string1[start_index:end_index]

    return substring


string1 = "abcdefg"
string2 = "xyzabcde"
print(longest_common_substring(string1, string2))
