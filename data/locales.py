class eng:
    enum_attributes = ['insight', 'knowledge', 'adaptiveness', 'analysis', 'persistence', 'love', 'willpower'];
    enum_passwords = ['loremaster', 'word', 'kvint', 'moment', 'coffee', 'fate', 'yes'];
    enum_entry_text   = [
                    "ODESZA - Above The Middle __ hidden in plain sight (or not so much)" ,       #+  "+1 insight",
                    "The Beatles - Across the Universe"  ,            #+  "+1 knowledge",
                    "Stromae - ave cesaria",  #+  "+1 creativity",
                    "Kygo - Raging ft. Kodaline" ,            #+  "+1 analysis",
                    "Labrinth - The Producer",  # +  "+1 adaptiveness",
                    "SAINT MOTEL - My Type"   ,            #+  "+1 love",
                    "The Waterboys - The Whole of the Moon"   ,            #+  "+1 willpower"
                    ];
    enum_riddles = ["You can give it to me, but it's not a gift\n\
                    You have a way with it, I must admit\n\
                    It can be easy, it can be hard\n\
                    I'll cherish it, with all my heart\n\
                    It's like a spell, powerful sound\n\
                    When snowy mountains are around\n\
                    For some it's blue, for some it's red\n\
                    What is this thing, that you once said?",

                    "go to minecraft server  => get next password",
                    "solve a map  => get next password",
                    "book code most likely  => get next password",
                    "fate riddle => get next password",
                    "link to a google doc  => get next password",
                    "you got a vigenere key! now wait for what it unlocks"
                    ];
    enum_key_pieces = ['wh', 'ol', 'eo', 'ft', 'he', 'mo', 'on'];

class ru:
    enum_attributes = ['проницательность', 'опыт', 'адаптивность', 'анализ', 'упорство', 'любовь', 'сила воли'];
    enum_passwords = [['лормастер','loremaster'], ['слово','word'], ['квинт','kvint'], ['момент','moment','день','day'], ['кофе','coffee'], ['судьба','судьбу'], ['да','yes','да!','yes!','готов']];
    enum_entry_text = [
    "Приветствую, Путник, я ждал тебя!\n\
Я чувствую страсть к путешествиям в твоих глазах и мужество в твоем сердце. Я Мастер Щифров,\n\
добро пожаловать в мою обитель. Ты нашел меня, а значит тебе открыто то, что доступно только избранному.\n\
Проказница Судба решила сыграть с тобой в игру - в награду за победу, она покажет тебе \n\
твое счастливое будущее. Тебе предстоит пройти 7 испытаний, каждое из которых - это загадка, \n\
ответ на которую поможет продвинуться дальше. Я буду сопровождать тебя на протяжении всего пути, \n\
стоит тебе почувствовать себя в тупике - произнеси заклинание relay, и оно донесет все твои \n\
последующие слова прямиком до меня.\n\
Мы создадим историю, ни одна деталь которой не будет утеряна, она неподвластна времени\n\
и всегда будет ждать своих творцов чтобы продолжить с последней точки.\n\
Готов ли ты принять вызов? \n\n\
[Уровень 1 получен, Нухрат получает: +1 проницательность]\n\n\
Вот твоя первая загадка:\n\
",

    "\n\n[Уровень 2 получен, Нухрат получает: +1 знание]\n\n\
Так точно! Поздравляю, ты справился с первым испытанием. Однако, это было легко, \n\
не думаешь ли ты, что и остальные загадки будут столь простыми?\n\
Посмотрим, сможешь ли ты отгадать вот это:\n\
",
    "\n\n[Уровень 3 получен, Нухрат получает: +1 адаптивность]\n\n\
Ха-ха, я раскидал часть последней загадки там, где мало кто догадался бы смотреть, дав только\n\
небольшую подсказку в первых двух строках. Но ты нашел все остальные, и нашел ответ, это отличный знак!\n\
Но сможешь ли ты найти свою следующую загадку, которую в этот раз я спрятал целиком?\n\
",  # +  "+1 adaptiveness",

    "\n\n[Уровень 4 получен, Нухрат получает: +1 анализ]\n\n\
Браво, Путник! Испытания становились все сложнее, но ты верно шел вперед,\n\
несмотря ни на что. А что, если я скажу тебе, что свою следующую загадку,\n\
ты должен собрать не по строкам, а по словам?\n\
",  # +  "+1 analysis",

    "\n\n[Уровень 5 получен, Нухрат получает: +1 настойчивость]\n\n\
Я рад видеть тебя снова, Путник! последняя загадка была особенно запутанной, и я, признаться, начал \n\
было волноваться. Но ты в очередной раз доказал, что твоя смекалка вне всяких похвал, \n\
и в награду, пусть следующая загадка послужит для тебя передышкой:\n\
    ",  # +  "+1 persistence",

    "\n\n[Уровень 6 получен, Нухрат получает: +1 любовь :smirk: ]\n\n\
Что ж, не буду задерживать, ведь тебя уже ждут:\n\
",  # +  "+1 love",

    "\n\n[Уровень 7 получен, Нухрат получает: +1 сила воли]\n\n\
[Достиженние получено: He said yes!] \n\n\
Наш путь подходит к концу, о бравый Путник. Для меня было честью, сопровождать\n\
тебя в этом приключении, и пусть мы прощаемся сейчас - я знаю это приключение будет одним\n\
из многих которые еще ждут нас впереди. Однако, это еще не все; перед тем, как ты получишь \n\
свою награду, я с радостью окажу тебе последнюю услугу. Думаешь у тебя уже есть все, для того чтобы\n\
открыть последний сундук?\n\
",  # +  "+1 willpower"
    ];
    enum_riddles = ["Ты дашь мне это, я приму\n\
и буду дорожить всем сердцем.\n\
Когда кругом снега и горы\n\
Поможет выжить и согреться,\n\
Красиво, плавно и могуче,\n\
Рассеивает в небе тучи\n\
Порой легко, порой сложнее\n\
Нет ничего его милее",

                    "Обитель есть, друзей отважных\n\
Руками их сотворена...",

                    "Для этого, тебе понадобится заклинание magicmap и циркуль :wink:",

                    "11:173 35:410 16:216 6:140 35:54 37:30 14:220 107:440 \n\
40:399, but 61:171 61:172 9:86 31:26 \n\
100:25 countless 9:186 47:248 16:344 18:345 22:78\n\
6:126 22:111 16:228 9:1 107:423 100:40 \n\
If 9:33 11:182 47:232 it'd 37:68 72:303\n\
\"Hey 11:57 23:113 16:7 23:63 6:54 6:4 6:178\n\
11:31 23:111 it's 9:307 107:320 31:102 pays 100:240\n\
72:194 22:6 push 35:17 61:44 14:20 40:2 18:243\n\
31:21 100:132 6:132 35:55 72:69 27:382 27:23 27:54\n\
23:297`` 22:2 31:118 35:8 14:89 smell\"",

                    "Карты, кости, игры шанса \n\
У меня свои пасьянсы \n\
Я играю на возможность,\n\
на короткий срок свернуть, \n\
Но в конце, как ни старайся, \n\
Приведет ко мне твой путь. \n\
Деспотична, хаотична,\n\
Я тебя везде найду, \n\
Как бы сильно ни пытался, \n\
Изменить свою ... :stuck_out_tongue_winking_eye:",

                    "https://drive.google.com/file/d/1CyUSBpO0okbYH5F8eGzKNhaHDCdxCLdI/view?usp=share_link",

                    "Твоя награда ждет тебя по адресу helploremaster@gmail.com!\n\
https://accounts.google.com/v3/signin/challenge/pwd?TL=AG7eRGAXyA_HWBaEgoQckjJU-ewYcwFLUW-cQAVZgDwUmStq7C3nP-mkDrXdG0m-&checkConnection=youtube%3A110%3A0&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fmail.google.com&dsh=S-1124009534%3A1682443995667237&flowEntry=AddSession&flowName=GlifWebSignIn&hl=en&pstMsg=1&service=mail&authuser=4" # vigenere hint?
                    ];
    enum_key_pieces = ['p', 'i', 'ec', 'eo', 'fc', 'a', 'ke'];


# Chapter names:
# audeamus - let us dare
# in verbo tuo	- at your word
# calamus gladio fortior	- The pen is mightier than the sword
# carpe diem - seize the day
# ?? per aspera ad astra - through hardships to the stars
# amor fati - love of fate
# cras es noster	- Tomorrow, be ours

# per angusta ad augusta	- through difficulties to greatness
# per aspera ad astra	through hardships to the stars
# ars celare artem - art [is] to conceal art
# ars longa, vita brevis	- art is long, life is short ***
# emeritus	veteran
# ex silentio - from knowledge


# dulce et utile	- a sweet and useful thing / pleasant and profitable	Horace, Ars Poetica: poetry must be dulce et utile, i.e., both enjoyable and instructive.
# tempus fugit -	Time flees.
# tempus rerum imperator	- time, commander of all things
# clavis aurea	golden key

# vero possumus	- yes, we can ***

# facta, non verba	- deeds, not words
# finis coronat opus -	the end crowns the work
# gratia et scientia -	grace and learning
# fortes fortuna adiuvat -	Fortune favors the brave or Fortune favors the strong
# fortes fortuna iuvat	Fortune favors the brave
# grandescunt aucta labore	- By hard work, all things increase and grow
# haec olim meminisse iuvabit	- one day, this will be pleasing to remember
# hic sunt dracones	- here there are dragons
# palma non sine pulvere	no reward without effort
# paulatim sed firmiter	slowly but surely
# tendit in ardua virtus	- virtue strives for what is difficult ***
#

# TO-DO: