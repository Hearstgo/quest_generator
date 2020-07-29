from random import choice
#CONSTANTES
difficulte_range={
"easy": [3,6],
"normal": [6,12],
"hard": [20,40]
}
price_range={
"easy":1.103,
"normal":1.11,
"hard":1.114
}

#VARIANT DESCRIPTION
#COLOR
dull_color=["black", "white", "grey", "dark", "brown"]
bright_colors=["red", "yellow", "green", "blue", "purple", "orange"]
fur_color=["striped", "speckled", "tricolor", "bay"]
#AJDECTION
adj_aggressive=["fierce," "powerful," "bloodthirsty," "moody," "bestial"]
adj_passif=["sweet", "lazy"]
adj_scaring=["frightening", "monstrous", "terrifying", "gloomy", "evil", "perfidious"]
bad_side=["corrupt"]
#Size
big=["giant," "colossal," "colossal," "goliath," "elite," "titan," "titanic"]

#PLACE
places_wild_earth=["in the steppes", "in the moors", "in the forest", "in the valley"]
places_urban_earth=["in cities," "in parks," "in sewers"]
ocean_places=["in tropical waters," "in the depths," "in the abyss," "in the reefs"]
river_places=["in rivers", "in streams", "in a river", "in torrents", "in fiords"]
dark_places=["in the forest", "in the caves", "in a chasm", "in the mines"]
creepy_places=["in a necropolis," "in crypts," "in sewers"]
humid_places=["in a swamp", 'in a peat bog', 'in marigots', 'in the mangrove swamp', "in the rice fields"]
high_places=["on the ridge," "in the hills," "in the mountains,"]
cold_places=["in the tundra," "in a glacier"]
dry_places=["in the desert", "in the dunes", "in the savannah", "in a mesa"]

bestiary_passif=["pigs", "cows", "chickens", "animals"]


bestiaire_agressif={
"Wolves":{
	"tag": ["carnivore", "group"],
	"variant":dull_color+fur_color+adj_aggressive,
	"places":places_wild_earth
},
"Ogres":{
	"tag": [ "group", "murderer" ],
	"variant":dull_color,
	"places":high_places+dark_places
},
"Goblins":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":dark_places+["in the swamp"]
},
"Slimes":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth
},
"Spiders":{
	"tag":[],
	"variant":[],
	"places":dark_places+["in the woods"]
},
"Banshees":{
	"tag":[],
	"variant":[],
	"places":dark_places
},
"Basil":{
	"tag":[],
	"variant":[],
	"places":dark_places+creepy_places
},
"Minor terrors":{
	"tag":[],
	"variant":[],
	"places":dark_places+["in hell"]
},
"Major Terror":{
	"tag":[],
	"variant":[],
	"places":dark_places+["in hell"]
},
"Cyclops":{
	"tag": ["murderer"],
	"variant":[],
	"places":dark_places+high_places
},
"Demon":{
	"tag": ["murderer"],
	"variant":[],
	"places":dark_places+["in hell"]
},
"Djin":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth+dry_places
},
"Dragon":{
	"tag":[],
	"variant":[],
	"places":high_places+ ["in the caves"]
},
"Dryades":{
	"tag":[],
	"variant":[],
	"places":river_places
},
"Centaurs":{
	"tag": ["group"],
	"variant":[],
	"places":places_wild_earth
},
"Bats":{
	"tag": ["airborne"],
	"variant":[],
	"places":dark_places+creepy_places
},
"Chimeras":{
	"tag":[],
	"variant":[],
	"places":dark_places
},
"Ectoplasms":{
	"tag":[],
	"variant":[],
	"places":dark_places+creepy_places
},
"Elementary":{
	"tag": ["group"],
	"variant":[],
	"places":places_wild_earth+river_places+dry_places+humid_places+cold_places+high_places
},
"Ents":{
	"tag":[],
	"variant":[],
	"places": ["in the woods", "in the woods" ]
},
"Ghosts":{
	"tag": [ "airborne" ],
	"variant":[],
	"places": ["in an old mansion"]+dark_places
},
"Leprechauns":{
	"tag": ["group"],
	"variant":[],
	"places":places_wild_earth
},
"Giants":{
	"tag": ["group"],
	"variant":[],
	"places":places_wild_earth+high_places
},
"Genius":{
	"tag":[],
	"variant":[],
	"places":dry_places+ ["in the woods"]
},
"Gnomes":{
	"tag": ["group"],
	"variant":[],
	"places":dark_places+high_places
},
"Golem":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth+dark_places+high_places
},
"Ghouls":{
	"tag": [ "murderer" ],
	"variant":[],
	"places":dark_places+creepy_places
},
"Gorgonians":{
	"tag": [ "group", "murderer" ],
	"variant":[],
	"places":humid_places+humid_places
},
"Griffins":{
	"tag": ["group"],
	"variant":[],
	"places":high_places
},
"Harpies":{
	"tag": [ "group", "murderer", "airborne" ],
	"variant":[],
	"places":high_places
},
"Hobgoblins":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":places_wild_earth+ ["in the swamps"]
},
"Hydra":{
	"tag":[],
	"variant":[],
	"places": ["in forest"]
},
"Kraken":{
	"tag":[],
	"variant":[],
	"places":ocean_places
},
"Leprechauns":{
	"tag": ["group"],
	"variant":[],
	"places":places_wild_earth+dark_places
},
"Manticore":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth
},
"Minautore":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth+high_places
},
"Mummies":{
	"tag": ["group"],
	"variant":[],
	"places":dry_places+creepy_places
},
"Nymphs":{
	"tag":[],
	"variant":[],
	"places":ocean_places+river_places
},
"Ondines":{
	"tag": [ "sailor" ],
	"variant":[],
	"places":ocean_places
},
"Orcs":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":places_wild_earth+dark_places
},
"Ghosts":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":creepy_places
},
"Scorpions":{
	"tag":[],
	"variant":[],
	"places":dry_places
},
"Sirens":{
	"tag": ["group", "sailor"],
	"variant":[],
	"places":ocean_places
},
"Witch":{
	"tag":[],
	"variant":[],
	"places":creepy_places
},
"Spectres":{
	"tag":[],
	"variant":[],
	"places":creepy_places
},
"Sphinx":{
	"tag":[],
	"variant":[],
	"places":high_places
},
"Skeletons":{
	"tag": [ "murderer" ],
	"variant":[],
	"places":dark_places+creepy_places
},
"Titan":{
	"tag":[],
	"variant":[],
	"places":places_wild_earth+high_places
},
"Trolls":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":places_wild_earth+cold_places+humid_places+dark_places
},
"Vampires":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":dark_places+creepy_places
},
"Zombies":{
	"tag": ["group", "murderer"],
	"variant":[],
	"places":creepy_places
}
}



#HELPPHRASES
ask_help_examples=[
	"asks you for help.",
	"asks for the help of a brave warrior.",
	"asks for the help of a powerful mage.",
	"asks for help from an adventurer"
	]


def create_quest_infos(type_of_quest,tag,giver,objectif,places,nb="None"):
	"""Entries:
	type_of_quest (str): kill/collect/escort
	giver (str): name of the quest giver
	objective: name of the monster/object/plant/pnj to kill/harvest/help/tell
	places (str): name of the place to find monsters/objects to collect/pnj to discuss with
	nb (str): number of monsters/objects to kill/harvest is set to "None" by default and for escort type quests
	Exit:
	a list 
	[0] name (str): the name of the quest
	[1] description (str): description of the quest
	"""
	ask_help=choice(ask_help_examples)


	if type_of_quest=="kill":
		passive_animals=choice(bestiary_passif)
		#Quest names by type
		quete_name={
		"kill": [ "Extermination of the "+ objectif,"the end of the "+ objectif]
		}
		
		quests_kill={
		"carnivore": [
			[giver+" "+ask_help+" to hunt the "+objectif+" that decimates its "+passive_animals+". You will be able to find the "+objectif+" "+places+". Kill "+nb+" of them"],
			["Protect the "+passive_animals+" from "+objectif, "Revenge the "+passive_animals, "Revenge "+giver+"'s "+passive_animals, "Help "+giver]],
		"aggressive": [
			[giver+" ask protection against the "+objectif+" that rage "+places+". According to "+giver+" it would be necessary to kill "+nb+" to eliminate the threat.",giver+" "+ask_help+" to kill "+nb+" "+objectif+". After attacking "+giver+", the "+objectif+" fled "+places],
			["Protect "+giver,"to the help of "+giver,giver+"'s Fears" ]],
		"group": [
		["For several days now, "+nb+" "+objectif+" have been wandering around in groups "+places+". "+giver+" "+ask_help+" in order to eradicate the threat."],
		["Hunting "+objectif,"Pacification "+places,"Hunting "+places ]],
		"murderer": [
		[objectif+" was seen "+places+" slaughtering his friends. "+giver+" is asking you to revenge his friends."],
		[ "A debt of blood","The revenge of the" +giver, "The blood of the" +objectif]],
		"airborne":[
		["For several weeks now, about "+nb+" "+objectif+" have been flying over us at night, making all night activity impossible. "+giver+" needs help to make the area safer. He thinks that these monsters are "+nb+" during the daytime. "],
		["Dangerous Night", "Air Raids", "The Den of the "+ objectif]],
		"sailor": [
		[giver+" "+ask_help+" because a lot of our fishermen get trapped and killed by "+ask_help+". According to some, you can find them "+places],
		[ "Fishing!", "Revenge of the Sailors" ]],
		"water": [
		[],
		[]],
		"Kidnapper": [
		[],
		[]],
		"evil spell": [
		[],
		[]],
		"thief": [
		[],
		[]],
		"Scavengers": [
		[],
		[]],
		"Conspiracy": [
		[],
		[]],
		"invaders": [
		[],
		[]],
		"herbivore": [
		[],
		[]],
		"scary": [
		[],
		[]],

	}
	name = choice(quete_name[type_of_quest]+quests_kill[tag][1])
	description =choice(quests_kill[tag][0])

	return name, description
