def teamChanger(teams):
    # https://en.wikipedia.org/wiki/Round-robin_tournament#Circle_method
    
    teams0 = teams[1:-1]
    sbt1 = teams[0]
    sbt2 = teams[-1]
    nTeam = [sbt1]
    nTeam.append(sbt2)
    
    for i in range(len(teams0)):
        nTeam.append(teams0[i])

    return nTeam


def teamLister(teams):
    for i in range(int(len(teams)/2)):
        print(f"{teams[i]} = {teams[-i-1]}")
    print("\n")