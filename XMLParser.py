from Tree import Tree, Node
import re


def XMLParse(XML_String):
    stk = []
    # Remove processing instruction if present
    XML_String = re.sub(r"<\?.*?\?>", "", XML_String)

    match = re.match(r"(?:\n)?<(\w+)(?:[^>]*?)>", XML_String)

    if match:
        root_tag = match.group(1)
    else:
        raise ValueError("Invalid XML format")

    root = Node()
    root.set_key(root_tag)
    tree = Tree()
    tree.set_root(root)
    st = XML_String.find("<", match.end())
    ps = XML_String.find(">", st)
    parent = root

    while XML_String.find("<", ps) != -1:
        if XML_String[st + 1] != "/":
            new_node = Node()
            new_node.set_key(XML_String[st + 1 : ps])
            st = XML_String.find("<", ps)
            tree.add_node(new_node, parent)

            if st != -1:
                value = XML_String[ps + 1 : st]
                new_node.set_value(value.rstrip().lstrip())
                if XML_String[st + 1] != "/":
                    stk.append(parent)
                    parent = new_node

            ps = XML_String.find(">", st)

        if XML_String[st + 1] == "/":
            st = XML_String.find("<", ps)
            ps = XML_String.find(">", st)

            if st != -1:
                if XML_String[st + 1] == "/":
                    if stk:
                        parent = stk.pop()

    return tree


# Example usage:
xml_string = """<?xml version="1.0" encoding="UTF-8" ?>
<users>
    <user>
        <id>1</id>
        <name>Ahmed Ali</name
        <posts>
            <post>
                <body>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </body
                <topics>
                    <topic>
                        economy
                    </topic>
                    <topic>
                        finance
                    </topic>
                </topics>
            </post>
            <post>
                <body>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </body>
                <topics>
                    <topic>
                        solar_energy
                    </topic>
                </topics>
            </post>
        </posts>
        <followers>
            <follower>
                <id>2</id>
            </follower>
            <follower>
                <id>3</id>
            </follower>
        </followers>
    </user>
</users>"""
parsed_tree = XMLParse(xml_string)
formatted_output = parsed_tree.PrettifyFormat()
print(formatted_output)
formatted_output = parsed_tree.MinifyFormat()
print(formatted_output)
# print(parsed_tree.toJson())
