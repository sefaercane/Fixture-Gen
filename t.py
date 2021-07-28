import func

numOfTeams = int(input("Number Of Teams: "))
teams = []

for i in range(numOfTeams):
    teams.append(input(f"{i+1}. Team Name: "))
    
if numOfTeams%2!=0:
    teams.append("BAY")

print("\n")

for i in range(len(teams)-1):
    print("------ week {} ------".format(i+1))
    teams = func.teamChanger(teams)
    func.teamLister(teams)