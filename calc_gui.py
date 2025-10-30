import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        # Create input field
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), width=50, bd=10, insertwidth=4, bg="powder blue", justify='right')
        input_field.pack()

        # Create buttons
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(buttons_frame, text=button, width=10, height=3, command=self.calculate).grid(row=row, column=col, columnspan=2)
                col += 2
            elif button == 'C':
                tk.Button(buttons_frame, text=button, width=10, height=3, command=self.clear).grid(row=row, column=col)
                col += 1
            else:
                tk.Button(buttons_frame, text=button, width=10, height=3, command=lambda b=button: self.click(b)).grid(row=row, column=col)
                col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
