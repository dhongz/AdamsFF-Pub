
class FantasyTeam:
    
    def __init__(self, id):
        self.id = id

        self.games = 0
        self.years = 0

        self.total_wins = 0
        self.total_losses = 0
        self.total_ties = 0
        self.total_points_for = 0
        self.total_points_against = 0

        self.pf_std = []
        self.pa_std = []
        self.mov_std = []

        self.highestpf = 0
        self.lowestpf = 10000
        self.h2h_record = []

        self.playoff_appearances = 0
        self.playoff_games = 0
        self.playoff_wins = 0
        self.playoff_losses = 0
        self.playoff_pf = 0
        self.playoff_pa = 0

        self.championship_wins = 0
        self.championship_losses = 0

        self.win_per_z = 0
        self.playoff_win_z = 0
        self.playoff_app_z = 0
        self.avg_pfrank_z = 0
        self.truevalue = 0

    def process_season(self, league, average_pf, average_pa):
        for team in league.teams:
            if team.team_id == self.id:
                self.years += 1
                self.total_wins += team.wins
                self.total_losses += team.losses
                self.total_ties += team.ties
                self.total_points_for += team.points_for
                self.total_points_against += team.points_against

                

    