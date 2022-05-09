import sqlite3
#create "phone book"
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

sql_new_table = """CREATE TABLE IF NOT EXISTS ENTRIES (
name VARCHAR PRIMARY KEY,
phone VARCHAR);"""

cursor.execute(sql_new_table)
#creating input
def create(name, phone):
    try:
        cursor.execute("""
        INSERT INTO Entries VALUES(?,?)
        """, (name,phone))
        conn.commit()
    except:
        print('Exception occured')
 #displaying all data i ntable          
def read():
    try:
        cursor.execute("""
        SELECT * FROM Entries
        """)
        res= cursor.fetchall()
        for c in res:
            print(c[0], '->', c[1])
    except:
        print('Exception occured')
#finding specific data from table
def readOne(name):
    try:
        cursor.execute("""
        SELECT * FROM Entries
        where name=?
        """, (name,))
        res = cursor.fetchall()
        if(len(res) == 0):
            print('no results found')
        else:
            for c in res:
                print(c[0], '::', c[1])
    except:
        print('exception occured')
#change existing data from table
def update(name,phone):
    try:
        cursor.execute("""
        UPDATE Entries
        SET phone=?
        where name=?
        """, (phone, name))
        conn.commit()
    except:
        print('Exception occured')
#remove specific data from table
def delete(name,phone):
    try:
        cursor.execute("""
        DELETE FROM Entries
        where name=?
        """, (name))
        conn.commit()
    except:
        print('Exception occured')
#creating menu
print('1. create new entry')
print('2. read all entries')
print('3. read one entry')
print('4. update an entry')
print('5. delete an entry')
print('6. Exit')
#creating menu pointers/choices
choice= int(input('enter your choice: '))
while choice != 6:
    if choice == 1:
        name=input('Enter a Name: ')
        phone=input('Enter a phone number: ')
        create(name, phone)
    elif choice == 2:
        read()
    elif choice == 3:
        name = input('enter a name: ')
        readOne(name)
    elif choice == 4:
        name = input('Enter a Name: ')
        phone = input('Enter a phone number: ')
        update(name, phone)
    elif choice== 5:
        name = input('enter a name: ')
        delete(name)
    elif choice == 6:
        break
    else:
        print('wrong choice')
    choice = int(input('enter a choice: '))