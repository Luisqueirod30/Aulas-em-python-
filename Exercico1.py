#Cauculando media de aluno// 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))

media = (nota1 + nota2) / 2
print(media)
if media >= 5:
  print("Aprovado") 
  print((nota1 + nota2)/2)

  if media >= 6:
    print("Aprovado")
    print((nota1 + nota2)/2)
  else: 
    print('aluno em exame' )
    print((nota1 + nota2)/2)

else:
  print("aluno reprovado")
  print((nota1 + nota2)/2)
  print("end")
