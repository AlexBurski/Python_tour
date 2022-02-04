from module import *

Session = sessionmaker(bind=engine)
session = Session()


def add_author(given_1name, given_2name, nation_id):
    author = Author()
    author.first_name = given_1name
    author.last_name = given_2name
    author.nationality_id = nation_id
    session.add(author)
    session.commit()


def add_author_nationality(kingdom):
    nation = AuthorNationality()
    nation.country = kingdom
    session.add(nation)
    session.commit()


def add_category(example):
    category = Categories()
    category.name = example
    session.add(category)
    session.commit()


def add_book(title, author_id, num_of_pages, description, release_date):
    book = Book()
    book.title = title
    book.author_id = author_id
    book.number_of_pages = num_of_pages
    book.short_description = description
    book.release_date = release_date
    session.add(book)
    session.commit()


def add_user(fname, sname, birth_date):
    user = User()
    user.first_name = fname
    user.last_name = sname
    user.birth_date = birth_date
    session.add(user)
    session.commit()


def add_review(book_id, user_id, rating):
    review = Reviews()
    review.book_id = book_id
    review.user_id = user_id
    review.feedback = rating
    session.add(review)
    session.commit()


def booklog(user_id, book_id, date_start, date_end):
    book_log = BookLog()
    book_log.user_id = user_id
    book_log.book_id = book_id
    book_log.date_start = date_start
    book_log.date_end = date_end
    session.add(book_log)
    session.commit()
