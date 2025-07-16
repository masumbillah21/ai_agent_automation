import pytest
from agents.classify_query import QueryClassifierAgent
from agents.retrieve_data import DataRetrieverAgent

@pytest.fixture
def classifier():
    """Fixture for QueryClassifierAgent instance"""
    return QueryClassifierAgent()

@pytest.fixture
def retriever():
    """Fixture for DataRetrieverAgent instance"""
    return DataRetrieverAgent()

def test_classify_query_billing(classifier):
    """Test classification of a billing-related query"""
    result = classifier.classify("I want a refund")
    assert result == "billing"

def test_classify_query_technical(classifier):
    """Test classification of a technical-related query"""
    result = classifier.classify("There is an error on my device")
    assert result == "technical"

def test_classify_query_general(classifier):
    """Test classification of a general query"""
    result = classifier.classify("Tell me your opening hours")
    assert result == "general"

def test_retrieve_data_billing(retriever):
    """Test retrieval of billing-related data"""
    result = retriever.retrieve("billing")
    assert "Billing info" in result

def test_retrieve_data_technical(retriever):
    """Test retrieval of technical-related data"""
    result = retriever.retrieve("technical")
    assert "Technical support" in result

def test_retrieve_data_general(retriever):
    """Test retrieval of general information"""
    result = retriever.retrieve("general")
    assert "General info" in result
