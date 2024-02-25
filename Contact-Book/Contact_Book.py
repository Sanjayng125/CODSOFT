import ast

user_input = None
while True:
    user_input = input("1 - All Contacts\n2 - Add Contact\n3 - Delete Contact\n4 - Update Contact\n5 - Search\n6 - Delete All Contacts\n7 - Exit\nChoose an option(1 - 7):")
    if user_input.lower() == "7":
        break
    elif user_input == "1":
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons == "" or cons == "{}":
            print("No Contacts Yet!!")
            continue
        if cons != "":
            contacts = dict(ast.literal_eval(cons))
        num = 1
        for i in contacts:
            if i != "":
                print(end=f"{num}.{i} - ")
                for j in contacts.get(i):
                    print(end=f"{j}: {contacts.get(i).get(j)}  ")
                print()
                num += 1
    elif user_input == "2":
        contacts = dict()
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons != "":
            contacts = dict(ast.literal_eval(cons))
        conatact_name = input("Enter contact name:")
        if conatact_name == "":
            print("Conatact name is required!")
            continue
        if conatact_name in contacts:
            print("Contact name already exists!")
            continue
        
        conatact_number = input("Enter contact Number:")
        if conatact_number == "" or len(conatact_number) < 7:
            print("Conatact number is required and\nconatact number length should be at least 7!")
            continue
        
        conatact_email = input("Enter contact Email:")
        if (conatact_email != "" and len(conatact_email) < 11) or (len(conatact_email) >= 11 and conatact_email.find("@") == -1):
            print("Invalid Email Address!")
            continue
        contacts.update({conatact_name: {"phone": conatact_number, "email": conatact_email}})
        with open("Python/Contact-Book/contact.txt", "w") as f:
            f.write(str(contacts))
            print("Contact Added!")
    elif user_input == "3":
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons == "" or cons == "{}":
            print("No Contacts Yet!!")
            continue
        if cons != "":
            contacts = dict(ast.literal_eval(cons))
        if not len(contacts) > 0:
            print("First Add Contacts!")
            continue
        else:
            conatact_name = input("Enter contact name to delete:")
            if conatact_name == "":
                print("Invalid Name!")
                continue
            elif conatact_name not in contacts:
                print("Contact Not Found!")
                continue
            else:
                contacts.pop(conatact_name)
                with open("Python/Contact-Book/contact.txt", "w") as f:
                    f.write(str(contacts))
                    print("Contact Deleted!")
    elif user_input == "4":
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons == "" or cons == "{}":
            print("No Contacts Yet!!")
            continue
        if cons != "":
            contacts = dict(ast.literal_eval(cons))
        if not len(contacts) > 0:
            print("First Add Contacts!")
            continue
        else:
            conatact_name = input("Enter contact name to update:")
            if conatact_name == "":
                print("Invalid Name!")
                continue
            elif conatact_name not in contacts:
                print("Contact Not Found!")
                continue
            else:
                update_options = input("Enter what to update (1 - phone, 2 - email):")
                if update_options != "1" and update_options != "2":
                    print("Invalid Option! Choose 1 - 2.")
                    continue
                else:
                    if update_options == "1":
                        conatact_number = input("Enter updated contact number:")
                        if conatact_number == "" or len(conatact_number) < 7:
                            print("Conatact number is required and\nconatact number length should be at least 7!")
                            continue
                        contacts[conatact_name]["phone"] = conatact_number
                    elif update_options == "2":
                        conatact_email = input("Enter updated contact email:")
                        if (conatact_email != "" and len(conatact_email) < 11) or (len(conatact_email) >= 11 and conatact_email.find("@") == -1):
                            print("Invalid Email Address!")
                            continue
                        contacts[conatact_name]["email"] = conatact_email
                    with open("Python/Contact-Book/contact.txt", "w") as f:
                        f.write(str(contacts))
                        print("Contact Updated!")
    elif user_input == "5":
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons == "" or cons == "{}":
            print("No Contacts Yet!!")
            continue
        if cons != "":
            contacts = dict(ast.literal_eval(cons))
        user_search = input("Search Contact Name:")
        if user_search != "":
            res = dict()
            if len(contacts) > 0:
                names = list(contacts.keys())
            if len(names) > 0:
                for i in names:
                    if str(i).lower().find(f"{str(user_search)}") != -1:
                        res[i] = contacts[i]
            if len(res) > 0:
                num = 1
                for i in res:
                    if i != "":
                        print(end=f"{num}.{i} - ")
                        for j in contacts.get(i):
                            print(end=f"{j}: {contacts.get(i).get(j)}  ")
                        print()
                        num += 1
            else:
                print("No contacts found!")
    elif user_input == "6":
        cons = str(open("Python/Contact-Book/contact.txt").read())
        if cons == "" or cons == "{}":
            print("No Contacts Yet!!")
            continue
        user_conf = input("Are you sure?(y/n):")
        if user_conf.lower() != "y" and user_conf.lower() != "n":
            print("invalid input!!")
            continue
        if user_conf == "y":
            with open("Python/Contact-Book/contact.txt", "w") as f:
                f.write("")
                print("All contacts deleted!")
    else:
        print("Invalid input!!")
        continue