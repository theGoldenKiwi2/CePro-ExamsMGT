import math
from ceproexamsmgtapp import models
from ceproexamsmgtapp.models import db, EmployeeType,Employee
import pandas as pd

#fonctions pour lire le fichier csv pour ensuite pouvoir les inséré dans la bd 
def parse_employee_csv(file_path):
    df = pd.read_csv(file_path)
    array_data = df.to_numpy()

    i = 1
    for row in array_data:

        ligne = "Lignes " + str(i) + " : "

        employee = None
        
        #on regarde si il est float ou pas en utilisant la fonctions qui est plus basse
        if is_float(row[0]):
            if math.isnan(row[0]):
            #si il est nul on filtre sur l'adresse email et pas sur le sciper
                employee = Employee.query.filter_by(email=row[1])
            else:
                employee = Employee.query.filter_by(sciper=row[0])

        #on récupère que le premier objet de la liste
        if employee:
            employee = employee.first()
        #si il y en a pas on met l'objet dans la base 
        else:
            employee = Employee()
            employee.sciper = row[0]
        
        #on rentre les champ email, firstname et last name dans la base avec leur équivalence a row de la boucle plus haute
        employee.email = row[1]
        employee.firstname = row[3]
        employee.lastname = row[2]

        employee_type = EmployeeType.query.filter_by(code=row[4])

        if employee_type:
            employee_type = employee_type.first() 

        employee.employee_type = employee_type

        db.session.add(employee)
        db.sesssion.commit()

        i += 1
        print(ligne)

def is_float(value):
    try:
        # float() is a built-in function
        float(value)
        return True
    except ValueError:
        return False