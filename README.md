# quest_generator
A quest generator made by Hearstgo
I'm French (that explain english mistakes)
coded in Python 3.8

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
