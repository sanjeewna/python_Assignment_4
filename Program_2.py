def login():
    # Define the correct username and password
    correct_username = "python"
    correct_password = "rules"

    # Initialize login attempts counter
    attempts = 0

    # Start the login loop
    while attempts < 5:
        # Ask the user to enter username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if username and password are correct
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return  # Exit the function if login is successful
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1

    # If the loop exits due to 5 failed attempts
    print("Access denied.")

# Start the login process
login()
