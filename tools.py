
import random
import codecs
def to_gold(price,lang="fr"):
	"""converted a float with 4 decimal max into gold, silver and bronze
	1.4586 = 1 gold 45 silver and 86 bronze"""
	gold = int(price//1)
	silver = int(100*(price%1))
	copper = round(((100*(price%1))%1)*100)
	#print(gold,"gold",silver,"silver and",copper,"copper")
	if lang=="fr":
		res = str(gold)+" or "+str(silver)+" argent "+str(copper)+" cuivre "
	elif lang=="eng":
		res = str(gold)+" gold "+str(silver)+" silver "+str(copper)+" copper "
	return res

def random_key(dico):
	"""pick a random key of a dictionary"""
	liste=[]
	for k in dico.keys():
		liste+=[k]
	return random.choice(liste)

def minimumEditDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],distances[index1+1],newDistances[-1])))
        distances = newDistances
    return distances[-1]
