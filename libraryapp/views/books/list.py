import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from ..connection import Connection


def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn_num,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id,
                l.name as location
            from libraryapp_book b
            join libraryapp_library l 
            on b.location_id = l.id;
            """)

            all_books = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                book = Book()
                book.id = row['id']
                book.title = row['title']
                book.isbn = row['isbn_num']
                book.author = row['author']
                book.year_published = row['year_published']
                book.librarian_id = row['librarian_id']
                book.location_id = row['location_id']
                book.library = row['title']

                all_books.append(book)

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)