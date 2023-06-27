from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class ExamType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    exams = db.relationship('Exam', backref='exam_type', lazy='dynamic')

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

class AcademicYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(100))
    exams = db.relationship('Exam', backref='academic_year', lazy='dynamic')

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(100))
    exams = db.relationship('Exam', backref='section', lazy='dynamic')

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30))
    name = db.Column(db.String(100))
    exam_date = db.Column(db.DateTime())
    exam_semester = db.Column(db.String(10))
    nb_students = db.Column(db.Integer)
    nb_pages = db.Column(db.Integer)
    deadline_prep = db.Column(db.DateTime())
    deadline_repro = db.Column(db.DateTime())
    remark = db.Column(db.String(250))
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_type.id'), primary_key=True)
    exam_status_id = db.Column(db.Integer, db.ForeignKey('exam_status.id'), primary_key=True)
    service_level_id = db.Column(db.Integer, db.ForeignKey('service_level.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    academic_year_id = db.Column(db.Integer, db.ForeignKey('academic_year.id'), primary_key=True)
    user_has_exams = db.relationship('UserHasExam', backref='exams', lazy='dynamic')
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), primary_key=True)
class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(20))
    users = db.relationship('User', backref='user_type', lazy='dynamic')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lastname = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    sciper = db.Column(db.String(6))
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), primary_key=True)
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
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    contact_person = db.Column(db.Boolean(), default=False)

class ExamHasSection(db.Model):
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), primary_key=True)
