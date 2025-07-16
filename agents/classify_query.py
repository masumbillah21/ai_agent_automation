from utils.logger import logger

class QueryClassifierAgent:
    def __init__(self):
        logger.info("QueryClassifierAgent initialized")

    def classify(self, user_input: str) -> str:
        if "refund" in user_input.lower():
            return "billing"
        elif "error" in user_input.lower():
            return "technical"
        else:
            return "general"
