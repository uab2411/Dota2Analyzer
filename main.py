import json
import requests

from data_extractor.user import User
from data_extractor.match import Match


def get_matches_for_user(account_id: int):
    url = f"""https://api.opendota.com/api/players/{str(account_id)}/matches"""
    matches_json = json.loads(requests.get(url).content)
    return matches_json


usr = User()
print(usr.dump_matches_json())

match = Match()
print(match.dump_match_details_json())
