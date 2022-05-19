import json
from data_extractor.extractor import Excractor


class Match(Excractor):
    def __init__(self) -> None:
        super().__init__()

    def get_match_details(self, match_id: int) -> list:
        return str(self.connector.get_match_details(match_id))

    def dump_match_details_json(self) -> None:
        with open(f"""data/{self.account_id}/matches.json""") as file:
            matches = json.load(file)

        for match in matches:
            match_id = match["match_id"]

            with open(f"data/{self.account_id}/matches/{match_id}", "w") as outfile:
                matche_details_json = self.get_match_details(match_id)
                outfile.write(matche_details_json)
