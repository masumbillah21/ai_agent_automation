from utils.logger import logger

class DataRetrieverAgent:
    def __init__(self):
        logger.info("DataRetrieverAgent initialized")

    def retrieve(self, category: str) -> str:
        data_map = {
            "billing": "Billing info: Order #123 has been refunded.",
            "technical": "Technical support: Please restart your device.",
            "general": "General info: We are open from 9 AM to 5 PM Monday through Friday."
        }
        return data_map.get(category, "No relevant data found.")
