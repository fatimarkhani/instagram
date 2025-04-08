import time

auth = False
user_id = 0

class Post:
    def __init__(self, content, user):
        self.content = content
        self.date = time.strftime("%Y-%m-%d %H:%M:%S")
        self.user = user
        self.likes = 0
        self.comments = []
        self.saves = 0


class Story:
    def __init__(self, content, user):
        self.content = content
        self.date = time.strftime("%Y-%m-%d %H:%M:%S")
        self.user = user
        self.likes = 0


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.followers = []
        
        # TODO
        if username != "mehdi":
            self.followings = [0]
        else:
            self.followings = []
        
        # TODO
        self.posts = [Post("salam post", 0)]
        self.stories = [Story("salam story", 0)]
        self.messages = []
        self.blocked_users = []
        self.saved_posts = []
        self.follow_requests = []
        self.privacy = "public"

users = []

# =======================================

def login():
    global auth
    global user_id
    print()
    print("Login to your account")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the username and password match any user
    for i in range(len(users)):
        if users[i].username == username and users[i].password == password:
            print(f"Welcome back, {username}!")
            auth = True
            user_id = i
            return

    print("Invalid username or password. Please try again.")

def register():
    print()
    print("Register a new user")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Check if the username already exists
    for user in users:
        if user.username == username:
            print("Username already exists. Please choose a different one.")
            return
        if user.email == email:
            print("Email already exists. Please choose a different one.")
            return

    # Create a new user and add to the list
    new_user = User(username, email, password)
    users.append(new_user)
    print(f"User {username} registered successfully!")

def auth_menu():
    while not auth:
        print()
        print("----------------------------------")
        print()
        print("Welcome to the Authentication Menu")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Please choose an option (1-3): ")
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

# =======================================

def see_posts():
    print()
    print("-----------------------------------")
    print()
    print("Posts of people you follow:")
    print()
    if len(users[user_id].followings) == 0:
        print("No posts available.")
        return
    
    # keep user id of the user who posted the post
    post_list = dict()
    
    for user in users[user_id].followings:
        if len(users[user].posts) > 0:
            print(f"🆔 {len(post_list) + 1}. @{users[user].username}")
            print(f"📰 {users[user].posts[-1].content} (Posted on {users[user].posts[-1].date})")
            print(f"❤️ Likes: {users[user].posts[-1].likes}")
            print(f"💾 Saved: {users[user].posts[-1].saves}")
            print("Comments: ")
            for comment in users[user].posts[-1].comments:
                print(f"- {comment}")
            print()
            print("-----------------------------------")
            print()
            post_list[len(post_list) + 1] = user
    
    while True:
        choice = input("Enter the number of the post to like or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice not in post_list:
                print("Invalid choice. Please try again.")
                continue
            id = post_list[choice]
            users[id].posts[-1].likes += 1
            print(f"You liked {users[id].posts[-1].content} by @{users[id].username}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def see_stories():
    print()
    print("-----------------------------------")
    print()
    print("Stories of people you follow:")
    print()
    if len(users[user_id].followings) == 0:
        print("No stories available.")
        return
    
    # keep user id of the user who posted the story
    story_list = dict()
    
    for user in users[user_id].followings:
        if len(users[user].stories) > 0:
            print(f"🆔 {len(story_list) + 1}. @{users[user].username}")
            print(f"📰 {users[user].stories[-1].content} (Posted on {users[user].stories[-1].date})")
            print()
            print("-----------------------------------")
            print()
            story_list[len(story_list) + 1] = user
    
    while True:
        choice = input("Enter the number of the story to like or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice not in story_list:
                print("Invalid choice. Please try again.")
                continue
            id = story_list[choice]
            users[id].stories[-1].likes += 1
            print(f"You liked {users[id].stories[-1].content} by @{users[id].username}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
def see_messages():
    pass

def create_post():
    print()
    print("Create a new post")
    content = input("Enter the content of the post: ")
    new_post = Post(content, users[user_id])
    users[user_id].posts.append(new_post)
    print("Post created successfully!")

def create_story():
    print()
    print("Create a new story")
    content = input("Enter the content of the story: ")
    new_story = Story(content, users[user_id])
    users[user_id].stories.append(new_story)
    print("Story created successfully!")

def see_follow_requests():
    print()
    print("Follow Requests:")
    if len(users[user_id].follow_requests) == 0:
        print("No follow requests.")
        return
    
    for i,user in enumerate(users[user_id].follow_requests):
        print(f"{i + 1}. {users[user].username}")

    while True:
        choice = input("Enter the number of the follow request to accept or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(users[user_id].follow_requests):
                print("Invalid choice. Please try again.")
                continue
            id = users[user_id].follow_requests[choice - 1]
            users[id].followings.append(user_id)
            users[user_id].followers.append(id)
            users[user_id].follow_requests.pop(choice - 1)
            print(f"You accepted the follow request from {users[id].username}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid index. Please try again.")

def home_menu():
    while True:
        print()
        print("Welcome to the Home Menu")
        print("1. See posts")
        print("2. See stories")
        print("3. See Messages")
        print("4. Create a post")
        print("5. Create a story")
        print("6. See follow requests")
        print("7. Exit")
        choice = input("Please choose an option (1-7): ")
        if choice == '1':
            see_posts()
        elif choice == '2':
            see_stories()
        elif choice == '3':
            see_messages()
        elif choice == '4':
            create_post()
        elif choice == '5':
            create_story()
        elif choice == '6':
            see_follow_requests()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# =======================================

def search_menu():
    print("Enter the username of the user you want to search for:")
    pass

# =======================================

def edit_profile():
    print("Edit your profile")
    pass

def see_my_posts():
    print("See your posts")
    pass

def see_saved_posts():
    print("See your saved posts")
    pass

def privacy_settings():
    print("Change your privacy settings")
    pass

def see_blocked_users():
    print("See blocked users")
    pass

def profile_menu():
    print()
    print("Welcome to the Profile Menu")
    print("1. Edit profile")
    print("2. See my posts")
    print("3. See saved posts")
    print("4. Privacy settings (public/private)")
    print("5. See blocked users")
    print("6. Exit")

    while True:
        choice = input("Please choose an option (1-6): ")
        if choice == '1':
            edit_profile()
        elif choice == '2':
            see_my_posts()
        elif choice == '3':
            see_saved_posts()
        elif choice == '4':
            privacy_settings()
        elif choice == '5':
            see_blocked_users()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# =======================================

def main_menu():
    while True:
        print()
        print("----------------------------------")
        print()
        print("Main Menu:")
        print("1. Home")
        print("2. Search")
        print("3. Profile")
        print("4. Logout")
        print("5. Exit")

        choice = input("Please choose an option (1-4): ")
        if choice == '1':
            home_menu()
        elif choice == '2':
            search_menu()
        elif choice == '3':
            profile_menu()
        elif choice == '4':
            global auth
            global user_id
            auth = False
            user_id = 0
            print("Logged out successfully.")
            break
        elif choice == '5':
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

# =======================================

if __name__ == "__main__":
    while True:
        if not auth:
            auth_menu()
        else:    
            main_menu()