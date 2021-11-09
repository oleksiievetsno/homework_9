def input_error(func):
    def wrapper(*args, **kwars):
        try:
            func(*args, **kwars)
        except KeyError:
            print("Please enter correct username and phone")
        except ValueError:
            print("Please enter a valid phone number")
        except IndexError:
            print("Please enter a username and maybe a phone number ")
    return wrapper


def check_exit_words(message):
    # Бот завершает свою работу, если встречает слова:
    exit_words = {'close', 'exit', 'good bye'}
    return bool(exit_words & set([message]))


@input_error
def response_hello(*args, **kwars):
    print("How I can help you?")


@input_error
def change_phone(contact_list, user_message):
    for contact in contact_list:
        if contact['name'] == user_message[0]:
            contact['phone'] = int(user_message[1])
            break
    else:
        print(f"{user_message[0]} is not in the contact list")


@input_error
def add_new_contact(contact_list, user_message):
    new_contact = {'name': user_message[0], 'phone': int(user_message[1])}
    contact_list.append(new_contact)


@input_error
def show_phone(contact_list, user_message):
    for contact in contact_list:
        if contact['name'] == user_message[0]:
            print(contact.get('phone'))
            break
    else:
        print(f"{user_message[0]} is not in the contact list")


@input_error
def show_all_contacts(contact_list, *args):
    for contact in contact_list:
        print(f"{contact['name'].title()}: {contact['phone']} ")


COMMAND_HANDLERS = {
    'phone': show_phone,
    'show all': show_all_contacts,
    'add': add_new_contact,
    'change': change_phone,
    'hello': response_hello,
}


def parser_user_input(user_input):
    """This function returns tuple with command and remaining user input"""
    user_input = user_input.split()
    if user_input[0] == 'phone':
        return 'phone', user_input[1:]
    elif user_input[0] == 'add':
        return 'add', user_input[1:]
    elif user_input[0] == 'change':
        return 'change', user_input[1:]
    elif user_input[0] == 'hello':
        return 'hello', user_input[1:]
    elif user_input[0] == 'show' and user_input[1] == 'all':
        return 'show all', user_input[2:]


def main():
    contact_list = [{'name': 'jack', 'phone': 38093462}]
    while True:
        user_input = input("Please enter the task:").lower()

        if check_exit_words(user_input):
            print("Good bye!")
            break

        try:
            command, message = parser_user_input(user_input)
        except TypeError:
            print("Please enter a valid command")
            continue
        except IndexError:
            print("Please enter a full command")
            continue

        command_handler = COMMAND_HANDLERS.get(command)
        command_handler(contact_list, message)


if __name__ == '__main__':
    main()
