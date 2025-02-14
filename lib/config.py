from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    ESPN_S2 = os.getenv('ESPN_S2')
    LEAGUE_ID = os.getenv('LEAGUE_ID')
    SWID = os.getenv('SWID')
    LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
    LANGCHAIN_URL = os.getenv('LANGCHAIN_URL')

config = Config()