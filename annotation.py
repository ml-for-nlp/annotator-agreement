'''Collect annotation from human subject.'''

import random

classes = [1,2,3,4,5]

def read_questions():
    f = open("data/questions.txt")
    questions = f.readlines()
    return questions

def write_annotation(username, answers):
    f = open("annotations/"+username+".txt",'w')
    for k,v in answers.items():
        f.write(k.rstrip('\n')+"::"+str(v)+"\n")
    f.close()

questions = read_questions()
random.shuffle(questions)
answers = {}

print("\n\nIn the following, you will find 50 statements about the person you have just read about.\nYour task is to say to what extent you agree with the statement, \ngiving a score between 1 and 5 (1=fully disagree, 5=fully agree).\n\nYou may find that some of the statements will have a clear answer, while others \nrequire some guesswork. Don't hesitate to answer based on what you imagine the \nperson to be like. For instance, if the article is on someone who went to drama \nschool and ended up being a famous actor, you may infer that the person is likely\nto know how to dance, even if the Wikipedia article does not say so. There is no \nright or wrong answer, and you can come back to the text as many times as you like \nif it helps you.")

username = input("\n\nPlease enter your name: ")

print("Now, answer each question with a value (1-5). You can always quit by pressing 'q'.\n\n")

for q in questions:
    user_answer = input(q)
    while user_answer not in [str(c) for c in classes] and user_answer != 'q':
        user_answer = input("Please enter a value in the range (1-5)\n"+q)
    if user_answer == 'q':
        break
    else:
        answers[q] = user_answer

write_annotation(username,answers)
print("Thank you! Your annotations are in the file annotations/"+username+".txt")
