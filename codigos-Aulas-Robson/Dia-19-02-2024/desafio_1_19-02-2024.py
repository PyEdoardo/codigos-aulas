nome_Aluno = input("Digite o Seu Nome ou Escreva Sair: ")
while nome_Aluno != "sair":
 perc_Frequencia = int(input("Digite o Percentual de Frequência: "))
 nota_G1 = float(input("Digite a Nota da G1: "))
 nota_G2 = float(input("Digite a Nota da G2: "))
 media_Parcial = (nota_G1 + (nota_G2 * 2)) / 3
 if media_Parcial >= 6 and perc_Frequencia >= 75:
    print(f"Você foi Aprovado! \nMédia Parcial: {media_Parcial}")
 elif perc_Frequencia >= 75 and media_Parcial < 6:
    print(f"Você está em Exame Final!")
    exame_Final = float(input("Digite a Nota do Exame Final: "))
    media_Final = (media_Parcial + (exame_Final * 2)) / 3
    if media_Final < 6:
      print("Você Reprovou!")
    else:
      print("Você foi aprovado!")
    nome_Aluno = input("\nDigite o Seu Nome ou Escreva Sair: ")  
 else:
    print("Você Reprovou Direto!")
 nome_Aluno = input("\nDigite o Seu Nome ou Escreva Sair: ")   
       


