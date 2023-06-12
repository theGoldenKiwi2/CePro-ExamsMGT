from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ExamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exams = db.relationship('Exam', backref='exam_type', lazy='dynamic')

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exam_has_sections = db.relationship('ExamHasSection', backref='section', lazy='dynamic')

class ExamStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exams = db.relationship('Exam', backref='exam_status', lazy='dynamic')

class ServiceLevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exams = db.relationship('Exam', backref='service_level', lazy='dynamic')

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    description = db.Column(db.String(100))
    exams = db.relationship('Exam', backref='service', lazy='dynamic')


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
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_type.id'))
    exam_status_id = db.Column(db.Integer, db.ForeignKey('exam_status.id'))
    service_level_id = db.Column(db.Integer, db.ForeignKey('service_level.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    user_has_exams = db.relationship('UserHasExam', backref='exams', lazy='dynamic')
    exam_has_sections = db.relationship('ExamHasSection', backref='exams', lazy='dynamic')

class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(20))
    users = db.relationship('User', backref='user_type', lazy='dynamic')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    sciper = db.Column(db.String(6))
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    exams = db.relationship('UserHasExam', backref='user', lazy='dynamic')

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

class UserHasExam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    contact_person = db.Column(db.Boolean(), default=False)

class ExamHasSection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))




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