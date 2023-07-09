from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):

        def click_true():
            print("true button clicked")

        def click_false():
            print("false button clicked")

        self.window = Tk()
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.label = Label(text="score: 0",fg="white",bg=THEME_COLOR,padx=20,pady=20)
        self.label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(
            50,
            50,
            text="some question text",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,bg=THEME_COLOR, highlightthickness=0, command=click_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,bg=THEME_COLOR, highlightthickness=0, command=click_false)
        self.false_button.grid(row=2, column=1)



        self.window.mainloop()