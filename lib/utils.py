#Function to find the owners FantasyTeam object within an array
def findTeam(array, findteam):
    for team in array:
        if team.name == findteam:
            return team
        
#Function used to give Connor stats from the time he shared a team with Brett
def connorShare(match, team_list, winloss, homeaway):
    connor = findTeam(team_list, "Connor Hess")
    if winloss:
        connor.wins += 1
    else:
        connor.losses += 1
    connor.games += 1
    if homeaway:
        connor.pa_per_g += match.away_score
    else:
        connor.pa_per_g += match.home_score

#If the home team wins in the regular season
def reghomeWin(match, team_list):
    home = findTeam(team_list, match.home_team.owner)
    away = findTeam(team_list, match.away_team.owner)
    home.wins += 1
    away.losses += 1
    home.games += 1
    away.games += 1
    home.pa_per_g += match.away_score
    away.pa_per_g += match.home_score
    if match.home_score > home.highestpf:
        home.highestpf = match.home_score
    if match.away_score > away.highestpf:
        away.highestpf = match.away_score
    if match.home_score < home.lowestpf:
        home.lowestpf = match.home_score
    if match.away_score < away.lowestpf:
        away.lowestpf = match.away_score

#If a team loses in the regular season
def regawayWin(match, team_list):
    home = findTeam(team_list, match.home_team.owner)
    away = findTeam(team_list, match.away_team.owner)
    away.wins += 1
    home.losses += 1
    home.games += 1
    away.games += 1
    home.pa_per_g += match.away_score
    away.pa_per_g += match.home_score
    if match.home_score > home.highestpf:
        home.highestpf = match.home_score
    if match.away_score > away.highestpf:
        away.highestpf = match.away_score
    if match.home_score < home.lowestpf:
        home.lowestpf = match.home_score
    if match.away_score < away.lowestpf:
        away.lowestpf = match.away_score

#If a team ties in the regular season
def regTie(match, team_list):
    home = findTeam(team_list, match.home_team.owner)
    away = findTeam(team_list, match.away_team.owner)
    home.wins += 0.5
    away.losses += 0.5
    away.wins += 0.5
    home.losses += 0.5
    home.games += 1
    away.games += 1
    home.pa_per_g += match.away_score
    away.pa_per_g += match.home_score
    if match.home_score > home.highestpf:
        home.highestpf = match.home_score
    if match.away_score > away.highestpf:
        away.highestpf = match.away_score
    if match.home_score < home.lowestpf:
        home.lowestpf = match.home_score
    if match.away_score < away.lowestpf:
        away.lowestpf = match.away_score