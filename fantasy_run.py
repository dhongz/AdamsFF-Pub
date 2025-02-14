import pandas as pd
import numpy as np
from scipy import stats
from espn_api.football import League

from lib.config import config
from dotenv import load_dotenv
# #Private Info

leagueid = config.LEAGUE_ID
cookie = config.ESPN_S2
swid = config.SWID

# # Function and class definitions
# #Class for each owner

# # Ignore for now. Implement later
# # class TeamRoster:
# #     df = 3

# # teamroster parameter removed for now








# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# Using Next.js with App Router. Working in TypeScript. FastAPI Backend. ShadCN and TailwindCSS

# ##      Main Code       ##
# select_years = [2015]
# leagues = []
# for year in select_years:
#     #Initialize each year
#     league_year = year
#     league = League(league_id=leagueid, year=league_year, espn_s2=cookie, swid=swid)
#     # print(league.scoreboard(18))
#     if year < 2021:
#         for week in range(1,17):
#             for match in league.scoreboard(week):
#                 print(match.matchup_type)
#                 print(match.home_team)
#                 print(match.home_team.owners)
#                 print(match.home_team.team_name)
#                 # print(match.home_team.stats)
#                 if hasattr(match, 'away_team'):
#                     print(match.away_team)
#                 print(match.home_score)
#                 print(match.away_score)
#     if year >= 2021:
#         for week in range(1,18):
#             print(week)
#             for match in league.scoreboard(week):
#                 print(match.matchup_type)
#                 print(match.home_team)
#                 print(match.home_team.owners)
#                 print(match.home_team.team_name)
#                 # print(match.home_team.stats)
#                 if hasattr(match, 'away_team'):
#                     print(match.away_team)
#                 print(match.home_score)
#                 print(match.away_score)
    # print(league.teams)
    # for team in league.teams:
    #     # print(team.owners)
    #     print(team.team_name)

    #     # print(team.points_for)
    #     # print(team.points_against)
    #     # print(team.schedule)
    #     # print(team.scores)
    #     # total_points = 0
    #     # for i in range(14):
    #     #     total_points += team.scores[i]
    #     # print("-----Added Up Scores-----")
    #     # print(total_points)
    #     # print("Difference")
    #     # print(team.points_for - total_points)

    #     # print(team.outcomes)
    #     # print(team.mov)
        
    # # print(league.members)

    # leagues.append(league)


# print(leagues)
# #adding pf and how many years played
#     fantasy_season = pd.DataFrame()
#     for league_team in league.teams:
#         for team in team_list:
#             if team.name == league_team.owner:
#                 team.years += 1
#                 team_pf = pd.DataFrame([[league_team.owner, league_team.points_for]], columns=['team', 'pf'])
#                 fantasy_season = pd.concat([fantasy_season, team_pf], sort=True)
        
#     fantasy_season['rank'] = fantasy_season['pf'].rank(method='max', ascending= False)

#     for team in team_list:
#         for index, row in fantasy_season.iterrows():
#             if team.name == row[1]:
#                 if team.pf_ranks == []:
#                     team.pf_ranks = [row[2]]
#                     # Conor and Brett share team
#                     if year == 2015 and row[1] == "Brett Nixon":
#                         connor_hess.pf_ranks = [row[2]]
#                 else:
#                     team.pf_ranks.append(row[2])

# #2014-2018 have to use scoreboard class
#     if year < 2019:
#         for week in range(1,17):
#             boxscore = league.scoreboard(week)
#             for match in boxscore:
#                 if not match.is_playoff:
#                     if match.home_score > match.away_score:
#                         reghomeWin(match, team_list)
#                         #Connor and Brett share team
#                         if (year == 2015):
#                             if match.home_team.owner == "Brett Nixon":
#                                 connorShare(match, team_list, True, True)
#                             if match.away_team.owner == "Brett Nixon":
#                                 connorShare(match, team_list, False, False)
#                     elif match.home_score < match.away_score:
#                         regawayWin(match, team_list)
#                         #Connor and Brett share team
#                         if (year == 2015):
#                             if match.home_team.owner == "Brett Nixon":
#                                 connorShare(match, team_list, False, True)
#                             if match.away_team.owner == "Brett Nixon":
#                                 connorShare(match, team_list, True, False)
#                     else:
#                         regTie(match, team_list)
#                 elif match.is_playoff & (match.matchup_type == 'WINNERS_BRACKET'):
#                     for team in team_list:
#                         if week == 14:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.home_score > match.away_score:
#                                         team.playoff_wins += 1
#                             if match.away_team != 0:
#                                 if match.away_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.away_score > match.home_score:
#                                         team.playoff_wins += 1
#                         elif week == 16:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                         else:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1
# #2019-2020 have to use box scores
#     elif year < 2021:
#         for week in range(1,17):
#             boxscore = league.box_scores(week)
#             for match in boxscore:
#                 if not match.is_playoff:
#                     if match.home_score > match.away_score:
#                         reghomeWin(match, team_list)
#                     elif match.home_score < match.away_score:
#                         regawayWin(match, team_list)
#                     else:
#                         regTie(match, team_list)
#                 elif match.is_playoff & (match.matchup_type == 'WINNERS_BRACKET'):
#                     for team in team_list:
#                         if week == 14:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.home_score > match.away_score:
#                                         team.playoff_wins += 1
#                             if match.away_team != 0:
#                                 if match.away_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.away_score > match.home_score:
#                                         team.playoff_wins += 1
#                         elif week == 16:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                         else:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1
# #2021 and on games were increased to 14 regular season games
#     else:
#         for week in range(1,18):
#             boxscore = league.box_scores(week)
#             for match in boxscore:
#                 if not match.is_playoff:
#                     if match.home_score > match.away_score:
#                         reghomeWin(match, team_list)
#                     elif match.home_score < match.away_score:
#                         regawayWin(match, team_list)
#                     else:
#                         regTie(match, team_list)
#                 elif match.is_playoff & (match.matchup_type == 'WINNERS_BRACKET'):
#                     for team in team_list:
#                         if week == 15:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.home_score > match.away_score:
#                                         team.playoff_wins += 1
#                             if match.away_team != 0:
#                                 if match.away_team.owner == team.name:
#                                     team.playoff_app += 1
#                                     if match.away_score > match.home_score:
#                                         team.playoff_wins += 1
#                         elif week == 17:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1
#                                     team.championships += 1
#                         else:
#                             if match.home_team != 0:
#                                 if match.home_team.owner == team.name and match.home_score > match.away_score:
#                                     team.playoff_wins += 1
#                             if match.home_team != 0:
#                                 if match.away_team.owner == team.name and match.away_score > match.home_score:
#                                     team.playoff_wins += 1



# ########################################################################################################################


# ## z-scores
# current_team_list = np.array([joey_dicresce, joel_fazecas, cameron_limke, ben_urbano, dillon_hong, chris_jenkins, jack_dunn, nick_durand, brett_nixon, connor_hess, marco_dicresce, nabil_chamra])

# for team in current_team_list:
#     team.pf_avg_ranks = np.mean(team.pf_ranks)
#     team.winperc = team.wins / (team.wins + team.losses)
#     team.pa_per_g = team.pa_per_g / team.games

# arr = []
# for team in current_team_list:
#     arr.append(team.winperc)
# wp_z_arr = stats.zscore(arr)
# for index in range(0,current_team_list.size):
#     current_team_list[index].win_per_z = wp_z_arr[index]
# arr = []
# for team in current_team_list:
#     arr.append(team.playoff_wins)
# pw_z_arr = stats.zscore(arr)
# for index in range(0,current_team_list.size):
#     current_team_list[index].playoff_win_z = pw_z_arr[index]
# arr = []
# for team in current_team_list:
#     arr.append(team.playoff_app/team.years)
# pa_z_arr = stats.zscore(arr)
# for index in range(0,current_team_list.size):
#     current_team_list[index].playoff_app_z = pa_z_arr[index]
# arr = []
# for team in current_team_list:
#     arr.append(team.pf_avg_ranks)
# pf_z_arr = stats.zscore(arr)
# for index in range(0,current_team_list.size):
#     current_team_list[index].avg_pfrank_z = -1 * pf_z_arr[index]

# #Organize Final Data
# final_data = pd.DataFrame()

# for team in current_team_list:
#     team.truevalue = team.win_per_z + (team.playoff_win_z * 1.35) + team.championships + (team.playoff_app_z * 0.25)+  team.avg_pfrank_z
#     team_data = pd.DataFrame([[team.name, team.truevalue, team.wins, team.losses, team.winperc, team.pf_avg_ranks, team.pf_ranks, team.playoff_app, team.playoff_wins, team.championships, team.highestpf, team.lowestpf, team.pa_per_g]], columns=['team', 'truevalue', 'wins', 'losses', 'win per', 'average pf rank', 'pf ranks','playoff app', 'playoff wins', 'championships', 'highest pf', 'lowest pf', 'pa per g'])
#     final_data = pd.concat([final_data, team_data], sort=True)

# final_data['TRUE Rank'] = final_data['truevalue'].rank(method='max', ascending= False)

# final_data.to_csv('finaldata.csv')

# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# ##       Printing to Console     ##
# # print("----------------------------------")
# # print("---------------")
# # for team in current_team_list:
# #     print("*******************")
# #     print("name: ",team.name)
# #     print("win percentage: ",team.winperc)
# #     print("losses: ", team.losses)
# #     print("average pf rank: ",team.pf_avg_ranks)
# #     print("playoff appearances: ",team.playoff_app)
# #     print("playoff wins: ",team.playoff_wins)
# #     print("championships: ",team.championships)
# #     print("-----------------------")
# #     print("win per z: ",team.win_per_z)
# #     print("playoff win z: ",team.playoff_win_z)
# #     print("playoff app z: ",team.playoff_app_z)
# #     print("average pf rank z: ",team.avg_pfrank_z)
# #     print("truevalue: ",team.truevalue)
# #     print("highest pf: ", team.highestpf)
# #     print("lowest pf: ", team.lowestpf)
# #     print("pa per g: ", team.pa_per_g)

def create_fantasy_dataset(start_year=2014, end_year=2024):
    # Create owner ID to name mapping
    owner_id_mapping = {
        '{ED2967D6-F92F-447A-A967-D6F92F147A25}': 'Chris',
        '{29D183EA-E761-43C0-93A4-6C47CA2926D7}': 'Chris',
        '{02AB2B26-BDB6-4013-AB2B-26BDB63013D0}': 'Ben',
        '{0A038966-B1EC-4363-93A4-1A746D1C05AA}': 'Joey',
        '{120EBF0B-960F-4C32-8EBF-0B960FEC32D1}': 'Nick',
        '{1328661D-EEAA-4F68-A866-1DEEAA6F68CC}': 'Carson',
        '{8E76C98C-033D-48E5-8735-71752E421497}': 'Carson',
        '{207DC893-5A3A-4A1B-BDC8-935A3AAA1B0B}': 'Marco',
        '{ED7135CE-1C99-405A-B135-CE1C99E05A9F}': 'Will',
        '{4E3A897B-4C6E-4A17-BA89-7B4C6E1A1789}': 'Will',
        '{2615CE14-DE41-462C-A141-C106A137008F}': 'Will',
        '{3702423F-DDE1-4F68-B13D-4597B2FBDC9B}': 'Nabil',
        '{45F320B7-A9EA-42AD-BEEA-AE97F33A55FE}': 'Connor',
        '{5B91BA7E-444A-403C-91BA-7E444AA03C4A}': 'Cameron',
        '{D96E6F84-EC60-4EA4-8672-B92B97A2C2FD}': 'Cameron',
        '{6248D1D4-C58C-4253-9C9B-D30AB9524116}': 'Brett',
        '{CB8801B1-2DC9-47DB-9752-626600865D83}': 'Brett',
        '{700F91F4-F9CD-4A3A-8F91-F4F9CDCA3AC2}': 'Joel',
        '{A928F5E8-8048-42E3-A4CE-63B009FB6A47}': 'Jack',
        '{77FBFE61-CB95-4C17-BBFE-61CB953C17C0}': 'Dillon',
        '{EAAD1FEA-A6D1-4BBE-A09A-EC86EF223450}': 'JMooney'
    }
    
    all_matches = []
    
    for year in range(start_year, end_year + 1):
        # Initialize league for current year
        league = League(league_id=leagueid, year=year, espn_s2=cookie, swid=swid)
        
        # Determine number of weeks based on year (17 weeks before 2021, 18 after)
        max_weeks = 17 if year < 2021 else 18
        championship_week = 16 if year < 2021 else 17
        
        for week in range(1, max_weeks):
            for match in league.scoreboard(week):
                # Determine if it's playoffs or championship
                is_playoffs = match.matchup_type == 'WINNERS_BRACKET'
                is_championship = (is_playoffs and week == championship_week)
                
                # Extract owner IDs
                def get_owner_ids(team):
                    if hasattr(team, 'owners') and team.owners:
                        return ', '.join(sorted(owner.get('id', '') for owner in team.owners))
                    return None
                
                home_owners = get_owner_ids(match.home_team) if hasattr(match, 'home_team') else None
                away_owners = get_owner_ids(match.away_team) if hasattr(match, 'away_team') else None
                
                # Convert owner IDs to names
                def get_owner_names(owner_ids):
                    if owner_ids:
                        # Split multiple owner IDs and look up each one
                        ids = [id.strip() for id in owner_ids.split(',')]
                        names = [owner_id_mapping.get(id, id) for id in ids]
                        # Remove duplicates and join with commas
                        return ', '.join(sorted(set(names)))
                    return None
                
                match_data = {
                    'year': year,
                    'week': week,
                    'matchup_type': 'CHAMPIONSHIP' if is_championship else 'PLAYOFF' if is_playoffs else 'REGULAR',
                    'is_playoff': is_playoffs,
                    'is_championship': is_championship,
                    'home_team': match.home_team.team_name if hasattr(match, 'home_team') else None,
                    # 'home_team_owner_ids': home_owners,
                    'home_team_owners': get_owner_names(home_owners),
                    'home_score': match.home_score,
                    'away_team': match.away_team.team_name if hasattr(match, 'away_team') else None,
                    # 'away_team_owner_ids': away_owners,
                    'away_team_owners': get_owner_names(away_owners),
                    'away_score': match.away_score,
                    'winner': 'bye' if not hasattr(match, 'away_team') else ('home' if match.home_score > match.away_score else 'away' if match.away_score > match.home_score else 'tie'),
                    'score_difference': match.home_score - match.away_score
                }
                all_matches.append(match_data)
                
        print(f"Completed processing year {year}")

    # Create DataFrame from all matches
    matches_df = pd.DataFrame(all_matches)
    
    # Add some derived columns
    matches_df['total_points'] = matches_df['home_score'] + matches_df['away_score']
    
    # Save to CSV
    matches_df.to_csv('fantasy_football_history.csv', index=False)
    
    return matches_df

if __name__ == "__main__":
    # Create dataset from 2015 to 2023
    df = create_fantasy_dataset()
    
    # Print some basic statistics
    print("\nDataset Summary:")
    print(f"Total matches: {len(df)}")
    print(f"Years covered: {df['year'].min()} to {df['year'].max()}")
    print("\nSample of the data:")
    print(df.head())