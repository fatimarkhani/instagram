auth = False

def login():
    pass

def register():
    pass

def auth_menu():
    print("Welcome to the Authentication Menu")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    while not auth:
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
    pass

def see_stories():
    pass

def see_messages():
    pass

def create_post():
    pass

def create_story():
    pass

def see_follow_requests():
    pass

def home_menu():
    print()
    print("Welcome to the Home Menu")
    print("1. See posts")
    print("2. See stories")
    print("3. See Messages")
    print("4. Create a post")
    print("5. Create a story")
    print("6. See follow requests")
    print("7. Exit")

    while True:
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
    print("Welcome to the Main Menu")
    print("1. Home")
    print("2. Search")
    print("3. Profile")
    print("4. Exit")

    while True:
        choice = input("Please choose an option (1-4): ")
        if choice == '1':
            home_menu()
        elif choice == '2':
            search_menu()
        elif choice == '3':
            profile_menu()
        elif choice == '4':
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

# =======================================

if __name__ == "__main__":
    auth_menu()
    main_menu()