from app import app
from flask import render_template, request
from utils import get_db_connection
from models.search_model import *


@app.route('/search', methods=['get', 'post'])
def search():
    conn = get_db_connection()

    # выполняем запросы к БД
    df_genre = get_genre(conn)
    df_author = get_author(conn)
    df_publisher = get_publisher(conn)

    if request.form.get('clear'):
        genres = []
        publishers = []
        authors = []

    else:
        genres = request.form.getlist('Жанр')
        authors = request.form.getlist('Автор')
        publishers = request.form.getlist('Издательство')

    df_book = get_book(conn, genres, authors, publishers)

    # выводим форму
    html = render_template(
        'search.html',
        sections=['Жанр', 'Автор', 'Издательство'],
        list_data=[df_genre, df_author, df_publisher],
        list_choices=[genres, authors, publishers],
        books=df_book,
        # genre=genres,
        # author=authors,
        # publisher=publishers,
        len=len,
        zip=zip,
    )

    return html
