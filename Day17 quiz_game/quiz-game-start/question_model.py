# new_q = Question("2+3=5", "True")
# attr = text, answ

from cgitb import text


class Question:
    def __init__(self,text,answer) -> None:
        self.text = text
        self.answer = answer