from dotenv import load_dotenv
load_dotenv()

from workflows.customer_support_graph import create_customer_support_graph
import asyncio

async def main():
    graph = create_customer_support_graph()
    user_query = input("Enter customer query: ")
    result = await graph.ainvoke({"input_text": user_query})
    print("\n[AI Agent Response]:", result["response"])

if __name__ == "__main__":
    asyncio.run(main())
