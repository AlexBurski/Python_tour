"""заполнение таблицы"""

from query import *
from faker import Faker
import random
from sqlalchemy.sql import func

CATEGORIES = ['comedy', 'drama', 'adventure', 'horror']
fake = Faker()
country_store = set()

def nat():
    for _ in range(30):
        fake_nation = fake.country()
        if fake_nation not in country_store:
            add_author_nationality(fake_nation)
            country_store.add(fake_nation)
            que = session.query(Book)
            session.add(categ)
            session.commit()

def adding_information_todb():
    for i in range(45):
        name, surname, *args = fake.name().split()
        country_id = random.randint(2, 30)
        add_author(name, surname, country_id)

    for category in CATEGORIES:
        add_category(category)

    for i in range(35):
        name, surname, *args = fake.name().split()
        date_of_birth = fake.date_time_between(start_date='-80y', end_date='-30y')
        add_user(name, surname, int(str(date_of_birth)[:4]))

    for i in range(40):
        title = fake.word()
        auth_id = random.randint(2, 20)
        pages_nums = random.randint(200, 500)
        plot = fake.sentence()
        release = str(fake.date())

        add_book(title, auth_id, pages_nums, plot, release)


    for i in range(2, 40):
        b_id = random.randint(2, 20)
        start_date = str(fake.date())
        end_date = str(fake.date())
        booklog(i, b_id, start_date, end_date)

    for _ in range(30):
        b_id = random.randint(2, 20)
        u_id = random.randint(2, 20)
        rating = random.randint(1, 10)
        add_review(b_id, u_id, rating)

    que = session.query(Book)
    for book in que:
        mark = session.query(func.avg(Reviews.feedback)).filter(Book.id == Reviews.book_id)
        book.rating = mark
        session.add(book)
        session.commit()

    que = session.query(Book)
    for b in que:
        categ = BookToCategory()
        categ.book_id = b.id
        categ.category_id = random.randint(1, 15)
        session.add(categ)
        session.commit()
