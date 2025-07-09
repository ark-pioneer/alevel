import random

with open("AQA-7517-SSV.csv", "r") as f:
    data = f.read().splitlines()

topic_questions = []
for row in data:
    row_list = row.split(", ")
    if row_list[3] == "4.2 Fundamentals of data structures":
        topic_questions.append(row_list)

answers = []
for i in range(5):
    print(topic_questions[i][1])
    answer = input("Write your answer here: ")
    answers.append(answer)

with open("quiz_answers", "w") as f:
    # one at a time store the user answers
    

    

# def get_random_question(topic_name):
#     topic = [line for line in data if line.split(",")[3] == topic_name]
#     random_index = random.randint(0, len(topic)-1)
#     return topic[random_index].split(",")

# # with open("quiz_answers", "w") as f:
#     for _i in range(5):
#         random_question = get_random_question(topic="4.2 Fundamentals of data structures")
#         print("Define: '" + random_question[1], end="'\tWrite your answer here: ")
#         user_answer = input()
#         f.write(f"{random_question[1]},{random_question[2]},{user_answer}\n")
    
    
    

