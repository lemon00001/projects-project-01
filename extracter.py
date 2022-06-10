
unique: tuple[str] = ()
class Extracter:

    def __init__(self, pdf_file: object()) -> None:
        self.pdf_file: object = pdf_file
        self.col_name: tuple[str] = ('овог, нэр', 'овог', 'нэр', 'эцэг/эхийн нэр', 'оюутны овог')
        self.replacement_values: dict() = {
            '\n-' : '-', 
            '-\n' : '-', 
            '.' : ' ',
            ' -' : '-',
            '- ' : '-',
            '\n' : ' ',
            'ѐ' : 'ё', 
            'є' : 'ө', 
            'ђ' : 'ү', 
            'ѓ' : 'ө', 
            'ї' : 'ү'
        }
        self.decoding_values: dict() = {
        }

    def extract(self) -> tuple[str]:
        global unique
        result: tuple[str] = ()
        num_pages = self.get_num_pages()
        col_ids = self.get_col_id()

        for page_num in range(num_pages):
            page_content = self.pdf_file.pages[page_num].extract_table()
            if page_content is None:
                continue
            for row_content in page_content:
                if row_content is None:
                    continue
                is_need_row = True if sum(1 for cell in row_content if cell is None) else False
                if is_need_row is True:
                    continue
                for col_id in col_ids:
                    if col_id >= len(row_content):
                        continue
                    names = self.fixer(str(row_content[col_id]))
                    for name in names:
                        name = name.capitalize()
                        if self.checker(name) and name not in unique:
                            unique += (name,)
                            result += (name,)
        return result

    def fixer(self, name: str) -> list[str]:
        for old_value, new_value in self.replacement_values.items():
            name = name.replace(old_value, new_value)
        cnt: int = 0
        for i in range(len(name)):
            if name[i].isupper():
                cnt += 1
            if cnt > 1:
                cnt -= 1
                if name[i - 1] != '-':
                    name = name[:i] + ' ' + name[i:]

        return name.split()

    def get_num_pages(self) -> int:
        return len(self.pdf_file.pages)

    def get_col_id(self,) -> tuple[int]:
        result: tuple[int] = ()
        found: bool = False
        for row in self.pdf_file.pages[0].extract_table():
            for col_id, col in enumerate(row):
                if col is not None and col.lower() in self.col_name:
                    result += (col_id,)
                    found = True

            if found is True:
                break
        return result

    def checker(self, name: str) -> bool:
        cnt = 0
        if name.lower() in self.col_name or len(name) < 2 or name == 'None':
            return False
        for ch in name:
            if ch == '-':
                continue
            if ord(ch) < 1025 or ord(ch) > 1257:
                return False
        return True

