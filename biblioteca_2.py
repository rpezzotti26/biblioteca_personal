import database
import utils

from utils import update_book_cli, delete_book_cli, list_books_cli


def main():
    database.create_table()
    while True:
        utils.display_menu()
        choice = input("Elige una opción: ")
        if choice == "1":
            utils.add_book()
        elif choice == "2":
            utils.update_book()
        elif choice == "3":
            utils.delete_book()
        elif choice == "4":
            utils.list_books()
        elif choice == "5":
            utils.search_books()
        elif choice == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
