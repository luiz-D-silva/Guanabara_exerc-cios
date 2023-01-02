real = float(input('Digite um valor em R$:'))
euro = real/5.69
if euro == round(euro):
    print("Inteiro")
else:
    print("Aredondado para baixo:", round(euro-0.5))
    print("Aredondado para cima:", round(euro+0.5))
print('Com R$ {:.2f}, você consegue comprar € {:.2f}'.format(real, euro))
