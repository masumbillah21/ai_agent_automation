import pytest
from agents.classify_query import QueryClassifierAgent
from agents.retrieve_data import DataRetrieverAgent

@pytest.fixture
def classifier():
    return QueryClassifierAgent()

@pytest.fixture
def retriever():
    return DataRetrieverAgent()

def test_classify_query_billing(classifier):
    assert classifier.classify("I want a refund") == "billing"

def test_classify_query_technical(classifier):
    assert classifier.classify("There is an error on my device") == "technical"

def test_classify_query_general(classifier):
    assert classifier.classify("Tell me your opening hours") == "general"

def test_retrieve_data_billing(retriever):
    assert "Billing info" in retriever.retrieve("billing")

def test_retrieve_data_technical(retriever):
    assert "Technical support" in retriever.retrieve("technical")

def test_retrieve_data_general(retriever):
    assert "General info" in retriever.retrieve("general")
