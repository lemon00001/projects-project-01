
import os
import pdfplumber
from extracter import Extracter
from converter import Converter

dir_path = r'input'
name_dataset: tuple[str] = ()
cyrillic_dataset: tuple[str] = ()
latin_dataset: tuple[str] = ()
for file in os.listdir(dir_path):
    with pdfplumber.open('input/{}'.format(file)) as pdf_file:
        my_obj = Extracter(pdf_file)
        name_dataset = my_obj.extract()
        cyrillic_dataset += name_dataset
        my_obj1 = Converter()
        latin_dataset += my_obj1.converter(name_dataset)

print(len(name_dataset))
print(len(latin_dataset))
