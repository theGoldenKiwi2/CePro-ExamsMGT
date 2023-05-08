import csv
import io
import os

from flask import current_app
import pandas as pd
from ceproexamgtapp.connector.database_tools import DBconnection


def parse_csv(csv_file_path):

    df = pd.read_csv(csv_file_path)
    print(df)
    array_data = df.to_numpy()
    i = 1

    # Ouvrir le fichier en mode écriture
    sql_file_path = os.path.join(current_app.config['UPLOAD_FOLDER'])+"/data.sql"
    sql_file = open(sql_file_path, 'w+')

    exam_insert_row_sql = "INSERT INTO exam (id, code, name, service_id, exam_status_id, exam_date, exam_years, " \
                          "exam_semester, nb_students, nb_pages, deadline_prep, deadline_repro, remark) VALUES \n"

    for row in array_data:

        nb_pages = 0
        exam_status_id = None
        exam_service_id = None
        deadline_prep = "NULL"
        deadline_repro = "NULL"
        remark = ""

        if not pd.isna(row[10]):
            nb_pages = int(row[10])

        if not pd.isna(row[15]):
            remark = str(row[15])

        if not pd.isna(row[14]):
            deadline_repro = "'"+str(row[14])+"'"

        if not pd.isna(row[13]):
            deadline_prep = "'"+str(row[13])+"'"

        strsql_exam_status = "SELECT id FROM exam_status WHERE LOWER(description) = '" + row[2].lower() + "'"
        strsql_service = "SELECT id FROM service WHERE LOWER(code) = '" + row[11].lower() + "'"
        print(strsql_service)
        try:
            with DBconnection() as db:
                db.execute(strsql_exam_status)
                result = db.fetchall()
                if result:
                    exam_status_id = result[0]['id']

                db.execute(strsql_service)
                result = db.fetchall()
                if result:
                    exam_service_id = result[0]['id']

        except Exception as ErreurConnectionBD:
            print(f"2547821146 Connection à la BD Impossible !"
                f"{ErreurConnectionBD.args[0]} , "
                f"{ErreurConnectionBD}")

        exam_insert_row_sql += "("+str(i)+",'"+row[3].replace("'","''")+"','"+row[4].replace("'","''")+"',"+str(exam_service_id)+","+str(exam_status_id)+",'"+row[1]+"','2022-2023',"+str(row[0])+","+str(row[9])+","+str(nb_pages)+","+str(deadline_prep)+","+deadline_repro+",'"+remark+"')"
        i +=1

        if str(row)!=str(array_data[-1]) :
            exam_insert_row_sql += ",\n"
        else:
            exam_insert_row_sql += ";"

        sql_file.write(exam_insert_row_sql)
        exam_insert_row_sql = ''

    sql_file.close()
    return sql_file_path