# -*- coding: utf-8 -*-


def saveEmail(email_path, message):
    with open(email_path, 'w', encoding="utf-8") as email:
        email.writelines(message)

	
if __name__ == "__main__":

    message = "111"
    email_path = "email.txt"
    saveEmail(email_path, message)
