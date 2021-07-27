# -*- coding: utf-8 -*-


def save(path, message):
    with open(path, 'w', encoding="utf-8") as f:
        f.writelines(message)

	
if __name__ == "__main__":

    message = "111"
    path = "users.txt"
    save(path, message)
