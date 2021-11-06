def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            print("Please enter correct username and phone")
        except ValueError:
            print("Please enter command and valid data")
        except IndexError:
            print("Please enter command and valid data")
    return wrapper


def check_exit(message):
    exit_words = ['exit', 'close', 'good bye']
    for word in exit_words:
        if word in message:
            return True


def hello():
    pass


@input_error
def change_phone(contact_list, name, phone):
    for contact in contact_list:
        if contact['name'] == name:
            contact['phone'] = phone


@input_error
def add_phone(contact_list, name, phone):
    new_contact = {'name': name, 'phone': phone}
    contact_list.append(new_contact)


@input_error
def show_phone(contact_list, name):
    for contact in contact_list:
        if contact['name'] == name:
            print(contact.get('phone'))


@input_error
def show_all_phones(contact_list):
    for contact in contact_list:
        print(f"{contact['name'].title()}: {contact['phone']} ")


# HANDLERS = {
#     'phone': show_phone,
#     'show': show_all_phones,
#     'add': add_phone,
#     'change': change_phone,

# }


# def get_handler(key):
#     return HANDLERS[key]


def main():
    contact_list = [{'name': 'jack', 'phone': '+38093462'}]
    while True:
        user_message = input("Please enter the task:").lower()
        if check_exit(user_message):
            print("Good bye!")
            break
        user_message = user_message.split()

        # get_handler(user_message[0])(
        #     contact_list, user_message[1], user_message[2])

        if user_message[0] == 'phone':
            show_phone(contact_list, user_message[1])
        elif user_message[0] == 'show' and user_message[1] == 'all':
            show_all_phones(contact_list)
        elif user_message[0] == 'add':
            add_phone(contact_list, user_message[1], user_message[2])
        elif user_message[0] == 'change':
            change_phone(contact_list, user_message[1], user_message[2])


if __name__ == '__main__':
    main()
