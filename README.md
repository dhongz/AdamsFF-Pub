# Fantasy-Football-Career-Rankings

Q/A Agent Fantasy Football League: https://adamsff.streamlit.app/

Background: 
- LLM is given different datasets with descriptions of each
- LLM generated python code to execute ETL to answer questions





Archive (used to do rankings but shifted to LLM Agent):
Fantasy Football Ranking for the Adams Fantasy Football League


Quick and dirty version of career rankings and performance.

Metrics measures
- Win percentage
- Number of Playoffs wins
- Number of Championships
- Playoff appearance rate
- Average Points For Rank

Each metric is standardized (how many standard deviations above or below the mean).
Playoff wins are given a 1.35x multipler to give more significance while playoff 
appearances are reduced to only 0.25x its value, reducing its impact.
All the Z-Scores are added together to give a true value.

Other metrics measures are miscellaneous.

Work in Progress:
- Rosters
- Most Valuable Player/Least Valuable Player
- Drafting rating
- More
