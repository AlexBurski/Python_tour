from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://dbuser:hello@localhost:5432/db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.id"))
    number_of_pages = Column(Integer)
    short_description = Column(String)
    rating = Column(Integer)
    release_date = Column(String)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    birth_date = Column(Integer)


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    feedback = Column(Integer)


class BookLog(Base):
    __tablename__ = 'booklog'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    date_start = Column(String)
    date_end = Column(String)


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality_id = Column(Integer, ForeignKey("author_nationality.id"))


class AuthorNationality(Base):
    __tablename__ = 'author_nationality'

    id = Column(Integer, primary_key=True)
    country = Column(String)


class BookToCategory(Base):
    __tablename__ = 'book_to_category'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    book_id = Column(Integer, ForeignKey("book.id"))


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)
