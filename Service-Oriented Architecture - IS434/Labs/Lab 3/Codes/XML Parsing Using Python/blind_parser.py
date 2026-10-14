import xml.etree.ElementTree as ET

def discover_and_print(element, indent=0):
    space = '  ' * indent
    attribs = ', '.join([f'{k}="{v}"' for k, v in element.attrib.items()])
    # Print structure and element content
    if attribs:
        print(f"{space}<{element.tag} {attribs}>")
    else:
        print(f"{space}<{element.tag}>")
    
    # Print text if available and not just whitespace
    if element.text and element.text.strip():
        print(f"{space}  Content: {element.text.strip()}")
    
    # Recursively process children
    for child in element:
        discover_and_print(child, indent + 1)
    
    print(f"{space}</{element.tag}>")

def parse_and_show_structure(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    discover_and_print(root)

if __name__ == '__main__':
    parse_and_show_structure('employees.xml')
