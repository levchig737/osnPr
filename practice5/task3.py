from queue import Queue

def is_proiz(wordDict, s):
    q = Queue()
    q.put(s)
    new_s = " "

    # Пока в стеке есть строки
    while not q.empty():
        s1 = q.get()
        for word in wordDict:
            if s1.startswith(word):
                new_s = s1[len(word):]  # Обрезаем слово от строки
                if new_s == "":
                    return True
                q.put(new_s)            # Кладем обрезанную строку в стек

    if new_s != "":
        return False


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = []

for word in range(len(words)):
    wordDict = words.copy()
    wordDict.pop(word)
    if is_proiz(wordDict, words[word]):
        res.append(words[word])
print(res)