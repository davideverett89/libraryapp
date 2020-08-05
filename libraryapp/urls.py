from django.urls import include, path
from .views import *
from .views import home

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('libraries/', library_list, name='libraries'),
    path('librarians/', list_librarians, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/form', book_form, name='book_form'),
    path('libraries/form', library_form, name="library_form"),
    path('books/<int:book_id>/', book_details, name='book'),
    path('logout/', logout_user, name='logout')
]