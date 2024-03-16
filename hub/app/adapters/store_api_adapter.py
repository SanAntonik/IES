import json
import logging
from typing import List

import pydantic_core
import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]) -> bool:
        """
        Save the processed road data to the Store API.
        Parameters:
            processed_agent_data_batch (List[ProcessedAgentData]): Processed road data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        logging.info("Inside save_data from StoreApiAdapter class")
        url = f"{self.api_base_url}/processed_agent_data"
        headers = {"Content-Type": "application/json"}
        data = [json.loads(value) for value in processed_agent_data_batch]

        logging.info(f"URL: {url}")
        logging.info(f"Headers: {headers}")
        logging.info(f"Data: {data}")

        try:
            logging.info("Inside TRY")
            response = requests.post(url, headers=headers, json=data)
            logging.info("Created response var")
            logging.info(f"Response var: {response}")
            response.raise_for_status()
            logging.info("Request successful")
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to save data: {e}")
            logging.info("Failed to save data:", e)
            return False
