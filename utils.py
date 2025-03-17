from random import choice

import database
from database import get_db, add_book, update_book, delete_book, list_books, search_books
from sqlalchemy.orm import Session


import database

def main():
    database.create_tables()
    while True:
        # ... (menú y lógica principal)
        if choice == "1":
            add_book_cli()
        # ... (otras opciones)

def display_menu():
    """Muestra el menú principal."""
    print("\n--- Biblioteca Personal ---")
    print("1. Agregar libro")
    print("2. Actualizar libro")
    print("3. Eliminar libro")
    print("4. Listar libros")
    print("5. Buscar libros")
    print("6. Salir")

def add_book_cli(db: Session = next(get_db())):
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado_lectura = input("Estado (leído/no leído): ")
    add_book(db, titulo, autor, genero, estado_lectura)

# Modifica update_book_cli, delete_book_cli, list_books_cli y search_books_cli...

def update_book():
    """Solicita datos del libro y llama a database.update_book()."""
    book_id = input("ID del libro a actualizar: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado_lectura = input("Estado (leído/no leído): ")
    database.update_book(book_id, titulo, autor, genero, estado_lectura)

def delete_book():
    """Solicita el ID del libro y llama a database.delete_book()."""
    book_id = input("ID del libro a eliminar: ")
    database.delete_book(book_id)

def list_books():
    """Llama a database.list_books() y muestra los resultados."""
    books = database.list_books()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Género: {book[3]}, Estado: {book[4]}")
    else:
        print("No hay libros en la biblioteca.")

def search_books():
    """Solicita la búsqueda y llama a database.search_books()."""
    query = input("Buscar: ")
    field = input("Buscar por (titulo/autor/genero): ")
    books = database.search_books(query, field)
    if books:
        for book in books:
            print(f"ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Género: {book[3]}, Estado: {book[4]}")
    else:
        print("No se encontraron libros.")


def search_books_cli():
    return None


def list_books_cli():
    return None