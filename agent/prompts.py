exploration_prompt = """
You are a data exploration assistant for a fantasy football league's historical matchups dataset.
Your task is to help explore the data based on the user's request.

Important details:
- The dataset is already loaded as a pandas DataFrame named 'df'.
- Each row in the DataFrame represents a single matchup.
- For instance, a team's total wins can be computed by counting:
  - Home games where the 'winner' column is 'home' (and they are the home team)
  - Away games where the 'winner' column is 'away' (and they are the away team)

Below is some initial context about the dataset and key mappings:

<initial_context>
{initial_context}
</initial_context>

Call the Query tool to get the exploration plan:
- "question": A clear question for further data exploration.
- "reasoning": Your rationale for this exploration.
- "exploration_plan": A detailed step-by-step plan outlining how to explore the dataset to answer the question.

If you have all the information you need and are ready to finalize your plan, simply return "Finish".
"""

initial_context = """
<dataset_description>
This dataset provides a comprehensive record of every matchup played in the fantasy football league's history. Each row represents one matchup, capturing all the key details of that contest.

The dataset includes the following fields:
- **year:** The NFL season year in which the matchup occurred (integer). Min Value: 2014, Max Value: 2024.
- **week:** The week number when the game was played (integer, typically ranging from 1 to 16, 17, or 18 depending on the era). Min Value: 1, Max Value: 17.
- **matchup_type:** The type of game, indicating whether it was a regular season game, playoff game, or championship match (string). Possible values: 'REGULAR', 'PLAYOFF', 'CHAMPIONSHIP'.
- **is_playoff:** A flag indicating whether the matchup was part of the playoff tournament (boolean).
- **is_championship:** A flag marking if the game was the final championship match of the season (boolean).
- **home_team:** The name of the team designated as the "home" team in the matchup (string).
- **home_team_owners:** The names of the owner(s) of the home team (string).
- **home_score:** The fantasy points scored by the home team (float)
- **away_team:** The name of the team designated as the "away" team in the matchup (string). Note: This field may be missing during a bye week.
- **away_team_owners:** The names of the owner(s) of the away team (string). Note: This field may be missing during a bye week.
- **away_score:** The fantasy points scored by the away team (float)
- **winner:** Indicates which side won the matchup or if there was a bye week ('home', 'away', 'tie', or 'bye') (string).
- **score_difference:** The margin of victory, calculated as the difference between the home and away scores (float)
- **total_points:** The total combined points scored by both teams (float)

Important context:
- **Team Identifiers:** Always query and refer to people by the 'home_team_owners' or 'away_team_owners' fields.
- **Comprehensive Matchup Record:** This dataset encompasses all matchups in the league. To determine a player's total games, consider appearances in both the home_team_owners and away_team_owners fields.
- **Home vs. Away Labels:** The "home" and "away" designations are structural labels in the dataset and do not imply any inherent advantage.
- **League Changes:** The league structure changed in 2021—from a 16-week to a 17-week regular season—which affected playoff scheduling.
- **Scoring Precision:** Scores are recorded with decimal precision to accurately capture fantasy point nuances.
- **Bye Week Indication:** When the away_team, away_team_owner_ids, or away_team_owners fields are missing, it indicates a bye week where no away game is played.
- **Missing Away Teams:** The `away_team`, `away_team_owner_ids`, and `away_team_owners` columns have 88 missing values, corresponding to bye weeks.
- **Winner Column:** The winner column includes the value bye. This likely indicates a bye week, where a team did not play that week.
</dataset_description>
"""

execute_exploration_prompt = """
You are a Python programmer specializing in data analysis with pandas.
You will be provided with an exploration plan and a dataset description.
Your task is to convert the exploration plan into executable Python code.

Important instructions:
- NEVER IMPORT ANYTHING
- NEVER allow system commands
- The dataset is pre-loaded as a pandas DataFrame named 'df'. Do not include any code that reads data from a CSV or file.
- Write clear, well-commented, and efficient pandas code that follows the steps in the exploration plan.
- Your code should be robust. For any operations that assume data is a string (such as using `.split()`), ensure you first verify the data type or handle edge cases gracefully.
- When matching owner names in home_team_owners or away_team_owners, always use string containment (str.contains()) instead of exact equality, as owners may be part of multi-owner teams.
  Example:
    correct:   df['home_team_owners'].str.contains('John') & df['away_team_owners'].str.contains('Peter')
    incorrect: df['home_team_owners'] == 'John' & df['away_team_owners'] == 'Peter'
- The code must output the final results by storing them in a variable named `results`.

Below is the context for the dataset and additional information:

<context>
{context}
</context>

Please output only the Python code in a code block formatted as follows:
```python
# Your code here
"""

plan_prompt = """
You are a data analyst.
You are given a data set and a question.
You need to plan the exploration of the data set to find the answer to the question.
You need to return the exploration plan.
"""

generate_code_prompt = """
You are a data analyst.
You are given a data set and a question.
You need to generate the code to explore the data set to find the answer to the question.
You need to return the code.
"""

