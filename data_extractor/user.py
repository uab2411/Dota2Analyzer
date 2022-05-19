import json
from data_extractor.extractor import Excractor


class User(Excractor):
    
    def __init__(self) -> None:
        super().__init__()

    def get_matches(self) -> str:
        return json.dumps(self.connector.get_matches(self.account_id))

    def dump_matches_json(self) -> None:
        with open(f"data/{self.account_id}/matches.json", "w") as outfile:
            matches_json = self.get_matches()
            outfile.write(matches_json)
