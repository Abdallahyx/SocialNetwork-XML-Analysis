

class Node:
    def __init__(self, key="", value=""):
        self.key = key
        self.value = value
        self.children = []

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key

    def find(self, key):
        if self.key == key:
            return self

        for child in self.children:
            result = child.find(key)
            if result:
                return result

        return None


class Tree:
    def __init__(self):
        self.m_root = None

    def set_root(self, t):
        self.m_root = t

    def add_node(self, node, parent=None):
        if parent is None:
            parent = self.m_root
        parent.children.append(node)

    def getroot(self):
        return self.m_root

    def PrettifyFormat(self, depth=0, parent=None):
        if parent is None:
            parent = self.m_root
            depth = 0

        output = ""
        indentation = "    " * depth

        output += indentation + "<" + parent.key + f">{parent.value.lstrip()}\n"

        for i in range(len(parent.children)):
            node = parent.children[i]

            if node.children:
                output += self.PrettifyFormat(depth + 1, node)
            else:
                output += (
                    indentation
                    + "    <"
                    + node.key
                    + ">"
                    + node.value
                    + "</"
                    + node.key
                    + ">\n"
                )

        output += indentation + "</" + parent.key + ">\n"

        return output

    def MinifyFormat(self, parent=None):
        if parent is None:
            parent = self.m_root

        output = ""
        parent_value = parent.value.lstrip().rstrip()
        output += "<" + parent.key + f">{parent_value}"

        for i in range(len(parent.children)):
            node = parent.children[i]

            if node.children:
                output += self.MinifyFormat(node)
            else:
                output += (
                    "<"
                    + node.key
                    + ">"
                    + node.value.lstrip().rstrip()
                    + "</"
                    + node.key
                    + ">"
                )

        output += "</" + parent.key + ">"

        return output

    def findall(self, key, parent=None):
        if parent is None:
            parent = self.m_root

        result = []
        if parent.key == key:
            result.append(parent)

        for child in parent.children:
            result.extend(self.findall(key, child))

        return result

    def toJson(self, parent=None, level=0):
        if parent is None:
            parent = self.m_root

        def format_value(value):
            if isinstance(value, list):
                formatted_list = ', '.join(format_value(item) for item in value)
                return '[{}]'.format(formatted_list)
            else:
                return '"{}"'.format(value)

        indent = '    ' * level
        if not parent.children:
            output = '{{\n{}"{}": {}'.format(indent, parent.key, format_value(parent.value))
        else:
            output = '{{\n{}"{}": '.format(indent, parent.key)

        if parent.children:
            output += '['
            for i, node in enumerate(parent.children):
                output += '\n{}{}'.format('    ' * (level + 1), self.toJson(node, level + 1))
                if i < len(parent.children) - 1:
                    output += ','
            output += '\n{}]'.format(indent)

        output += '\n{}}}'.format(indent)
        return output
 
    
# xml= """<users>
#     <user>
#         <id>1</id>
#         <name>Ahmed Ali</name>
#         <posts>
#             <post>
#                 <body>
#                     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#                 </body>
#                 <topics>
#                     <topic>
#                         economy
#                     </topic>
#                     <topic>
#                         finance
#                     </topic>
#                 </topics>
#             </post>
#             <post>
#                 <body>
#                     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#                 </body>
#                 <topics>
#                     <topic>
#                         solar_energy
#                     </topic>
#                 </topics>
#             </post>
#         </posts>
#         <followers>
#             <follower>
#                 <id>2</id>
#             </follower>
#             <follower>
#                 <id>3</id>
#             </follower>
#         </followers>
#     </user>
#     <user>
#         <id>2</id>
#         <name>Yasser Ahmed</name>
#         <posts>
#             <post>
#                 <body>
#                     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#                 </body>
#                 <topics>
#                     <topic>
#                         education
#                     </topic>
#                 </topics>
#             </post>
#         </posts>
#         <followers>
#             <follower>
#                 <id>1</id>
#             </follower>
#         </followers>
#     </user>
#     <user>
#         <id>3</id>
#         <name>Mohamed Sherif</name>
#         <posts>
#             <post>
#                 <body>
#                     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
#                 </body>
#                 <topics>
#                     <topic>
#                         sports
#                     </topic>
#                 </topics>
#             </post>
#         </posts>
#         <followers>
#             <follower>
#                 <id>1</id>
#             </follower>
#         </followers>
#     </user>
# </users>"""
#
# def remove_spaces_and_enters(input_string):
#     # Remove spaces
#     input_string = input_string.replace("    ", "")
#
#     # Remove newline characters
#     input_string = input_string.replace("\n", "").replace("\r", "")
#
#     return input_string
#
#
# def TreeParsing(xml, Nod=None, start=0):
#     open_tag = False
#     tag = []
#     tree = Tree()
#     tree.set_root(Nod)
#     tree.m_root = Nod
#     current_node = None
#     insidechild = False
#     value = []
#     parentnodevalue = []
#     insideparent = False
#     closed_tag = False
#     childnumber = 0
#     newindex = 0
#     parentindexend = None
#     if (Nod != None):
#         parentindexend = xml[newindex:].find('<' + '/' + tree.m_root.key + '>')
#
#     for i, char in enumerate(xml):
#         if (parentindexend != None):
#             if (i == parentindexend):
#                 return (tree.m_root)
#         if (i < newindex):
#             continue
#
#         if (insidechild == False and open_tag == False and char != '<'):
#             parentnodevalue.append(char)
#         elif (insidechild == True and open_tag == False and char != '<'):
#             value.append(char)
#         if (open_tag == True and current_node != tree.m_root):
#
#             if (value != []):
#                 current_node.set_value(''.join(value))
#                 value = []
#         if (closed_tag == True and char == '>'):
#             closed_tag = False
#         if (closed_tag == True):
#             continue
#         if (char == '<' and xml[i + 1] == '/'):
#             closed_tag = True
#
#         if (char == '<'):
#             open_tag = True
#             if (xml[i + 1] == '/'):
#                 insidechild = False
#             if (insidechild == True):
#                 substring_start = xml[i:].find('<' + '/' + current_node.key + '>')
#                 if substring_start != -1:
#                     node = TreeParsing(xml[i:(i + substring_start)], current_node)
#                     newindex = xml[i:].find('<' + '/' + current_node.key + '>')
#                     newindex += i
#
#                 continue
#
#         if char == '>':
#             open_tag = False
#             if tree.m_root is None:
#                 current_node = Node(''.join(tag[0:]))
#                 tree.set_root(current_node)
#                 insideparent = True
#             else:
#                 if ((''.join(tag[0:])) != ''):
#                     tree.add_node(Node(''.join(tag[0:])))
#                     current_node = tree.m_root.children[childnumber]
#                     childnumber += 1
#                     insidechild = True
#             tag = []
#
#         if (open_tag == True):
#             if (char != '<'):
#                 tag.append(char)
#             continue
#
#         if (char == '<' and xml[i + 1] == '/'):
#             parentnodevalue.append(char)
#         if (char == '<' and xml[i + 1] == '/'):
#             current_node.set_value(''.join(parentnodevalue))
#
#     tree.m_root.set_value(''.join(parentnodevalue))  # making sure the root node has a value
#
#     return (tree.m_root)
#
#
# xml = remove_spaces_and_enters(xml)
# tree = Tree()
# tree.set_root(TreeParsing(xml))
# json_output = tree.toJson()
#
# # Print the JSON output
# print(json_output)



