import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from utils.logger import logger

class ResponseGeneratorAgent:
    def __init__(self, model: str = "llama3-70b-8192"):
        logger.info("ResponseGeneratorAgent initialized with LangChain + Groq")
        self.model = model
        self.client = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=self.model
        )

    async def generate(self, context: str, user_input: str) -> str:
        try:
            prompt = (
                f"Answer the following question concisely and directly, using only the information provided.\n"
                f"Question: {user_input}\n"
                f"Relevant information: {context}\n"
                f"Do not include extra pleasantries, disclaimers, or additional help offers. Provide a short, factual answer only."
            )

            messages = [
                SystemMessage(content="You are an AI customer support assistant. Be concise and factual."),
                HumanMessage(content=prompt)
            ]

            response = await self.client.ainvoke(messages)
            reply = response.content
            logger.info(f"Groq (LangChain) response: {reply}")
            return reply.strip()
        except Exception as e:
            logger.error(f"LangChain Groq invocation failed: {e}")
            return "Sorry, I couldn't process your request at the moment."

