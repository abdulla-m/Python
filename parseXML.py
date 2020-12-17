import xml.etree.ElementTree as ET

def get_score(node, score):
    for item in node:
        score += len(item.attrib)
        score = get_score(item, score)
    return score;

if __name__ == "__main__":
    tree = ET.parse("books.xml")
    root = tree.getroot()
    score = len(root.attrib)
    score = get_score(root,score)
    print("Score::", score)
