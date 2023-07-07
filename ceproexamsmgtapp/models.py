from falcon.bench.nuts.config import app
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

user_has_exam = db.Table('user_has_exam',
    db.Column('exam_id', db.Integer, db.ForeignKey('exam.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('contact_person', db.Boolean(), default=False)
)

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(30))
    name = db.Column(db.String(100))
    exam_date = db.Column(db.DateTime())
    exam_semester = db.Column(db.String(10))
    nb_students = db.Column(db.Integer)
    nb_pages = db.Column(db.Integer)
    total_pages = db.Column(db.Integer)
    deadline_prep = db.Column(db.Date(), nullable=True)
    deadline_repro = db.Column(db.Date(), nullable=True)
    remark = db.Column(db.String(250))
    exam_type_id = db.Column(db.Integer, db.ForeignKey('exam_type.id'))
    exam_status_id = db.Column(db.Integer, db.ForeignKey('exam_status.id'))
    service_level_id = db.Column(db.Integer, db.ForeignKey('service_level.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    academic_year_id = db.Column(db.Integer, db.ForeignKey('academic_year.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    userhasexam = db.relationship('User', secondary=user_has_exam, lazy='subquery',
                                  backref=db.backref('exams', lazy=True))

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
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    userhasexam = db.relationship('Exam', secondary=user_has_exam, lazy='subquery',
                           backref=db.backref('users', lazy=True))


    def is_active(self):
        return True
    def get_id(self):
        return self.email
    def is_authenticated(self):
        return self.authenticated
    def is_anonymous(self):
        return False

# userhasexam = db.Table('userhasexam',
#     db.Column('exam_id', db.Integer, db.ForeignKey('exam.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('contact_person', db.Boolean(), default=False)
# )

class ExamHasSection(db.Model):
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), primary_key=True)


