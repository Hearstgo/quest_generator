#Crédits : Hearstgo

import random
from tools import random_key, to_gold
from item import generate_item
from quest_data import difficulte_range, price_range, create_quest_infos, bestiaire_agressif


#-------------------------------------------------------------------------------
#CLASS QUEST--------------------------------------------------------------------
#-------------------------------------------------------------------------------

class Quest():
	"""docstring for Quest"""
	def __init__(self,lvl="default",name="Extermination des Loups",description="Ceci est la quête créé par défaut, il faut tuer 10 Loups",reward={},objectif=["Loup",10],objectif_statut=0,difficulte="Normal",type_quest="kill"):
		self.name = name
		self.description = description
		self.reward = reward
		self.objectif = objectif
		self.objectif_statut=objectif_statut
		self.difficulte = difficulte
		self.type_quest = type_quest
		self.lvl = lvl

	def update(self,pos=0):
		"""pos est la position du joueur, info nécessaire à la complétion d'une quête d'escorte 
		Attention, cette méthode est encore une ébauche"""
		if self.type_quest == "kill":
			if self.objectif_statut==self.objectif:
				self.getReward()
			else:
				self.objectif_statut+=1

		elif self.type_quest == "collect":
			if self.objectif_statut==self.objectif:
				self.getReward()
			else:
				self.objectif_statut+=1

		elif self.type_quest == "escort":
			if self.objectif==pos:
				self.getReward()

	def getReward(self):
		return self.reward

	def seeRewardInfos(self):
		print("INFO RECOMPENSE\nNom de l'item (self.reward['name']) :",self.reward["name"],"\nData à transferer (self.reward['data']):",self.reward["data"])

	def info(self):
		infos=("Nom : {0}\nType : {1}\ndifficulte : {6}\nNiveau : {7}\nDescription : {2}\nRécompense : {3}\nstatut : {5}/{4}")
		print(infos.format(self.name,self.type_quest,self.description,self.reward["name"],self.objectif[1],self.objectif_statut,self.difficulte,self.lvl))




#-------------------------------------------------------------------
#GENERATION---------------------------------------------------------
#-------------------------------------------------------------------

def generate_quest(giver,lvl="default",lvl_max=30,name="default",description="default",reward="default",objectif=["default",-1],difficulte="default",type_quest="default"):
	""" si le nom ou la description de la quete ou l'objectif est modifié alors il faut aussi modifier ceux cité précédement"""

	#creation de l'objet quete
	quest=Quest()

	#type de quete
	if type_quest=="default":
		quest.type_quest = random.choice("kill","collect","talk")
	else :
		quest.type_quest=type_quest

	#niveau (lvl)
	if lvl=="default":
		quest.lvl=random.randint(1,lvl_max)
	else:
		quest.lvl = lvl

	#difficulte
	if difficulte=="default":
		if quest.lvl <= lvl_max//4:
			quest.difficulte=random.choice(["facile","normal"])
		elif quest.lvl <=(3*lvl_max)//4:
			quest.difficulte=random.choice(["normal"])

		else :
			quest.difficulte=random.choice(["difficile"])

	else:
		quest.difficulte=difficulte

	#making data
	if objectif[0]=="default":
		if type_quest=="kill":
			obj = random_key(bestiaire_agressif) #obj = objectif donc dans la cas d'une quete de kill, un monstre du bestiaire_agressif
			tag = random.choice(bestiaire_agressif[obj]["tag"]+["agressif"])
			lieu = random.choice(bestiaire_agressif[obj]["lieux"])
			if random.randint(1,2)==2:
				if len(bestiaire_agressif[obj]["variante"])!=0:
					obj+=" "+random.choice(bestiaire_agressif[obj]["variante"])
			
			number=random.randint(difficulte_range[quest.difficulte][0],difficulte_range[quest.difficulte][1])

		elif type_quest=="collect":
			print("------------- A CODER -------------")
		elif type_quest=="talk":
			print("------------- A CODER -------------")

	#name 
	if name=="default":
		if type_quest=="kill":
			quest_name_descri =create_quest_infos(type_of_quest="kill",tag=tag,giver=giver,objectif=obj,lieux=lieu,nb=str(number))
			quest.name=quest_name_descri[0]
			descri = quest_name_descri[1]
		elif type_quest=="collect":
			print("------------- A CODER -------------")
		elif type_quest=="talk":
			print("------------- A CODER -------------")

	else:
		quest.name=name

	#description
	if description=="default":
		if type_quest=="kill":
			quest.description=descri
		elif type_quest=="collect":
			print("------------- A CODER -------------")
		elif type_quest=="talk":
			print("------------- A CODER -------------")
	else:
		quest.description=description

	#statut
	quest.objectif[1]=number
	#reward
	if reward=="default":
		gold=round(price_range[quest.difficulte]**quest.lvl,4)
		quest.reward["name"]=[to_gold(gold)]
		quest.reward["data"]=[gold]

		#ajout d'un item:
		if random.randint(0,2)==2 or quest.difficulte=="difficile":
			item=generate_item(lvl=random.randint(quest.lvl,quest.lvl+3))
			quest.reward["name"]+=[item.name]
			quest.reward["data"]+=[item]

	else:
		quest.reward= reward

	return quest



#--------------------------------------------------------------------------
#TEST----------------------------------------------------------------------
#--------------------------------------------------------------------------
ma_quete=generate_quest(giver="Mr Beans",type_quest="kill")
ma_quete.info()