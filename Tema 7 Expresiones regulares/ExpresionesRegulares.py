import re

id1 = "cantidad"
id2 = "_cantidad"
id3 = "can-tidad"
id4 = "3can_tidad"
id5 = "_cantidad3"
id6 = "C35132"
id7 = "_"
ids=[id1,id2,id3,id4,id5,id6,id7]

expresion_regular = "[a-zA-Z_]+[a-zA-Z0-9_]*"

for id in ids:
    resultado = re.fullmatch(expresion_regular,id)
    if(resultado):
        print(id,"hace 'match'")
    else:
        print(id,"no hace 'match'")