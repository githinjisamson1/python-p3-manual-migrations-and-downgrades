# models.py
from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import (CheckConstraint, UniqueConstraint,
                        Column, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'scholars'
    __table_args__ = (
        UniqueConstraint('email',
                         name='unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12',
                        name='grade_between_1_and_12')
    )

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, "
