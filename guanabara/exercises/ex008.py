"""
    curso Python 3 - Exercício Python #008
    crie um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
    24.10.2020 - Felipe Ferreira de Aguiar
"""

#! quilômetro (km), hectômetro (hm), decâmetro (dam), metro (m), decímetro (Dm)
#! centímetro (cm), milímetro (mm)

m = float(input('Digite o valor em metros '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('O valor digitado foi {:.1f} metros\nconvertido em mm  = {:.0f}\n'.format(m, mm), end='')
print('convertido em cm  = {:.0f}\n'.format(cm), end='')
print('convertido em dm  = {:.0f}\nconvertido em dam = {:.3f}\n'.format(dm, dam), end='')
print('convertido em hm  = {:.3f}\nconvertido em km  = {:.3f}'.format(hm, km))
