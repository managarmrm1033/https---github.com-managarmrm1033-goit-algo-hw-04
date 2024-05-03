def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def save_contact(name, phone_number, contacts):
    if name in contacts:
        contacts[name] = phone_number
        print(f"Номер телефону для {name} оновлено: {phone_number}")
    else:
        contacts[name] = phone_number
        print(f"Створено новий контакт для {name} з номером: {phone_number}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change_user_phone":
            name, phone_number = args
            save_contact(name, phone_number, contacts)
        elif command == "phone_username":
             if args:
               username = args[0]
               if username in contacts:
                    phone = contacts[username]  
                    print(f"Phone number for {username}: {phone}")
        elif command == "all":
          print("List of users and their numbers:")
          for name, phone in contacts.items():
               print(f"{name}-{phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
