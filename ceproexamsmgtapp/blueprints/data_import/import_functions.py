import math
from ceproexamsmgtapp import models
from ceproexamsmgtapp.models import db, UserType, User, ExamStatus, UserHasExam, Exam, ServiceLevel, Service, ExamType, AcademicYear
import pandas as pd
from flask import Blueprint

#fonctions pour lire le fichier csv pour ensuite pouvoir les inséré dans la bd
def parse_user_csv(file_path):
    df = pd.read_csv(file_path)
    array_data = df.to_numpy()

    i = 1
    for row in array_data:

        print(row)

        ligne = "Lignes " + str(i) + " : "

        user = None
        
        #on regarde si il est float ou pas en utilisant la fonctions qui est plus basse
        if is_float(row[0]):
            if math.isnan(row[0]):
            #si il est nul on filtre sur l'adresse email et pas sur le sciper
                user = User.query.filter_by(lastname=row[2], firstname=row[3])
            else:
                user = User.query.filter_by(sciper=row[0])

        #on récupère que le premier objet de la liste
        if user.first() is not None:
            print('user exist')
            user = user.first()
        #si il y en a pas on met l'objet dans la base 
        else:
            print('user does not exist')
            user = User()
            if not math.isnan(row[0]):
                user.sciper = row[0]

        #on rentre les champ email, firstname et last name dans la base avec leur équivalence a row de la boucle plus haute
        if isinstance(row[1], str):
            user.email = row[1]
        user.firstname = row[3]
        user.lastname = row[2]

        #on filtre le user type pour que le modèle du type (code) soit égal à la row 4 du fichier csv
        if isinstance(row[4], str):
            user_type = UserType.query.filter_by(code=row[4])

            #si il récupère quelque chose il prend donc le première objet (donc dans se cas le seul)
            if user_type:
                user_type = user_type.first()

            #on récupère l'objet et on le met dans l'objet de l'user correspondant
            user.user_type = user_type

        db.session.add(user)
        db.session.commit()

        i += 1
        print(ligne)

    return True

#fonctions pour lire le fichier csv pour ensuite pouvoir les inséré dans la bd 
def parse_exam_csv(file_path):
    df = pd.read_csv(file_path, sep=';')
    array_data = df.to_numpy()

    i = 1
    for row in array_data:

        ligne = "Lignes " + str(i) + " : "

        exam = None
        exam = Exam()
        user = None
        user = User()

        #si il est nul on filtre sur l'adresse email et pas sur le sciper
        exam = Exam.query.filter_by(code=row[4], academic_year_id=row[0], exam_semester=row[1])

        #on récupère que le premier objet de la liste
        if exam.first() is not None:
            print('exam exist')
            exam = exam.first()
        #si il y en a pas on met l'objet dans la base
        else:
            print('exam does not exist')
            exam = Exam()

        exam.academic_year_id = row[0]
        exam.exam_semester = row[1]
        exam.exam_date = row[2]
        exam.exam_status_id = row[3]
        exam.code = [4]
        exam.name = [5]
        exam.service_level_id = row[8]
        exam.nb_students = row[10]
        exam.nb_pages = row[11]
        exam.total_pages = row[12]
        exam.service_id = row[13]
        exam.exam_type_id = row[14]
        exam.deadline_prep = row[15]
        exam.deadline_repro = row[16]
        exam.remark = row[17]

        exam = Exam()
        # db.session.add(exam)
        # db.sesssion.commit()

        user_list = []
        # if row[6]:
        #     if not is_float(row[6]):
        #         user_list = row[6].split(',')
        #         for user in user_list :
        #             print(user)
        #     else:



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #
        # #on regarde si il est float ou pas en utilisant la fonctions qui est plus basse
        # if is_float(row[0]):
        #     if math.isnan(row[0]):
        #     #si il est nul on filtre sur l'adresse email et pas sur le sciper
        #         user = User.query.filter_by(email=row[1])
        #     else:
        #         user = User.query.filter_by(sciper=row[0])
        #
        # #on récupère que le premier objet de la liste
        # if user:
        #     user = user.first()
        # #si il y en a pas on met l'objet dans la base
        # else:
        #     user = User()
        #     user.sciper = row[0]
        #
        # #on rentre les champ email, firstname et last name dans la base avec leur équivalence a row de la boucle plus haute
        # user.email = row[1]
        # user.firstname = row[3]
        # user.lastname = row[2]
        #
        # #on filtre le user type pour que le modèle du type (code) soit égal à la row 4 du fichier csv
        # user_type = UserType.query.filter_by(code=row[4])
        #
        # #si il récupère quelque chose il prend donc le première objet (donc dans se cas le seul)
        # if user_type:
        #     user_type = user_type.first()
        #
        # #on récupère l'objet et on le met dans l'objet de l'user correspondant
        # user.user_type = user_type

        # db.session.add(user)
        # db.sesssion.commit()
        #
        # i += 1
        # print(ligne)

def is_float(value):
    try:
        # float() is a built-in function
        float(value)
        return True
    except ValueError:
        return False