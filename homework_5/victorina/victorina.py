# Implement a simple quiz-game that will contain lists of questions and 
# answers. Random from starting the game in principle, a question should 
# be asked to the player and depending on the answer, the number of 
# correct answers will appear at the end of the game. Questions should not be repeated.


import random

# to complete the question file

# f = open('questions.txt', 'w')
# for i in range(100):
#     f.write(str(i + 1)+ ' question' + str(i + 1) + '\n')
# f.close()

# to complete the answer file

# f = open('answers.txt', 'w')
# for i in range(100):
#     true = random.randint(1, 4)
#     f.write(str(i + 1) + ' ' + str(true))
#     for j in range(4):
#         f.write(' [' + str(j + 1) + '.variant]')
#     f.write('\n')
# f.close()

# randomly select 10 questions for a given player from the question file
quest = [] 
while len(quest) <= 10:
    line = random.choice(list(open('questions.txt')))
    # questions should not be repeated
    if line not in quest:
        quest.append(line.split())
q_list = []
q_number = []
# cut the numbers of the questions (the word about the number in the file) by storing it in the q_number list
for i in quest:
    q_number.append(i[0])
    del i[0]
    # fill the questions in the processed form into q_list
    q_list.append(str(i[0]))

# find the answer versions of the selected questions from the answer file, add them to a_list
a_list = []
right_answer = []
for i in q_number: 
    file = open('answers.txt')   
    while True:        
        line = file.readline().split()
        if line[0] == i:
            right_answer.append(line[1])
            a_list.append(line[2:])
            break

# number of correct answers
res_points = 0
# questions with their answers are shown on the screen one by one
for i in range(10):
    print('\n' + str(i + 1) + '. ' + q_list[i])
    for j in range(len(a_list[i])):
        print(a_list[i][j][1:-1])
    answer = input('your choice:  ')
    while answer not in ('1', '2', '3', '4'):
        print('your input is not correct, please input \'1\', \'2\', \'3\' or \'4\'')
        answer = input('your choice:  ')
    # if the answer is correct, points are added
    if answer == right_answer[i]:
        res_points += 1
# at the end we see the total points
print('\nCongratulations, you have scored ' + str(res_points) + ' points!!!\n')