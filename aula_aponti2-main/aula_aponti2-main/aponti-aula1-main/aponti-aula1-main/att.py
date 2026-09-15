nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
if nota1 >= 7 and nota2 >= 7:
    print(f"{nome} está aprovado! {nota1} e {nota2}")
elif nota1 >= 7 or nota2 >= 7:
    print(f"{nome} está de recuperação! {nota1} e {nota2}")
else:
    print(f"{nome} está reprovado! {nota1} e {nota2}")