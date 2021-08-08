import re

txt_path = 'assets/potential-contacts.txt'
email_write_path = 'assets/found-emails.txt'
phone_write_path = 'assets/found-phone-numbers.txt'
# txt_path = 'assets/test.txt'

def find_emails():
    with open(txt_path) as file:
        for_regex = file.read()
        emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', for_regex)
        print(emails)
        # return emails
    with open(email_write_path, 'w') as writer:
        for email in emails:
            writer.write(email + '\n')

print(find_emails())

def find_phone_numbers():
    with open(txt_path) as file:
        for_regex = file.read()
        phone_numbers = re.findall(r'\(?\d{3}\)?-? *\d{3}-? *-?\d{4}', for_regex)
        # return phone
    with open(phone_write_path, 'w') as writer:
        for number in phone_numbers:
            writer.write(number + '\n')
        
print(find_phone_numbers())

