"""
Emails
Estimate: 15 minutes
Actual:   20 minutes
"""


def main():
    """Create dictionary of emails to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract expected name from email address."""
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


main()
