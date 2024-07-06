print("Welcome to Email Slider !!! \n")
email = input("Please enter your email: ")

(username, domain) = email.split("@")
(domain, extension) = domain.split(".")
print("Your username is: " + username)
print("Your domain is: " + domain)
print("Your extension is:" + extension)