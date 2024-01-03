class User:
    
    def __init__(self, id, username):
        print("new user being created...")
        self.id = id
        self.username = username
        self.followers = 0

    def enter_race_environment(self):
        self.followers = 2



user_1 = User(5, "Hans")
user_1.enter_race_environment()

print(user_1.id, user_1.username, user_1.followers)
