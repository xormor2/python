#!/bin/python3
def toiminto(puput_arvo, porkkanat_arvo):
	puput = puput_arvo
	porkkanat = porkkanat_arvo
	print("puput, porkkanat =")
	print(puput, porkkanat)
	porkkanat=puput
	print("puput, porkkanat =")
	print(puput, porkkanat)
	return 0
palautusarvo = toiminto(15,10)
print(f'funktion toiminto() palautusarvo = {palautusarvo}')
palautusarvo=toiminto(30,20)
print(f'funktion toiminto() palautusarvo = {palautusarvo}')
palautusarvo = toiminto(80,40)
print(f'funktion toiminto() palautusarvo = {palautusarvo}')
