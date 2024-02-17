class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'a+')  

    def list_books(self):
        self.file.seek(0)  
        book_list = self.file.read().splitlines() 
        if len(book_list) == 0:
            print('No books to list')
        else:
            for book in book_list:
                book_info = book.split(', ')  
                print(f"Book Name: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input('Enter the book title: ')
        author = input('Enter the author: ')
        release_year = input('Enter the release year: ')
        number_of_page = input('Enter the number of page: ')
        
        kitap_bilgileri = f"{title}, {author}, {release_year}, {number_of_page}\n"
        self.file.write(kitap_bilgileri)
        print("Book added successfully...")

    def remove_book(self):
        title = input("Enter the name of the book you want to delete: ").strip() 
        self.file.seek(0)
        book_list = self.file.readlines()
        updated_list = [book for book in book_list if title not in book.split(",")[0].strip()] 
        if len(updated_list) != len(book_list): 
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines(updated_list)
            print("Book deleted successfully")
        else:
            print('Book not available, try again')

    def __del__(self):
        self.file.close()


def menu():
    print(' ')
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice = input("Please make a choice (1-3 or q): ")
    return choice


lib = Library('books.txt')

while True:
    choice = menu()

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        print('Program Terminated\n**********')  
        break
    else:
        print("Invalid selection. Please try again.")
