import zipfile, os, xml.etree.ElementTree as ET
path = r'c:\Users\Shreya G S\Downloads\Activity_6_LeetCode_Portfolio.docx'
print('exists:', os.path.exists(path))
if os.path.exists(path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    texts = []
    for p in root.findall('.//w:p', ns):
        bits = []
        for t in p.findall('.//w:t', ns):
            bits.append(t.text or '')
        joined = ''.join(bits)
        if joined.strip():
            texts.append(joined)
    print('\n'.join(texts[:400]))
