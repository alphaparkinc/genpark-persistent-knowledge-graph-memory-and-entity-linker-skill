"""Persistent Knowledge Graph Memory & Entity Linker.
100% Python Standard Library.
"""

class KnowledgeGraphMemoryEngine:
    """Manages entity nodes, typed directed edges, and multi-hop subgraph retrieval."""

    @staticmethod
    def build_and_query_graph(triples: list, query_entity: str, max_hops: int = 2) -> dict:
        nodes = set()
        adjacency = {}
        for item in triples:
            src = item.get("source", "").strip()
            rel = item.get("relation", "related_to").strip()
            dst = item.get("target", "").strip()
            confidence = float(item.get("confidence", 1.0))
            if not src or not dst:
                continue
            nodes.add(src)
            nodes.add(dst)
            adjacency.setdefault(src, []).append({
                "target": dst,
                "relation": rel,
                "confidence": round(confidence, 3)
            })

        visited = {query_entity}
        frontier = [(query_entity, 0)]
        subgraph_edges = []

        while frontier:
            curr, depth = frontier.pop(0)
            if depth >= max_hops:
                continue
            for edge in adjacency.get(curr, []):
                subgraph_edges.append({
                    "source": curr,
                    "relation": edge["relation"],
                    "target": edge["target"],
                    "hop": depth + 1,
                    "confidence": edge["confidence"]
                })
                if edge["target"] not in visited:
                    visited.add(edge["target"])
                    frontier.append((edge["target"], depth + 1))

        return {
            "query_entity": query_entity,
            "total_graph_nodes": len(nodes),
            "subgraph_edges_count": len(subgraph_edges),
            "reachable_entities": sorted(list(visited)),
            "subgraph": subgraph_edges
        }
