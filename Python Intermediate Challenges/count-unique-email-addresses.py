# Write a function to count the number of unique email addresses from a list of emails

def count_unique_emails(emails):

    return len(set(emails))

emails = ['a@b.c', 'x@y.z', '1@2.3']

print(count_unique_emails(emails))