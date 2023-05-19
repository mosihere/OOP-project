import os
from os import system
import mysql.connector
from typing import List
from os import name as osname
import mysql.connector.errors
from typing import Callable


if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'


db = mysql.connector.connect(

    host="localhost",
    user="root",
    password=os.environ['DB_PASS'],
    database="student"
    )

class StudentManager:
    """
    A class to instantiate as a Student Manager
    """

    def __init__(self) -> None:
        pass
    
        self.list_of_students = list()
    

    def create_record(self, student_info: dict) -> None:
        """
        Commit a Record in Database

        Args:
            student_info: Dict

        Returns:
            None
        """

        sql = """INSERT INTO Students (
        ID, FirstName, LastName, NationalCode,
        BirthDate, Gender, Python, Csharp,
        Js, Php, Java
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = [
            (
            student_info['student_number'],
            student_info['first_name'],
            student_info['last_name'],
            student_info['national_code'],
            student_info['birth_date'],
            student_info['gender'],
            student_info['python_score'],
            student_info['csharp_score'],
            student_info['java_script_score'],
            student_info['java_score'],
            student_info['php_score'],
            )
        ]

        cursor = db.cursor()

        try:
            cursor.executemany(sql, val)
            db.commit()

            return None
        
        except mysql.connector.Error as err:
            return f'Something went Wrong!{err}\n'


    def read_record(self, query: str = None) -> Callable:
        """
        Reading Data From Database.

        Returns:
            __printer method
        """

        if query:
            sql = query

        else:
            sql = "SELECT * FROM Students;"
        
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            students = cursor.fetchall()
            return self.__printer(students)
        
        except mysql.connector.Error as err:
            return f'Something went Wrong!{err}\n'


    def update_record(self, column_name: str, new_value: str, id_: int) -> str:
        """
        Update a Record In DataBase.

        Args:
            column_name: Name of Column to update.
            new_value: New value to update with.
            id_: ID of Student/Student Number.
        
        Returns:
            str (status of execution)
        """

        sql = f'UPDATE Students SET {column_name} = %s WHERE ID = %s'
        values = (new_value, id_)
        cursor = db.cursor()

        try:
            cursor.execute(sql, values)
            db.commit()
            system(clear_command)
            return 'Record Updated Succesfully.\n'
        
        except mysql.connector.Error as err:
            return f'Something went Wrong!{err}\n'


    def delete_record(self, id_: int) -> str:
        """
        This method will find student by id
        and delete information of that student.

        Args:
            id_: Student Number
        
        Returns:
            str (status of execution)
        """

        cursor = db.cursor()
        sql = 'SELECT ID FROM Students WHERE ID=%s'
        value = (id_, )

        try:
            cursor.execute(sql, value)
            result = cursor.fetchone()
            if result:
                sql = 'DELETE FROM Students WHERE ID=%s'
                cursor.execute(sql, value)
                db.commit()
                return 'Student Deleted Succesfully.\n'
            else:
                return 'No Student Found!\n'
        
        except mysql.connector.Error as err:
            return f'Something went Wrong!{err}\n'
                    

    def add_student(self):
        """
        populate student infromation
        and append that to main info list

        Return:
            str
        """

        self.student_info = dict()

        self.national_code = input('Student National Code: ')
        self.student_number = input('Student Number: ')
        self.first_name = input('Student First Name: ')
        self.last_name = input('Student Last Name: ')
        self.gender = input('Student Gender(m/f): ')
        self.birth_date = input('Student Birthdate (1990-10-10): ')
        self.csharp_score = input('Student C# Score: ')
        self.python_score = input('Student Python Score: ')
        self.java_score = input('Student Java Score: ')
        self.java_script_score = input('Student JavaScript Score: ')
        self.php_score = input('Student PHP Score: ')


        # Appending information to List.

        self.student_info['first_name'] = self.first_name
        self.student_info['last_name'] = self.last_name
        self.student_info['gender'] = self.gender
        self.student_info['national_code'] = self.national_code
        self.student_info['student_number'] = self.student_number
        self.student_info['birth_date'] = self.birth_date
        self.student_info['csharp_score'] = self.csharp_score
        self.student_info['python_score'] = self.python_score
        self.student_info['java_score'] = self.java_score
        self.student_info['java_script_score'] = self.java_script_score
        self.student_info['php_score'] = self.php_score

        self.list_of_students.append(self.student_info)

        system(clear_command)

        self.create_record(self.student_info)
        
        return f'{self.first_name} Saved.\n'
    

    def show_student(self) -> Callable:
        """
        Print Students information.

        Return:
            Str: read_record method.
        """

        system(clear_command)
        print('List of Students:')

        return self.read_record()


    def __printer(self, value: List, nested: bool = True) -> str:
        """
        Takes a list as argument and unpack and pretify values.

        Args:
            value: List
            nested: Bool
        
        Return: Str
        """

        if nested:
            print('***********************************************************************************************')
            for record in value:
                print(record, sep='\t')
            print('***********************************************************************************************')
            return f'{len(value)} records found\n'  
                  
        else:
            print('***********************************************************************************************')
            print(value, sep='\t')
            print('***********************************************************************************************')
            return f'\n'


    def edit_student(self, id_: int, edited_column: str) -> Callable:
        """
        This method takes edit_by and id_ as argument
        then edit the specific part.

        Args:
            edit_by: str (User Chosen Method)
            id_: str (Could be National Code / Student Number)

        Return: update_record method
        """

        value_translate = {
            '1': 'FirstName',
            '2': 'LastName',
            '3': 'ID',
            '4': 'NationalCode',
            '5': 'Gender',
            '6': 'BirthDate',
            '7': 'Python',
            '8': 'Java',
            '9': 'Js',
            '10': 'Php',
            '11': 'Csharp'
        }

        if edited_column not in value_translate:
            system(clear_command)
            return 'You Must enter a Number Between 1-11!\n'
        
        value = value_translate[edited_column]
        system(clear_command)
        new_value = input(f'Enter New {value}: ')

        try:
            student_exists_query = f'SELECT ID from Students WHERE ID = {id_}'
            cursor = db.cursor()
            cursor.execute(student_exists_query)
            data = cursor.fetchone()

            if data:

                return self.update_record(value, new_value, id_)
            else:
                return 'No Students Found!\n'
            
        except mysql.connector.Error as err:
            return f'SomeThing Went Wrong!, {err}'
    
            
    def remove_student(self, id_: int) -> Callable:
        """
        Check if this student exists
        if True, Then remove the student.

        Args:
            id_: int Student Number
        
        Returns: delete_record method.
        """

        system(clear_command)

        return self.delete_record(id_)


    def search_student(self, search_option: str, student_id: str) -> Callable:
        """
        Searching Student Based on Chosen Method and id.

        Args:
            search_option: str (User chosen Method)
            student_id: str (Could be First_name, Last_name, National_code ...)

        Return: read_record method.
        """

        system(clear_command)

        value_translate = {
            '1': 'FirstName',
            '2': 'LastName',
            '3': 'Gender',
            '4': 'NationalCode',
            '5': 'ID'
            }
        
        if search_option not in value_translate:
            return 'You Must enter a Number Between 1-5!\n'
        
        value = value_translate[search_option]
        sql_query = f'SELECT * FROM Students WHERE {value} = "{student_id}"'

        return self.read_record(sql_query)
         

    def best_student(self, course: str) -> Callable:
        """
        Find Best Student Based on Score in specific Course.
        
        Args:
            course: str

        Returns:
            read_record method.
        """

        system(clear_command)

        value_translate = {
            '1': 'Csharp',
            '2': 'Python',
            '3': 'Java',
            '4': 'Js',
            '5': 'Php'
        }

        if course not in value_translate:
            return 'You Must enter a Number Between 1-5!\n'

        value = value_translate[course]
        sql_query = f"""SELECT MAX({value}) FROM Students"""
        return self.read_record(sql_query)


if __name__ == '__main__':

    student_manager = StudentManager()
    while True:

        options = input('1-Add Student\n2-Show Student\n3-Edit Student\n4-Remove Student\n5-Search Student\n6-Find Best Student By Score\n7-Exit\n\nHow Can I Help You: ')
        system(clear_command)

        if options == '1':
            system(clear_command)
            print(student_manager.add_student())


        elif options == '2':
            print(student_manager.show_student())


        elif options == '3':

            system(clear_command)

            student_id = int(input('Student Number: '))
            print()

            student_exists_query = f'SELECT ID from Students WHERE ID = {student_id}'
            cursor = db.cursor()

            cursor.execute(student_exists_query)
            data = cursor.fetchone()
            
            if not data:
                system(clear_command)
                print('No Students Found!\n')

            else:
                system(clear_command)
                edited_attribute = input('What Do you Want to Update:\n\n1-First Name\n2-Last Name\n3-Student Number\n4-National Code\n5-Gender\n6-Birth Date\n7-Python Score\n8-Java Score\n9-Js Score\n10-Php Score\n11-C# Score\n\nWhich One: ')

                print(student_manager.edit_student(student_id, edited_attribute))


        elif options == '4':

            system(clear_command)
            student_id = int(input('Enter Student Number: '))

            print(student_manager.remove_student(student_id))


        elif options == '5':

            system(clear_command)
            while True:
                search_option = input('Search Student By:\n\n1-First name:\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Exit\n\nWhich One: ')
                
                if search_option == '6':
                    system(clear_command)
                    print('Exit')
                    print()
                    break

                value_translate = {
                    '1': 'FirstName',
                    '2': 'LastName',
                    '3': 'Gender',
                    '4': 'NationalCode',
                    '5': 'ID',
                    }
                
                if search_option not in value_translate:
                    system(clear_command)
                    print('You Have To Enter a Number Between 1-6!')
                    break
                
                student_id = input(f'Enter Student {value_translate[search_option]}:')
                print(f'++ Filter by {value_translate[search_option]} ++')
                print()
                print(student_manager.search_student(search_option, student_id))
                break

        elif options == '6':
            
            system(clear_command)
            while True:
                filter_by = input('Find Best Student By:\n\n1-C# Score\n2-Python Score\n3-Java Score\n4-JavaScirpt Score\n5-PHP Score\n\nWhich one: ')

                value_translate = {
                    '1': 'Csharp',
                    '2': 'Python',
                    '3': 'Java',
                    '4': 'Js',
                    '5': 'Php'
                }

                if filter_by not in value_translate:
                    system(clear_command)
                    print('You Have To Choose Between (1-5)!')
                    print()
            
                print(student_manager.best_student(filter_by))
                break

        elif options == '7':

            system(clear_command)
            print('Good Bye.')
            break