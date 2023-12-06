from collections import deque
from Tree import Tree
from Tree import Node

def remove_spaces_and_enters(input_string):
    # Remove spaces
    input_string = input_string.replace("    ", "")
    
    # Remove newline characters
    input_string = input_string.replace("\n", "").replace("\r", "")
    
    return input_string


def TreeParsing(xml,Nod=None,start=0):
    open_tag = False
    tag=[] 
    tree=Tree()
    tree.set_root(Nod)
    tree.m_root=Nod
    current_node = None
    insidechild=False
    value=[]
    parentnodevalue=[]
    insideparent=False
    closed_tag=False
    childnumber=0
    newindex=0
    parentindexend=None
    if(Nod!=None):
        parentindexend=xml[newindex:].find('<'+'/'+tree.m_root.key+'>')
    
    for i,char in enumerate(xml):
        if(parentindexend!=None):
            if(i==parentindexend):
                return (tree.m_root)
        if(i<newindex):
            continue

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

    
        if(char=='<'):
            open_tag=True
            if(xml[i+1]=='/'):
                insidechild=False
            if(insidechild==True):
                substring_start = xml[i:].find('<'+'/'+current_node.key+'>')
                if substring_start != -1:
                    node = TreeParsing(xml[i:(i+substring_start)], current_node)
                    newindex=xml[i:].find('<'+'/'+current_node.key+'>')
                    newindex+=i
              
                continue
               
        
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
            tag=[]
            
        if(open_tag==True):
            if(char!='<'): 
                tag.append(char)
            continue


                
        if( char=='<' and xml[i+1]=='/' ):

         parentnodevalue.append(char)
        if(char=='<' and xml[i+1]=='/'):
            current_node.set_value(''.join(parentnodevalue)) 
    
    tree.m_root.set_value(''.join(parentnodevalue))
   
    return (tree.m_root)


def ParseintoTree(filepath):
    with open(filepath,'r') as file:
        xml = file.read()
    xml=remove_spaces_and_enters(xml)
    tree=Tree()
    tree.set_root(TreeParsing(xml))
    return tree
tree=ParseintoTree('New Text Document.xml')
print(tree.m_root.value)
print(tree.format())
