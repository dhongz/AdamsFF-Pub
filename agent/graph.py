from langgraph.graph import END, START, StateGraph

from .state import DataAnalysisState, ConfigSchema
from .tools import explore_data_set, should_explore, execute_exploration, plan_query, execute_query, regular_season_exploration, playoff_exploration, player_stats_exploration, matchups_exploration

data_analysis_graph = StateGraph(DataAnalysisState, config_schema=ConfigSchema)

data_analysis_graph.add_node("explore_data_set", explore_data_set)
data_analysis_graph.add_node("should_explore", should_explore)

data_analysis_graph.add_node("regular_season_exploration", regular_season_exploration)
data_analysis_graph.add_node("playoff_exploration", playoff_exploration)
data_analysis_graph.add_node("player_stats_exploration", player_stats_exploration)
data_analysis_graph.add_node("matchups_exploration", matchups_exploration)

data_analysis_graph.add_node("execute_exploration", execute_exploration)

data_analysis_graph.add_node("plan_query", plan_query)
data_analysis_graph.add_node("execute_query", execute_query)





data_analysis_graph.add_edge(START, "explore_data_set")
data_analysis_graph.add_edge("explore_data_set", "should_explore")

data_analysis_graph.add_edge("plan_query", "execute_query")
data_analysis_graph.add_edge("execute_query", END)

