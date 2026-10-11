"""MCP server for Persistent Knowledge Graph Memory & Entity Linker."""
import sys
import json
from client import KnowledgeGraphMemoryEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "query_knowledge_graph_memory",
                "description": "Builds entity-relation graph and retrieves multi-hop subgraphs",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "triples": {"type": "array"},
                        "query_entity": {"type": "string"},
                        "max_hops": {"type": "integer"}
                    },
                    "required": ["triples", "query_entity"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "query_knowledge_graph_memory":
            args = params.get("arguments", {})
            res = KnowledgeGraphMemoryEngine.build_and_query_graph(
                args.get("triples", []),
                args.get("query_entity", ""),
                args.get("max_hops", 2)
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
