import re


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

    def findall(self, key):
        result = []
        if self.key == key:
            result.append(self)

        for child in self.children:
            result.extend(child.findall(key))

        return result


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

    def toJson(self, parent=None, level=0):
        if parent is None:
            parent = self.m_root

        def format_value(value):
            if isinstance(value, list):
                formatted_list = ", ".join(format_value(item) for item in value)
                return "[{}]".format(formatted_list)
            else:
                return '"{}"'.format(value)

        indent = "    " * level
        if not parent.children:
            output = '{{\n{}"{}": {}'.format(
                indent, parent.key, format_value(parent.value)
            )
        else:
            if len(parent.children) > 1:
                output = '{{\n{}"{}": ['.format(indent, parent.key)
                for i, node in enumerate(parent.children):
                    output += "\n{}{}".format(
                        "    " * (level + 1), self.toJson(node, level + 1)
                    )
                    if i < len(parent.children) - 1:
                        output += ","
                output += "\n{}]".format(indent)
            else:
                output = '{{\n{}"{}": '.format(indent, parent.key)
                for i, node in enumerate(parent.children):
                    output += "\n{}{}".format(
                        "    " * (level + 1), self.toJson(node, level + 1)
                    )
                output += "\n{}".format(indent)

        output += "\n{}}}".format(indent)
        return output

    def XMLParse(self, XML_String):
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
                    new_node.set_value(self.format_value(value.rstrip().lstrip()))
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

    def Parse(self, filepath):
        with open(filepath, "r") as file:
            xml = file.read()
        tree = self.XMLParse(xml)
        return tree

    def ParseString(self, string):
        tree = self.XMLParse(string)
        return tree

    def Consistency(self, XML_String):
        stk = []
        errors = []

        # Remove processing instruction if present
        XML_String = re.sub(r"<\?.*?\?>", "", XML_String)

        match = re.match(r"(?:\n)?<(\w+)(?:[^>]*?)>", XML_String)

        if match:
            root_tag = match.group(1)
        else:
            raise ValueError("Invalid XML format")

        parent = root_tag
        stk.append(parent)
        st = XML_String.find("<", match.end())
        ps = XML_String.find(">", st)

        while XML_String.find("<", ps) != -1:
            if XML_String[st + 1] != "/":
                child = XML_String[st + 1 : ps]
                last_st = st + 1
                st = XML_String.find("<", ps)

                if st != -1:
                    if (
                        XML_String[ps + 1 : st].rstrip().lstrip() != ""
                        and XML_String[st + 1] != "/"
                    ):
                        errors.append(("Unclosed Tag", child))
                        XML_String = (
                            XML_String[:st] + "</" + child + ">" + XML_String[st:]
                        )
                        last_st += len(child)

                    if XML_String[st + 1] != "/":
                        parent = child
                        stk.append(parent)

                    elif child != XML_String[st + 2 : XML_String.find(">", st)]:
                        errors.append(
                            (
                                "Mismatched Tag",
                                child,
                                XML_String[st + 2 : XML_String.find(">", st)],
                            )
                        )
                        closing_tag = XML_String[st + 2 : XML_String.find(">", st)]
                        diff = len(child) - len(closing_tag)
                        XML_String = (
                            XML_String[:last_st] + closing_tag + XML_String[ps:]
                        )
                        st -= diff

                ps = XML_String.find(">", st)

            if XML_String[st + 1] == "/":
                st = XML_String.find("<", ps)
                ps = XML_String.find(">", st)

                if st != -1:
                    if XML_String[st + 1] == "/":
                        while stk:
                            if stk[-1] == XML_String[st + 2 : ps]:
                                stk.pop()
                                break
                            else:
                                errors.append(("Unclosed Tag", stk[-1]))
                                XML_String = (
                                    XML_String[:st]
                                    + "</"
                                    + stk.pop()
                                    + ">"
                                    + XML_String[st:]
                                )
                                break

        return XML_String, errors

    def export_file(self, string, output_path, output_format=None):
        if output_format.lower() == "json":
            output_path = self._add_extension(output_path, "json")
            with open(output_path, "w") as json_file:
                json_file.write(string)
            print(f"Data exported as JSON to {output_path}")

        elif output_format.lower() == "xml":
            output_path = self._add_extension(output_path, "xml")
            with open(output_path, "w") as xml_file:
                xml_file.write(string)
            print(f"Data exported as XML to {output_path}")
        else:
            raise ValueError(
                "Invalid output format. Supported formats are 'xml' and 'json'."
            )

    def _add_extension(self, filename, extension):
        """
        Add the specified extension to the filename if not already present.

        Parameters:
        - filename (str): The original filename.
        - extension (str): The extension to add.

        Returns:
        - str: The filename with the correct extension.
        """
        if not filename.lower().endswith(f".{extension}"):
            filename += f".{extension}"
        return filename

    def format_value(self, input_string):
        # Remove spaces
        input_string = input_string.replace("    ", "")

        # Remove newline characters
        input_string = input_string.replace("\n", "").replace("\r", "")

        return input_string

    ### Another Function for the parsing

    def TreeParsing(self, xml, Nod=None, start=0):  # O(N) time and space complexity
        open_tag = False
        tag = []
        tree = Tree()
        tree.set_root(Nod)
        tree.m_root = Nod
        current_node = None
        insidechild = False
        value = []
        parentnodevalue = []
        insideparent = False
        closed_tag = False
        childnumber = 0
        newindex = 0
        parentindexend = None
        if Nod != None:
            parentindexend = xml[newindex:].find("<" + "/" + tree.m_root.key + ">")

        for i, char in enumerate(xml):
            if parentindexend != None:
                if i == parentindexend:
                    return tree.m_root
            if i < newindex:
                continue

            if insidechild == False and open_tag == False and char != "<":
                parentnodevalue.append(char)
            elif insidechild == True and open_tag == False and char != "<":
                value.append(char)
            if open_tag == True and current_node != tree.m_root:
                if value != []:
                    current_node.set_value("".join(value))
                    value = []
            if closed_tag == True and char == ">":
                closed_tag = False
            if closed_tag == True:
                continue
            if char == "<" and xml[i + 1] == "/":
                closed_tag = True

            if char == "<":
                open_tag = True
                if xml[i + 1] == "/":
                    insidechild = False
                if insidechild == True:
                    substring_start = xml[i:].find("<" + "/" + current_node.key + ">")
                    if substring_start != -1:
                        node = self.TreeParsing(
                            xml[i : (i + substring_start)], current_node
                        )
                        newindex = xml[i:].find("<" + "/" + current_node.key + ">")
                        newindex += i

                    continue

            if char == ">":
                open_tag = False
                if tree.m_root is None:
                    current_node = Node("".join(tag[0:]))
                    tree.set_root(current_node)
                else:
                    if ("".join(tag[0:])) != "":
                        tree.add_node(Node("".join(tag[0:])))
                        current_node = tree.m_root.children[childnumber]
                        childnumber += 1
                        insidechild = True
                tag = []

            if open_tag == True:
                if char != "<":
                    tag.append(char)
                continue

            if char == "<" and xml[i + 1] == "/":
                parentnodevalue.append(char)
            if char == "<" and xml[i + 1] == "/":
                current_node.set_value("".join(parentnodevalue))

        tree.m_root.set_value(
            "".join(parentnodevalue)
        )  # making sure the root node has a value

        return tree.m_root
