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
        cursor.executemany(sql, val)
        db.commit()

        return None


    def read_record(self) -> Callable:
        """
        Reading Data From Database.

        Returns:
            __printer method
        """

        sql = "SELECT * FROM Students;"
        
        cursor = db.cursor()
        cursor.execute(sql)
        students = cursor.fetchall()

        return self.__printer(students)


    def update_record(self, column_name: str, new_value: str, id_: int) -> None:
        """
        Update a Record In DataBase.

        Args:
            column_name: Name of Column to update.
            new_value: New value to update with.
            id_: ID of Student/Student Number.
        
        Returns:
            None
        """

        sql = f'UPDATE Students SET {column_name} = %s WHERE ID = %s'
        cursor = db.cursor()
        values = (new_value, id_)
        cursor.execute(sql, values)
        db.commit()
        system(clear_command)
        return 'Record Updated Succesfully.\n'


    def delete_record(self, id_: int) -> None:
        """
        This method will find student by id
        and delete information of that student.

        Args:
            id_: Student Number
        
        Returns:
            None
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
        self.birth_date = input('Student Birthdate: ')
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
    

    def show_student(self):
        """
        Print Students information.

        Return:
            Str: List of Students
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


    def edit_student(self, id_: int, edited_column: str) -> None:
        """
        This method takes edit_by and id_ as argument
        then edit the specific part.

        Args:
            edit_by: str (User Chosen Method)
            id_: str (Could be National Code / Student Number)

        Return: None
        """

        if edited_column == '1':
            value = 'FirstName'
            new_value = input('Enter New First Name: ')
        
        elif edited_column == '2':
            value = 'LastName'
            new_value = input('Enter New Last Name: ')

        elif edited_column == '3':
            value = 'ID'
            new_value = input('Enter New Student Number: ')
        
        elif edited_column == '4':
            value = 'NationalCode'
            new_value = input('Enter New National Code: ')

        elif edited_column == '5':
            value = 'Gender'
            new_value = input('Enter New Gender: ')
        
        elif edited_column == '6':
            value = 'BirthDate'
            new_value = input('Enter New BirthDate --> Format -> 1998-08-12: ')
        
        elif edited_column == '7':
            value = 'Python'
            new_value = input('Enter New Python Score: ')
        
        elif edited_column == '8':
            value = 'Java'
            new_value = input('Enter New Java Score: ')
        
        elif edited_column == '9':
            value = 'Js'
            new_value = input('Enter New Js Score: ')
        
        elif edited_column == '10':
            new_value = input('Enter New Php Score: ')
            value = 'Php'
        
        elif edited_column == '11':
            new_value = input('Enter New Csharp: ')
            value = 'Csharp'


        return self.update_record(value, new_value, id_)
    
            
    def remove_student(self, id_: int):
        """
        Check if this student exists
        if True, Then remove the student.

        Args:
            id_: int Student Number
        """

        system(clear_command)

        return self.delete_record(id_)


    def search_student(self, search_option: str, student_id: str):
        """
        Searching Student Based on Chosen Methdo and id.

        Args:
            search_option: str (User chosen Method)
            student_id: str (Could be First_name, Last_name, National_code ...)

        Return: Str
        """

        system(clear_command)

        if search_option == '1':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name['first_name'] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First Add Student!\n'

        elif search_option == '2':

            filtered_list = list()

            if len(self.list_of_students) >= 1:

                for name in self.list_of_students:
                    if name['last_name'] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add Student!\n'

        elif search_option == '3':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name['gender'] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add Student!\n'

        elif search_option == '4':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name['national_code'] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add student!\n'

        elif search_option == '5':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name['student_number'] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add student!\n'
        

    def best_student(self, course: str):
        """
        Find Best Student Based on Score in specific Course.
        
        Args:
            course: str
        """

        system(clear_command)

        if course == '1':
            highest_score = 1.0

            if len(self.list_of_students) >= 1:
                for student in self.list_of_students:

                    if float(student['csharp_score']) > highest_score:
                        highest_score = float(student['csharp_score'])
                        sharpest_student = student
                    continue
                print(f'{sharpest_student["first_name"]} get highest Score in C#')
                return self.__printer(sharpest_student, nested=False)

            return 'You have to add student first!\n'


        if course == '2':
            highest_score = 1.0
            if len(self.list_of_students) >= 1:
                for student in self.list_of_students:
                    if float(student['python_score']) > highest_score:
                        highest_score = float(student['python_score'])
                        sharpest_student = student
                    continue

                print(f'{sharpest_student["first_name"]} get highest Score in Python')
                return self.__printer(sharpest_student, nested=False)
            
            return 'You have to add student first!\n'


        if course == '3':
            highest_score = 1.0
            if len(self.list_of_students) >= 1:
                for student in self.list_of_students:
                    if float(student['java_score']) > highest_score:
                        highest_score = float(student['java_score'])
                        sharpest_student = student
                    continue
            
                print(f'{sharpest_student["first_name"]} get highest Score in Java')
                return self.__printer(sharpest_student, nested=False)
            
            return 'You have to add student first!\n'

        if course == '4':
            highest_score = 1.0
            for student in self.list_of_students:
                if float(student['java_script_score']) > highest_score:
                    highest_score = float(student['java_script_score'])
                    sharpest_student = student
                continue

            if len(self.list_of_students) >= 1:

                print(f'{sharpest_student["first_name"]} get highest Score in JavaScript')
                return self.__printer(sharpest_student, nested=False)

            return 'You have to add student first!\n'

    
        if course == '5':
            highest_score = 1.0
            for student in self.list_of_students:
                if float(student['php_score']) > highest_score:
                    highest_score = float(student['php_score'])
                    sharpest_student = student
                continue

            if len(self.list_of_students) >= 1:

                print(f'{sharpest_student["first_name"]} get highest Score in JavaScript')
                return self.__printer(sharpest_student, nested=False)
    
            return 'You have to add Students First\n'


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
            edited_attribute = input('What Do you Want to Update:\n1-First Name\n2-Last Name\n3-Student Number\n4-National Code\n5-Gender\n6-Birth Date\n7-Python Score\n8-Java Score\n9-Js Score\n10-Php Score\n11-C# Score\n\nWhich One: ')

            system('clear')
            print(student_manager.edit_student(student_id, edited_attribute))


        elif options == '4':

            system(clear_command)
            student_id = int(input('Enter Student Number: '))

            print(student_manager.remove_student(student_id))


        elif options == '5':

            system(clear_command)
            while True:
                search_option = input('Search Student By:\n1-First name:\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Exit\n\nWhich One: ')

                if search_option == '1':
                    print('++ Filter by First Name ++')
                    student_id = input('Enter Student First Name: ')
                    break

                elif search_option == '2':
                    print('++ Filter by Last Name ++')
                    student_id = input('Enter Student Last Name: ')
                    break

                elif search_option == '3':
                    print('++ Filter by Gender ++')
                    student_id = input('Enter Gender (m/f): ')
                    break

                elif search_option == '4':
                    print('++ Filter by National Code ++')
                    student_id = input('Enter Student National Code: ')
                    break

                elif search_option == '5':
                    print('++ Filter by Student Number ++')
                    student_id = input('Enter Student Number: ')
                    break
                
                elif search_option == '6':
                    system(clear_command)
                    print('Exit')
                    print()
                    break

                else:
                    system(clear_command)
                    print('Choose a number between (1-6)')
                    print()
            
            if search_option != '6':
                print(student_manager.search_student(search_option, student_id))
            else:
                continue

        elif options == '6':
            
            system(clear_command)
            while True:
                filter_by = input('Find Best Student By:\n1-C# Score\n2-Python Score\n3-Java Score\n4-JavaScirpt Score\n5-PHP Score\n\nWhich one: ')

                if filter_by == '1':
                    print('Finding best student by C# Score')
                    break

                elif filter_by == '2':
                    print('Finding best student by Python Score')
                    break

                elif filter_by == '3':
                    print('Finding best student by Java Score')
                    break

                elif filter_by == '4':
                    print('Finding best student by JavaScript Score')
                    break

                elif filter_by == '5':
                    print('Finding best student by PHP Score')
                    break

                else:
                    system(clear_command)
                    print('You Have To Choose Between (1-5)!')
                    print()
            
            print(student_manager.best_student(filter_by))

        elif options == '7':

            system(clear_command)
            print('Good Bye.')
            break