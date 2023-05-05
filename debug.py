debug_pages_path = "./debug/raw/"
clean_pages_path = "./debug/clean/"

orig_riddle = "It knows when you stay up all night\n\
Exhausted when the stakes are high\n\
The countless times it's seen you tired\n\
Eyes half asleep your drive expired\n\
If it could talk it'd likely say\n\
Hey friend I'm with you, all the way\n\
I know it's hard but it pays back\n\
If you push on and stay on track\n\
But while you're here you might as well\n\
Enjoy my taste and pleasant smell"

riddleCiphered =   "11:173 35:410 16:213 6:138 35:54 37:30 14:215 107:437 \n\
40:362 61:115 61:169 61:170 9:86 31:26 \n\
100:25 countless 9:182 47:242 16:344 18:342 22:77\n\
6:331 18:102 16:225, 9:151 107:420 100:39 \n\
22:452 9:59 11:178 47:227, it'd 37:68 72:303\n\
\"Hey 11:56, 23:113 16:7 23:63, 6:53 6:97 6:117\n\
11:32 23:111 it's 9:304 107:320 31:102 72:163''''' 100:240\n\
72:337 22:6 push 35:236 61:44 14:21 40:2 18:241\n\
31:21 100:132 6:132 35:55 72:69 27:382 27:383 27:384\n\
23:297`` 22:2 31:115 35:8 14:88 smell\""

def analyzeRiddleText():
    pages = []
    #words = locales.ru.enum_riddles[3].split();
    words = riddleCiphered.split();
    #print(words)
    for word in words:
        try:
            pages.append(int(word.split(":")[0]))
        except ValueError:
            pass

    #pageNos = list(map(int, locales.eng.enum_riddles[3].split(" ").split(":")[0]));
    #print(pages)
    returMessage = "All page numbers: \n"
    returMessage += str(pages) + "\n\n"
    returMessage += "Unique page numbers:\n"
    pageSet = set(pages)
    returMessage += str(len(pageSet)) + "\n\n"
    for uniquePage in pageSet:
        count = 0;
        for page in pages:
            if int(page) == int(uniquePage):
                count +=1
        returMessage += "page #: " + str(uniquePage) + ", count: "+ str(count) + "\n"
    print(returMessage)
    return( returMessage )


def getWord(pageNo):
    words = riddleCiphered.split();
    orig_riddle_words = orig_riddle.split();
    wordsOnPage = []
    wordNos=[]
    i = 0
    for word in words:
        try:
            page = (int(word.split(":")[0]))
            wordNumber = (int(word.split(":")[1]))
            if page == pageNo:
                wordsOnPage.append(orig_riddle_words[i])
                wordNos.append(wordNumber)
        except ValueError:
            pass
        i += 1
    print(str(pageNo) + " : " + str(wordsOnPage) + " , under numbers " + str(wordNos))


def getPage(wordSearched):
    pages = []
    words = riddleCiphered.split();
    wordNos=[]
    orig_riddle_words = orig_riddle.split();
    pagesForWord = []

    # for word in words:
    #     try:
    #         pages.append(int(word.split(":")[0]))
    #     except ValueError:
    #         pass

    i = 0
    for word in orig_riddle_words:
        if word.lower() == wordSearched.lower():
            try:
                pagesForWord.append(int(words[i].split(":")[0]))
                wordNos.append(int(words[i].split(":")[1]))
            except ValueError:
                pass
        i += 1
    print(wordSearched + " : on pages " + str(pagesForWord) + " , under numbers " + str(wordNos))


def mapWords():
    words = riddleCiphered.split();
    orig_riddle_words_lines = orig_riddle.splitlines();

    i = 0
    for line in orig_riddle_words_lines:
        orig_words = line.split()
        for word in orig_words:
            try:
                page_and_number = words[i].split(":")
                i += 1
                if len (page_and_number) > 1:
                    print(word  + "("  + str(page_and_number[0]) + ":" + str(page_and_number[1]) + ")   ", end=" ")
                else:
                    print(word + "   ", end=" ")
            except ValueError:
                i += 1

        print("\n")

pagesOnDrive = {}

import os
def createArrays():
    global debug_pages_path
    global pagesOnDrive
    keys = []
    values = []
    tupleList = []

    for filename in os.listdir(debug_pages_path):
        #f = os.path.join(debug_pages_path, filename)
        # checking if it is a file
        #if os.path.isfile(f):
        wordsOnPage = []
        #print(filename)
        with open((debug_pages_path) + str(filename)) as file:
            for line in file:
                wordsOnLine = line.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ").replace("—"," ").replace("-"," ").replace("\""," ").split();
                for word in wordsOnLine:
                    wordsOnPage.append(word)
        file.close()
        mapped = []
        #outfile here
        with open(clean_pages_path + str(filename.split(".")[0]) + ".doc", "w+") as outfile:
            #wordNumbers = list(range(1,len(wordsOnPage)))
            wordNo = 1
            for word in wordsOnPage:
                mapped.append((word, wordNo))
                wordNo+=1

            outfile.write(str(mapped))
        outfile.close();
        tupleList.append([filename.split(".")[0], wordsOnPage])

    #print(list)
    pagesOnDrive = dict(tupleList);

def findWord(newWord):
    global pagesOnDrive
    wordNos = []
    print("searching " + newWord)
    for key in pagesOnDrive:

        i = 0
        wordsOnPage = list(pagesOnDrive.get(key))
        for word in wordsOnPage:
            i += 1;
            if newWord.lower() == word.lower():
                wordNos.append([str(i), str(key)]);

    for number_page in wordNos:
        print("found # " + number_page[0] + " on page " + number_page[1])


analyzeRiddleText()
getWord(79) #change or target
getWord(40) #target
getWord(31) #taste
getWord(67) #one word but at top
getWord(100) #target
getWord(107) #target
getWord(109) #target
getWord(18) #target
getWord(6) #
getWord(72) #
getWord(9) #
# (23) #target
# 35 target
#18 target
#72) #target

getPage("and")


half = 7
createArrays()
#print(len(pagesOnDrive))
#findWord("it'd")


def check():
    wordlines = riddleCiphered.replace(",", "").replace("'", "").replace(".", "").splitlines();

    i = 0
    for line in wordlines:
        words = line.split()
        for word in words:
            try:
                page_and_number = word.split(":")
                i += 1
                if len(page_and_number) > 1:
                    pageNo = page_and_number[0]
                    wordNo = int(page_and_number[1])-1
                    print(str(pagesOnDrive.get(pageNo)[wordNo]) + " ", end=" ")
                else:
                    print(" [" + page_and_number[0] + "] ", end=" ")
            except ValueError:
                i += 1

        print("\n")
#map()
check()
