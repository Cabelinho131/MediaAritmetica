def aprovação(p1, p2, ac):
    media_inicial = (p1 * 0.4) + (p2 * 0.4) + (ac * 0.2)
    if media_inicial >= 7:
        print(f"Você foi aprovado! Sua média foi: {media_inicial:.2f}")
        return  
    print("Sua média foi inferior a 7, precisa fazer a prova substitutiva!")
    prova_substitutiva = float(input("Informe sua prova substitutiva:"))
 
    if p1 < p2:
        p1 = prova_substitutiva 
    else:
        p2 = prova_substitutiva 
    
    media_ajustada = (p1 * 0.4) + (p2 * 0.4) + (ac * 0.2)
    
    if media_ajustada >= 7:
        print(f"Você foi aprovado após a prova substitutiva! Sua média foi: {media_ajustada:.2f}")
    else:
        print(f"Reprovado! Sua média foi: {media_ajustada:.2f}")

p1 = float(input("Informe sua p1: "))
p2 = float(input("Informe sua p2: "))
ac = float(input("Informe sua ac: "))
aprovação(p1, p2, ac)

