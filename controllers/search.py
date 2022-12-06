from app import app
from flask import render_template, request
from utils import get_db_connection
from models.search_model import *


@app.route('/search', methods=['get'])
def search():
    conn = get_db_connection()

    # выполняем запросы к БД
    df_genre = get_genre(conn)
    df_author = get_author(conn)
    df_publisher = get_publisher(conn)

    genres = request.form.getlist('genres')
    authors = request.form.getlist('authors')
    publishers = request.form.getlist('publishers')

    df_book = get_book(conn, genres, authors, publishers)

    # выводим форму
    html = render_template(
        'search.html',
        sections=['Жанр', 'Автор', 'Издательство'],
        list_data=[df_genre, df_author, df_publisher],
        list_choices=[genres, authors, publishers],
        books=df_book,
        genres=genres,
        authors=authors,
        publishers=publishers,
        len=len,
        zip=zip,
    )

    return html
