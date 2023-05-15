from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ExamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))

class ExamStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))

class ServiceLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    description = db.Column(db.String(100))


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exam_date = db.Column(db.DateTime())
    exam_years = db.Column(db.String(10))
    exam_semester = db.Column(db.String(10))
    nb_students = db.Column(db.Integer)
    nb_pages = db.Column(db.Integer)
    deadline_prep = db.Column(db.DateTime())
    deadline_repro = db.Column(db.DateTime())
    remark = db.Column(db.String(250))
    exam_type = db.relationship('ExamType', backref='exams', lazy='dynamic')
    exam_status = db.relationship('ExamStatus', backref='exams', lazy='dynamic')
    service_level = db.relationship('ServiceLevel', backref='exams', lazy='dynamic')
    service = db.relationship('Service', backref='exams', lazy='dynamic')
    responsable = db.relationship('Employee', backref='exams', lazy='dynamic')

class EmployeeType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(20))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    sciper = db.Column(db.String(6))
    employee_type = db.relationship('EmployeeType', backref='employees', lazy='dynamic')

class EmployeeHasExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam = db.relationship('Exams', backref='EmployeeHasExam', lazy='dynamic')
    employee = db.relationship('Employee', backref='EmployeeHasExam', lazy='dynamic')
    contact_person = db.Column(db.Boolean(), default=False)

class ExamHasSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.relationship('Section', backref='ExamHasSection', lazy='dynamic')
    exam = db.relationship('Exam', backref='ExamHasSection', lazy='dynamic')




    # ExamStatus
    #   id = 1
    #   code = scanned
    #   name = Scanned exam
    
# exams : 1,2,5 --> examstatus.1
    # Exam
    #   id = 1
    #   code = A
    #   name = toto
    #   exam_status = id=1
    
#    print(exam.code)
#    A



#    print(exam.name)
#    toto

#    print(exam_status.code)
#    scanned

#    print(exam_status.exams)

#    for exam in exam_status.exams:
#        print(exam.id)
#
#        1
#       2
#        5