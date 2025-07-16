from utils.logger import logger

class DataRetrieverAgent:
    def __init__(self):
        logger.info("DataRetrieverAgent initialized")

    def retrieve(self, category: str) -> str:
        if category == "billing":
            return "Billing info: refunds, payments, invoices."
        elif category == "technical":
            return "Technical support help: troubleshooting, errors."
        elif category == "general":
            return "General info: our company is based in Dhaka, Bangladesh. Business hours are 9 AM to 5 PM."
        else:
            return ""

