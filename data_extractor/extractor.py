from abc import ABC
import os
import yaml

from connector.opendota_connector import OpendotaConnector


class Excractor(ABC):
    def __init__(self) -> None:
        with open("config.yaml") as file:
            self.account_id = yaml.safe_load(file)["account_id"]
        self.connector = OpendotaConnector()
        if not os.path.exists(f"data/{self.account_id}/matches"):
            os.makedirs(f"data/{self.account_id}/matches")
