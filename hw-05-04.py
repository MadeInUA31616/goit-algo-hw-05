def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact changed!"
    else:
        return "Contact is missing"

def show_phone(args, contacts):
    name = args.pop(0)
    try:
        return contacts[name]
    except KeyError:
        return "Contact is missing"
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "close" or command == "exit":
            print ("Good bye! :)")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))  

        elif command == "change":
            print(change_contact(args,contacts))
                  
        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(contacts)

        else:
            print("Invalid command.")  

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter name and new phone."
        except KeyError:
            return "Contact is missing."
        except IndexError:
            return "Please enter a name to get phone."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact changed!"
    else:
        return "Contact is missing"

@input_error
def show_phone(args, contacts):
    name = args.pop(0)
    try:
        return contacts[name]
    except KeyError:
        return "Contact is missing"

if __name__ == "__main__":
    main()