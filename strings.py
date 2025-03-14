email = "rafael.avigad@nmtafe.wa.edu.au"
def get_domain(email):
    return email[email.find('@') + 1:]
print("Your Domain is> " + get_domain(email))