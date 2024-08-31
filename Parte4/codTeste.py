

def programa():
    l = [
        ("call","print","Entre A:",None),
        ("call","scan","a",None),
        ("<","temp","a",10),
        (">=","temp2","a",5),
        ("&&","temp3","temp","temp2"),
        ("if","temp3","verdade","falsidade"),
        ("label","verdade",None,None),
        ("call","print","A esta entre 5 e 10",None),
        ("jump","fimif",None,None),
        ("label","falsidade",None,None),
        ("call","print","A nao esta entre 5 e 10",None),
        ("label","fimif",None,None)
    ]
    return l