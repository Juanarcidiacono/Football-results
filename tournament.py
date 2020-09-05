'''ally the results of a small football competition.

Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1

What do those abbreviations mean?

    MP: Matches Played
    W: Matches Won
    D: Matches Drawn (Tied)
    L: Matches Lost
    P: Points

A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome should be ordered by points, descending. In case of a tie, teams are ordered alphabetically.

Input

Your tallying program will receive input that looks like:



Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win

The result of the match refers to the first team listed. So this line

Allegoric Alaskans;Blithering Badgers;win

Means that the Allegoric Alaskans beat the Blithering Badgers.

This line:

Courageous Californians;Blithering Badgers;loss

Means that the Blithering Badgers beat the Courageous Californians.

And this line:

Devastating Donkeys;Courageous Californians;draw

Means that the Devastating Donkeys and Courageous Californians tied.'''

import numpy as np
class Score:
    def __init__(self, team_list, matrix):
        self.team_list = team_list
        self.matrix = matrix

    def split_team(self):
        conditions = ('win', 'loss', 'draw')
        while True:
            match = input()
            team1 = match.split(';')[0]
            team2 = match.split(';')[1]
            con = match.split(';')[2]
            condition = True
            while condition:
                if not (con in conditions):
                    con = input('Enter again the condition ')
                else:
                    condition = False
            ind_team1 = self.team_list.index(team1)
            ind_team2 = self.team_list.index(team2)
            matrix[ind_team1][0] += 1
            matrix[ind_team2][0] += 1
            if con == conditions[0]:
                matrix[ind_team1][1] += 1
                matrix[ind_team2][3] += 1
                matrix[ind_team1][4] += 3
            elif con == conditions[1]:
                matrix[ind_team1][3] += 1
                matrix[ind_team2][1] += 1
                matrix[ind_team2][4] += 3
            elif con == conditions[2]:
                matrix[ind_team1][2] += 1
                matrix[ind_team2][2] += 1
                matrix[ind_team1][4] += 1
                matrix[ind_team2][4] += 1
            print(matrix)
            ans = input('Continue? ')
            if ans == 'N':
                break

    def board(self):
        print('\t\t\t'+ '|MP | ' + 'W |' + ' D  |' + ' L  |' + ' P  |' )
        for i in range(len(self.team_list)):
            print(self.team_list[i],end = "")
            print('\t| ' + str(int(self.matrix[i][0])) + ' |', end = "")
            for j in range(4):
                print(str(int(self.matrix[i][j+1])) + '  | ', end = "")
            print()


team_list = []

while True:
    team_name = input('Enter the team')
    team_list.append(team_name)
    ans = input('>> Continue? ')
    if ans == 'N':
        break
        print(team_list)
team_list = list(set(team_list))
matrix = np.zeros((len(team_list), 5))

puntaje = Score(team_list,matrix)
puntaje.split_team()
puntaje.board()