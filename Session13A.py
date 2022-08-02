class WebPage:

    def __init__(self, title, domain, url):
        self.title = title
        self.domain = domain
        self.url = url
        self.next = None
        self.previous = None

    def show(self):
        print(self.title, self.domain, self.url)


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Stack Created...")

    def push(self, page):
        self.size += 1

        if self.head is None:
            self.head = page
            self.tail = page
        else:
            self.tail.next = page
            page.previous = self.tail
            self.tail = page

    def pop(self):

        self.size -= 1
        temp = self.tail
        self.tail = self.tail.previous
        self.tail.next = None
        del temp

    def peek(self, option=1):
        if option == 1:
            return self.tail
        else:
            return self.head

    def iterate(self):
        temp = self.tail
        while True:

            temp.show()
            temp = temp.previous

            if temp.previous is None:
                temp.show()
                break


stack = Stack()
stack.push(WebPage(title="Auribises", domain="www.auribises.com", url="elearning.auribises.com"))
stack.push(WebPage(title="StackOverlflow", domain="www.stackoverflow.com", url="stackoverflow.com/python"))
stack.push(WebPage(title="GoDaddy", domain="www.godaddy.in", url="https://www.godaddy.com/en-in"))


stack.pop()
stack.iterate()

print("SIZE of Stack is:", stack.size)

print("PEEK...")
stack.peek().show()