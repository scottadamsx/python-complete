# Email Creator
import csv


def title():
    print("Email Creator")

def read_file():
    FILENAME = "contact_emails.csv"
    contacts = []
    with open(FILENAME) as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def read_sample_email():
    FILENAME = "email_template.txt"
    with open(FILENAME) as file:
        email = file.read()
    return email

def display_email(contact, email):
    email = email.replace("{email}", contact[2])
    firstName = contact[1].capitalize()
    email = email.replace("{first_name}", firstName)
    print(email)


def main():

    title()
    contacts = read_file()
    email = read_sample_email()
    for contact in contacts:
        display_email(contact, email) 


if __name__ == "__main__":
    main()
