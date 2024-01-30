import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Властелин колец')

        assert collector.books_genre.get('Властелин колец') == ''

    @pytest.mark.parametrize('book_name', [
        'Властелин колец',
        '',
        'Длинное название любимой книги, 41 символ'
    ])
    def test_add_new_book_book_is_not_added(self, book_name, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book(book_name)

        assert collector.books_genre == {'Властелин колец': ''}

    def test_set_book_genre_set_one_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.books_genre.get('Властелин колец') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre', [
        ['Несуществующее название', 'Фантастика'],
        ['Бедная Лиза', 'Несущетвующий жанр'],
        ['Несуществующее название', 'Несущетвующий жанр']
    ])
    def test_set_book_genre_genre_is_not_set(self, book_name, genre, collector):
        collector.add_new_book('Бедная Лиза')
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre == {'Бедная Лиза': ''}

    def test_get_book_genre_get_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_get_books_with_specific_genre_get_books_with_identical_genre(self, collector):
        collector.books_genre = {
            'Властелин колец': 'Фантастика',
            'Дракула': 'Ужасы',
            'Рассказы о Шерлоке Холмсе': 'Детективы',
            'Остров сокровищ': 'Мультфильмы',
            'Ревизор': 'Комедии',
            'Гарри Поттер': 'Фантастика'
        }

        assert collector.get_books_with_specific_genre('Фантастика') == ['Властелин колец', 'Гарри Поттер']

    def test_get_books_genre_get_dictionary_books_with_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Дракула', 'Ужасы')

        expected_result = {
            'Властелин колец': 'Фантастика',
            'Дракула': 'Ужасы'
        }

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_get_books_not_from_the_genre_age_rating_list(self, collector):
        collector.books_genre = {
            'Властелин колец': 'Фантастика',
            'Дракула': 'Ужасы',
            'Рассказы о Шерлоке Холмсе': 'Детективы',
            'Остров сокровищ': 'Мультфильмы',
            'Ревизор': 'Комедии'
        }

        expected_result = ['Властелин колец', 'Остров сокровищ', 'Ревизор']

        assert collector.get_books_for_children() == expected_result

    def test_get_books_for_children_get_empty_book_list(self, collector):
        collector.books_genre = {
            'Дракула': 'Ужасы',
            'Рассказы о Шерлоке Холмсе': 'Детективы',
            'Выдуманная книга': '',
            'Несуществующая книга': 'Жанр'
        }

        expected_result = []

        assert collector.get_books_for_children() == expected_result

    def test_add_book_in_favorites_add_one_book_in_favorites(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Властелин колец')

        assert 'Властелин колец' in collector.favorites

    def test_delete_book_from_favorites_delete_one_book_from_favorites(self, collector):
        collector.favorites = ['Властелин колец', 'Остров сокровищ']
        collector.delete_book_from_favorites('Властелин колец')

        assert collector.favorites == ['Остров сокровищ']

    def test_get_list_of_favorites_books_get_two_favorites_books(self, collector):
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Остров сокровищ')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Остров сокровищ')

        assert collector.get_list_of_favorites_books() == ['Властелин колец', 'Остров сокровищ']
