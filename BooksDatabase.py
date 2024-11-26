# Darlene Lopez
# CIS 131
# Finds authors and their books using SQL database

import sqlite3
import pandas as pd


try:
    conn = sqlite3.connect('books.db')
    print("Database connection successful.")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    exit()


try:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

    # Check if 'authors' exists in the list of tables
    if ('authors',) not in tables:
        print("Error: 'authors' table does not exist in the database.")
        conn.close()
        exit()
except sqlite3.Error as e:
    print(f"Error checking tables: {e}")
    conn.close()
    exit()


try:
    query = "SELECT last AS last_name FROM authors ORDER BY last_name DESC;"
    df_authors = pd.read_sql_query(query, conn)
    print("Authors' Last Names (Descending Order):")
    print(df_authors)
except sqlite3.Error as e:
    print(f"Error executing query: {e}")


try:
    query = "SELECT title FROM titles ORDER BY title ASC;"
    df_titles = pd.read_sql_query(query, conn)
    print("\nBook Titles (Ascending Order):")
    print(df_titles)
except sqlite3.Error as e:
    print(f"Error executing query: {e}")

try:
    author_last_name = 'Wald'
    query = """
    SELECT titles.title, titles.copyright, titles.isbn
    FROM titles
    INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
    INNER JOIN authors ON authors.rowid = author_ISBN.id
    WHERE authors.last = ?
    ORDER BY titles.title ASC;
    """
    df_books = pd.read_sql_query(query, conn, params=(author_last_name,))
    print(f"\nBooks by {author_last_name}:")
    print(df_books)
except sqlite3.Error as e:
    print(f"Error executing query: {e}")

conn.close()
