from langgraph.graph import StateGraph, START, END
from agents.classify_query import QueryClassifierAgent
from agents.retrieve_data import DataRetrieverAgent
from agents.generate_response import ResponseGeneratorAgent
from utils.logger import logger
from typing_extensions import TypedDict

class State(TypedDict, total=False):
    input_text: str
    category: str
    context: str
    response: str

def create_customer_support_graph():
    classifier = QueryClassifierAgent()
    retriever = DataRetrieverAgent()
    generator = ResponseGeneratorAgent()

    builder = StateGraph(State)

    # Sync node for classification
    def classify_node(state: State) -> dict:
        input_text = state["input_text"]
        logger.info(f"Classifying query: {input_text}")
        category = classifier.classify(input_text)
        return {"category": category}

    # Sync node for data retrieval
    def retrieve_node(state: State) -> dict:
        category = state["category"]
        logger.info(f"Retrieving data for category: {category}")
        context = retriever.retrieve(category)
        return {"context": context}

    # Async node for response generation
    async def generate_node(state: State) -> dict:
        context = state["context"]
        input_text = state["input_text"]
        logger.info(f"Generating response for input: {input_text} with context: {context}")
        response = await generator.generate(context, input_text)
        return {"response": response}

    # Explicitly add all nodes, mark async properly
    builder.add_node("classify", classify_node)
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("generate", generate_node, is_async=True)

    # Define edges between nodes
    builder.add_edge(START, "classify")
    builder.add_edge("classify", "retrieve")
    builder.add_edge("retrieve", "generate")
    builder.add_edge("generate", END)

    # Compile the graph
    return builder.compile()
