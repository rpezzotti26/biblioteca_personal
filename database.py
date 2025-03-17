import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql://usuario_biblioteca:contraseña_biblioteca@localhost/biblioteca_personal"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DATABASE_NAME = "biblioteca.db"

import sqlite3

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    autor = Column(String)
    genero = Column(String)
    estado_lectura = Column(String)

DATABASE_NAME = "biblioteca.db"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)

def add_book(db: Session, titulo: str, autor: str, genero: str, estado_lectura: str):
    db_book = Libro(titulo=titulo, autor=autor, genero=genero, estado_lectura=estado_lectura)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Implementa las funciones update_book, delete_book, list_books y search_books...

def create_connection():
    """Crea una conexión a la base de datos."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table():
    """Crea la tabla 'libros' si no existe."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = """
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                genero TEXT NOT NULL,
                estado_lectura TEXT NOT NULL
            );
            """
            cursor = conn.cursor()
            cursor.execute(sql)
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def add_book(titulo, autor, genero, estado_lectura):
    """Agrega un nuevo libro a la base de datos."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = """
            INSERT INTO libros (titulo, autor, genero, estado_lectura)
            VALUES (?, ?, ?, ?);
            """
            cursor = conn.cursor()
            cursor.execute(sql, (titulo, autor, genero, estado_lectura))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def update_book(book_id, titulo, autor, genero, estado_lectura):
    """Actualiza la información de un libro."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = """
            UPDATE libros
            SET titulo = ?, autor = ?, genero = ?, estado_lectura = ?
            WHERE id = ?;
            """
            cursor = conn.cursor()
            cursor.execute(sql, (titulo, autor, genero, estado_lectura, book_id))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def delete_book(book_id):
    """Elimina un libro por su ID."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = "DELETE FROM libros WHERE id = ?;"
            cursor = conn.cursor()
            cursor.execute(sql, (book_id,))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

def list_books():
    """Recupera y muestra todos los libros."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = "SELECT * FROM libros;"
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return []

def search_books(query, field):
    """Busca libros por título, autor o género."""
    conn = create_connection()
    if conn is not None:
        try:
            sql = f"SELECT * FROM libros WHERE {field} LIKE ?;"
            cursor = conn.cursor()
            cursor.execute(sql, (f"%{query}%",))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
    return []