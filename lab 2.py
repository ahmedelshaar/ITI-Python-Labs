import re
import time
import datetime


def project_page(user_id):
    while True:
        print("""*************** Project ***********************
            1) create project
            2) view all project
            3) edit Your projects
            4) delete his own projects
            5) exit
        """)
        choice = input_validation()
        if choice == 1:
            create_project(user_id)
        elif choice == 2:
            list_all()
        elif choice == 3:
            edit_project(user_id)
        elif choice == 4:
            delete_project(user_id)
        elif choice == 5:
            exit()


def input_validation():
    x = input("Enter Your Choice: ")
    if x.isdigit() and int(x) in range(1, 6):
        return int(x)
    return input_validation()


def project_name():
    x = input("Project Name: ")
    if x.isalpha():
        return x
    else:
        return project_name()


def project_details():
    x = input("project details: ")
    return x


def total_target():
    x = input("Total target: ")
    if x.isdigit() and x != 0:
        return x
    else:
        return total_target()


def enter_date():
    input_date = input("Enter the date in format 'dd/mm/yy' : ")
    day, month, year = input_date.split('/')
    is_valid_date = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_valid_date = False

    if (is_valid_date):
        return input_date
    else:
        return enter_date()


def input_project(user_id):
    title = project_name()
    details = project_details()
    total = total_target()
    start_date = enter_date()
    end_date = enter_date()
    project_id = round(time.time())
    data = f"{user_id}:{project_id}:{title}:{details}:{total}:{start_date}:{end_date}\n"
    return data


def create_project(user_id):
    data = input_project(user_id)
    file = open("projects.txt", 'a')
    file.writelines(data)
    file.close()


def list_all():
    file = open("projects.txt", 'r')
    data = file.readlines()
    print(data)


def edit_project(user_id):
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if d[2] == name and d[0] == user_id:
            data[index] = input_project(user_id)

        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()


def delete_project(user_id):
    name = input("enter your project name: ")
    file = open("projects.txt", 'r')
    data = file.readlines()
    file.close()
    index = 0
    for i in data:
        d = i.split(":")
        if d[2] == name and d[0] == user_id:
            del data[index]
        index += 1
    file = open("projects.txt", 'w')
    file.writelines(data)
    file.close()


def entry_input_validation():
    x = input("Enter Your Choice: ")
    if x.isdigit() and int(x) in [1, 2, 3]:
        return int(x)
    return entry_input_validation()


def enter_first_name():
    x = input("Enter your First Name: ")
    if x.isalpha() or not x:
        return x
    else:
        return enter_first_name()


def enter_last_name():
    x = input("Enter your Last Name: ")
    if x.isalpha() or not x:
        return x
    else:
        return enter_last_name()


def enter_email():
    x = input("Enter email: ")
    if email_validator(x):
        return x
    else:
        return enter_email()


def email_validator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


def enter_password():
    x = input("Enter Password: ")
    if len(x) < 8 or not x:
        return enter_password()
    else:
        confirmed_password = confirm_password(x)
        if confirmed_password:
            return x
        else:
            return enter_password()


def confirm_password(password):
    x = input("Enter Password Again: ")
    if password == x or not x:
        return True
    else:
        return False


def enter_phone():
    x = input("Enter Your Phone: ")
    if re.match(r"^01[0-2,5]\d{1,8}$", x):
        return x
    else:
        return enter_phone()


def save_data(data):
    file = open('usersdata.txt', 'a')
    file.writelines(data)
    file.close()


def registration():
    first_name = enter_first_name()
    last_name = enter_last_name()
    email = enter_email()
    password = enter_password()
    phone = enter_phone()
    id_user = round(time.time())
    data = f"{id_user}:{email}:{password}:{first_name}:{last_name}:{phone}\n"
    save_data(data)


def check_exist(email,password):
    file = open("usersdata.txt", "r")
    data = file.readlines()
    for i in data:
        d = i.split(":")
        if d[1] == email and d[2] == password:
            return d[0]
    return login()


def login():
    print("---------LOGIN------------")
    email = input("EMAIL : ")
    password = input("Password: ")
    user_id = check_exist(email,password)
    project_page(user_id)


if __name__ == '__main__':
    while True:
        print("""============ Entry Page =========== 
        1) Registration
        2) Login 
        3) Exit """)
        select_login = entry_input_validation()
        if select_login == 1:
            registration()
        elif select_login == 2:
            login()
        elif select_login == 3:
            exit()