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


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.date = time.strftime("%Y-%m-%d %H:%M:%S")

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.followers = []
        self.bio = ""
        self.followings = []
        self.posts = []
        self.stories = []
        self.blocked_users = []
        self.saved_posts = []
        self.follow_requests = []
        self.privacy = "public"

users = []
chats = dict()

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
        print("3. Exit (Close program)")
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
    
    print("Actions:")
    print("1. Save post")
    print("2. Comment on post")
    print("3. Like post")
    
    while True:
        choice = input("Please choose an option (1-3) or 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == '1':
            while True:
                choice = input("Enter the number of the post to save or 'q' to quit: ")
                if choice == 'q':
                    break
                try:
                    choice = int(choice)
                    if choice not in post_list:
                        print("Invalid choice. Please try again.")
                        continue
                    id = post_list[choice]
                    users[id].posts[-1].saves += 1
                    users[user_id].saved_posts.append(users[id].posts[-1])
                    print(f"You saved {users[id].posts[-1].content} by @{users[id].username}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
        elif choice == '2':
            while True:
                choice = input("Enter the number of the post to comment on or 'q' to quit: ")
                if choice == 'q':
                    break
                try:
                    choice = int(choice)
                    if choice not in post_list:
                        print("Invalid choice. Please try again.")
                        continue
                    id = post_list[choice]
                    comment = input("Enter your comment: ")
                    users[id].posts[-1].comments.append(comment)
                    print(f"You commented on {users[id].posts[-1].content} by @{users[id].username}.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
        elif choice == '3':
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
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
        else:
            print("Invalid choice. Please try again.")
        break

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
            print(f"❤️ Likes: {users[user].stories[-1].likes}")
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
    print()
    print("Your chats:")
    print()
    mark = dict()
    for i, chat in enumerate(chats.keys()):
        if user_id == chat[0] or user_id == chat[1]:
            print(f"🆔 {len(mark) + 1}. Chat with @{users[chat[1]].username if user_id == chat[0] else users[chat[0]].username}")
            mark[len(mark) + 1] = chat
    if len(mark) == 0:
        print("No chats available.")
        
    while True:
        print()
        print("Actions:")
        print("1. Start new chat")
        print("2. Open chat")
        print("3. Delete chat")
        print()
        choice = input("Please choose an option (1-3) or 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == '1':
            id = -1
            username = input("Enter the username to chat with: ")
            for index,user in enumerate(users):
                if user.username == username and user_id != index and user_id not in user.blocked_users:
                    id = index
                    break

            if id == -1:
                print("User not found.")
                continue
            if (user_id, id) not in chats.keys() and (id, user_id) not in chats.keys():
                chats[(min(user_id, id),max(user_id, id))] = []
            print(f"Chat started with @{users[id].username}. Open the chat to send messages.")
        elif choice == '2':
            if len(mark) == 0:
                print("No chats available.")
                continue
            while True:
                choice = input("Enter the number of the chat to open or 'q' to quit: ")
                if choice == 'q':
                    break
                try:
                    choice = int(choice)
                    if choice not in mark:
                        print("Invalid choice. Please try again.")
                        continue
                    id = mark[choice]
                    print(f"Chat with @{users[id[1]].username if user_id == id[0] else users[id[0]].username}:")
                    for message in chats[id]:
                        print(f"{users[message.sender].username}: {message.content} (Sent on {message.date})")
                    print()
                    content = input("Enter your message: ")
                    new_message = Message(user_id, content)
                    chats[id].append(new_message)
                    print("Message sent successfully!")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '3':
            if len(mark) == 0:
                print("No chats available.")
                continue
            while True:
                choice = input("Enter the number of the chat to delete or 'q' to quit: ")
                if choice == 'q':
                    break
                try:
                    choice = int(choice)
                    if choice not in mark:
                        print("Invalid choice. Please try again.")
                        continue
                    id = mark[choice]
                    chats.pop(id)
                    print("Chat deleted successfully!")
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please try again.")
            continue

def create_post():
    print()
    print("Create a new post")
    content = input("Enter the content of the post: ")
    new_post = Post(content, user_id)
    users[user_id].posts.append(new_post)
    print("Post created successfully!")

def create_story():
    print()
    print("Create a new story")
    content = input("Enter the content of the story: ")
    new_story = Story(content, user_id)
    users[user_id].stories.append(new_story)
    print("Story created successfully!")

def see_follow_requests():
    print()
    print("Follow Requests:")
    if len(users[user_id].follow_requests) == 0:
        print("No follow requests.")
        return
    
    for i,user in enumerate(users[user_id].follow_requests):
        print(f"{i + 1}. @{users[user].username}")

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
    username = input("Enter the username to search: ")
    id = -1
    for index,user in enumerate(users):
        if user.username == username and user_id != index and user_id not in user.blocked_users:
            id = index
            break
    
    if id == -1:
        print("User not found.")
        return
    print(f"🆔 User found: @{users[id].username}")
    print(f"📝 Bio: {users[id].bio}")
    print(f"👥 Followers: {len(users[id].followers)}")
    print(f"👥 Followings: {len(users[id].followings)}")
    print(f"📰 Posts: {len(users[id].posts)}")
    print(f"📰 Privacy type: {users[id].privacy}")
    print()
    print("-----------------------------------")
    print()
    
    print("Actions:")
    
    # if current user is following searched user show unfollow option otherwise show follow option
    if id in users[user_id].followings:
        print("1. Unfollow")
    else:
        print("1. Follow")

    # if current user has blocked searched user show unblock option otherwise show block option
    if id in users[user_id].blocked_users:
        print("2. Unblock")
    else:
        print("2. Block")

    while True:
        choice = input("Please choose an option (1-2) or 'q' to quit: ")
        if choice == 'q':
            break
        if choice == '1':
            if id in users[user_id].followings:
                users[user_id].followings.remove(id)
                users[id].followers.remove(user_id)
                print(f"You unfollowed @{users[id].username}.")
            else:
                if users[id].privacy == "private":
                    users[id].follow_requests.append(user_id)
                    print(f"Follow request sent to @{users[id].username}.")
                else:
                    users[user_id].followings.append(id)
                    users[id].followers.append(user_id)
                    print(f"You followed @{users[id].username}.")
            break
        elif choice == '2':
            if id in users[user_id].blocked_users:
                users[user_id].blocked_users.remove(id)
                print(f"You unblocked @{users[id].username}.")
            else:
                users[user_id].blocked_users.append(id)
                print(f"You blocked @{users[id].username}.")

            break
        else:
            print("Invalid choice. Please try again.")

# =======================================

def edit_profile():
    print()
    print("Edit your profile")
    print("1. Change username")
    print("2. Change email")
    print("3. Change password")
    print("4. Change bio")
    choice = input("Please choose an option (1-4) or q to quit: ")
    if choice == 'q':
        return
    elif choice == '1':
        new_username = input("Enter new username: ")
        users[user_id].username = new_username
        print(f"Username changed to {new_username}.")
    elif choice == '2':
        new_email = input("Enter new email: ")
        users[user_id].email = new_email
        print(f"Email changed to {new_email}.")
    elif choice == '3':
        new_password = input("Enter new password: ")
        users[user_id].password = new_password
        print("Password changed successfully.")
    elif choice == '4':
        new_bio = input("Enter new bio: ")
        users[user_id].bio = new_bio
        print("Bio changed successfully.")
    else:
        print("Invalid choice. Please try again.")

def see_my_posts():
    print()
    print("See your posts")
    if len(users[user_id].posts) == 0:
        print("No posts available.")
        return
    
    for i, post in enumerate(users[user_id].posts):
        print(f"{i + 1}. {post.content} (Posted on {post.date})")
        print(f"❤️ Likes: {post.likes}")
        print(f"💾 Saved: {post.saves}")
        print("Comments: ")
        for comment in post.comments:
            print(f"- {comment}")
        print()
    
    while True:
        choice = input("Enter the number of the post to delete or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(users[user_id].posts):
                print("Invalid choice. Please try again.")
                continue
            users[user_id].posts.pop(choice - 1)
            print("Post deleted successfully.")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def see_saved_posts():
    print()
    print("See your saved posts")
    if len(users[user_id].saved_posts) == 0:
        print("No saved posts available.")
        return
    
    for i, post in enumerate(users[user_id].saved_posts):
        print(f"🆔 {i + 1}. @{users[post.user].username}")
        print(f" {post.content} (Posted on {post.date})")
        print(f"❤️ Likes: {post.likes}")
        print(f"💾 Saved: {post.saves}")
        print("Comments: ")
        for comment in post.comments:
            print(f"- {comment}")
        print()
    
    while True:
        choice = input("Enter the number of the post to unsave or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(users[user_id].saved_posts):
                print("Invalid choice. Please try again.")
                continue
            users[user_id].saved_posts.pop(choice - 1)
            print("Post unsaved successfully.")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def privacy_settings():
    print()
    print("Privacy Settings")
    print("1. Public")
    print("2. Private")
    choice = input("Please choose an option (1-2): ")
    if choice == '1':
        users[user_id].privacy = "public"
        print("Your profile is now public.")
    elif choice == '2':
        users[user_id].privacy = "private"
        print("Your profile is now private.")
    else:
        print("Invalid choice. Please try again.")

def see_blocked_users():
    print()
    print("Blocked Users:")
    if len(users[user_id].blocked_users) == 0:
        print("No blocked users.")
        return
    
    for i, user in enumerate(users[user_id].blocked_users):
        print(f"{i + 1}. @{users[user].username}")

    while True:
        choice = input("Enter the number of the user to unblock or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(users[user_id].blocked_users):
                print("Invalid choice. Please try again.")
                continue
            id = users[user_id].blocked_users[choice - 1]
            users[user_id].blocked_users.remove(id)
            print(f"You unblocked @{users[id].username}.")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

def profile_menu():
    while True:
        print()
        print("Welcome to the Profile Menu")
        print("1. Edit profile")
        print("2. See my posts")
        print("3. See saved posts")
        print("4. Privacy settings (public/private)")
        print("5. See blocked users")
        print("6. Exit")
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
        print("5. Exit (Close program)")

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