import pytest
import asyncio
from workflows.customer_support_graph import create_customer_support_graph
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.asyncio
async def test_customer_support_workflow():
    graph = create_customer_support_graph()
    input_payload = {"input_text": "I want a refund for my order."}
    result = await graph.ainvoke(input_payload)
    assert "refund" in result["response"].lower() or "sorry" in result["response"].lower()
