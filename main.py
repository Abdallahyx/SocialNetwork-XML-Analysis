from Tree import Tree
from Network import Network
from compressor import XIPCompressor

xml_file = "Main Project\example.xml"
tree = Tree()
tree = tree.Parse(xml_file)
out = "Main Project\output"
tree.export_file(Tree.PrettifyFormat(tree), out, "xml")
tree.export_file(Tree.MinifyFormat(tree), out, "xml")
tree.export_file(Tree.toJson(tree), out, "json")
# print(Tree.PrettifyFormat(tree))
# print(Tree.MinifyFormat(tree))
# print(Tree.toJson(tree))
compressed = XIPCompressor()
compressed.decompress_binary("Main Project\example.xip")
graph = Network.create_graph(xml_file)

Network.most_influential(graph)
Network.most_active(graph)
Network.mutual_followers(graph, 1, 2)
Network.mutual_followers(graph, 2, 3)
Network.suggest_followers(graph)
Network.post_search(graph, "lorem")
