import csv
import pickle

class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

def save_books_to_csv(books, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for book_item in books:
            book_list = list(book_item)
            writer.writerow([book_list])

def load_books_from_csv():
    with open('books.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        data = []
        for row in csv_reader:
            data.append(tuple(row))
    csv_file.close()
    print(data)

def save_books_to_pickle(books, filename):
    with open(filename, 'wb') as f:
        pickle.dump(books, f)

def load_books_from_pickle(filename):
    with open(filename, 'rb') as f:
        books = pickle.load(f)
        print(books)

def function_task1():
    books = []
    book_item = ("War-and-Peace", "Tolstoy", 1869)
    books.append(book_item)
    book_item = ("Anna-Karenina", "Tolstoy", 1877)
    books.append(book_item)
    book_item = ("Idiot", "Dostoevskiy", 1869)
    books.append(book_item)
    book_item = ("Prestuplenie-i-nakazanie", "Dostoevskiy", 1866)
    books.append(book_item)
    save_books_to_csv(books, "books.csv")
    print("csv file value")
    load_books_from_csv()
    save_books_to_pickle(books, "books.pickle")
    print("pickle file value")
    load_books_from_pickle("books.pickle")
    author = input("Enter author's last name: ")
    for book in books:
        if author == book[1]:
            print(f"{book[0]} ({book[2]})")