itens = int(input())
lista = input()
lista = [int(n) for n in lista.split(" ")]
dobra = int(input())
saida = input()
saida = [int(n) for n in saida.split(" ")]
for k in range(2):
  if (k!= 0):
    lista = lista[::-1].copy()
  tamanho = len(lista)
  fatia = tamanho//dobra
  listafinal = lista[:dobra]
  i = 0
  while i < fatia:
    inicio = (i+1) * dobra
    fim = (i+1)* dobra + dobra
    if fim < tamanho:
      lista2 = lista[inicio:fim]
    else:
      lista2 = lista[inicio:]
    j = -1
    for x in lista2:
      listafinal[j] += x 
      j -= 1 
    i += 1
  if (listafinal == saida):
    resposta = "S"
    break
  else:
    resposta = "N"
print(resposta)
