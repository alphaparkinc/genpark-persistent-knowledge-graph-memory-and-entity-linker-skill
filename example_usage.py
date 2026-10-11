"""Example usage for Persistent Knowledge Graph Memory & Entity Linker."""
from client import KnowledgeGraphMemoryEngine

if __name__ == "__main__":
    triples = [
        {"source": "Agent_Alpha", "relation": "uses_protocol", "target": "MCP_v2", "confidence": 0.98},
        {"source": "MCP_v2", "relation": "secured_by", "target": "OAuth_2.1", "confidence": 0.95}
    ]
    res = KnowledgeGraphMemoryEngine.build_and_query_graph(triples, "Agent_Alpha", max_hops=2)
    print("Subgraph Edges:", res["subgraph"])
