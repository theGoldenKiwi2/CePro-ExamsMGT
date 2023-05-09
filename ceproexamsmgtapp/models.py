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

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(50))
    exam_date = db.column(db.DateTime)
    exam_years = db.column(db.string(10))
    exam_semester = db.column(db.string(10))
    nb_students = db.column(db.Integer)
    nb_pages = db.column(db.Integer)
    deadline_prep = db.column(db.DateTime)
    deadline_repro = db.column(db.DateTime)
    remark = db.column(db.string(250))
    exam_type = db.relationship('ExamType', backref='exams', lazy='dynamic')
    exam_status = db.relationship('ExamStatus', backref='exams', lazy='dynamic')

class ExamHasSection(db.Model):
    id=db.column(db.Integer, primary_key=True)
    section = db.relationship('Section', backref='ExamHasSections', lazy='dynamic', nullable=False)
    exam = db.relationship('Exams', backref='ExamHasSections', lazy='dynamic', nullable=False)

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