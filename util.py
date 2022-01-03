import pandas
from config import config


def load_data(columns=[]):
    """
    Loads a csv file according to the 'data' parameter in the config file
    and returns  the columns specified, plus 'strength', 'dexterity', 'constitution',
    'intelligence', 'wisdom', 'charisma', and 'challenge_rating'.

    The returned data is a pandas data frame.
    """
    columns.extend(config.get("stats"))
    return pandas.read_csv(config.get("data"), usecols=columns)


def extract_metadata(data):
    """
    Separate out the columns that aren't raw stats and return them
    """
    return data["challenge_rating"], data["hit_points"], data["armor_class"]


def setup():
    monster_data = load_data(config.get("data"))
    cr, hp, md = extract_metadata(monster_data)
    return monster_data, cr, hp, md
