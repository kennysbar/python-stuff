#get user email address

email = input("What is your email address?: ").strip()

#slice out user name

user = email[:email.index("@"):]
print(user)

#slice domain name

domain = email[email.index("@"):].strip("@")
print(domain)

# format message

output = "Your username is {} and you domain name is {}" .format(user,domain)
print(output)
#display output message
