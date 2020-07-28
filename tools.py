#Codé et imaginé par Hugo Rey
import random

def to_gold(price):
	"""converti un float avec 4 décimales en or, argent et bronze
	1,4586 = 1 or 45 argent et 86 bronze"""
	gold = int(price//1)
	silver = int(100*(price%1))
	cooper = round(((100*(price%1))%1)*100)
	#print(gold,"gold",silver,"silver and",cooper,"cooper")
	res = str(gold)+" or "+str(silver)+" argent "+str(cooper)+" cuivre "
	return res

def random_key(dico):
	liste=[]
	for k in dico.keys():
		liste+=[k]
	return random.choice(liste)