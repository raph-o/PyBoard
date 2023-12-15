from pathlib import Path
import importlib

graphs = Path(__file__).parent.glob("*.py")
for graph in graphs:
    if graph.stem != "__init__":
        graph_name = f"core.graphs.{graph.stem}"
        importlib.import_module(graph_name)
