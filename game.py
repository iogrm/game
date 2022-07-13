import string
import random


scoreboard = {}
contests = []
scores = []

def get_score_by_index(matrix, index,letter):
    # print('get_score_by_index')
    temp = []
    result = []
    for record in matrix:
        temp.append(record[index])
    for t in temp:
        if t == 'none' or t[0]!=letter:
            # print(t, t[0], letter)
            result.append(0)
        else:
            try:
                index = temp.index(t, temp.index(t)+1, len(temp))
                result.append(5)
            except ValueError:
                result.append(10)
    return result
    
def get_matrix_scores(matrix, letter):
    # print('get_matrix_scores')
    result = []
    for i in range(1,5):
        m = get_score_by_index(matrix,i,letter)
        result.append(m)
        # print(m)
    return result


def set_scores(matrix,letter):
    # print('set_scores')
    for record in matrix:
        index = matrix.index(record)
        score = 0
        result = get_matrix_scores(matrix,letter)
        # print(result)
        for r in result:
            score += r[index]
        record.append(score)

def print_result(matrix):
    for record in matrix:
        print(record[0]," : ",record[5])

def get_random_letter():
    letter = random.choice(string.ascii_letters)
    return letter

def get_input():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input().split())
    return matrix

def save_scores(matrix, contest_index):
    for record in matrix:
        player = record[0]
        score = record[5]
        scores.append([player, contest_index, score])
        player_score = scoreboard.get(player, 0)
        scoreboard[player] = player_score + score
        # print(scoreboard[player])

def new_contest():
    letter = get_random_letter()
    print(letter)
    matrix = get_input()
    set_scores(matrix,letter)
    print_result(matrix)
    contests.append([letter,matrix])
    save_scores(matrix, len(contests))

def show_results():
    key_list = list(scoreboard.keys())
    for key in key_list:
        print(key, " : ", scoreboard[key])


command = input().split()
while command[0] != 'end':
    if command[0] == 'new':
        new_contest()
    elif command[0] == 'show':
        show_results()
    command = input().split()

