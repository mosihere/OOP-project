import sys
from os import system
from os import name as osname
from typing import List


if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'

class StudentManager:
    """
    A class to instantiate as a Student Manager
    """

    def __init__(self) -> None:
        pass
    
        self.list_of_students = list()
    

    def add_student(self):
        """
        populate student infromation
        and append that to main info list

        Return:
            str
        """

        self.student_info = list()

        self.national_code = input('Student National Code: ')
        if self.__check_duplicate(self.national_code, 3):
            system(clear_command)
            return 'This National Code Already Exists.\n'
        
        self.student_number = input('Student Number: ')
        
        if self.__check_duplicate(self.student_number, 4):
            system(clear_command)
            return 'This Student Number Already Exists.\n'

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

        self.student_info.append(self.first_name)
        self.student_info.append(self.last_name)
        self.student_info.append(self.gender)
        self.student_info.append(self.national_code)
        self.student_info.append(self.student_number)
        self.student_info.append(self.birth_date)
        self.student_info.append(self.csharp_score)
        self.student_info.append(self.python_score)
        self.student_info.append(self.java_score)
        self.student_info.append(self.java_script_score)
        self.student_info.append(self.php_score)

        self.list_of_students.append(self.student_info)
        system(clear_command)
        return f'{self.first_name} Saved.\n'
    

    def show_student(self):
        """
        Print Students information.

        Return:
            Str: List of Students
        """

        system(clear_command)
        print('List of Students:')

        return self.__printer(self.list_of_students)


    def __check_duplicate(self, id_, index):
        """
        Check if Value is Duplicate.

        Return: Bool
        """

        for element in self.list_of_students:
            if element[index] == id_:
                return True
            
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
                print(*record, sep='\t')
            print('***********************************************************************************************')
            return f'{len(value)} records found\n'  
                  
        else:
            print('***********************************************************************************************')
            print(*value, sep='\t')
            print('***********************************************************************************************')
            return f'\n'


    def edit_student(self, edit_by: str, id_: str) -> str:
        """
        This method takes edit_by and id_ as argument
        then edit the specific part.

        Args:
            edit_by: str (User Chosen Method)
            id_: str (Could be National Code / Student Number)

        Return: Str
        """

        system(clear_command)
        if edit_by == '1':
            for element in self.list_of_students:

                 if element[3] == id_:
                    system(clear_command)
                    edit_choices = input('What Do you want to edit about this Student:\n1-First Name\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Birthdate\n7-C# Score\n8-Python Score\n9-Java Score\n10-JS Score\n11-PHP Score:\n\n')

                    if edit_choices == '1':
                        element[0] = input('Enter New First Name: ')
                        system(clear_command)
                        return 'First Name Changed.\n'

                    elif edit_choices == '2':
                        element[1] = input('Enter New Last Name: ')
                        system(clear_command)
                        return 'Last Name Changed.\n'

                    elif edit_choices == '3':
                        system(clear_command)
                        element[2] = input('Enter New Gender: ')
                        system(clear_command)
                        return 'Gender Changed.\n'

                    elif edit_choices == '4':
                        system(clear_command)
                        new_national_code = input('Enter New National Code: ')
                        system(clear_command)

                        if self.__check_duplicate(new_national_code, 3):
                            return 'National Code Already Exists.\n'
                        
                        element[3] = new_national_code
                        system(clear_command)
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '5':
                        new_student_number = input('Enter New Student Number: ')

                        if self.__check_duplicate(new_student_number, 4):
                            return 'Student Number Already Exists.\n'
                        
                        element[4] = new_student_number
                        system(clear_command)
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '6':
                        element[5] = input('Enter New BirthDate: ')
                        system(clear_command)
                        return 'BirthDate Changed.\n'
                    
                    elif edit_choices == '7':
                        element[6] = input('Enter New C# Score: ')
                        system(clear_command)
                        return 'C# Score Changed.\n'

                    elif edit_choices == '8':
                        element[7] = input('Enter New Python Score: ')
                        system(clear_command)
                        return 'Python Score Changed.\n'

                    elif edit_choices == '9':
                        element[8] = input('Enter New Java Score: ')
                        system(clear_command)
                        return 'Java Score Changed.\n'

                    elif edit_choices == '10':
                        element[9] = input('Enter New Java Script Score: ')
                        system(clear_command)
                        return 'Java Script Score Changed.\n'

                    elif edit_choices == '11':
                        element[10] = input('Enter New PHP Score: ')
                        system(clear_command)
                        return 'PHP Score Changed.\n'
                    
                    else:
                        system(clear_command)
                        return 'You Must Choose an option between (1-11)!\n'
                
            else:
                return f'National Code Does Not Exists: {id_}\n'


        elif edit_by == '2':
            system(clear_command)

            for element in self.list_of_students:
                
                if element[4] == id_:
                    system(clear_command)
                    edit_choices = input('What Do you want to edit about this Student:\n1-First Name\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Birthdate\n7-C# Score\n8-Python Score\n9-Java Score\n10-JS Score\n11-PHP Score:\n12-Exit\n\n')

                    if edit_choices == '1':
                        element[0] = input('Enter New First Name: ')
                        system(clear_command)
                        return 'First Name Changed.\n'

                    elif edit_choices == '2':
                        element[1] = input('Enter New Last Name: ')
                        system(clear_command)
                        return 'Last Name Changed.\n'

                    elif edit_choices == '3':
                        element[2] = input('Enter New Gender: ')
                        system(clear_command)
                        return 'Gender Changed.\n'

                    elif edit_choices == '4':
                        system(clear_command)
                        new_national_code = input('Enter New National Code: ')
                        system(clear_command)

                        if self._check_duplicate(new_national_code, 3):
                            return 'National Code Already Exists.\n'
                        
                        element[3] = new_national_code
                        system(clear_command)
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '5':
                        system(clear_command)
                        new_student_number = input('Enter New Student Number: ')

                        if self._check_duplicate(new_student_number, 4):
                            return 'Student Number Already Exists.\n'
                        
                        element[4] = new_student_number
                        system(clear_command)
                        return 'National Code Changed.\n'
                    

                    elif edit_choices == '6':
                        element[5] = input('Enter New BirthDate: ')
                        system(clear_command)
                        return 'BirthDate Changed.\n'
                    
                    elif edit_choices == '7':
                        element[6] = input('Enter New C# Score: ')
                        system(clear_command)
                        return 'C# Score Changed.\n'

                    elif edit_choices == '8':
                        element[7] = input('Enter New Python Score: ')
                        system(clear_command)
                        return 'Python Score Changed.\n'

                    elif edit_choices == '9':
                        element[8] = input('Enter New Java Score: ')
                        system(clear_command)
                        return 'Java Score Changed.\n'

                    elif edit_choices == '10':
                        element[9] = input('Enter New Java Script Score: ')
                        system(clear_command)
                        return 'Java Script Score Changed.\n'

                    elif edit_choices == '11':
                        element[10] = input('Enter New PHP Score: ')
                        system(clear_command)
                        return 'PHP Score Changed.\n'
                    
                    elif edit_choices == '12':
                        system(clear_command)
                        return 'You Did not Change AnyThing.\n'
                    
                    else:
                        system(clear_command)
                        return 'You Must Choose an option between (1-12)!\n'
                    
                else:
                    return f'Student Number Does Not Exists: {id_}\n'

                    
        else:
            system(clear_command)
            return 'Wrong Option, You have to Choose a Number between (1-2)!\n'
                    
            
    def remove_student(self, edit_by: str, id_: str):
        """
        Check if this student exists
        if True, Then remove the student.

        Args:
            edit_by: str (User Chosen Method Number)
            id_: str (Could be National Code / Student Number)
        """

        system(clear_command)
        if edit_by == '1':

            for index, element in enumerate(self.list_of_students):
                if element[3] == id_:
                    removed_data = self.list_of_students.pop(index)
                    system(clear_command)
                    return f'{removed_data[0]} Removed Successfully.\n'
                
                else:
                    system(clear_command)
                    return f'There is no records with this National code.\n'
                

        elif edit_by == '2':

            for index, element in enumerate(self.list_of_students):
                if element[4] == id_:
                    removed_data = self.list_of_students.pop(index)
                    system(clear_command)
                    return f'{removed_data[0]} Removed Successfully.\n'
                
                else:
                    system(clear_command)
                    return f'There is no records with this Student Number.\n'
                  
        else:
            system(clear_command)
            return 'Wrong Option, you have to Choose between (1-2)!\n'


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
                    if name[0] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First Add Student!\n'

        if search_option == '2':

            filtered_list = list()

            if len(self.list_of_students) >= 1:

                for name in self.list_of_students:
                    if name[1] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add Student!\n'

        if search_option == '3':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name[2] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add Student!\n'

        if search_option == '4':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name[3] == student_id:
                        filtered_list.append(name)
                    continue

                return self.__printer(filtered_list)
            
            return 'First add student!\n'

        if search_option == '5':

            filtered_list = list()

            if len(self.list_of_students) >= 1:
                for name in self.list_of_students:
                    if name[4] == student_id:
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

                    if float(student[6]) > highest_score:
                        highest_score = float(student[6])
                        sharpest_student = student
                    continue
                print(f'{sharpest_student[0]} get highest Score in C#')
                return self.__printer(sharpest_student, nested=False)

            return 'You have to add student first!\n'


        if course == '2':
            highest_score = 1.0
            if len(self.list_of_students) >= 1:
                for student in self.list_of_students:
                    if float(student[7]) > highest_score:
                        highest_score = float(student[7])
                        sharpest_student = student
                    continue

                print(f'{sharpest_student[0]} get highest Score in Python')
                return self.__printer(sharpest_student, nested=False)
            
            return 'You have to add student first!\n'


        if course == '3':
            highest_score = 1.0
            if len(self.list_of_students) >= 1:
                for student in self.list_of_students:
                    if float(student[8]) > highest_score:
                        highest_score = float(student[8])
                        sharpest_student = student
                    continue
            
                print(f'{sharpest_student[0]} get highest Score in Java')
                return self.__printer(sharpest_student, nested=False)
            
            return 'You have to add student first!\n'
    


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

            while True:
                edit_option = input('Select Student By:\n1-NationalCode\n2-StudentNumber\n\nWhich One: ')

                if edit_option == '1':
                    student_id = input('Enter Student National Code: ')
                    break 

                elif edit_option == '2':
                    student_id = input('Enter Student Number: ')
                    break

                else:
                    print('Wrong Option, You have to Choose a Number between (1-2)!')

            print(student_manager.edit_student(edit_option, student_id))

        elif options == '4':

            system(clear_command)
            while True:
                edit_option = input('Remove Student By:\n1-National Code\n2-Student Number\n\nWhich One: ')

                if edit_option == '1':
                    student_id = input('Enter Student National Code: ')
                    break

                elif edit_option == '2':
                    student_id = input('Enter Student Number: ')
                    break

                else:
                    print('Wrong Option, You have to Choose a Number between (1-2)!')

            print(student_manager.remove_student(edit_option, student_id))

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
                    print('Exit.')
                    student_id = input('Enter Student Last Name: ')
                    break
            
            print(student_manager.search_student(search_option, student_id))

        elif options == '6':
            
            system(clear_command)
            while True:
                filter_by = input('Find Best Student By:\n1-C# Score\n2-Python Score\n3-Java Score\n\nWhich one: ')

                if filter_by == '1':
                    print('Finding best student by C# Score')
                    break

                elif filter_by == '2':
                    print('Finding best student by Python Score')
                    break

                elif filter_by == '3':
                    print('Finding best student by Java Score')
                    break
            
            print(student_manager.best_student(filter_by))

        elif options == '7':

            system(clear_command)
            print('Good Bye.')
            break