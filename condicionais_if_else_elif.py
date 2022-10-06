"""
Estruturas condicionais
if(se), else(se não), elif(else if) (se não se)
"""

"""
Estrutura condicional if, else em C.

idade = 6

if(idade < 18){
    printf("Menor de idade")
}else if (idade == 18){
    printf("Tem 18 anos")
}else{
    printf("É menor de idade"):
}
"""

"""
Estrutura condicional if, else em Java.

idade = 6

if(idade < 18){
    System.out.println("Menor de idade")
}else if (idade == 18){
    System.out.println("Tem 18 anos")
}else{
    System.out.println("É menor de idade"):
}
"""


idade = int(input("Olá usuário, digite sua idade:"))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print('Tem 18 anos')
elif idade == 25:
    print('Tem 25 anos')
else:
    print("Maior de idade")
