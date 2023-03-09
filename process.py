import sys
import os
import json
import fDiscord

enum_attributes = ['insight', 'persistence', 'adaptiveness', 'analysis', 'knowledge', 'love', 'willpower'];
enum_passwords = ['loremaster', 'songs', 'minecraft', 'map', 'english', 'fate', 'yes'];
enum_entry_text   = [
                "You found a secret!" ,       #+  "+1 insight",
                "You are quite persistent!" , #+  "+1 persistence",
                "Adapt, Survive, Overcome!",  #+  "+1 adaptiveness",
                "That's smart!"  ,            #+  "+1 analysis",
                "Habla Inglesa"  ,            #+  "+1 knowledge",
                "*lenny face*"   ,            #+  "+1 love",
                "He said yes!"   ,            #+  "+1 willpower"
                ];

enum_riddles = ["now go listen to 1000 songs => get next password",
                "go to minecraft server  => get next password",
                "solve a map  => get next password",
                "book code most likely  => get next password",
                "love riddle? => get next password",
                "link to a google doc  => get next password",
                "you got a vigenere key! now wait for what it unlocks"
                ];
enum_key_pieces = ['I', 'a', 'm', 'k', 'e', 'y', '_'];



class Stage:
    #static vars defined here
    next_stage = 0;

    def __init__(self, index):
        self.index = index;
        self.stage_name = enum_attributes[index];
        self.entry_password = enum_passwords[index];
        self.entry_text = enum_entry_text[index];
        self.reward_attribute = enum_attributes[index];
        self.reward_key_piece = "to be implemented";
        self.reward_riddle = enum_riddles[index];


class Actor:
    def __init__(self,stage, attributes_dict):
        self.next_stage = stage;
        self.attributes = attributes_dict;

save_path = "./data/save.json";

stages = [];
for i in range(0, len(enum_attributes)):
    stage = Stage(i);
    stages.append(stage);

# dev stuff
class Command:
    def __init__(self, name, functiion):
        self.name = name;
        self.function = functiion;

def main(msg):
    print("debug info here\n");
    for i in range(0, len(stages)):
        if (msg.casefold() == stages[i].entry_password.casefold()):
            with open(save_path, 'r') as openfile:
                actor_dict = json.load(openfile);
            actor = Actor(actor_dict['next_stage'], actor_dict['attributes']);
            actor.attributes[stages[i].stage_name]+=1;
            save(actor);

            response = "\n" + \
                       fDiscord.bold(stages[i].entry_text) + "\n" + \
                       stages[i].reward_attribute + " +1 for your character.\n\n" +\
                       "You get a key piece:" + \
                       "\n" + enum_key_pieces[i] + "\n" +\
                       "keep it safe!\n\n" + \
                       stages[i].reward_riddle;

            print(actor.__dict__);
            return(response);


        

    return "..."; #implement pick random idle line


if __name__ == "__main__":
    main(sys.argv[1]);


def save(obj):
    json_object = json.dumps(obj.__dict__, indent=4)
    with open(save_path, "w+") as outfile:
        outfile.write(json_object)
    return;

def init():
    if(os.path.exists(save_path)):
        return;
    else:
        actor_default = Actor(0, dict.fromkeys(enum_attributes, 0));
        save(actor_default);
        return;

def reset():
    os.remove(save_path);