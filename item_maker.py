#Codé et imaginé par Hearstgo

import random
from tools import to_gold, random_key

#TOOLS-------------------------------------------------------------------

def check_orthographe(mot,genre):
	new_mot=mot
	if genre in liste_genre_feminins:
		if mot in dico_ortographe_m_to_f:
			new_mot=dico_ortographe_m_to_f[mot]
		if genre in liste_genre_pluriel:
			if new_mot[-1]!='x' and new_mot[-1]!='s':
				new_mot+='s'
	return new_mot

#CLASS-------------------------------------------------------------------
class Item():
	"""docstring for item"""
	def __init__(self, name="épée rouillée",lvl=1,grade="commun",price=0.1,stackable=False,stats={"force":1,"dexterite":0.5},durabilite=[3,10],description="Une vieille épée rouillée qui coupe à peine du pain",effect="None"):
		self.name = name
		self.lvl = lvl
		self.grade = grade
		self.price = price
		self.stackable = stackable
		self.stats = stats
		self.durabilite = durabilite
		self.description = description
		self.effect = effect

	def info(self):
		infos=("Nom : {0}\nLevel : {1}\nGrade : {9}\nprix : {2}\nstackable : {3}\nStatistiques : {4}\nDurabilité : {5}/{6}\ndescription : {7}\neffet : {8}")
		print(infos.format(self.name,self.lvl,to_gold(self.price),self.stackable,self.stats,self.durabilite[0],self.durabilite[1],self.description,self.effect,self.grade))




#FUNC-------------------------------------------------------------------
def generate_item(type_of_item="default",name="default",genre="default",lvl="default",lvl_max=30,grade="default",stats="default",price="default",stackable="default",durabilite="default",description="default",effect="default"):
	"""
	Entrées (tout est optionnel):
	- (str) type_of_item : catégorie d'item généré, au choix entre arme, armure et bijoux
	- (str) name : nom de l'objet, si il est modifié, il faut aussi modifier type_of_item et genre en conséquence
	- (str) genre : sous-catégorie de l'objet. 
			ARME : épée, masse, dague, katana, lance, bâton, baguette, orbe, arc long, arc court, arbalète, kunai
			ARMURE : heaume, plastron, jambière, bottes, masque, veste, pantalon, chaussures, chapeau, cape, robe, sandales
			BIJOUX : boucle d'oreilles, collier, pendentif, ceinture, anneau, bague
	- (int) lvl : niveau de l'item
	- (int) lvl_max : niveau maximum d'un item (par défaut 30)
	- (str) grade : grade de l'item au choix, dans l'orde du moins au plus rare : commun, rare, légendaire, mythique, unique. Les 3 rangs les plus rares seront généré uniquement au niveau max si grade est laissé par défaut
	- (dico) stats : un dictionnaire écrit de la manière suivante : {"le nom de votre stat":value,etc...} avec value un entier.
			 stats possibles :  {"force":,"puissance",intelligence":,"dexterité":,"endurance":,"intelect":,"vitalite":,"vitesse":,"resistance_magique":,"resistance_physique"}
	- (float) price : un float à 4 décimales max : 1.4586 signigie 1 pièce d'or 45 pièce d'argent et 86 de cuivre
	- (booléen) stackable : True si l'item est stackable. Par défaut, toutes les armes, armures et les bijoux ne le sont pas
	- (liste) durabilité : une liste de deux entier avec en indice 1, la durabilité max. Exemple : [15,20] l'item a une durabilité max de 20 et il lui reste 15
	- (str) description : une descritpion de l'item, modifier ce paramètre n'a aucun incidence sur les autres
	- (str) effect : effet de l'objet, sans modification de ce paramètre, il y a 1 chance sur 21 qu'un item est un effet. Sinon, l'effet est automatiquement appliqué.

	Sortie :
	return l'item généré, c'est un objet de class Item, vous pouvez voir les infos de l'item avec la méthode .info()
	"""
	global liste_genre_feminins, dico_ortographe_m_to_f, liste_genre_pluriel
	liste_type_of_item = ["arme","armure","bijoux"]
	liste_type_of_item_proba=[2,5,1]
	liste_genre_feminins=["épée","masse","dague","lance","baguette","orbe","arbalète","jambières","bottes","veste","chaussures","cape","robe","sandales","boucle d'oreille","ceinture","bague"]
	liste_genre_pluriel=["jambières","bottes","chaussures","sandales"]
	dico_ortographe_m_to_f={
	"commun":"commune","éternel":"éternelle","enchanté":"enchantée","intemporel":"intemporelle",
	"tranchant":"tranchante","acéré":"acérée","pointu":"pointue","vif":"vive","résitant":"résitante",
	"rouillé":"rouillée","brillant":"brillante","léger":"légère","soyeux":"soyeuse"," serti":" sertie","meutrier":"meurtrière"
	}

	#GRADES----------------------------------------------------------------------------------------------------------
	liste_grades=["commun","rare","légendaire","mythique","unique"]
	liste_grades_proba = [64,32,4,2,1]
	liste_grade_prix ={"commun":[0,0],"rare":[0,1],"légendaire":[250,300],"mythique":[500,750],"unique":[1000,1250]}
	liste_grades_bonus ={"commun":[0,5],"rare":[10,15],"légendaire":[20,35],"mythique":[50,70],"unique":[100,110]}

	#EFFECTS--------------------------------------------------------------------------------------------------------
	liste_of_effects_arme=["poison","feu","vol de vie","saignement","faiblesse"]
	liste_of_effects_armure=["parade","épine"]
	liste_of_effects_bijoux=["régénération de vie","régénération d'endurance","régénération de mana"]
	
	#NAME AJOUTS----------------------------------------------------------------------------------------------------	
	dico_adjectif={
	" de ":["l'aube","l'ombre","la nuit","la brume","l'espoir","la forêt","l'eau","la malice","l'intelligence","Cronos"],
	" serti":[" d'or"," de diamants"," de rubis"," de saphirs"," d'émeraudes"," de pierres précieuses"],
	" d'":["espoir","Artémis","Athéna","Arès","Apollon","Eole","Hécate","Helios","Hestia"],
	" ":["éternel","enchanté","intemporel","sombre"],
	" en ":["fer","or","os"],
	" du ":["soleil","désespoir"],
	" des ":["montagnes","nains","hommes","elfes"],
	"spé":"CHOISIR UN ADJECTIF DE SPE"
	}

	liste_dieux=["d'Artémis","d'Athéna","d'Arès","d'Apollon","d'Eole","de Cronos","d'Hécate","d'Helios","d'Hestia"]

	liste_adjectif_cac=["tranchant","acéré","pointu"]
	liste_adjectif_dist=["rapide","véloce","vif"]
	liste_adjectif_mag=["magique","enchanté","élémentaire"]

	liste_adjectif_def=["solide","robuste","résitant"]
	liste_adjectif_heavy =["rouillé","brillant"]
	liste_adjectif_medium =["souple","léger","en cuir"]
	liste_adjectif_light =["léger","soyeux","en laine","en velour"]

	liste_adjectif_bijoux=["de précision","meutrier","sublime"]

	#ARMES-------------------------------------------------------------------------------------------------------------------------------------------
	liste_cac=["épée","masse","dague","katana","lance"]
	liste_mag=["bâton","baguette","orbe"]
	liste_dist=["arc long","arc court","arbalète","kunai"]

	dico_armes ={
	"épée":Item(name="épée",stats={"force":5,"dexterité":4},price=0.15,stackable=False,durabilite=[10,10],description="une épée...",effect="None"),
	"masse":Item(name="masse",stats={"force":10,"dexterité":2},price=0.15,stackable=False,durabilite=[10,10],description="une masse...",effect="None"),
	"dague":Item(name="dague",stats={"force":3,"dexterité":8},price=0.15,stackable=False,durabilite=[10,10],description="une dague...",effect="None"),
	"katana":Item(name="katana",stats={"force":4,"dexterité":6},price=0.15,stackable=False,durabilite=[10,10],description="un katana...",effect="None"),
	"lance":Item(name="lance",stats={"force":13,"dexterité":1},price=0.15,stackable=False,durabilite=[10,10],description="une lance...",effect="None"),
	"bâton":Item(name="bâton",stats={"intelligence":13,"dexterité":1},price=0.15,stackable=False,durabilite=[10,10],description="un bâton...",effect="None"),
	"baguette":Item(name="baguette",stats={"intelligence":6,"dexterité":8},price=0.15,stackable=False,durabilite=[10,10],description="une baguette...",effect="None"),
	"orbe":Item(name="orbe",stats={"intelligence":7,"dexterité":7},price=0.15,stackable=False,durabilite=[10,10],description="une orbe...",effect="None"),
	"arc long":Item(name="arc long",stats={"puissance":9,"dexterité":4},price=0.15,stackable=False,durabilite=[10,10],description="un arc long...",effect="None"),
	"arc court":Item(name="arc court",stats={"puissance":7,"dexterité":8},price=0.15,stackable=False,durabilite=[10,10],description="une arc court...",effect="None"),
	"arbalète":Item(name="arbalète",stats={"puissance":13,"dexterité":1},price=0.15,stackable=False,durabilite=[10,10],description="une arbalète...",effect="None")
	}

	#ARMURES----------------------------------------------------------------------------------------------------------------------------------------
	liste_def_heavy=["heaume","plastron","jambières","bottes"]
	liste_def_medium=["masque","veste","pantalon","chaussures"]
	liste_def_light=["chapeau","cape","robe","sandales"]

	dico_armures={
	"heaume":Item(name="heaume",stats={"endurance":3,"vitalite":7,"resistance_magique":2,"resistance_physique":8},price=0.05,stackable=False,durabilite=[10,10],description="un heaume...",effect="None"),
	"masque":Item(name="masque",stats={"endurance":3,"vitalite":4,"resistance_magique":4,"resistance_physique":4},price=0.05,stackable=False,durabilite=[10,10],description="un masque...",effect="None"),
	"chapeau":Item(name="chapeau",stats={"intelect":5,"vitalite":2,"resistance_magique":8,"resistance_physique":2},price=0.05,stackable=False,durabilite=[10,10],description="un chapeau...",effect="None"),
	"plastron":Item(name="plastron",stats={"endurance":4,"vitalite":15,"resistance_magique":4,"resistance_physique":15},price=0.07,stackable=False,durabilite=[10,10],description="un plastron...",effect="None"),
	"veste":Item(name="veste",stats={"endurance":4,"vitalite":10,"resistance_magique":8,"resistance_physique":8},price=0.07,stackable=False,durabilite=[10,10],description="une veste...",effect="None"),
	"cape":Item(name="cape",stats={"intelect":6,"vitalite":8,"resistance_magique":15,"resistance_physique":4},price=0.07,stackable=False,durabilite=[10,10],description="une cape...",effect="None"),
	"jambières":Item(name="jambières",stats={"endurance":3,"vitalite":13,"resistance_magique":3,"resistance_physique":3},price=0.07,stackable=False,durabilite=[10,10],description="une paire de jambières...",effect="None"),
	"pantalon":Item(name="pantalon",stats={"endurance":3,"vitalite":8,"resistance_magique":7,"resistance_physique":7},price=0.07,stackable=False,durabilite=[10,10],description="un pantalon...",effect="None"),
	"robe":Item(name="robe",stats={"intelect":5,"vitalite":6,"resistance_magique":14,"resistance_physique":14},price=0.07,stackable=False,durabilite=[10,10],description="une robe...",effect="None"),
	"bottes":Item(name="bottes",stats={"vitesse":1,"resistance_magique":2,"resistance_physique":8},price=0.05,stackable=False,durabilite=[10,10],description="une paire de bottes...",effect="None"),
	"chaussures":Item(name="chaussures",stats={"vitesse":3,"resistance_magique":4,"resistance_physique":4},price=0.05,stackable=False,durabilite=[10,10],description="une paire chaussures...",effect="None"),
	"sandales":Item(name="sandales",stats={"vitesse":2,"resistance_magique":8,"resistance_physique":2},price=0.05,stackable=False,durabilite=[10,10],description="une paire sandales...",effect="None"),
	}

	#BIJOUX----------------------------------------------------------------------------------------------------------------------------------------
	oreilles=["boucle d'oreille"]
	cou=["collier","pendentif"]
	taille=["ceinture"]
	main=["anneau","bague"]
	dico_bijoux={
	"boucle d'oreille":Item(name="boucle d'oreille",stats={"critique":5,"précision":5},price=0.12,stackable=False,durabilite=[10,10],description="une boucle d'oreille...",effect="None"),
	"collier":Item(name="collier",stats={"précision":5},price=0.12,stackable=False,durabilite=[10,10],description="un collier...",effect="None"),
	"pendentif":Item(name="pendentif",stats={"critique":5},price=0.12,stackable=False,durabilite=[10,10],description="un pendentif...",effect="None"),
	"ceinture":Item(name="ceinture",stats={"critique":2,"précision":2},price=0.12,stackable=False,durabilite=[10,10],description="une ceinture...",effect="None"),
	"anneau":Item(name="anneau",stats={"critique":1,"précision":1},price=0.12,stackable=False,durabilite=[10,10],description="un anneau...",effect="None"),
	"bague":Item(name="bague",stats={"critique":1,"précision":1},price=0.12,stackable=False,durabilite=[10,10],description="une bague...",effect="None"),
	}


	if type_of_item=="default":
		type_of_item = random.choices(liste_type_of_item,liste_type_of_item_proba)[0]

	#nom--------------------------------------------------------------------------------------------------
	if name=="default":
		if genre =="default":
			if type_of_item=="arme":
				name=random_key(dico_armes)
			elif type_of_item=="armure":
				name=random_key(dico_armures)
			elif type_of_item=="bijoux":
				name =random_key(dico_bijoux)

		else:
			name = genre
		genre = name
		#mot de liaison
		liaison=random_key(dico_adjectif)
		
		#exception armure
		if liaison==" en ":
			if type_of_item=="armure":
				liaison=" des "

		if liaison==" serti":
			name=genre+check_orthographe(liaison,genre)+random.choice(dico_adjectif[liaison])

		#adjectif spécifique au type d'objet
		elif liaison =="spé":
			if genre in liste_cac:
				adj = random.choice(liste_adjectif_cac)
			elif genre in liste_dist:
				adj = random.choice(liste_adjectif_dist)
			elif genre in liste_mag:
				adj = random.choice(liste_adjectif_mag)
			elif genre in liste_def_heavy:
				adj = random.choice(liste_adjectif_heavy)
			elif genre in liste_def_medium:
				adj = random.choice(liste_adjectif_medium)
			elif genre in liste_def_light:
				adj = random.choice(liste_adjectif_light)
			elif genre in dico_bijoux:
				adj = random.choice(liste_adjectif_bijoux)
			else:
				adj = random.choice(dico_adjectif[" "])
			name=genre+" "+check_orthographe(adj,genre)
		#sans mot de liaison + possibilité double descriptif
		elif liaison ==" ":
			name=genre+liaison+check_orthographe(random.choice(dico_adjectif[liaison]),genre)
			if random.randint(0,5)>4:
				name+=" "+random.choice(liste_dieux)
		else:
			name+=liaison+check_orthographe(random.choice(dico_adjectif[liaison]),genre)


	#creation de la base de l'item--------------------------------------------------------------------------------------------------
	if type_of_item=="arme":
		item = dico_armes[genre]
	elif type_of_item=="armure":
		item = dico_armures[genre]
	elif type_of_item=="bijoux":
		item = dico_bijoux[genre]

	#mise a jour du nom
	item.name = name

	#lvl--------------------------------------------------------------------------------------------------
	if lvl == "default":
		if grade in ["légendaire","mythique","unique"]:
			lvl =lvl_max
		else :
			lvl = random.randint(1,lvl_max)
	item.lvl = lvl

	#grade--------------------------------------------------------------------------------------------------
	if grade =="default":
		if lvl == lvl_max:
			if type_of_item=="bijoux":
				grade=random.choices(["rare","légendaire","mythique","unique"],[100,10,3,1])[0]
			else:
				grade = random.choices(liste_grades,liste_grades_proba)[0]
		else :
			if type_of_item=="bijoux":
				grade = "rare"
			else :
				grade = random.choice(["commun","rare"])
	item.grade = grade

	#stats--------------------------------------------------------------------------------------------------
	somme_stats=0
	if stats =="default":
		#pour les bijoux les stats sont calculées différement
		if type_of_item=="bijoux":
			bonus_grade = random.randint(liste_grades_bonus[grade][0],liste_grades_bonus[grade][1])
			valeurs_alea = random.randint(round(lvl*1.1),round(lvl*1.5)) + bonus_grade//5
			spe_dmg=random.choice(["dégats magique","dégats physique"])
			for k in item.stats.keys():
				item.stats[k] =round(item.stats[k]*(1+(lvl/15))) + bonus_grade
				somme_stats+=item.stats[k]
			#ajout de la stats spécifique + mise a jour de somme_stats
			item.stats[spe_dmg] = valeurs_alea
			somme_stats+=valeurs_alea
			#ajout de stats en fonction du nom
			if "précision" in item.name:
				item.stats["précision"] *=2
				somme_stats+=item.stats["précision"]//2
			elif ("meutrier" or "meurtrière") in item.name:
				item.stats["critique"]*=2
				somme_stats+=item.stats["critique"]//2
		#Armes et armures
		else:
			for k in item.stats.keys():
				bonus_grade = random.randint(liste_grades_bonus[grade][0],liste_grades_bonus[grade][1])
				item.stats[k] =round(item.stats[k]*(1+(lvl/3))) + bonus_grade
				somme_stats+=item.stats[k]
	#si les stats sont fixés
	else :
		item.stats = stats
		for k in item.stats.keys():
			somme_stats+=item.stats[k]
	#price--------------------------------------------------------------------------------------------------
	if price =="default":
		prix_grade = (random.randint(liste_grade_prix[grade][0],liste_grade_prix[grade][1]))
		price = round(somme_stats/43+prix_grade,4)
	item.price = price

	#durabilité--------------------------------------------------------------------------------------------------
	if durabilite=="default":
		durabilite_max = item.durabilite[1]+lvl+random.randint(liste_grades_bonus[grade][0],liste_grades_bonus[grade][1])
	item.durabilite=[durabilite_max,durabilite_max]

	#description--------------------------------------------------------------------------------------------------
	if description!="default":
		item.description=description

	#effet--------------------------------------------------------------------------------------------------
	if effect=="default":
		if lvl >=lvl_max//2 and random.randint(0,20)==20:
			if type_of_item=="arme":
				effect=random.choice(liste_of_effects_arme)
			elif type_of_item=="armure":
				effect=random.choice(liste_of_effects_armure)
			elif type_of_item=="bijoux":
				effect=random.choice(liste_of_effects_bijoux)
	item.effect=effect


	return item



#mon_arme=generate_item()
#mon_arme.info()


