import os
from flask_login import login_required
from flask import render_template, Blueprint, request, redirect, current_app
from .import_functions import parse_user_csv, parse_exam_csv
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter

bp = Blueprint('data_import', __name__, url_prefix='/data_import ')


@bp.route("/user_import", methods=['GET', 'POST'])
@login_required
def user_import():
    result = ' '
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
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER']) + "/" + file.filename
            result = parse_user_csv(file_path)

            if result:
                msg = 'super ça marche'
            else:
                msg = 'gros caca boudin'

            data = pd.read_csv(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename), sep=',', keep_default_na=False)

            # page = request.args.get('page', 1, type=int)
            #
            # table = Table.query.paginate(page=page, per_page=ROWS_PER_PAGE)



            return render_template(r'data_import/import_user.html', message=msg, tables=[data.to_html()], titles=[''])

        return render_template(r'data_import/import_user.html', message="Veuillez choisir un fichier .csv")
    else:
        return render_template(r'data_import/import_user.html')


@bp.route("/exam_import", methods=['GET', 'POST'])
@login_required
def exam_import():
    result = ' '
    if request.method == 'POST':
        # check if the post request has the file part
        print('post')
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
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER']) + "/" + file.filename
            result = parse_exam_csv(file_path)

            if result:
                msg = 'super ça marche'
            else:
                msg = 'gros caca boudin'

            # reading the data in the csv file
            data = pd.read_csv(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename), sep=';', keep_default_na=False)


            return render_template(r'data_import/import_exam.html', message=msg, tables=[data.to_html()], titles=[''])

        return render_template(r'data_import/import_exam.html', message="Veuillez choisir un fichier .csv")
    else:
        return render_template(r'data_import/import_exam.html')


#     # reading the data in the csv file
#     df = pd.read_csv(file.filename)
#     df.to_csv(file.filename, index=None)
#
#
# @bp.route('/table', methods=['GET', 'POST'])
# def table():
#     # converting csv to html
#     print(file.filename)
#     data = pd.read_csv(file.filename)
#     return render_template('tables.html', tables=[data.to_html()], titles=[''])


