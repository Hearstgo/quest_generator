from random import choice
#CONSTANTES--------------------------------------------------------------
difficulte_range={
"facile":[3,6],
"normal":[6,12],
"difficile":[20,40]
}
price_range={
"facile":1.103,
"normal":1.11,
"difficile":1.114
}

#VARIANTE DESCRIPTION------------------------------------------------------------------------------
#COLOR
couleur_ternes=["noir","blanc","gris","sombre","marron"]
couleurs_vives=["rouge","jaune","vert","bleu","violet","orange"]
couleur_pelage=["rayé","moucheté","tricolor","bai"]
#AJDECTIF
adj_agressif=["féroce","puissant","sanguinaire","lunatique","bestial"]
adj_passif=["doux","paresseux"]
adj_peur=["effrayant","monstrueux","terrifiant","lugubre","maléfique","perfide"]
bad_side=["corrompu"]
#Taille
gros=["géant","colossal","colosse","goliath","élite","titan","titanesque"]

#LIEUX------------------------------------------------------------------------------
lieux_terre_sauvage=["dans les steppes","dans les landes","dans la forêt",'dans le val']
lieux_terre_urbain=["en ville","dans les parcs","dans les égouts"]
lieux_ocean=["en eaux tropicales","dans les profondeurs","dans les abysses","dans les récifs"]
lieux_riviere=["dans les rivières","dans les ruisseaux","dans un fleuve","dans les torrents","dans les fiords"]
lieux_sombres=["en forêt","dans les cavernes","dans les grottes","dans un gouffre","dans les mines"]
lieux_glauque=["dans une nécrople","dans les cryptes","dans les égouts"]
lieux_humides=["dans un marais",'dans une toubière','dans des marigots',"dans la mangrove","dans les rizières"]
lieux_altitude=["sur la crête","dans les pierriers","dans la montagne","dans les montagnes",]
lieux_froids=["dans la toundra","dans un glacier"]
lieux_sec=["dans le desert","dans les dunes","dans la savane","dans un mesa"]

bestiaire_passif=["cochons","vaches","poules","animaux"]


bestiaire_agressif={
"Loups":{
	"tag":["carnivore","groupe"],
	"variante":couleur_ternes+couleur_pelage+adj_agressif,
	"lieux":lieux_terre_sauvage
},
"Ogres":{
	"tag":["groupe","meurtrier"],
	"variante":couleur_ternes,
	"lieux":lieux_altitude+lieux_sombres
},
"Gobelins":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+["dans les marais"]
},
"Slimes":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage
},
"Araignées":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres+["dans les forêt"]
},
"Banshees":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres
},
"Basilic":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Terreurs mineures":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque+["en enfer"]
},
"Terreur majeure":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque+["en enfer"]
},
"Cyclope":{
	"tag":["meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+lieux_altitude
},
"Démon":{
	"tag":["meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque+["en enfer"]
},
"Djin":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_sec
},
"Dragon":{
	"tag":[],
	"variante":[],
	"lieux":lieux_altitude+["dans les cavernes"]
},
"Dryades":{
	"tag":[],
	"variante":[],
	"lieux":lieux_riviere
},
"Centaures":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_terre_sauvage
},
"Chauves-souris":{
	"tag":["aérien"],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Chimères":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres
},
"Ectoplasmes":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Elementaires":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_riviere+lieux_sec+lieux_humides+lieux_froids+lieux_altitude
},
"Ents":{
	"tag":[],
	"variante":[],
	"lieux":["dans les forêt","en forêt"]
},
"Fantômes":{
	"tag":["aérien"],
	"variante":[],
	"lieux":["dans un vieux manoir"]+lieux_sombres
},
"Farfadets":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_terre_sauvage
},
"Géants":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_altitude
},
"Génie":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sec+["dans les bois"]
},
"Gnomes":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_sombres+lieux_altitude
},
"Golem":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_sombres+lieux_altitude
},
"Goules":{
	"tag":["meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Gorgones":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_humides+lieux_glauque
},
"Griffons":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_altitude
},
"Harpies":{
	"tag":["groupe","meurtrier","aérien"],
	"variante":[],
	"lieux":lieux_altitude
},
"Hobgobelins":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_sombres+["dans les marais"]
},
"Hydre":{
	"tag":[],
	"variante":[],
	"lieux":["en forêt"]
},
"Kraken":{
	"tag":[],
	"variante":[],
	"lieux":lieux_ocean
},
"Lutins":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_sombres
},
"Manticore":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage
},
"Minautore":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_altitude
},
"Momies":{
	"tag":["groupe"],
	"variante":[],
	"lieux":lieux_sec+lieux_glauque
},
"Nymphes":{
	"tag":[],
	"variante":[],
	"lieux":lieux_ocean+lieux_riviere
},
"Ondines":{
	"tag":["marin"],
	"variante":[],
	"lieux":lieux_ocean
},
"Orcs":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_sombres
},
"Revenants":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_glauque
},
"Scorpions":{
	"tag":[],
	"variante":[],
	"lieux":lieux_sec
},
"Sirènes":{
	"tag":["groupe","marin"],
	"variante":[],
	"lieux":lieux_ocean
},
"Sorcière":{
	"tag":[],
	"variante":[],
	"lieux":lieux_glauque
},
"Spectres":{
	"tag":[],
	"variante":[],
	"lieux":lieux_glauque
},
"Sphinx":{
	"tag":[],
	"variante":[],
	"lieux":lieux_altitude
},
"Squelettes":{
	"tag":["meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Titan":{
	"tag":[],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_altitude
},
"Trolls":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_terre_sauvage+lieux_froids+lieux_humides+lieux_sombres
},
"Vampires":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_sombres+lieux_glauque
},
"Zombies":{
	"tag":["groupe","meurtrier"],
	"variante":[],
	"lieux":lieux_glauque
}
}


#PHRASES D'ACCROCHE--------------------------------------------------------------
ask_help_exemples=[
	"vous demande de l'aide",
	"demande de l'aide d'un valeureux guerrrier",
	"demande de l'aide d'un mage puissant",
	"demande de l'aide d'un aventurier",
	]
#Nom de quetes par type
quete_name={
"kill":["Extermination des {1}","la fin des {1}"]
}

def create_quest_infos(type_of_quest,tag,giver,objectif,lieux,nb="None"):
	"""Entrées :
	type_of_quest (str) : kill/collect/escort
	giver (str) : nom du donneur de quête
	objectif : nom  du monstre/objet/plante/pnj à tuer/récolter/aider/parler
	lieux (str) : nom du lieux pour trouver les monstres/objets a recolter/pnj avec qui discuter
	nb (str) : nombre de monstre/objets à tuer/recolter vaut "None" par défaut et pour les quêtes de type escort
	Sortie :
	name (str) : le nom de la quête
	description (str) : description de la quête
	"""
	ask_help=choice(ask_help_exemples)

	if type_of_quest=="kill":
		animaux_passif=choice(bestiaire_passif)
		
		quetes_kill={
		"carnivore":[
			[giver+" "+ask_help+" pour chasser les "+objectif+" qui déciment ses "+animaux_passif+". Vous pourrez trouver les "+objectif+" "+lieux+". Tuez-en "+nb],
			["Protéger les "+animaux_passif+" de "+giver,"Venger les "+animaux_passif,"Venger les "+animaux_passif+" de "+giver,"Aider "+giver]],
		"agressif":[
			[giver+" "+ask_help+" pour le protéger des "+objectif+" qui sévissent "+lieux+". D'après "+giver+" il faudrait en tuer "+nb+" pour éliminer la menace.",giver+" "+ask_help+" pour tuer "+nb+" "+objectif+". Après avoir attaqué "+giver+", les "+objectif+" ont fuis "+lieux+"."],
			["Protégez "+giver,"Au secours de "+giver,"Les peurs de "+giver]],
		"groupe":[
		["Cela fait maintenant plusieurs jours que des "+nb+" "+objectif+" vagabondent en groupe "+lieux+". "+giver+" "+ask_help+" afin d'éradiquer la menace."],
		["Chasse aux "+objectif,"Pacification "+lieux,"Chasse "+lieux]],
		"meurtrier":[
		["Des "+objectif+" ont été vus "+lieux+" en train de massacrer ses amis. "+giver+" vous demande de venger ses amis."],
		["Une dette de sang","La vengeance de "+giver,"Le sang des "+objectif]],
		"aérien":[
		["Cela fait maintenant plusieurs semaines qu'environ "+nb+" "+objectif+" nous survolent la nuit rendant toute activité nocture impossible. "+giver+" à besoin d'aide pour rendre la zone plus sûre. Il pense que ces monstres sont "+lieux+" durant la journée."],
		["Nuit dangereuses","Raids aériens","le repaire des "+objectif]],
		"marin":[
		[giver+" "+ask_help+" car nombre de nos pêcheurs se font pièger et tuer par les "+objectif+". D'après certains, vous pourrez les trouver "+lieux],
		["A la pêche !","La vengeance des marins"]],
		"eau":[
		[],
		[]],
		"kidnapeur":[
		[],
		[]],
		"maléfice":[
		[],
		[]],
		"voleur":[
		[],
		[]],
		"pilleurs":[
		[],
		[]],
		"complot":[
		[],
		[]],
		"envahisseurs":[
		[],
		[]],
		"herbivore":[
		[],
		[]],
		"effrayant":[
		[],
		[]],

	}
	name = choice(quete_name[type_of_quest]+quetes_kill[tag][1])
	description =choice(quetes_kill[tag][0])

	return name, description
