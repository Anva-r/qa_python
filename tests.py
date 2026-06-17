import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book_name', [
        'Гарри Поттер',
        'Властелин колец',
        '1984'
    ])
    def test_add_new_book_adds_book(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_not_added(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name not in collector.books_genre

    def test_add_new_book_added_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_set_book_genre_sets_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Роман')

        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Марсианин')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Гарри Поттер',
            'Марсианин'
        ]

    def test_get_books_genre_returns_books_genre_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_adds_book_once(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_deletes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []