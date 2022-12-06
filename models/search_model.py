import pandas as pd


def get_genre(conn):
    return pd.read_sql('''
    SELECT 
    genre_id AS id,
    COUNT(genre_id) AS Количество_экземпляров, 
    genre_name AS Название
    FROM genre
    JOIN book USING (genre_id)
    GROUP BY genre_id
    ORDER BY Название
    ''', conn)


def get_author(conn):
    return pd.read_sql('''
        SELECT 
        author_id AS id,
        COUNT(author_id) AS Количество_экземпляров, 
        author_name AS Название
        FROM author
        JOIN book_author USING (author_id)
        GROUP BY author_id
        ORDER BY Название
        ''', conn)


def get_publisher(conn):
    return pd.read_sql('''
        SELECT 
        publisher_id AS id,
        COUNT(publisher_id) AS Количество_экземпляров, 
        publisher_name AS Название
        FROM publisher
        JOIN book USING (publisher_id)
        GROUP BY publisher_id
        ORDER BY Название
        ''', conn)


def get_book(conn, genre, author, publisher):
    return pd.read_sql(f'''
    WITH author_books AS (
        SELECT book_id,
               title AS Название,
               genre_name AS Жанр,
               publisher_name AS Издательство,
               year_publication AS Год_издания,
               available_numbers AS Количество
        FROM book
        JOIN book_author USING (book_id)
        JOIN author USING (author_id)
        JOIN genre USING (genre_id) 
        JOIN publisher USING (publisher_id) 
            
        WHERE (author_name IN ({str(author).strip('[]')}) OR {not author}) 
            AND (Жанр IN ({str(genre).strip('[]')}) OR {not genre}) 
            AND (Издательство IN ({str(publisher).strip('[]')}) OR {not publisher})                 
        GROUP BY book_id)
        
    SELECT book_id, Название, Жанр, Издательство, Год_издания, Количество, group_concat(author_name) AS Авторы
    FROM author_books
    JOIN book_author USING (book_id)
    JOIN author USING (author_id)
    GROUP BY Название
    ''', conn)
