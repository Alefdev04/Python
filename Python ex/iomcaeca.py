print('Média do Aluno(a) do 6º Ano!\n')

nome = input('Qual é o nome do aluno(a): ')
mat = float(input('Nota de Matemática: '))
port = float(input('Nota de Língua Portuguesa: '))
cien = float(input('Nota de Ciências: '))
hist = float(input('Nota de História: '))
geo = float(input('Nota de Geografia: '))

if all(0 <= nota <= 10 for nota in [mat, port, cien, hist, geo]):
    media = (mat + port + cien + hist + geo) / 5

    print(f"""
Com as seguintes notas:
Matemática: {mat:.1f}
Português: {port:.1f}
Ciências: {cien:.1f}
História: {hist:.1f}
Geografia: {geo:.1f}
""")
    print(f'O aluno(a) {nome} teve uma média de {media:.1f}')
else:
    print("Erro: Alguma nota está fora do intervalo permitido (0 a 10).")
