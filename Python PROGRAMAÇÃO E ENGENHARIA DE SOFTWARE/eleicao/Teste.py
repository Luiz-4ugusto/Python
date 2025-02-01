from candidato import Candidato
from partido import Partido
from apuracao import Apuracao


p1 = Partido(1, "PHS", "Partido das Hortaliças Selvagens")
p2 = Partido(2, "PFA", "Partido do Frango Assado")
c1 = Candidato(1, "Baby Chicken", p2, 50)
c2 = Candidato(2, "Chicória nutritiva", p1, 100)
c3 = Candidato(3, "Rabanete ensaboado", p1, 80)
c4 = Candidato(4, "Frangolino", p2, 500)

apuracao = Apuracao()
apuracao.inclui_candidato(c1)
apuracao.inclui_candidato(c2)
apuracao.inclui_candidato(c3)
apuracao.inclui_candidato(c4)

print(apuracao)