class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):  # Add the missing colon here
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    people = [
        MyClass("Alice", 25),
        MyClass("Bob", 30),
        MyClass("Charlie", 35),
    ]

    for person in people:
        person.print_info()

    print("Total people: ", len(people))

    with open('/Users/oasishun/workspace/chatgpt/book-ai-pair-programming/05/syntax/file.txt') as f:
        content = f.read()
        print("File content: ", content)  # Add the missing closing parenthesis here

    x = lambda a, b: a + b  # Add the missing colon here
    print("Lambda result: ", x(5, 10))

if __name__ == "__main__":
    main()