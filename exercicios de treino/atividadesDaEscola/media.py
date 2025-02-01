totalNotas = int(input("total de notas: "))
notas = 0
nota =0

while notas <totalNotas:
    n = float(input("digite nota:"))
    nota += n
    notas = notas + 1

if notas == totalNotas:
    media = nota/totalNotas
    print(f"a media das notas é {media} possuindo um total de {totalNotas} notas")