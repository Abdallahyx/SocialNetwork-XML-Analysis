from collections import deque
class Node:
    def __init__(self, key="", value=""):
        self.key = key
        self.value = value
        self.children = []

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key


class Tree:
    def __init__(self):
        self.m_root = None

    def set_root(self, t):
        self.m_root = t

    def add_node(self, node, parent=None):
        if parent is None:
            parent = self.m_root
        parent.children.append(node)

    def format(self, depth=0, parent=None):
        if parent is None:
            parent = self.m_root
            depth = 0

        output = ""
        indentation = "    " * depth

        output += indentation + "<" + parent.key + ">\n"

        for i in range(len(parent.children)):
            node = parent.children[i]

            if node.children:
                output += self.format(depth + 1, node)
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


def remove_spaces_and_enters(input_string):
    # Remove spaces
    input_string = input_string.replace(" ", "")
    
    # Remove newline characters
    input_string = input_string.replace("\n", "").replace("\r", "")
    
    return input_string


def TreeParsing(xml,Nod=None):
    tagslist=[]
    open_tag = False
    tag=[] 
    tree=Tree()
    current_node = None
    insidechild=False
    value=[]
    parentnodevalue=[]
    insideparent=False
    closed_tag=False
    childnumber=0
    
    for i,char in enumerate(xml):
        if(insidechild==False and open_tag==False and char!='<'):
            parentnodevalue.append(char)
        elif(insidechild==True and open_tag==False and char!='<'):
            value.append(char)
        if(open_tag==True and current_node!=tree.m_root):
            
            if(value!=[]):
                
                current_node.set_value(''.join(value))
                value=[]
        if(closed_tag==True and char=='>'):
            closed_tag=False
        if(closed_tag==True):
            continue
        if(char=='<' and xml[i+1]=='/'):
            closed_tag=True
        if(insidechild==False and open_tag==False and char!='<'):
           # parentnodevalue.append(char)
            continue
    
        if(char=='<'):
            open_tag=True
            if(xml[i+1]=='/'):
                insidechild=False
                tagslist.pop()
                #current_node.set_key(''.join(value))
                
                #value=[]
            if(insidechild==True):
               tree.add_node(TreeParsing(xml[i:],current_node))

        
        if char=='>':
            open_tag=False
            if tree.m_root is None:
                current_node = Node(''.join(tag[0:]))
                tree.set_root(current_node)
                insideparent=True
            else:
                if((''.join(tag[0:])) != ''):
                    tree.add_node(Node(''.join(tag[0:])))
                    current_node = tree.m_root.children[childnumber]
                    childnumber+=1
                    insidechild=True
            if((''.join(tag[0:])) != ''):        
                tagslist.append(''.join(tag))
            tag=[]
            
        if(open_tag==True):
            if(char!='<'): 
                tag.append(char)
            continue


       # else:
           # if(char!='<'):
                #value.append(char)
                
        #if( char=='<' and xml[i+1]=='/' and current_node.key==tagslist[-1]):
           #current_node.set_value(''.join(value)) 
            #value=[]
        #parentnodevalue.append(char)
        #if(char=='<' and xml[i+1]=='/' and current_node.key==tagslist[-1]):
           # current_node.set_value(''.join(parentnodevalue)) 
    
    
   
    return tree

with open('New Text Document.xml','r') as file:
    xml = file.read()

xml = remove_spaces_and_enters(xml)
tree = TreeParsing(xml)
print(tree.format())

#for child in tree.m_root.children:
 #   print(child.key)
  #  print(child.value)
#print(xml)