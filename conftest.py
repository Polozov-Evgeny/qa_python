import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope='function')
def add_books_with_genres(collector):
    collector.add_new_book('Властелин колец')
    collector.add_new_book('Дракула')
    collector.add_new_book('Рассказы о Шерлоке Холмсе')
    collector.add_new_book('Остров сокровищ')
    collector.add_new_book('Ревизор')

    collector.set_book_genre('Властелин колец', 'Фантастика')
    collector.set_book_genre('Дракула', 'Ужасы')
    collector.set_book_genre('Рассказы о Шерлоке Холмсе', 'Детективы')
    collector.set_book_genre('Остров сокровищ', 'Мультфильмы')
    collector.set_book_genre('Ревизор', 'Комедии')
