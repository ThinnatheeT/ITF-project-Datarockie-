import sqlite3

def verify_user():
    """
    verify if user input correct usernam and password
    then run get_data function else program ends
    """
    print("Student Exam Score Result")
    print("Please type in your username and password")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "2020":
        get_data()
    else:
        print("Your usernam and password is incorrect")

def get_data():
    """
    connect to database and get data
    format and present result in console
    """
    conn = sqlite3.connect("university.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student;")
    result = cur.fetchall()
    conn.close()
    print("Student Exam Score Report")
    print("=" * 30)
    for row in result:
        print(f"name: {row[1]} {row[2]} \texam score: {row[4]}")

def main():
    """ our main program """
    verify_user

if __name__== "__main__":
    main()

main()