import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Address(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)     
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    follower_number = Column(Integer, nullable=False)
    city = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))  

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    number_post = Column(Integer, nullable=False)
    number_likes = Column(Integer, nullable=False)
    number_coments = Column(Integer, nullable=False)
    perfil_id = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    number_follows = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_txt = Column(String(250), nullable=False)
    comment_number = Column(Integer, nullable=False)
    profile_id = relationship(Profile, backref='profile', lazy=True)
    post_id = relationship(Post, backref='post', lazy=True)
    user_id = Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e