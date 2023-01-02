# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
àrea = altura * largura

print('Dada a largura {}, e a altura {}, têm-se {} m² de àrea'.format
      (largura, altura, àrea))
tinta = àrea/2
print('Para pintar esta parede você precisará de {} L de tinta'.format(tinta))
