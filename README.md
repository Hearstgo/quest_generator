
# quest_generator
A quest generator made by Hearstgo<br>
I'm French (that explain english mistakes)<br>
coded in Python 3.8<br>
Go check it at https://trinket.io/python3/a580beb024<br>
yeah just click on the link

# How to use it if the version on the previous link is outdated ? 
There is 2 options to begin with :
If you want you can instal python 3.8 on your pc, then open quest_maker.py with the IDLE
OR
Go on this website : https://www.codabrainy.com/python-compiler/
then copy-paste the code of quest_maker in main.py
then upload the followings files :
- item_maker.py
- quest_data for french user
- quest_data_eng for english user
- tools.py
(you can upload both quest_data and quest_data_eng if you want to try the differents languages)

# quest_generator() tutorial

Now you are ready to use the fonction. You can find a test part at the bottom of the quest_maker script (main.py if you are on codabrainy). Don't forget to chose the good language in the test part if you only uploaded 1 quest_data.
It should look like that :

<code>

#--------------------------------------------------------------------------

#TEST----------------------------------------------------------------------

#--------------------------------------------------------------------------

#to generate a item randomly : generate_item()

ma_quete=generate_quest(giver="O'Conor",language="eng") #or language="fr"

ma_quete.info()

</code>


### Entry: 
(type of variable)[mendatory/optional/special]
ATTENTION special parameters are optional BUT if one of the special is modified, you need to modify also all the other [special]
or you won't have correlation between the name of the quest, the description and the objective

- giver (str)[mendatory] : Name of the pnj who give the quest.<br>
Exemple : giver = "Mr. Bean"<br><br>
- language (str)[optional] : The language used. it's english by default, can be switch to french.<br>
Exemple : language = "eng"/language = "fr"<br><br>
- lvl (int)[optional] : The level of the quest. Bewtween 1 and the level max.<br>
Exemple : lvl = 15<br><br>
- lvl_max (int)[optional] : The level max allowed. It's 30 by default.<br>
Exemple : lvl_max = 100<br><br>
- name (str)[special] : Name of the quest.<br>
Exemple : name = "Wolfs extermination"<br><br>
- description (str)[special] : Description of the quest<br>
Exemple : description = "You need to kill 10 wolfs who live in the forest."<br><br>
- reward (liste)[optional] : Reward of the quest, in first position it's the amout of money earned then the items. Important : the amont of money is a float with 4 decimals : 1.4586 means 1 gold coin 45 silver coins and 86 copper coins<br>
Exemple : reward=[1.4586,item1,item2,etc...] item1 and item2 are from the Item class<br><br>
- objectif (liste)[special] : Objectif of the quest, in first position, the name of the monster/object/plant/pnj to kill/harvest/help/tell,
	in second position the number to kill/collect or the position to reach.<br>
Exemple : objectif = ["Wolfs",10]<br><br>
- difficulty (str)[optional] : difficulty of the quest, bewteen "easy", "normal" and "hard"<br>
Exemple difficulty = "normal"<br><br>
- type_quest (str)[special] : the type of quest. Actually only "kill" is possible.<br>
Exemple : type_quest = "kill"<br><br>

### Output
- quest (Quest) The quest. you can do quest.info() to get the informations on a Quest variable

## Exemple :
<code>
  
ma_quete=generate_quest(giver="O'Conor",language="eng",
lvl=10,
lvl_max=30,
name="Wolfs extermination",
description="You need to kill 10 wolfs who live in the forest.",
reward=[1.4586,generate_item()],
objectif=["Wolfs",10],
difficulty="easy",
type_quest="kill")
  
ma_quete.info()

</code>

Here I used all parameters...but it's better to use less parameters to see the potential of this tools.

# How it works ?
the goal is to generate quests to bring variety to RPGs.
The principle of this generator is very simple, it generates quests in the following categories:
-hunting 
(collection or escort not yet developed.)

Among the quest categories, the generator uses "tags", each tag representing a sub-category of a quest, a kind of narrative line.
For example: for the "carnivore" tag, the quests will be of the type :

Name: Help The Farmer
Type: kill
difficulty: difficult
Level: 23
Description: The farmer asks for help from a brave warrior to hunt wolves that are decimating his cows.
You can find the wolves in the valley. Kill 25 of them.
Reward: ['11 gold 97 silver 73 copper ', 'Hat of Hestia']
status: 0/25

You just have to add in the quests_kill dictionary (in this example because we are talking about a hunting quest) other scenario possibilities.
The description of this example has been generated from the following paterns:
<code>description = giver+" "+ask_help+" to hunt the "+objective+" which decimates its "+animals_passive+". You will be able to find the "+objective+" "+place+". Kill "+nb</code>" of them.

You just have to add quest name or description paterns to the tags, or add tags to multiply the possibilities.

# item_maker
this file is used to generate items (weapons, armor or jewelry)

