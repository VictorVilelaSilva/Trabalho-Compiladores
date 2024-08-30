
#receba 3 notas de um aluno. Realize a média aritmética destas. Calcule se o aluno foi aprovado(media >=6). Diga se  o aluno foi aprovado


def programa():
    l = [
        ("call","print","Digite a primeira nota:",None),
        ("call","scan","p1",None),
        ("call","print","Digite a segunda nota:",None),
        ("call","scan","p2",None),
        ("call","print","Digite a terceira nota:",None),
        ("call","scan","p3",None),
        ("+","somap1p2","p1","p2"),
        ("+","somap1p2p3","somap1p2","p3"),
        ("/","nota","somap1p2p3", 3),
        ("call","print","Média é :" ,None),
        ("call","print","nota" ,None),
        (">=","temp4","nota", 6),
        ("if","temp4","verdade","falsidade"),
        ("label","verdade",None,None),
        ("call","print","Aluno aprovado",None),
        ("jump","fimif",None,None),
        ("label","falsidade",None,None),
        ("call","print","Aluno reprovado",None),
        ("label","fimif",None,None)
    ]
    return l