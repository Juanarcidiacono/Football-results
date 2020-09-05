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