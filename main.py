
login_details = []
user_details = {}


def main():
    print("\n===== Test Your Knowledge =====")
    print("1. Registration")
    print("2. Login")
    print("3. Exit")

    ch = input("Choose an option: ")

    if ch == "1":
        registration()
    elif ch == "2":
        login()
    elif ch == "3":
        print("Thank you for visiting!")
        return
    else:
        print("Wrong input!")

    main()


def registration():
    global login_details, user_details

    print("\n===== Registration Form =====")
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact = input("Enter contact: ")
    enroll = input("Enter enrollment number: ")
    college = input("Enter college: ")
    password = input("Create password: ")

    if email in login_details:
        print("Email already registered!")
        return

    login_details.append(email)
    user_details[email] = {
        "name": name,
        "email": email,
        "contact": contact,
        "enroll": enroll,
        "college": college,
        "password": password
    }

    print("Registration successful!")
    login()


def login():
    print("\n===== Login =====")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email in user_details and user_details[email]["password"] == password:
        print("Login successful!")
        user_menu(email)
    else:
        print("Invalid email or password!")


def user_menu(email):
    print("\n===== User Menu =====")
    print("1. Profile")
    print("2. Update Profile")
    print("3. Attempt Quiz")
    print("4. Result")
    print("5. Logout")

    choice = input("Choose an option: ")

    if choice == "1":
        profile(email)
    elif choice == "2":
        update_profile(email)
    elif choice == "3":
        attempt_quiz(email)
    elif choice == "4":
        show_result(email)
    elif choice == "5":
        print("Logged out successfully!")
        return
    else:
        print("Wrong input!")

    user_menu(email)


def profile(email):
    print("\n===== Profile =====")
    for key, value in user_details[email].items():
        if key != "password":
            print(key.capitalize() + ":", value)


def update_profile(email):
    print("\n1. Update name")
    print("2. Update contact")
    choice = input("Choose field: ")

    if choice == "1":
        user_details[email]["name"] = input("Enter new name: ")
    elif choice == "2":
        user_details[email]["contact"] = input("Enter new contact: ")
    else:
        print("Wrong input!")
        return

    print("Profile updated!")


quiz_results = {}


def attempt_quiz(email):
    subjects = {
        "1": ("DSA", [
            ("Which data structure follows FIFO?",
             ["Stack", "Queue", "Tree", "Graph"], "2"),
            ("Which data structure follows LIFO?",
             ["Queue", "Array", "Stack", "Graph"], "3")
        ]),
        "2": ("DBMS", [
            ("What is the full form of DBMS?",
             ["Database Management System", "Digital Base System",
              "Data Backup System", "None"], "1"),
            ("Which language is used for database queries?",
             ["HTML", "CSS", "SQL", "C"], "3")
        ]),
        "3": ("PYTHON", [
            ("Which symbol starts a Python comment?",
             ["//", "#", "$", "&"], "2"),
            ("Which function displays output?",
             ["input()", "print()", "read()", "scan()"], "2")
        ]),
        "4": ("System Design", [
            ("What does scalability mean?",
             ["Handling increased load", "Deleting files",
              "Writing comments", "Closing a program"], "1"),
            ("Which is a database?",
             ["HTML", "MySQL", "CSS", "Git"], "2")
        ])
    }

    print("\nChoose a subject:")
    for key, value in subjects.items():
        print(key + ".", value[0])

    choice = input("Enter subject number: ")

    if choice not in subjects:
        print("Invalid choice!")
        return

    subject, questions = subjects[choice]
    score = 0

    for number, (question, options, answer) in enumerate(questions, 1):
        print("\nQuestion", number, ":", question)

        for i, option in enumerate(options, 1):
            print(str(i) + ".", option)

        user_answer = input("Enter answer (1-4): ")

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")

    quiz_results.setdefault(email, {})[subject] = {
        "score": score,
        "total": len(questions)
    }

    print("Quiz completed!")
    print("Score:", score, "/", len(questions))


def show_result(email):
    print("\n===== Quiz Results =====")
    results = quiz_results.get(email, {})

    if not results:
        print("No quiz attempted yet.")
        return

    total_score = 0
    total_questions = 0

    for subject, result in results.items():
        print(subject + ":", result["score"], "/", result["total"])
        total_score += result["score"]
        total_questions += result["total"]

    print("Total Score:", total_score, "/", total_questions)



main()
