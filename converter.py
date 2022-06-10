
import json

class Converter:

    def __init__(self) -> None:
        self.special_letters = ('е', 'ё', 'ю', 'я')
        self.vowels = ('а', 'э', 'о', 'у', 'ө', 'ү', 'и')
        with open('lang/data.json', 'r') as json_file:
            self.decode = json.loads(json_file.read())

    def converter(self, cyrillic_names: tuple[str]) -> tuple[str]:
        """
        nernii list ee tus bureer avaad buh usegiin jijig bolgood mun urd
        hoino zai baival tuuniig hasaad cyr to latin hurvuuldeg method oor latin
        neriig gargaj avaad ur dung tuple eer bucaasan
        """
        return tuple([self.convert(name.lower().strip()) for name in cyrillic_names])
    
    def convert(self, name: str) -> str():
        """
        cyr to latin ur dung hadgalah hooson str
        """
        temp: str = ''
        # umnuh useg ni deerh special_letters baih yum bol
        # vowels iig algasah heregtei
        # ex: 'оюун' -> 'ю' daraah 'у' useg bicigdehgui
        prev = False
        # nernii useg bureer ni decode hiine
        printed = []
        for ch in name:
            # useg mun esehiig shalgana
            if ch.isalpha():
                # umnuh ni special_letters bsan eseh evsel
                # uruu vowels bish bol edgeerig zalgana
                if not prev or ch not in self.vowels:
                    temp += self.decode[ch]
                prev = False
                # special_letters mun esehiig shalgana
                # herev unen bol prev dee True utga
                # onooj daraagiin useg shalgahad
                # prev ni True utgatai bn
                if ch in self.special_letters:
                    prev = True
                continue
            # herev ugui bol - gej uzeed shuud zalgana
            temp += ch
        return temp

if __name__ == '__main__':
    myObj = Converter()
    sample_data = ['Оюун']
    print(myObj.converter(sample_data))

