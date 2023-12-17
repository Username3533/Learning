#work with lists

""" friends_names = ['richard', 'justin', 'tony']
print(type(friends_names))
print(f"I like that we are friends", {friends_names[0].title()})
print(f"I like that we are friends", {friends_names[1].title()})
print(f"I like that we are friends", {friends_names[2].title()})

friends_names.append(input("Do you have any other friends? : "))
print(friends_names) """

guest_list = ["richard", "mark", "alan", "ryan"]

def announce_guests():
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

print(guest_list)