from abc import ABC, abstractmethod



# Book Class


class Book:

    book_count = 0

    def __init__(self, title, author, category, available_copies):
        Book.book_count += 1

        self.__book_id = Book.book_count
        self.__title = title
        self.__author = author
        self.__category = category
        self.__available_copies = available_copies
        self.__total_copies = available_copies

    # Getters
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def category(self):
        return self.__category

    @property
    def available_copies(self):
        return self.__available_copies

    @property
    def total_copies(self):
        return self.__total_copies

    # Methods
    def display_info(self):
        borrowed_copies = self.__total_copies - self.__available_copies

        print(f"Book ID          : {self.__book_id}")
        print(f"Title            : {self.__title}")
        print(f"Author           : {self.__author}")
        print(f"Category         : {self.__category}")
        print(f"Available Copies : {self.__available_copies}")
        print(f"Borrowed Copies  : {borrowed_copies}")

    def borrow_book(self):

        if self.__available_copies > 0:
            self.__available_copies -= 1
            return True

        return False

    def return_book(self):

        if self.__available_copies < self.__total_copies:
            self.__available_copies += 1
            return True

        return False



# User Abstract Class


class User(ABC):

    user_count = 0

    def __init__(self, name):

        User.user_count += 1

        self.__user_id = User.user_count
        self.__name = name
        self.__borrowed_books = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    @abstractmethod
    def borrow(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

    @abstractmethod
    def show_menu(self):
        pass



# Student Class


class Student(User):

    MAX_BOOKS = 3

    def borrow(self, book):

        if len(self.borrowed_books) >= self.MAX_BOOKS:
            print("You cannot borrow more than 3 books.")
            return

        if book.borrow_book():

            self.borrowed_books.append(book)

            print("Book borrowed successfully.")

        else:

            print("This book is not available.")


    def return_book(self, book):

        if book not in self.borrowed_books:

            print("You did not borrow this book.")
            return

        if book.return_book():

            self.borrowed_books.remove(book)

            print("Book returned successfully.")


    def show_menu(self):

        print("\n===== Student Menu =====")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Display available books")
        print("4. Display borrowed books")
        print("0. Exit")



# Teacher Class


class Teacher(User):

    MAX_BOOKS = 5

    def borrow(self, book):

        if len(self.borrowed_books) >= self.MAX_BOOKS:
            print("You cannot borrow more than 5 books.")
            return

        if book.borrow_book():

            self.borrowed_books.append(book)

            print("Book borrowed successfully.")

        else:

            print("This book is not available.")


    def return_book(self, book):

        if book not in self.borrowed_books:

            print("You did not borrow this book.")
            return

        if book.return_book():

            self.borrowed_books.remove(book)

            print("Book returned successfully.")


    def show_menu(self):

        print("\n===== Teacher Menu =====")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Display available books")
        print("4. Display borrowed books")
        print("0. Exit")



# Librarian Class


class Librarian(User):

    def __init__(self, name):

        super().__init__(name)

        self.__library_books = []

    @property
    def library_books(self):
        return self.__library_books

    def add_book(self, title, author, category, available_copies):

        book = Book(
            title,
            author,
            category,
            available_copies
        )

        self.__library_books.append(book)

        print("Book added successfully.")

    def remove_book(self, book_id):

        for book in self.__library_books:

            if book.book_id == book_id:

                if book.available_copies != book.total_copies:

                    print("Cannot remove a borrowed book.")
                    return

                self.__library_books.remove(book)

                print("Book removed successfully.")
                return

        print("Book not found.")

    def search_books(self, title):

        found = False

        for book in self.__library_books:

            if title.lower() in book.title.lower():

                book.display_info()

                print("-" * 50)

                found = True

        if not found:

            print("Book not found.")

    def view_all_books(self):

        if len(self.__library_books) == 0:

            print("No books in the library.")
            return

        for book in self.__library_books:

            book.display_info()

            print("-" * 50)

    def view_available_books(self):

        found = False

        for book in self.__library_books:

            if book.available_copies > 0:

                book.display_info()

                print("-" * 50)

                found = True

        if not found:

            print("No available books.")

    def view_borrowed_books(self):

        found = False

        for book in self.__library_books:

            if book.available_copies < book.total_copies:

                book.display_info()

                print("-" * 50)

                found = True

        if not found:

            print("No borrowed books.")

    def borrow(self, book):

        print("Librarian does not borrow books.")

    def return_book(self, book):

        print("Librarian does not return books.")

    def show_menu(self):

        print("\n===== Librarian Menu =====")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search books")
        print("4. View all books")
        print("5. Display available books")
        print("6. Display borrowed books")
        print("0. Exit")



# Helper Functions


def get_integer(message):

    while True:

        try:

            value = int(input(message))

            return value

        except ValueError:

            print("Invalid input. Please enter a number.")


def find_book(librarian):

    book_id = get_integer("Enter Book ID: ")

    for book in librarian.library_books:

        if book.book_id == book_id:

            return book

    print("Book not found.")

    return None


def display_user_borrowed_books(user):

    if len(user.borrowed_books) == 0:

        print("You have not borrowed any books.")

        return

    for book in user.borrowed_books:

        book.display_info()

        print("-" * 50)



# Main Program


print("=" * 50)
print("       SMART LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)


# Create librarian
librarian = Librarian("Library Admin")


# Some initial books
librarian.add_book(
    "Python Basics",
    "John Smith",
    "Programming",
    3
)

librarian.add_book(
    "Clean Code",
    "Robert Martin",
    "Programming",
    2
)

librarian.add_book(
    "Database Systems",
    "Thomas Connolly",
    "Database",
    4
)



# User Login


name = input("\nEnter your name: ")

print("\nChoose your role:")
print("1. Student")
print("2. Teacher")
print("3. Librarian")


role = get_integer("Enter your choice: ")


if role == 1:

    user = Student(name)

    print(f"\nWelcome {user.name}")
    print("You can borrow up to 3 books.")

elif role == 2:

    user = Teacher(name)

    print(f"\nWelcome {user.name}")
    print("You can borrow up to 5 books.")

elif role == 3:

    user = librarian

    print(f"\nWelcome {user.name}")

else:

    print("Invalid role.")
    exit()



# Main Menu Loop


while True:

    user.show_menu()

    choice = get_integer("Choose an option: ")


    
    # Student / Teacher
    

    if isinstance(user, (Student, Teacher)):

        if choice == 1:

            book = find_book(librarian)

            if book is not None:

                user.borrow(book)


        elif choice == 2:

            book = find_book(librarian)

            if book is not None:

                user.return_book(book)


        elif choice == 3:

            librarian.view_available_books()


        elif choice == 4:

            display_user_borrowed_books(user)


        elif choice == 0:

            print("Thank you for using the library.")

            break


        else:

            print("Invalid menu choice.")


    
    # Librarian
    

    elif isinstance(user, Librarian):

        if choice == 1:

            print("\n===== Add New Book =====")

            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category: ")

            available_copies = get_integer(
                "Enter number of copies: "
            )

            if available_copies <= 0:

                print("Number of copies must be greater than 0.")

            else:

                user.add_book(
                    title,
                    author,
                    category,
                    available_copies
                )


        elif choice == 2:

            book = find_book(user)

            if book is not None:

                user.remove_book(book.book_id)


        elif choice == 3:

            title = input("Enter book title to search: ")

            user.search_books(title)


        elif choice == 4:

            user.view_all_books()


        elif choice == 5:

            user.view_available_books()


        elif choice == 6:

            user.view_borrowed_books()


        elif choice == 0:

            print("Thank you for using the library.")

            break


        else:

            print("Invalid menu choice.")