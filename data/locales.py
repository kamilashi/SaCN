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
    #enum_passwords = ['лормастер', 'слово', 'квинт', 'момент', 'кофе', 'судьба', 'да'];
    enum_passwords = [['лормастер','loremaster'], ['слово','word'], ['квинт','kvint'], ['момент','moment'], ['кофе','coffee'], ['судьба','судьбу'], ['да','yes']];
    enum_entry_text = [
    "Приветствую, Путник, я ждал тебя!\n\
Я чувствую страсть к путешествиям в твоих глазах и мужество в твоем сердце. Я Мастер Щифров,\n\
добро пожаловать в мою обитель. Ты нашел меня, а значит тебе открыто то, что доступно только избранному.\n\
Проказница Судба решила сыграть с тобой в игру - в награду за победу, она покажет тебе \n\
твое счастливое будущее. Тебе предстоит пройти 7 испытаний, каждое из которых - это загадка, \n\
ответ на которую поможет продвинуться дальше. Я буду сопровождать тебя на протяжении всего пути, \n\
стоит тебе почувствовать себя в тупике - ты всегда найдешь помощь по адресу helploremaster@gmail.com.\n\
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
Наш путь подошел к концу, о бравый Путник. Для меня было честью, сопровождать\n\
тебя в этом приключении, и пусть мы прощаемся сейчас - я знаю это одно из многих которые еще\n\
с нетерпением ждут нас впереди. Но перед тем, как ты получишь свою награду, я\n\
с радостью окажу тебе последнюю услугу. Думаешь у тебя есть все, для того чтобы\n\
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
                    
                    "Для этого, тебе понадобится заклинание \"magicmap\" и циркуль :wink:",

                    "It knows when you stay up all night, \n\
Time pressured while the stakes are high \n\
The countless times it's seen you tired\n\
Eyes half-asleep, your drive expired \n\
If it could talk, it'd likely say\n\
\"Hey friend, I'm with you, all the way\n\
I know it's hard but it pays back\n\
If you push on and stay on track\n\
But while you're here you might as well\n\
Enjoy my taste and pleasant smell\"",

                    "Карты, кости, игры шанса \n\
У меня свои пасьянсы \n\
Я играю на возможность,\n\
на короткий срок свернуть, \n\
Но в конце, как ни старайся, \n\
Приведет ко мне твой путь. \n\
Деспотична, хаотична,\n\
Я тебя везде найду, \n\
Как бы сильно ни пытался, \n\
Изменить свою ...",

                    "https://docs.google.com/presentation/d/11T3BM4vjDc104epOwh_JXwTCBAACQbF-sMmpuco5dyE/edit?usp=sharing",

                    "Твоя награда ждет тебя!\n\
https://accounts.google.com/v3/signin/challenge/pwd?TL=AG7eRGAXyA_HWBaEgoQckjJU-ewYcwFLUW-cQAVZgDwUmStq7C3nP-mkDrXdG0m-&checkConnection=youtube%3A110%3A0&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fmail.google.com&dsh=S-1124009534%3A1682443995667237&flowEntry=AddSession&flowName=GlifWebSignIn&hl=en&pstMsg=1&service=mail&authuser=4" # vigenere hint?
                    ];
    enum_key_pieces = ['wh', 'ol', 'eo', 'ft', 'he', 'mo', 'on'];


# Notes in the sketchbook:
# sketch of the target location in minecraft
# Momento di restaurant in Hamburg hint in sketchbook
# MOMENTUM Deichstraße 41, 20459 Hamburg
# command for the song check-in
# password protected folder

# amor fati - love of fate ***
# ars celare artem - art [is] to conceal art
# ars longa, vita brevis	- art is long, life is short ***
# audeamus - let us dare ***
# carpe diem ***
# cras es noster	Tomorrow, be ours
# dulce et utile	a sweet and useful thing / pleasant and profitable	Horace, Ars Poetica: poetry must be dulce et utile, i.e., both enjoyable and instructive.
# tempus fugit	Time flees.
# tempus rerum imperator	time, commander of all things
# clavis aurea	golden key
# tendit in ardua virtus	- virtue strives for what is difficult ***
# vero possumus	- yes, we can ***
# in verbo tuo	at your word ***
# facta, non verba	- deeds, not words
# finis coronat opus -	the end crowns the work
# gratia et scientia -	grace and learning

# TO-DO: