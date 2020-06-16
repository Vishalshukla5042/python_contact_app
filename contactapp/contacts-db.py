import sqlite3
import datetime


conn = sqlite3.connect('contacts.db')

cur = conn.cursor()

def main():
    print('''Welcome to Contact! Follow the menu below to interact
    with the database''')


    cur.execute('''SELECT count(name) FROM sqlite_master WHERE 
    type = 'table' AND name = 'contacts' ''')


    if cur.fetchone()[0] == 1: 
        print('''\nThere is an existing table of contacts. Continuing
        with the existing table.\n''')

    else:
        cur.execute('''CREATE TABLE contacts (name TEXT, 
        email TEXT, phone INTEGER, last_update TEXT)''')


    while True:

        print('''\n
        Menu:\n
        A) Print All Contacts\n
        B) Add A Contact\n
        C) Delete A Contact\n
        D) Update A Contact\n
        E) Restart The Database\n
        U) Search Database\n
        Q) Quit
        \n''')


        user_input = str(input('Enter selection: ')).upper()

        # print all contacts
        if user_input == 'A':
            while True:
                # secondary menu for printing contacts by a certain order
                print('''\n
                Please select the way in which the contacts should
                be ordered when printed.\n
                Sub-menu:\n
                1) Order By Name
                2) Order By Email
                3) Order By Phone
                4) Order By Last Update
                5) Quit Sub-menu
                ''')


                user_input = str(input('Enter selection: ')).upper()


                if user_input == '1':
                    sqlstr = '''SELECT name, email, phone, last_update
                    FROM contacts ORDER BY name'''

                    for row in cur.execute(sqlstr):
                        print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))

                elif user_input == '2':
                    sqlstr = '''SELECT name, email, phone, last_update
                    FROM contacts ORDER BY email'''

                    for row in cur.execute(sqlstr):
                        print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))

                elif user_input == '3':
                    sqlstr = '''SELECT name, email, phone, last_update
                    FROM contacts ORDER BY phone'''

                    for row in cur.execute(sqlstr):
                        print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))

                elif user_input == '4':
                    sqlstr = '''SELECT name, email, phone, last_update
                    FROM contacts ORDER BY last_update'''

                    for row in cur.execute(sqlstr):
                        print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))

                elif user_input == '5':
                    print('\nExiting the sub-menu...\n')
                    break

                else:
                    print('\nInvalid user input. Please try again!\n')
        

        elif user_input == 'B':
            name = str(input('Contact Name: '))
            email = str(input('Contact Email: '))
            phone = int(input('Contact Phone: '))
            

            cur.execute('''SELECT name FROM contacts WHERE name = ?''',
            (email,))
            row = cur.fetchone()

            if row is None:
                cur.execute('''INSERT INTO contacts (name, email, phone, 
                last_update) VALUES(?, ?, ?, ?)''', 
                (name, email, phone, str(datetime.datetime.now())))

                print('\n' + name + ' added to the contacts database')

            else:
                print('\n There already exists a ' + name + ' in the database.\n')
                

                for row in cur.execute('''SELECT name, email, phone, last_update FROM contacts
                WHERE name = ?''', (name, )):
                    print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))




            conn.commit()            


        elif user_input == 'C':
            name = str(input('Contact Name: '))


            cur.execute('''SELECT name FROM contacts WHERE name = ?''',
            (name,))
            row = cur.fetchone()


            if row is None:
                print('''\nThere exists no contact in the database with the 
                    given name. Continuing with the program...\n''')
            else:
                cur.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
                print('''\nDeleted all contacts with the given name ''' + name + '''.\n''')
            conn.commit()    

        elif user_input == 'D':
            name = str(input('Contact Name: '))


            for row in cur.execute('''SELECT name, email, phone, last_update FROM contacts
            WHERE name = ?''', (name,)):
                print(str(row[0]) + ' ' + str(row[1]) + ' ' + 
                        str(row[2]) + ' ' + str(row[3]))

            while True:

                print('''\n
                Please select the attributes of the contact
                that you would like to update.\n
                Sub-menu:\n
                1) Update Email
                2) Update Phone
                3) Quit Sub-menu
                ''')


                user_input = str(input('Enter selection: ')).upper()


                if user_input == '1':
                    email = str(input('New Contact Email: '))
                    cur.execute('''UPDATE contacts SET email = ? WHERE name = ?''', (email, name))
                    
                    print('\nEmail of ' + name + ' updated.\n')

                elif user_input == '2':
                    phone = int(input('New Contact Phone: '))
                    cur.execute('''UPDATE contacts SET phone = ? WHERE name = ?''', (phone, name))

                    print('\nPhone number of ' + name + ' updated.\n')

                elif user_input == '3':
                    print('\nExiting the sub-menu...\n')
                    break
                else:
                    print('\nInvalid user input. Please try again!\n')
            conn.commit()

        elif user_input == 'E':
            user_input = str(input('''Are you sure? 
            This will delete all current data. (Y/N): ''')).upper()

            if user_input == 'Y':
                # delete current table and create new table
                cur.execute('DROP TABLE IF EXISTS contacts')
                cur.execute('''CREATE TABLE contacts (name TEXT, 
                email TEXT, phone INTEGER, last_update TEXT)''')

                print('\nInitialized new database for contacts.\n')
            else:
                print('\nContinuing the program...\n')
            conn.commit()

        elif user_input == 'Q':
            user_input = str(input('Are you sure? (Y/N)')).upper()

            if user_input == 'Y':
                # close the SQL connection
                conn.commit()
                conn.close()
                print('\nExiting the program...\n')
                exit()
            else:
                print('\nContinuing the program...\n')
        
        elif user_input == 'U':
            name=str(input("contact:"))
            cur.execute('''SELECT name FROM contacts WHERE name = ?''',
                        (email,))
            row = cur.fetchone()


            print('\n There already exists a ' + name + ' in the database.\n')


            for row in cur.execute('''SELECT name, email, phone, last_update FROM contacts WHERE name = ?''', (name,)):
                print(str(row[0]) + ' ' + str(row[1]) + ' ' +
                          str(row[2]) + ' ' + str(row[3]))

                string = '\n Continue to add ' + name + ' ? (Y/N)\n'



        else:
            print('\nInvalid user input. Please try again!\n')
main()