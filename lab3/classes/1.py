class String:
    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("Uppercase version:", self.input_string.upper())

manipulator = String()
manipulator.getString()
manipulator.printString()