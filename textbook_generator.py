import tkinter as tk
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class MathPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Practice")
        self.questions_frame = tk.Frame(self.root)
        self.questions_frame.pack()

        tk.Label(self.root, text="Addition digits (e.g., 2,2)").pack()
        self.addition_entry = tk.Entry(self.root)
        self.addition_entry.pack()
        self.addition_entry.insert(0, "2,2")
		
        tk.Label(self.root, text="Subtraction digits (e.g., 2,2)").pack()
        self.subtraction_entry = tk.Entry(self.root)
        self.subtraction_entry.pack()
        self.subtraction_entry.insert(0, "2,2")

        tk.Label(self.root, text="Multiplication digits (e.g., 2,2)").pack()
        self.multiplication_entry = tk.Entry(self.root)
        self.multiplication_entry.pack()
        self.multiplication_entry.insert(0, "2,2")

        tk.Label(self.root, text="Division digits (e.g., 2,2)").pack()
        self.division_entry = tk.Entry(self.root)
        self.division_entry.pack()
        self.division_entry.insert(0, "2,2")

        tk.Label(self.root, text="Number of pages (e.g. 2)").pack()
        self.pages_entry = tk.Entry(self.root)
        self.pages_entry.pack()
        self.pages_entry.insert(0, "2")

        self.generate_button = tk.Button(self.root, text="Generate Questions", command=self.generate_questions)
        self.generate_button.pack()

    def generate_questions(self):
        for widget in self.questions_frame.winfo_children():
            widget.destroy()

        operations = ['+', '-', '*', '/']
        pages = int(self.pages_entry.get())
        c = canvas.Canvas("math_practice.pdf", pagesize=A4)
        for page in range(pages):
            questions = []
            for i in range(40):
                operation = random.choice(operations)
                if operation == '+':
                    digits = self.addition_entry.get().split(',')
                    num1 = random.randint(10**(int(digits[0])-1), 10**int(digits[0])-1)
                    num2 = random.randint(10**(int(digits[1])-1), 10**int(digits[1])-1)
                elif operation == '-':
                    digits = self.subtraction_entry.get().split(',')
                    num1 = random.randint(10**(int(digits[0])-1), 10**int(digits[0])-1)
                    num2 = random.randint(10**(int(digits[1])-1), 10**int(digits[1])-1)
                    num1, num2 = max(num1, num2), min(num1, num2)
                elif operation == '*':
                    digits = self.multiplication_entry.get().split(',')
                    num1 = random.randint(10**(int(digits[0])-1), 10**int(digits[0])-1)
                    num2 = random.randint(10**(int(digits[1])-1), 10**int(digits[1])-1)
                elif operation == '/':
                    digits = self.division_entry.get().split(',')
                    num1 = random.randint(10**(int(digits[0])-1), 10**int(digits[0])-1)
                    num2 = random.randint(10**(int(digits[1])-1), 10**int(digits[1])-1)
                    num1 *= num2

                question = f"{i+1}. {num1} {operation} {num2} = ?"
                questions.append(question)
#                label = tk.Label(self.questions_frame, text=question)
#                label.pack()

            self.generate_pdf(questions, c, page, pages)
        c.save()

    def generate_pdf(self, questions, c, page, pages):
        for i, question in enumerate(questions):
            c.drawString(10, A4[1] - 20 * (i + 1), question)
        if page < pages - 1:
            c.showPage()

root = tk.Tk()
app = MathPracticeApp(root)
root.mainloop()
