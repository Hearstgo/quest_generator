#Crédits : Hearstgo

import random
from tools import random_key, to_gold
from item_maker import generate_item


#-------------------------------------------------------------------------------
#CLASS QUEST--------------------------------------------------------------------
#-------------------------------------------------------------------------------

class Quest():
	"""docstring for Quest"""
	def __init__(self,lvl="default",name="Extermination des Loups",description="Ceci est la quête créé par défaut, il faut tuer 10 Loups",reward={},objectif=["Loup",10],objectif_statut=0,difficulty="Normal",type_quest="kill"):
		self.name = name
		self.description = description
		self.reward = reward
		self.objectif = objectif
		self.objectif_statut=objectif_statut
		self.difficulty = difficulty
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
		print("INFO REWARD\nName of the item (self.reward['name']) :",self.reward["name"],"\nData to transfert (self.reward['data']):",self.reward["data"])

	def info(self):
		infos=("Name : {0}\nType : {1}\ndifficulty : {6}\nLevel : {7}\nDescription : {2}\nReward : {3}\nstatut : {5}/{4}")
		print(infos.format(self.name,self.type_quest,self.description,self.reward["name"],self.objectif[1],self.objectif_statut,self.difficulty,self.lvl))




#-------------------------------------------------------------------
#GENERATION---------------------------------------------------------
#-------------------------------------------------------------------

def generate_quest(giver,language="eng",lvl="default",lvl_max=30,name="default",description="default",reward="default",objectif=["default",-1],difficulty="default",type_quest="default"):
	"""Entry: (type of variable)[mendatory/optional/special]
	ATTENTION special parameters are optional BUT if one of the special is modified, you need to modify also all the other [special]
	or you won't have correlation between the name of the quest, the description and the objective

	- giver (str)[mendatory] : Name of the pnj who give the quest. Exemple : giver = "Mr. Bean"
	- language (str)[optional] : The language used. it's english by default, can be switch to french. Exemple : language = "eng"/language = "fr"
	- lvl (int)[optional] : The level of the quest. Bewtween 1 and the level max. Exemple : lvl = 15
	- lvl_max (int)[optional] : The level max allowed. It's 30 by default. Exemple : lvl_max = 100
	- name (str)[special] : Name of the quest. Exemple : name = "Wolfs extermination"
	- description (str)[special] : Description of the quest Exemple : description = "You need to kill 10 wolfs who live in the forest."
	- reward (liste)[optional] : Reward of the quest, in first position it's the amout of money earned then the items.
		Exempe : reward=[1.4586,item1,item2,etc...] item1 and item2 are from the Item class, 
		Important : the amont of money is a float with 4 decimals : 1.4586 means 1 gold coin 45 silver coins and 86 copper coins
	- objectif (liste)[special] : Objectif of the quest, in first position, the name of the monster/object/plant/pnj to kill/harvest/help/tell,
		in second position the number to kill/collect or the position to reach. Exemple : objectif = ["Wolfs",10]
	- difficulty (str)[optional] : difficulty of the quest, bewteen "easy", "normal" and "hard" Exemple difficulty = "normal"
	- type_quest (str)[special] : the type of quest. Actually only "kill" is possible. Exemple : type_quest = "kill"

	Output
	- quest (Quest) The quest. you can do quest.info() to get the informations on a Quest variable
	"""
	#Language
	if language=="fr":
		from quest_data import difficulty_range, price_range, create_quest_infos, bestiaire_agressif
	elif language=="eng":
		from quest_data_eng import difficulty_range, price_range, create_quest_infos, bestiaire_agressif

	#Creation of the object
	quest=Quest()

	#type of quete
	if type_quest=="default":
		quest.type_quest = random.choice(["kill"]) #,"collect","talk" not codded yet
	else :
		quest.type_quest=type_quest

	#Level
	if lvl=="default":
		quest.lvl=random.randint(1,lvl_max)
	else:
		quest.lvl = lvl

	#difficulty
	if difficulty=="default":
		if quest.lvl <= lvl_max//4:
			quest.difficulty=random.choice(["easy","normal"])
		elif quest.lvl <=(3*lvl_max)//4:
			quest.difficulty=random.choice(["normal"])

		else :
			quest.difficulty=random.choice(["hard"])

	else:
		quest.difficulty=difficulty

	#making data
	if objectif[0]=="default":
		if quest.type_quest=="kill":
			obj = random_key(bestiaire_agressif) #obj = objectif donc dans la cas d'une quete de kill, un monstre du bestiaire_agressif
			tag = random.choice(bestiaire_agressif[obj]["tag"]+["aggressive"])
			lieu = random.choice(bestiaire_agressif[obj]["places"])
			if random.randint(1,2)==2:
				if len(bestiaire_agressif[obj]["variant"])!=0:
					obj+=" "+random.choice(bestiaire_agressif[obj]["variant"])
			
			number=random.randint(difficulty_range[quest.difficulty][0],difficulty_range[quest.difficulty][1])

		elif quest.type_quest=="collect":
			print("------------- TO CODE -------------")
		elif quest.type_quest=="talk":
			print("------------- TO CODE -------------")



	#name 
	if name=="default":
		if quest.type_quest=="kill":
			quest_name_and_descri =create_quest_infos(type_of_quest="kill",tag=tag,giver=giver,objectif=obj,places=lieu,nb=str(number))
			quest.name=quest_name_and_descri[0]
			descri = quest_name_and_descri[1]
		elif quest.type_quest=="collect":
			print("------------- TO CODE -------------")
		elif quest.type_quest=="talk":
			print("------------- TO CODE -------------")

	else:
		quest.name=name

	#description
	if description=="default":
		if quest.type_quest=="kill":
			quest.description=descri
		elif quest.type_quest=="collect":
			print("------------- TO CODE -------------")
		elif quest.type_quest=="talk":
			print("------------- TO CODE -------------")
	else:
		quest.description=description

	#statut
	quest.objectif[1]=number

	#reward
	if reward=="default":
		gold=round(price_range[quest.difficulty]**quest.lvl,4)
		quest.reward["name"]=[to_gold(gold,lang=language)]
		quest.reward["data"]=[gold]

		#add item to rewards:
		if random.randint(0,2)==2 or quest.difficulty=="difficile":
			item=generate_item(lvl=random.randint(quest.lvl,quest.lvl+3))
			quest.reward["name"]+=[item.name]
			quest.reward["data"]+=[item]

	else:
		quest.reward["name"]=[to_gold(reward[0],lang=language)]
		quest.reward["data"]=[reward[0]]
		for item in reward[1::]:
			quest.reward["name"]+= [item.name]
			quest.reward["data"]+= [item]

	#return the quest
	return quest



#--------------------------------------------------------------------------
#TEST----------------------------------------------------------------------
#--------------------------------------------------------------------------

#to generate a item randomly : generate_item()

ma_quete=generate_quest(giver="O'Conor",reward=[1.28,generate_item(),generate_item()])
ma_quete.info()