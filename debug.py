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

riddleCiphered =   "11:173 35:410 16:216 6:140 35:54 37:30 14:220 107:440 \n\
40:399 61:115 61:171 61:172 9:86 31:26 \n\
100:25 countless 9:186 47:248 16:344 18:345 22:78\n\
6:126 22:111 16:228 9:1 107:423 100:40 \n\
22:136 9:33 11:182 47:232 it'd 37:68 72:303\n\
\"Hey 11:57 23:113 16:7 23:63 6:54 6:4 6:178\n\
11:31 23:111 it's 9:307 107:320 31:102 72:163''''' 100:240\n\
72:194 22:6 push 35:17 61:44 14:20 40:2 18:243\n\
31:21 100:132 6:132 35:55 72:69 27:382 27:23 27:54\n\
23:297`` 22:2 31:118 35:8 14:89 smell\""

adjusted_riddle = ""

def analyzeRiddleText():
    pages = []
    words = riddleCiphered.split();
    for word in words:
        try:
            pages.append(int(word.split(":")[0]))
        except ValueError:
            pass

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


def getWord(pageNo, wordNo=-1):
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
                if {wordNo > 0 and wordNo == wordNumber} or wordNo < 0 :
                    wordsOnPage.append(orig_riddle_words[i])
                    wordNos.append(wordNumber)
                    return str(orig_riddle_words[i])
        except ValueError:
            pass


        i += 1
    print(str(pageNo) + " : " + str(wordsOnPage) + " , under numbers " + str(wordNos))
    return str(wordsOnPage)


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
    return[pagesForWord, wordNos]


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
                wordNos.append([ str(key), str(i)]);

    for page_number in wordNos:
        print("found on page " + page_number[0] + " # "+ page_number[1] )

    return wordNos


analyzeRiddleText()
# getWord(79) #change or target
# getWord(40) #target
# getWord(31) #taste
# getWord(67) #one word but at top
# getWord(100) #target
# getWord(107) #target
# getWord(109) #target
# getWord(18) #target
# getWord(6) #
# getWord(72) #
# getWord(9) #
# (23) #target
# 35 target
#18 target
#72) #target

# getPage("and")


createArrays()
#print(len(pagesOnDrive))



def check():
    wordlines = riddleCiphered.replace(",", "").replace(".", "").splitlines();
    wordsSet = set(riddleCiphered.replace(",", "").replace(".", "").split());
    i = 0
    for line in wordlines:
        words = line.split()
        for word in words:
            try:
                page_and_number = word.split(":")
                i += 1
                if len(page_and_number) > 1:
                    pageNo = page_and_number[0]
                    wordNo = int(page_and_number[1])-1 #convert to index
                    print(str(pagesOnDrive.get(pageNo)[wordNo]) + " ", end=" ")
                else:
                    print(" [" + page_and_number[0] + "] ", end=" ")
            except ValueError:
                i += 1
        print("\n")
    print("\n words: " + str(len(riddleCiphered.replace(",", "").replace(".", "").split())))
    print("\n unique words: " + str(len(wordsSet)))

def adjust():
    global adjusted_riddle
    wordlines = orig_riddle.replace(",", "").replace(".", "").splitlines();
    ciphered_words = riddleCiphered.replace(",", "").replace(".", "").split();
    pageNos = []
    for c_word in ciphered_words:
        pageNos.append(c_word.split(":")[0])

    i = 0
    for line in wordlines:
        words = line.split()
        for word in words:
            wordReference = word
            pageNo = pageNos[i]
            i+=1
            #print(wordReference + " at " + str(pageNo) + ":" + str(wordNo+1))
            foundNewWord = False
            foundWordsPage_No = findWord(wordReference)
            for wordCandidatePage_No in foundWordsPage_No:
                if wordCandidatePage_No[0] == pageNo:
                    adjusted_riddle += str(pageNo) + ":" + str(wordCandidatePage_No[1]) + " "
                    foundNewWord = True
                    break
            if not foundNewWord:
                adjusted_riddle += " [" + str(pageNo) + ":" + str(-000) + "] "

        adjusted_riddle += "\n"

def adjust2():
    global adjusted_riddle
    rangeCount = 15
    wordlines = riddleCiphered.replace(",", "").replace(".", "").splitlines();
    i = 0
    for line in wordlines:
        words = line.split()
        for word in words:
            try:
                page_and_number = word.split(":")
                i += 1
                if len(page_and_number) > 1:
                    pageNo = page_and_number[0]
                    wordNo = int(page_and_number[1]) - 1
                    wordReference = getWord(int(pageNo), wordNo+1)
                    #print(wordReference + " at " + str(pageNo) + ":" + str(wordNo+1))
                    foundNewWord = False
                    for j in range(max(wordNo-rangeCount,0), min(wordNo+rangeCount, len(pagesOnDrive.get(pageNo))-1)):
                        wordCandidateIndex = j
                        if(str(pagesOnDrive.get(pageNo)[wordCandidateIndex]).lower() == wordReference.lower()):
                            # if found first occurrence:
                            adjusted_riddle += str(pageNo) + ":" + str(wordCandidateIndex + 1) + " "
                            foundNewWord = True
                            break
                    if not foundNewWord:
                        adjusted_riddle += str(pageNo) + ":" + str(-000) + " "
                else:
                    adjusted_riddle += " [" + page_and_number[0] + "] "
            except ValueError:
                i += 1

        adjusted_riddle += "\n"
#map()

#getWord(11,173)
#adjust()
print(adjusted_riddle)
check()
findWord("If")