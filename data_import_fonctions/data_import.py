import os

import sqlparse
from flask import render_template, Blueprint, request, redirect, current_app

from ceproexamgtapp.connector.database_tools import ToolsBd
from ceproexamgtapp.views.data_import.import_functions import parse_csv

bp = Blueprint('data_import', __name__, url_prefix='/data_import ')

@bp.route("/dataimport", methods=['GET','POST'])
def csv_import():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return redirect(request.url)
        if file.filename.rsplit('.', 1)[1].lower() == 'csv':
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'])+"/"+file.filename
            sql_file_path = parse_csv(file_path)

            #execute SQL
            sql_file = open(sql_file_path, 'r')
            sql_lines = sql_file.read()
            sql_lines = sqlparse.split(sql_lines)

            dbTools = ToolsBd()
            dbTools.execute_sql(sql_lines)

            sql_file.close()

            return redirect(request.url)

        return redirect(request.url)
    else:
        return render_template(r'data_import/csv_import.html')