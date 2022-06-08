import os
import pdfplumber

col = ['овог, нэр', 'овог', 'нэр', 'эцэг/эхийн нэр', 'оюутны овог']
sets = []


def checker(name: str) -> bool:
    cnt = 0
    if name.lower() in col or len(name) < 2 or name == 'None':
        return False
    for ch in name:
        if ch == '-':
            continue
        if ord(ch) < 1025 or ord(ch) > 1257:
            return False
    return True

r = {
    '-\n' : '-', 
    '.' : '',
    ' -' : '-',
    '- ' : '-',
    '\n' : ' ',
    chr(1111) : chr(1199)
}

def fixing(fullname):
    for r1, r2 in r.items():
        fullname = fullname.replace(r1, r2)
    return fullname.split()


def extract(pdf):
    num_pages = len(pdf.pages)
    cols_num = []
    for row_idx, row in enumerate(pdf.pages[0].extract_table()):
        for col_idx, col_name in enumerate(row):
            if col_name is None:
                continue
            col_name = col_name.lower()
            if col_name in col:
                cols_num.append(col_idx)
        if row_idx > 5:
            break

    for i in range(num_pages):
        page = pdf.pages[i].extract_table()
        if page is None:
            continue
        for row in page:
            for col_num in cols_num:
                if col_num >= len(row):
                    continue
                
                names = fixing(str(row[col_num]))
                for name in names:
                    name = name.strip('.,')
                    if not checker(name):
                        continue
                    if name not in sets:
                        sets.append(name)
    return sets
