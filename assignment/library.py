def take_book(layer):
    if len(layer) > 0:
        book = layer.pop()
        print("Student took off a book. Remaining books in the layer:", len(layer))
    else:
        print("No books left in the layer.")

def put_book(layer, book):
    layer.append(book)
    print("Student put a book back on the layer. Remaining books in the layer:", len(layer))

book_layer = []  # Initially, the book layer is empty
put_book(book_layer, "Book 1")
put_book(book_layer, "Book 2")
put_book(book_layer, "Book 3")
take_book(book_layer)
take_book(book_layer)
take_book(book_layer)
take_book(book_layer)  # No books left to take off
put_book(book_layer, "Book 4")
put_book(book_layer, "Book 5")
take_book(book_layer)
take_book(book_layer)
take_book(book_layer)  
