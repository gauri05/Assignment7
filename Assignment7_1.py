print("BookStore......")


class BookStore:
    NoOfBooks = 0

    def __init__(self, nm, au):
        self.name = nm
        self.author = au
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print ("Book name====", self.name)
        print ("Author=====", self.author)
        print ("Number of books==", BookStore.NoOfBooks)


def main():
    Obj1 = BookStore("Linux System Programming", "RobertLove")
    Obj1.Display()  # Linux System Programming by Robert Love. No of books : 1
    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()  # C Programming by Dennis Ritchie. No of books : 2


if __name__ == '__main__':
    main()
