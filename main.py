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
    print("Welcome to the Home Menu")
    print("1. See posts")
    print("2. See stories")
    print("3. See Messages")
    print("4. Create a post")
    print("5. Create a story")
    print("6. See follow requests")
    print("7. Exit")

    while not auth:
        choice = input("Please choose an option (1-3): ")
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
            print("Exiting the program.")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    auth_menu()
    home_menu()