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


# def check_exit(message):
#     # Бот завершает свою работу, если встречает слова:
#     exit_words = ['paka', 'close', 'exit', 'good bye']
#     for word in exit_words:
#         if word in message:
#             return True


@input_error
def hello(*args, **kwars):
    print("How I can help you?")


@input_error
def change_phone(contact_list, user_message):
    for contact in contact_list:
        if contact['name'] == user_message[0]:
            contact['phone'] = int(user_message[1])
            return True
    else:
        print(f"{user_message[0]} is not in the contact list")


@input_error
def add_phone(contact_list, user_message):
    new_contact = {'name': user_message[0], 'phone': int(user_message[1])}
    contact_list.append(new_contact)


@input_error
def show_phone(contact_list, user_message):
    for contact in contact_list:
        if contact['name'] == user_message[0]:
            print(contact.get('phone'))
            return True
    else:
        print(f"{user_message[0]} is not in the contact list")


@input_error
def show_all_phones(contact_list, *args):
    for contact in contact_list:
        print(f"{contact['name'].title()}: {contact['phone']} ")


HANDLERS = {
    'phone': show_phone,
    'show all': show_all_phones,
    'add': add_phone,
    'change': change_phone,
    'hello': hello,
}


def get_handler(key):
    return HANDLERS[key]


def parser(user_message):
    user_message = user_message.split()
    if user_message[0] == 'phone':
        return 'phone', user_message[1:]
    elif user_message[0] == 'add':
        return 'add', user_message[1:]
    elif user_message[0] == 'change':
        return 'change', user_message[1:]
    elif user_message[0] == 'hello':
        return 'hello', user_message[1:]
    elif user_message[0] == 'exit' or user_message[0] == 'close':
        return 'exit', user_message[1:]
    elif user_message[0] == 'good' and user_message[1] == 'bye':
        return 'exit', user_message[1:]
    elif user_message[0] == 'show' and user_message[1] == 'all':
        return 'show all', user_message[2:]


def main():
    contact_list = [{'name': 'jack', 'phone': 38093462}]
    while True:
        user_message = input("Please enter the task:").lower()

        # if check_exit(user_message):
        #     print("Good bye!")
        #     break

        try:
            user_message = parser(user_message)
            if user_message[0] == 'exit':
                print("Good bye!")
                break
            get_handler(user_message[0])(contact_list, user_message[1])
        except:
            print("Please enter a valid command")


if __name__ == '__main__':
    main()
