def setupFiles():
     with open("password.txt", "w") as pas:
          password = input("Enter password: ")
          pas.write(password)
     with open("mail.txt", "w") as mal:
          mail = input("Enter mail address: ")
          mal.write(mail)