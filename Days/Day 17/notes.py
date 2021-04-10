#Day 17 - creating classes and were making a True or False quiz today!

#creating your own class in Python

class User:
    #pass #pass skips the function for now

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "Carl")
user_2 = User("002", "Lenny")

print(f"Section 1 answer {user_1.followers}")

#Classes have the first letter of every work Capitalisted (this is called Pascal Case). Camel case is the same but the first word is lower case and the rest are caps and finally snake case where all the words are lowercase but they are seperated by '_' underscores.

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Lenny"


print("- - - - - - - - - - -")
#Adding method to a class

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Carl")
user_2 = User("002", "Lenny")

user_1.follow(user_2)

print(f"user1 follower {user_1.followers} and following {user_1.following}")
print(f"user2 follower {user_2.followers} and following {user_2.following}")

print("- - - - - - - - - - -")



# notes now moves into main project, yay tonnes of debugging.....   what was that challenge between Gilfoyle and Dinesh its not who had had less errors it was who made fewer errors... well lets do this!