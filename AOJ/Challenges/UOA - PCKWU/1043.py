# https://onlinejudge.u-aizu.ac.jp/challenges/sources/UOA/PCKWU/1041
while(True):
    team_count = int(input())
    if team_count == 0:
        break

    teams = [list(map(int, input().split())) for i in range(team_count)]

    sorted_teams = sorted(teams, key=lambda x: (-x[2], x[3], x[0]))
    selected_members = []
    for i in range(len(sorted_teams)):
        team_members = sum(s[1] == sorted_teams[i][1] for s in selected_members)
        if len(selected_members) < 10 and team_members < 3:
            selected_members.append(sorted_teams[i])
        elif len(selected_members) < 20 and team_members < 2:
            selected_members.append(sorted_teams[i])
        elif len(selected_members) < 26 and team_members < 1:
            selected_members.append(sorted_teams[i])
        else:
            continue

        print(sorted_teams[i][0])

