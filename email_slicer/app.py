def main():
    print("Welcome the email slicer app!")

    # Get user's email address
    email = input("What is your email address? ").strip()
    (username, domain) = email.split("@")
    (domain, extension) = domain.split(".")

    print(f"Your username is {username}")
    print(f"Your domain is {domain}")
    print(f"Your extension is {extension}")


main()
