from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root@localhost/shiyanlou')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    def __repr__(self):
        return '<User(name=%s)>'% self.name

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer,ForeignKey('user.id'))
    teacher = relationship('User')
    def __repr__(self):
        return '<Course(name=%s)>'%self.name

class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer,ForeignKey('course.id'))
    course = relationship('Course',backref='labs')
    def __repr__(self):
        return '<Lab(name=%s)>'%self.name

Base.metadata.create_all(engine)

course = session.query(Course).first()

lab1 = Lab(name='ORM Basic',course_id=course.id)
lab2 = Lab(name='Relationship Database',course=course)

session.add(lab1)
session.add(lab2)
session.commit()

course.labs
