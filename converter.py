with open('data/en', 'r') as f:
    en: list[str] = [ch[:-1] for ch in f.readlines()]

with open('data/mn', 'r') as f:
    mn: list[str] = [ch[:-1] for ch in f.readlines()]

converter = dict(zip(mn, en))

with open('data/in', 'r') as f:
    cyrillic_names: list[str] = [name.lower().strip() for name in f.readlines()]
    latin_names: list[str] = []
    for name in cyrillic_names:
        a_name: str = ''
        for ch in name:
            if ch.isalpha():
                a_name += converter[ch]
                continue
            a_name += ch
        latin_names.append(a_name)

print(latin_names)
