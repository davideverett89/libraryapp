import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from libraryapp.models import model_factory
from ..connection import Connection

def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT l.id, l.location_id, l.user_id, u.first_name, u.last_name, u.email, lb.name, u.date_joined
        FROM libraryapp_librarian l
        JOIN auth_user u ON u.id = l.user_id
        JOIN libraryapp_library lb ON lb.id = l.location_id
        WHERE l.id = ?
        """, (librarian_id,))

        return db_cursor.fetchone()

@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        dataset = get_librarian(librarian_id)

        librarian = Librarian()
        librarian.id = dataset["id"]
        librarian.location_id = dataset["location_id"]
        librarian.user_id = dataset["user_id"]
        librarian.first_name = dataset["first_name"]
        librarian.last_name = dataset["last_name"]
        librarian.email = dataset["email"]
        librarian.branch_name = dataset["name"]
        librarian.date_joined = dataset["date_joined"]

        template = 'librarians/detail.html'

        context = {
            'librarian': librarian
        }

    return render(request, template, context)