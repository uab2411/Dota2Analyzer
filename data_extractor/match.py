import json
import os
import time
from data_extractor.extractor import Excractor


class Match(Excractor):
    def __init__(self) -> None:
        super().__init__()

    def get_match_details(self, match_id: int):
        return str(self.connector.get_match_details(match_id))

    def dump_match_details_json(self) -> None:
        with open(f"""data/{self.account_id}/matches.json""") as file:
            matches = json.load(file)

        for match in matches:
            match_id = match["match_id"]
            if not os.path.isfile(f"data/{self.account_id}/matches/{match_id}.json"):
                print(f"Writing {match_id}")
                match_details_json = self.get_match_details(match_id)
                if "match_id" in match_details_json:
                    with open(
                        f"data/{self.account_id}/matches/{match_id}.json", "w"
                    ) as outfile:
                        outfile.write(match_details_json)
                else:
                    print(f"Error {match_id}: {match_details_json}")
                    print(f"Sleeping 10 seconds and retrying.")
                    time.sleep(10)
                    match_details_json = self.get_match_details(match_id)
                    if "match_id" in match_details_json:
                        with open(
                            f"data/{self.account_id}/matches/{match_id}.json", "w"
                        ) as outfile:
                            outfile.write(match_details_json)
