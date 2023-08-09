from os import system
import mysql.connector
from typing import Callable
from os import name as osname
from .bl import check_input_type





if osname == 'posix':
    clear_command = 'clear'
else:
    clear_command = 'cls'



def create_record(student_info: dict, db):
        """
        Commit a Record in Database

        Args:
            student_info: Dict

        Returns:
            Tuple
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

        result = check_input_type(student_detail=student_info)
        
        if result[0] == 'SUCCESS':
            
            cursor = db.cursor()

            try:
                cursor.executemany(sql, val)
                db.commit()
                return True, 'Done'

                
            except mysql.connector.Error as err:
                return err, False
            
        elif result[0] == 'FAILED':
            return '\n'.join(result[1]), 'FAILED'

        
def read_record(db, query: str = None) -> Callable:
        """
        Reading Data From Database.

        Returns:
            List
        """

        if query:
            sql = query

        else:
            sql = "SELECT * FROM Students;"
        
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            students = cursor.fetchall()
            return students
        
        except mysql.connector.Error as err:
            return f'Something went Wrong!{err}\n'


def update_record(column_name: str, new_value: str, id_: int, db) -> str:
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


def delete_record(id_: int, db) -> str:
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