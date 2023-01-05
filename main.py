from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from gui import QuizInterface

question_bank = [Question(question) for question in question_data]
quiz_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain)
