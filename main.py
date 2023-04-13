from os import system


class StudentManager:
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
        if self._check_duplicate(self.national_code, 3):
            system('clear')
            return 'This National Code Already Exists.\n'
        
        self.student_number = input('Student Number: ')
        
        if self._check_duplicate(self.student_number, 4):
            system('clear')
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
        system('clear')
        print(self.list_of_students)
        return f'{self.first_name} Saved.\n'
    

    def show_student(self):
        """
        Print Students information.

        Return:
            None
        """

        print('List of Students:')

        print('***********************************************************************************************')
        for student in self.list_of_students:
            print(*student, sep='\t')      
        print('***********************************************************************************************') 

        return f'{len(self.list_of_students)} records found.'


    def _check_duplicate(self, id_, index):
        for element in self.list_of_students:
            if element[index] == id_:
                return True

    def edit_student(self, edit_by: str, id_: str):
        system('clear')
        if edit_by == '1':
            for element in self.list_of_students:

                 if element[3] == id_:
                    system('clear')
                    edit_choices = input('What Do you want to edit about this Student:\n1-First Name\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Birthdate\n7-C# Score\n8-Python Score\n9-Java Score\n10-JS Score\n11-PHP Score:\n\n')

                    if edit_choices == '1':
                        element[0] = input('Enter New First Name: ')
                        system('clear')
                        return 'First Name Changed.\n'

                    elif edit_choices == '2':
                        element[1] = input('Enter New Last Name: ')
                        system('clear')
                        return 'Last Name Changed.\n'

                    elif edit_choices == '3':
                        system('clear')
                        element[2] = input('Enter New Gender: ')
                        system('clear')
                        return 'Gender Changed.\n'

                    elif edit_choices == '4':
                        system('clear')
                        new_national_code = input('Enter New National Code: ')
                        system('clear')

                        if self._check_duplicate(new_national_code, 3):
                            return 'National Code Already Exists.\n'
                        
                        element[3] = new_national_code
                        system('clear')
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '5':
                        new_student_number = input('Enter New Student Number: ')

                        if self._check_duplicate(new_student_number, 4):
                            return 'Student Number Already Exists.\n'
                        
                        element[4] = new_student_number
                        system('clear')
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '6':
                        element[5] = input('Enter New BirthDate: ')
                        system('clear')
                        return 'BirthDate Changed.\n'
                    
                    elif edit_choices == '7':
                        element[6] = input('Enter New C# Score: ')
                        system('clear')
                        return 'C# Score Changed.\n'

                    elif edit_choices == '8':
                        element[7] = input('Enter New Python Score: ')
                        system('clear')
                        return 'Python Score Changed.\n'

                    elif edit_choices == '9':
                        element[8] = input('Enter New Java Score: ')
                        system('clear')
                        return 'Java Score Changed.\n'

                    elif edit_choices == '10':
                        element[9] = input('Enter New Java Script Score: ')
                        system('clear')
                        return 'Java Script Score Changed.\n'

                    elif edit_choices == '11':
                        element[10] = input('Enter New PHP Score: ')
                        system('clear')
                        return 'PHP Score Changed.\n'
                    
                    else:
                        system('clear')
                        return 'You Must Choose an option between (1-11)!\n'
                
            else:
                return f'National Code Does Not Exists: {id_}\n'



        elif edit_by == '2':
            system('clear')

            for element in self.list_of_students:
                
                if element[4] == id_:
                    system('clear')
                    edit_choices = input('What Do you want to edit about this Student:\n1-First Name\n2-Last Name\n3-Gender\n4-National Code\n5-Student Number\n6-Birthdate\n7-C# Score\n8-Python Score\n9-Java Score\n10-JS Score\n11-PHP Score:\n12-Exit\n\n')

                    if edit_choices == '1':
                        element[0] = input('Enter New First Name: ')
                        system('clear')
                        return 'First Name Changed.\n'

                    elif edit_choices == '2':
                        element[1] = input('Enter New Last Name: ')
                        system('clear')
                        return 'Last Name Changed.\n'

                    elif edit_choices == '3':
                        element[2] = input('Enter New Gender: ')
                        system('clear')
                        return 'Gender Changed.\n'

                    elif edit_choices == '4':
                        system('clear')
                        new_national_code = input('Enter New National Code: ')
                        system('clear')

                        if self._check_duplicate(new_national_code, 3):
                            return 'National Code Already Exists.\n'
                        
                        element[3] = new_national_code
                        system('clear')
                        return 'National Code Changed.\n'
                    
                    elif edit_choices == '5':
                        system('clear')
                        new_student_number = input('Enter New Student Number: ')

                        if self._check_duplicate(new_student_number, 4):
                            return 'Student Number Already Exists.\n'
                        
                        element[4] = new_student_number
                        system('clear')
                        return 'National Code Changed.\n'
                    

                    elif edit_choices == '6':
                        element[5] = input('Enter New BirthDate: ')
                        system('clear')
                        return 'BirthDate Changed.\n'
                    
                    elif edit_choices == '7':
                        element[6] = input('Enter New C# Score: ')
                        system('clear')
                        return 'C# Score Changed.\n'

                    elif edit_choices == '8':
                        element[7] = input('Enter New Python Score: ')
                        system('clear')
                        return 'Python Score Changed.\n'

                    elif edit_choices == '9':
                        element[8] = input('Enter New Java Score: ')
                        system('clear')
                        return 'Java Score Changed.\n'

                    elif edit_choices == '10':
                        element[9] = input('Enter New Java Script Score: ')
                        system('clear')
                        return 'Java Script Score Changed.\n'

                    elif edit_choices == '11':
                        element[10] = input('Enter New PHP Score: ')
                        system('clear')
                        return 'PHP Score Changed.\n'
                    
                    elif edit_choices == '12':
                        system('clear')
                        return 'You Did not Change AnyThing.\n'
                    
                    else:
                        system('clear')
                        return 'You Must Choose an option between (1-12)!\n'
                    
                else:
                    return f'Student Number Does Not Exists: {id_}\n'

                    
        else:
            system('clear')
            return 'Wrong Option, You have to Choose a Number between (1-2)!\n'
                    
            
            




if __name__ == '__main__':

    mostafa = StudentManager()
    while True:

        options = input('1-Add Student\n2-Show Student\n3-Edit Student\n4-Remove Student\n5-Search Student\n6-Find Best Student By Score\n6-Exit\n\nHow Can I Help You: ')
        system('clear')

        if options == '1':
            system('clear')
            print(mostafa.add_student())

        elif options == '2':
            print(mostafa.show_student())

        elif options == '3':

            system('clear')

            while True:
                edit_option = input('Want to find Student By National Code or Student Number (1-NationalCode, 2-StudentNumber): ')

                if edit_option == '1':
                    student_id = input('Enter Student National Code: ')
                    break 

                elif edit_option == '2':
                    student_id = input('Enter Student Number: ')
                    break

                else:
                    print('Wrong Option, You have to Choose a Number between (1-2)!')

            print(mostafa.edit_student(edit_option, student_id))

        elif options == '5':
            print('Good Bye.')
            break