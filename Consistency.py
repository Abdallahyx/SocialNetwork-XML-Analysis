from Tree import Tree, Node
import re


# def check_xml_consistency(xml_string):
#     stack = []
#     errors = []

#     i = 0
#     while i < len(xml_string):
#         if xml_string[i] == "<":
#             i += 1

#             if i < len(xml_string) and xml_string[i] == "/":
#                 # Closing tag
#                 i += 1
#                 start_index = i
#                 while i < len(xml_string) and xml_string[i] not in [">", " ", "/"]:
#                     i += 1
#                 closing_tag = xml_string[start_index:i].strip()

#                 matching_opening_found = False

#                 while stack:
#                     if stack[-1][0] == closing_tag:
#                         opening_tag, opening_index = stack.pop()
#                         matching_opening_found = True
#                         break
#                     else:
#                         opening_tag, opening_index = stack.pop()
#                         errors.append(("Unclosed tag", opening_tag, opening_index))

#                 if not matching_opening_found:
#                     errors.append(("Mismatched tags", closing_tag, start_index))

#             elif i < len(xml_string) and xml_string[i] != "/":
#                 # Opening tag
#                 start_index = i
#                 while i < len(xml_string) and xml_string[i] not in [">", " ", "/"]:
#                     i += 1
#                 tag = xml_string[start_index:i].strip()

#                 stack.append((tag, start_index))

#         i += 1

#     for opening_tag, opening_index in stack:
#         errors.append(("Unclosed tag", opening_tag, opening_index))

#     return errors if errors else None


import re


def Consistency(XML_String):
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
                    errors.append(("Unclosed Tag", child, st, st + len(child)))
                    XML_String = XML_String[:st] + "</" + child + ">" + XML_String[st:]
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
                    if len(XML_String[st + 2 : XML_String.find(">", st)]) < len(child):
                        diff = len(child) - len(
                            XML_String[st + 2 : XML_String.find(">", st)]
                        )
                    else:
                        diff = len(XML_String[st + 2 : XML_String.find(">", st)]) - len(
                            child
                        )
                    XML_String = (
                        XML_String[:last_st]
                        + XML_String[st + 2 : XML_String.find(">", st)]
                        + XML_String[ps:]
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


# Example usage:
xml_example = """<users>
<user>
<id>1
<name>Ahmed Ali</name>
<posts>
<post>
<body>
</body>
<topics>
<topic>
finance
</topic>
</topics>
</post>
</posts>
<followers>
<follower>
<name>2</id>
</follower>
<follower>
<id>3</id>
</follower>
</user>
</users>"""
# result = check_xml_consistency(xml_example)

# # if result:
# #     for error_type, tag, error_index in result:
# #         print(f"{error_type} at index {error_index}: {tag}")
# # else:
# #     print("XML is consistent.")


result, errors = Consistency(xml_example.replace("\n", "").replace("\r", ""))
for error in errors:
    print(error)
print(result)
