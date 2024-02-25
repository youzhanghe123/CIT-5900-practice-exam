from SystemCreator import *
from SystemManager import *
from SystemExporter import *

def main():
    # Instantiate the other classes
    creator = SystemCreator()
    manager = SystemManager()
    exporter = SystemExporter()
    
    # Create database of users and empty database of logged-in users
    users, logged_in = creator.init_db('users.csv')

    while True:
        # Print options
        print("Options:\n"
              "Press 1 to log in\n" +
              "Press 2 to sign up\n" +
              "Press 3 to change password\n" +
              "Press 4 to delete account\n" +
              "Press 5 to show statistics (sign-ups and log-ins)\n" +
              "Press 6 to save all sign-ups to the file\n" +
              "Press 0 to quit\n")

        # Get user input
        option_input = input()

        # Try to cast as int
        try:
            option = int(option_input)

        # Catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            if option == 0:
                # Quit
                print("Goodbye!")
                break
            elif option == 1:
                # Log in
                username = input("username: ")
                password = input("password: ")

                success = manager.log_in(users, logged_in, username, password)
            elif option == 2:
                # Sign up
                username = input("username: ")
                password = input("password: ")

                success = manager.sign_up(users, logged_in, username, password)
            elif option == 3:
                # Change password
                username = input("username: ")
                old_password = input("old password: ")
                new_password = input("new password: ")

                success = manager.change_password(users, username, old_password, new_password)
            elif option == 4:
                # Delete account
                username = input("username: ")
                password = input("password: ")

                success = manager.delete_account(users, logged_in, username, password)
            elif option == 5:
                # Show statistics
                print('Signed up users:', manager.get_sign_ups(users))
                print('Logged in users:', manager.get_log_ins(logged_in))
            elif option == 6:
                # Save user credentials to 'users_output.csv'
                exporter.write_users_db(users, 'users_output.csv')
                print("Saved!")

            print("=" * 80)


if __name__ == "__main__":
    main()