from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(300, 400)
        self.window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

        tick_img = PhotoImage(file='images/true.png')
        cross_img = PhotoImage(file='images/false.png')

        self.tick_button = Button(image=tick_img, bd=0, highlightthickness=0, command=self.answered_true)
        self.cross_button = Button(image=cross_img, bd=0, highlightthickness=0, command=self.answered_false)
        self.q_card = Canvas(width=250, height=250, bg='white', highlightthickness=0, bd=0)
        self.question_text = self.q_card.create_text(
            125,
            125,
            text='',
            font=['Arial', 20, 'italic'],
            width=230,
            justify="center"
        )
        self.get_next_question()
        self.score = Label(bg=BACKGROUND_COLOR, highlightthickness=0, text="Score: 0",
                           fg='white', font=['Arial', 14, 'bold'])

        self.score.grid(row=0, column=1, pady=5)
        self.q_card.grid(row=1, column=0, columnspan=2, pady=10)
        self.tick_button.grid(row=2, column=0, padx=20, pady=10)
        self.cross_button.grid(row=2, column=1, padx=20, pady=10)

        self.window.mainloop()

    def get_next_question(self):
        self.tick_button.config(state="normal")
        self.cross_button.config(state="normal")
        if self.brain.still_has_questions():
            self.q_card.config(bg='white')
            q_text = self.brain.next_question()
            if len(q_text) > 100:
                self.q_card.itemconfig(self.question_text, font=['Arial', 16, 'italic'])
            else:
                self.q_card.itemconfig(self.question_text, font=['Arial', 20, 'italic'])
            self.q_card.itemconfig(self.question_text, text=q_text)

    def answered_true(self):
        self.tick_button.config(state="disabled")
        result = self.brain.check_answer("True")
        self.update_quiz(result)

    def answered_false(self):
        self.cross_button.config(state="disabled")
        result = self.brain.check_answer("False")
        self.update_quiz(result)

    def update_quiz(self, result):
        self.score.config(text=f"Score: {self.brain.score}")

        if result:
            self.q_card.config(bg='#98FB98')
        else:
            self.q_card.config(bg='#f54c4c')

        if self.brain.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.window.after(1000, self.finish_quiz)

    def finish_quiz(self):
        self.q_card.config(bg="white")
        self.q_card.itemconfig(self.question_text, text=f"You finished the Quiz! You scored {self.brain.score}/10")
        self.tick_button.config(state="disabled")
        self.cross_button.config(state="disabled")
