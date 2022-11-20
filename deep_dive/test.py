

per = {
    'j': {'age': 20, 'eye': 'blue'},
    'm': {'age': 25, 'eye': 'brown'}
}

for k,v in per.items():
    if 'ey' in v:
        print(k, v)