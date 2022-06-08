
import os
import pdfplumber
from extracter import extract
#from converter import convert

dir_path = r'input'
files = []
for file in os.listdir(dir_path):
    with pdfplumber.open(r'{}'.format(file), 'rb') as pdf:
        name_dataset = extract(pdf)


