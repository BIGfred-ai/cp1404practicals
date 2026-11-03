
"""Program that stores users' emails (unique keys)
and names (values) in a dictionary.
Estimate: 40 minutes
Actual:  60  minutes
"""


def main():
    """Main menu loop"""
    email_to_name = {}

    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        name = determine_name(name)
        email_to_name[email] = name

        email = input("Email: ")

    print()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email address by splitting, and joining"""
    name = email.split("@")[0]
    parts = name.split(".")
    name = " ".join(parts).title()
    return name


def determine_name(name):
    """Confirm the extracted name or ask for a correction."""
    answer = input(f"Is your name {name}? (Y/n) ")

    if answer == "" or answer.lower() == "y":
        return name

    return input("Name: ")


main()
