arquivo = open ("meses.txt", "w")

meses = ["janeiro", "feveiro", "março", "abril", "maio", "Junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

for linha in meses:
    arquivo.write("%s\n" % linha)

arquivo.close()