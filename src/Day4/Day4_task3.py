friend_a = {"Python", "Cooking", "Hiking", "Movies"}
print(friend_a)
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_b)
Shared_interests = friend_a & friend_b
print("Shared_Interests:", Shared_interests)
All_interests=friend_a | friend_b
print("All_interests:",All_interests)
Unique_interests=friend_a-friend_b
print("Unique_interests:",Unique_interests)#difference