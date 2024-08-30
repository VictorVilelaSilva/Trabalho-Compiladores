
#receba 3 medidas de um triangulo (A,B,C). Verifique se essas medidas formam 1 triangulo, ou seja a soma de 2 lados quaissquer deve ser maior que o terceiro lado.
#Duga se o trinagulo pode ser formado ou não

#exemplo de triangulo que pode ser formado: 3,4,5
#exemplo de triangulo que não pode ser formado: 1,2,3
def programa():
    l = [
        ("call","print","Entre a:",None),
        ("call","scan","A",None),
        ("call","print","Entre b:",None),
        ("call","scan","B",None),
        ("call","print","Entre c:",None),
        ("call","scan","C",None),
        ("+","somaAB","A","B"),
        (">","temp","somaAB","C"),
        ("+","somaAC","A","C"),
        (">","temp2","somaAC","B"),
        ("+","somaBC","B","C"),
        (">","temp3","somaBC","A"),
        ("&&","temp4","temp","temp2"),
        ("&&","temp5","temp3","temp4"),
        ("if","temp5","verdade","falsidade"),
        ("label","verdade",None,None),
        ("call","print","Triangulo pode ser formado",None),
        ("jump","fimif",None,None),
        ("label","falsidade",None,None),
        ("call","print","Triangulo nao pode ser formado",None),
        ("label","fimif",None,None)


        
    ]
    return l