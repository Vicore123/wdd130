with open("books.txt") as book_file:
    for line in book_file:
        line = line.strip()
        print(line)