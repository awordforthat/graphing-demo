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
