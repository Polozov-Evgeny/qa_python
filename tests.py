import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Властелин колец')

        assert collector.books_genre.get('Властелин колец') == ''

    def test_set_book_genre_set_one_genre(self, collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.books_genre.get('Властелин колец') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre', [
        ['Властелин колец', 'Фантастика'],
        ['Дракула', 'Ужасы'],
        ['Рассказы о Шерлоке Холмсе', 'Детективы'],
        ['Остров сокровищ', 'Мультфильмы'],
        ['Ревизор', 'Комедии']
    ])
    def test_get_book_genre_get_genres(self, book_name, genre, collector, add_books_with_genres):
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre', [
        ['Властелин колец', 'Фантастика'],
        ['Дракула', 'Ужасы'],
        ['Рассказы о Шерлоке Холмсе', 'Детективы'],
        ['Остров сокровищ', 'Мультфильмы'],
        ['Ревизор', 'Комедии']
    ])
    def test_get_books_with_specific_genre_get_books_with_different_genres(self, book_name, genre, collector,
                                                                           add_books_with_genres):
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_genre_get_books_with_all_genres(self, collector, add_books_with_genres):
        expected_result = {
            'Властелин колец': 'Фантастика',
            'Дракула': 'Ужасы',
            'Рассказы о Шерлоке Холмсе': 'Детективы',
            'Остров сокровищ': 'Мультфильмы',
            'Ревизор': 'Комедии'
        }

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_get_books_not_from_the_genre_age_rating_list(self, collector, add_books_with_genres):
        expected_result = ['Властелин колец', 'Остров сокровищ', 'Ревизор']

        assert collector.get_books_for_children() == expected_result

    def test_add_book_in_favorites_add_one_book_in_favorites(self, collector, add_books_with_genres):
        collector.add_book_in_favorites('Властелин колец')

        assert 'Властелин колец' in collector.favorites

    def test_delete_book_from_favorites_delete_one_book_from_favorites(self, collector, add_books_with_genres):
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Остров сокровищ')
        collector.delete_book_from_favorites('Властелин колец')

        assert not 'Властелин колец' in collector.favorites and 'Остров сокровищ' in collector.favorites

    def test_get_list_of_favorites_books_get_three_favorites_books(self, collector, add_books_with_genres):
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('Остров сокровищ')
        collector.add_book_in_favorites('Ревизор')
        expected_result = ['Властелин колец', 'Остров сокровищ', 'Ревизор']

        assert collector.get_list_of_favorites_books() == expected_result
