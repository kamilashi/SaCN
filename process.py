import sys
import os
import json
import fDiscord
import data.locales as locales

save_path = "./data/save.json";
locale_path = "./data/locale.json";

enum_attributes = [];
enum_passwords = [];
enum_entry_text   = [];
enum_riddles = [];
enum_key_pieces = [];
stages = [];
locale = "";

class Stage:
    #static vars defined here
    next_stage = 0;

    def __init__(self, index):
        self.index = index;
        self.stage_name = enum_attributes[index];
        self.entry_password = enum_passwords[index];
        self.entry_text = enum_entry_text[index];
        self.reward_attribute = enum_attributes[index];
        self.reward_key_piece = enum_key_pieces[index];
        self.reward_riddle = enum_riddles[index];


class Actor:
    def __init__(self,stage, attributes_dict):
        self.next_stage = stage;
        self.attributes = attributes_dict;

def init():
    global locale
    locale = loadLocale();
    set_locale(locale);
    loadActor();
    actor_locale(locale) #add check!

def main(msg):
    print("debug info here\n");
    for i in range(0, len(stages)):
        if (msg.lower() == stages[i].entry_password.lower()):
            actor = loadActor();
            if(actor.next_stage==i): # should be the same as stages[i].index
                actor.attributes[stages[i].stage_name]+=1;
                actor.next_stage+=1;
                saveActor(actor);

                response = "\n" + \
                           fDiscord.bold(stages[i].entry_text) + "\n" + \
                           stages[i].reward_attribute + " +1 for your character.\n\n" +\
                           "You get a key piece:" + \
                           "\n" + stages[i].reward_key_piece + "\n" +\
                           "keep it safe!\n\n" + \
                           stages[i].reward_riddle;

                return(response);




    return "..."; #implement pick random idle line


if __name__ == "__main__":
    main(sys.argv[1]);


def saveActor(obj):
    json_object = json.dumps(obj.__dict__, indent=4)
    with open(save_path, "w+") as outfile:
        outfile.write(json_object)
    outfile.close();
    return;

def loadActor():
    if (os.path.exists(save_path)): #load if exists
        with open(save_path, 'r') as openfile:
            actor_dict = json.load(openfile);
        actor = Actor(actor_dict['next_stage'], actor_dict['attributes']);
        openfile.close();
    else: #create new if not
        actor = Actor(0, dict.fromkeys(enum_attributes, 0));
        saveActor(actor);
        return;
    return actor;

def initActor():    #only dev function, use carefully
    if(os.path.exists(save_path)):
        return;
    else:
        actor_default = Actor(0, dict.fromkeys(enum_attributes, 0));
        saveActor(actor_default);
        return;

def actorToString():
    if (os.path.exists(save_path)):
        actor = loadActor();
        string = fDiscord.bold("Character: Nuhrat");
        string += "\n" + str(actor.attributes);
        #print (str(actor.attributes)); # add only printing of arrtibutes != 0
        return string;

def gameToString():
    string = fDiscord.bold("enum_attributes: ");
    string += "\n" + str(enum_attributes);
    string += "\n" + "--" * 30+ "\n" ;
    string += fDiscord.bold("enum_passwords: ");
    string += "\n" + str(enum_passwords);
    string += "\n" + "--" * 30+ "\n" ;
    string += fDiscord.bold("enum_entry_text: ");
    string += "\n" + str(enum_entry_text);
    string += "\n" + "--" * 30+ "\n" ;
    string += fDiscord.bold("enum_riddles: ");
    string += "\n" + str(enum_riddles);
    string += "\n" + "--" * 30+ "\n" ;
    string += fDiscord.bold("enum_key_pieces: ");
    string += "\n" + str(enum_key_pieces);
    # string += "\n\n";
    # string += fDiscord.bold("stages: ");
    # string += "\n" + str(stages);

    return string;

def resetActor(): #only dev function, use carefully
    os.remove(save_path);

def loadLocale():
    if (os.path.exists(locale_path)): #load if exists
        with open(locale_path, 'r') as openfile:
            lang = json.load(openfile);
        openfile.close();
    else: #create new if not
        lang = "eng"; # default english
        json_object = json.dumps(lang);
        with open(locale_path, "w+") as outfile:
            outfile.write(json_object)
        outfile.close();
    return lang;


# game language switch, default is english
def set_locale(lang): # to-do: refactor to reload
    global locale
    global enum_attributes
    global enum_passwords
    global enum_entry_text
    global enum_riddles
    global enum_key_pieces
    if(lang == "eng"):
        enum_attributes = locales.eng.enum_attributes;
        enum_passwords = locales.eng.enum_passwords;
        enum_entry_text = locales.eng.enum_entry_text;
        enum_riddles = locales.eng.enum_riddles;
        enum_key_pieces = locales.eng.enum_key_pieces;
    elif(lang == "ru"):
        enum_attributes = locales.ru.enum_attributes;
        enum_passwords = locales.ru.enum_passwords;
        enum_entry_text = locales.ru.enum_entry_text;
        enum_riddles = locales.ru.enum_riddles;
        enum_key_pieces = locales.ru.enum_key_pieces;
    global stages
    stages = [];  # reset just in case
    for i in range(0, len(enum_attributes)):
        stage = Stage(i);
        stages.append(stage);
    locale = lang;  # save
    json_object = json.dumps(locale);
    with open(locale_path, "w+") as outfile:
        outfile.write(json_object)


# resave actor to new language
def actor_locale(lang):
    if (os.path.exists(save_path)):
        actor = loadActor();
        attributes_old = actor.attributes;
        actor.attributes = dict(zip(enum_attributes, attributes_old.values()));
        saveActor(actor);
    else:
        return;