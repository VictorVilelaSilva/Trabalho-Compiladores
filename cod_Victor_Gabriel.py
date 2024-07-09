

def programa():
    l = [
        ("=","i",0,None),
        ("label","reset",None,None),
        ("==","temp","i",10),
        ("if","temp","verdade","falsidade"),
        ("label","verdade",None,None),
        ("call","print","i é igual a 10",None),
        ("jump","fimloop",None,None),
        ("label","falsidade",None,None),
        ("call","print","i",None),
        ("+","i","i",1),
        ("jump","reset",None,None),
        ("label","fimloop",None,None)
    ]
    return l