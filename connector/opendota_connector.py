import json
import requests
import yaml


class OpendotaConnector:
    def __init__(self) -> None:
        with open("config.yaml") as file:
            self.account_id = yaml.safe_load(file)["opendota_api_key"]

    def get_matches(self, account_id: int):
        url = f"""https://api.opendota.com/api/players/{str(account_id)}/matches"""
        matches_json = json.loads(requests.get(url).content)
        return matches_json

    def get_match_details(self, match_id: int):
        url = f"""https://api.opendota.com/api/matches/{match_id}"""
        matche_details_json = json.loads(requests.get(url).content)
        return matche_details_json
