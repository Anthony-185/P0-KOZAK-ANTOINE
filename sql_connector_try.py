from vendetta import *

if __name__ == '__main__' : print(the_wolf)
print(' <MYSQL CONNECTOR PROGRAM> '.center(79, '-'))

import mysql.connector
from mysql.connector import errorcode

class MainWindow:

    def __init__(self):
    
        self.frame = tkinter.Frame(
            V.tk,
            background = 'cyan')
        self.frame.grid(column = V.tk.grid_size()[0] + 1, row = 0)
        
        self.frame_menu = tkinter.Frame( # <----------------------- menu frame
            self.frame,
            background = 'black')
        self.frame_menu.grid(column = 0, row = 0)
        # define the list to show
        self.list_database = tkinter.StringVar()
        self.tk_listbox_DB = tkinter.Listbox(
            self.frame_menu,
            background = 'black', foreground = 'cyan',
            listvariable = self.list_database, activestyle = 'dotbox',
            selectbackground = 'cyan', selectforeground  = 'green',
            )
        self.tk_listbox_DB.grid(row = 0, column = 0)
        # <------------------------------------------------- end of menu frame
        
        self.labelText = tkinter.StringVar()
        self.label = tkinter.Label(
            self.frame,
            foreground = 'cyan',
            background = 'black',
            textvariable = self.labelText,
            font = ('Terminal', -12), anchor = 'nw', justify = 'left',
            width = 59)
        self.label.grid(column = 0, row = 1)
        
        self.canvas = tkinter.Canvas(
            self.frame,
            width = 300,
            background = 'black')
        self.canvas.grid(column = 0, row = 2)
        
        self.frame_button = tkinter.Frame( # <------------------- button frame
            self.frame,
            background = 'black')
        self.frame_button.grid(column = 0, row = 3)
        # main button 'class' in a function
        def _tk_button(posx: int, command: 'func', text: str, posy: int = 0):
            ''' return a tkinter button placed '''
            button = tkinter.Button(
                self.frame_button, background = 'black', foreground = 'cyan',
                command = command, text = text)
            button.grid(column = posx, row = posy)
            return button
        # all buttons
        self.b_connect = _tk_button(0, self.connect_s, 'Log in')
        self.b_initiat = _tk_button(1, self.launch_database, 'Init')
        self.b_inserti = _tk_button(2, self.inserting_data, 'Insert')
        self.b_queryng = _tk_button(3, self.querying_data, 'Show')
        self.b_deconne = _tk_button(4, self.deconnect_s, 'Log out')
        self.b_ShowAll = _tk_button(5, self.view_database, 'View Databases')
        # <----------------------------------------------- end of button frame
        
        self.status_mysql_oval = self.canvas.create_oval(
            10, 10, 20, 20, fill = 'red', outline = 'cyan')
        self.status_mysql_text = self.canvas.create_text(
            30, 7, text = 'not connected', fill = 'red', anchor = 'nw')
            
        V.tk.update()


        
    def main(self):
        ''' main program '''
        print(' <<< starting main >>> '.center(79, '=') + '\n')
        
        if __name__ != '__main__':
            pass
            # self.connect_s()
            # self.launch_database() ; print(1)
            # # self.inserting_data() ; print(2) # <------------- problem here
            # self.querying_data() ; print(3)
            # self.deconnect_s()
        else:
            print(' <<<Ending main : starting tk mainloop >>> '.center(79,'='))
            V.tk.mainloop() ; raise SystemExit()
    
    
    def deconnect_s(self):
        
        try:
            self.cnx.close()
        except Exception as error:
            print(' <!> ERROR <!> '.center(79, r'/'))
            print(error)
        else:
            self.canvas.itemconfig(
                self.status_mysql_oval,
                fill = 'red')
            self.canvas.itemconfig(
                self.status_mysql_text,
                text = 'not connected',
                fill = 'red')
            V.tk.update()
            print(' <OK> DECONNECTED <OK> '.center(79, '_'))

    
    def connect_s(self):

        user_name = 'Anthony'
        print('attempt to connect with', user_name)
        print('<.> password required >>> ', end='')
        password = input() # input()
        print()
        try:
            self.cnx = mysql.connector.connect(
                user = user_name,
                password = password,
                host = 'localhost',
                database = 'employees')
        except mysql.connector.Error as e:
            print(' <!> FAILED <!> '.center(79, ':'))
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('<!> password or name False')
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print('<!> DataBase does not exit')
            else:
                print(e)
            print()
            return False
        else:
            print(' <0K> CONNECTED <0K> '.center(79, '_'))
            self.canvas.itemconfig(
                self.status_mysql_oval,
                fill = 'green')
            self.canvas.itemconfig(
                self.status_mysql_text,
                text = 'connected',
                fill = 'green')
            V.tk.update()
            return True

    def use_database(self, DB_NAME, cursor):
    
        try:
            cursor.execute("USE {}".format(DB_NAME))
            self.labelText.set(cursor)
        except mysql.connector.Error as err:
            print('Database {} does not exists.'.format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print('Database {} created successfully.'.format(DB_NAME))
                self.cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
        else:
            print('Database {} ready to use'.format(DB_NAME))
        finally:
            return cursor

    def querying_data(self):
        ''' corresponding to 5.4 Querying Data using Connector/Python '''
        import datetime
        
        cursor = self.cnx.cursor()
        cursor = self.use_database('employees', cursor)
        
        query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE hire_date BETWEEN %s AND %s")
            
        hire_start = datetime.date(1999, 1, 1)
        hire_end = datetime.date(1999, 12, 31)
        
        cursor.execute(query, (hire_start, hire_end))
        self.labelText.set(cursor)
        
        for first_name, last_name, hire_date in cursor:
            print('{}, {} was hired on {: %d %b %Y}'.format(
                last_name, first_name, hire_date))
                
        cursor.close()
        
    def view_database(self):
        ''' tkinter version of SHOW DATABASE from SQL'''
        
        cursor = self.cnx.cursor()
        cursor.execute("SHOW DATABASES")
        self.labelText.set(cursor)
        list_database = []
        for each_database in cursor:
            list_database += each_database
            print(each_database)
        print(list_database)
        list_database = ' '.join(list_database)
        self.list_database.set(list_database)
        cursor.close()


    def inserting_data(self): # <----------------------------------------- BUG
        ''' --> 5.3 Inserting Data Using Connector/Python '''
        from datetime import date, datetime, timedelta
        
        print(1)
        cursor = self.cnx.cursor()
        cursor = self.use_database('employees', cursor)
        tomorrow = datetime.now().date() + timedelta(days=1)
        print(2)
        add_employee = ("INSERT INTO EMPLOYEES "
            "(emp_no, first_name, last_name, hire_date, gender, birth_date) "
            "VALUES (NULL, %s, %s, %s, %s, %s)")
        print(3)
        data_employee = ('Geert', 'Vanderkelen',
            tomorrow, 'M', date(1977, 6, 14))
        print(4)
        self.labelText.set(cursor)
        cursor.execute(add_employee, data_employee)
        self.labelText.set(cursor)
        print(emp_no)
        emp_no = cursor.lastrowid() # <- what is that ????
        print(emp_no)
        print(5)
        add_salary = ("INSERT INTO salaries "
            " (emp_no, salary, from_date, to_date) "
            "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
        print(6)
        data_salary = {
            'emp_no': emp_no, 'salary': 50000,
            'from_date': tomorrow, 'to_date': date(9999, 1, 1),}
        print(7)
        cursor.execute(add_salary, data_salary)
        print(8)
        self.cnx.commit() # <- make sure data is commited to database
        cursor.close()
        

    def launch_database(self):
        ''' initiate database, or restore it '''
        
        print('initiate database')
        DB_NAME = 'employees'
        TABLES = {}
        cursor = self.cnx.cursor()
        cursor = self.use_database(DB_NAME, cursor)

        TABLES['employees'] = (
            "CREATE TABLE `employees` ("
            " `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
            " `birth_date` date NOT NULL,"
            " `first_name` varchar(14) NOT NULL,"
            " `last_name` varchar(16) NOT NULL,"
            " `gender` enum('M','F') NOT NULL,"
            " `hire_date` date NOT NULL,"
            " PRIMARY KEY (`emp_no`)"
            ") ENGINE=InnoDB")
            
        TABLES['departments'] = (
            "CREATE TABLE `departments` ("
            " `dept_no` char(4) NOT NULL,"
            " `dept_name` varchar(40) NOT NULL,"
            " PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
            ") ENGINE=InnoDB")
            
        TABLES['salaries'] = (
            "CREATE TABLE `salaries` ("
            " `emp_no` int(11) NOT NULL,"
            " `salary` int(11) NOT NULL,"
            " `from_date` date NOT NULL,"
            " `to_date` date NOT NULL,"
            " PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
            " CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
            " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
            ") ENGINE=InnoDB")
            
        TABLES['dept_emp'] = (
            "CREATE TABLE `dept_emp` ("
            " `emp_no` int(11) NOT NULL,"
            " `dept_no` char(4) NOT NULL,"
            " `from_date` date NOT NULL,"
            " `to_date` date NOT NULL,"
            " PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
            " KEY `dept_no` (`dept_no`),"
            " CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
            " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
            " CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
            " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
            ") ENGINE=InnoDB")
            
        TABLES['dept_manager'] = (
            " CREATE TABLE `dept_manager` ("
            " `dept_no` char(4) NOT NULL,"
            " `emp_no` int(11) NOT NULL,"
            " `from_date` date NOT NULL,"
            " `to_date` date NOT NULL,"
            " PRIMARY KEY (`emp_no`,`dept_no`),"
            " KEY `emp_no` (`emp_no`),"
            " KEY `dept_no` (`dept_no`),"
            " CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
            " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
            " CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
            " REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
            ") ENGINE=InnoDB")
            
        TABLES['titles'] = (
            "CREATE TABLE `titles` ("
            " `emp_no` int(11) NOT NULL,"
            " `title` varchar(50) NOT NULL,"
            " `from_date` date NOT NULL,"
            " `to_date` date DEFAULT NULL,"
            " PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
            " CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
            " REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
            ") ENGINE=InnoDB")
         
        def create_database(cursor):
            print(' <i> creating database <i> '.center(79))
            try:
                cursor.execute(
                    "CREATE DATABASE {} "
                    "DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
                self.labelText.set(cursor)
            except mysql.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit(1)
        
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
                self.labelText.set(cursor)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        cursor.close()
        
        def raise_employee_salaries():
            
            curA = self.cnx.cursor(buffered=True)
            curB = self.cnx.cursor(buffered=True)
            
            query = (
                "SELECT s.emp_no, salary, from_date, to_date"
                    "FROM employees AS e"
                "LEFT JOIN salaries AS s USING (emp_no)"
                "WHERE to_date = DATE('9999-01-01')"
                "AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")
                
            update_old_salary = (
                "UPDATE salaries SETto_date = %s"
                "WHERE emp_no = %s AND from_date = %s")
            insert_new_salary = (
                "INSERT INTO salaries (emp_no, from_date, to_date, salary)"
                "VALUES (%s; %s, %s, %s)")
                
            curA.execute(query, (date(200, 1,1 ), date(2000, 12, 31)))
            
            for (emp_no, salary, from_date, to_date) in curA:
                new_salary = int(round(salary * Decimal('1.15')))
                curB.execute(update_old_salary, (tomorrow, emp_no, from_date))
                curB.execute(insert_new_salary, (
                    emp_no, tomorrow, date(9999, 1, 1,), new_salary))
                    
            self.cnx.commit()
if __name__ == '__main__' : MainWindow().main()

# a = 
# '''
# SELECT * FROM animal;
# 
# SELECT DISTINCT espece FROM animal;
# 
# SELECT espece FROM animal LIMIT 10 OFFSET 5;
# 
# SELECT id, name FROM animal ORDER BY name DESC LIMIT 10;
# 
# SELECT id, sexe, espece, date_naissance FROM Animal 
# WHERE date_naissance > '2009-12-31'
#     OR
#     ( espece='chat'
#         AND
#         ( sexe='M'
#             OR
#         ( sexe='F' AND date_naissance < '2007-06-01' )
#         )
#     );
# 
# SELECT name, commentaire FROM animal WHERE commentaire IS NOT NULL;
# 
# SELECT * FROM animal WHERE commentaire LIKE '%\%%';
# 
# SELECT * 
# FROM Animal 
# WHERE nom LIKE '%Lu%'; -- insensible à la casse
# 
# SELECT * 
# FROM Animal 
# WHERE nom LIKE BINARY '%Lu%'; -- sensible à la casse
# 
# SELECT * FROM animal 
# WHERE date_naissance BETWEEN '2008-01-01 00:00:00' AND '2009-12-31 00:00:00';
# SELECT * FROM animal 
# WHERE date_naissance >= '2008-01-01 00:00:00' 
#   AND date_naissance <= '2009-12-31 00:00:00';
# 
# SELECT id, name, espece FROM animal WHERE espece IN ('chien', 'chat');
# 
# SELECT id, name FROM animal WHERE id LIKE '_9' OR id LIKE '2%':