from GraphVisualization import create_graph
from NetworkAnalysis import *
from PostSearch import post_search


xml_file = "example3.xml"
graph = create_graph(xml_file)

most_influential(graph)
most_active(graph)
mutual_followers(graph, 1, 2)
mutual_followers(graph, 2, 3)
suggest_followers(graph)
post_search(graph, "lorem")
