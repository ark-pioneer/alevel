# ./quiz.py
import random

class Quiz():
    def __init__(self, rounds, questions, topics):
        self.__rounds = rounds
        self.__questions = questions
        self.__topics = topics
    
    def play(self):
        return [self.__format_round_result(self.__play_round(self.__get_random_question())) for _i in range(self.__rounds)]

    def __get_random_question(self):
        question_set = [q for q in self.__questions if q.split(",")[3] in self.__topics]
        question_data = question_set[random.randint(0, len(question_set)-1)].split(",")
        return {
            "number": question_data[0],
            "text": question_data[1],
            "answer": question_data[2],
            "topic": question_data[3]
        }

    def __prompt_for(self, question):
        return f"Define: '{question['text']}'\t\tWrite your answer here: "

    def __format_round_result(self, question):
        return f"{question['text']},{question['answer']},{question['user_answer']}"

    def __play_round(self, question):
        print(self.__prompt_for(question), end="")
        question["user_answer"] = input()
        return question

# ./main.py
from quiz import Quiz

with open("AQA-7517-SSV.csv", "r") as f:
    data = f.read().splitlines()

quiz = Quiz(rounds=5, questions=data, topics=["4.2 Fundamentals of data structures"])
result = quiz.play()

with open("quiz_answers", "w") as f:
    for round in result:
        f.write(round + "\n")