

def programa():
    l = [
        ("call","print","Entre a:",None),
        ("call","scan","A",None),
        ("==","temp","i",10),
        ("if","temp","verdade","falsidade"),
        ("label","verdade",None,None),
        ("call","print","i é igual a 10",None),
        ("jump","fimif",None,None),
        ("label","falsidade",None,None),
        ("label","fimif",None,None)
    ]
    return l