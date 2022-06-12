# s = "applepenapple" 
# wordDict = ["apple","pen"]

# def check(i, word):
#     flag = False
#     global s, wordDict
#     if s.startswith(word,i):
#         flag = True

#     return flag


# def search_word(num_word, i):
#     global s, wordDict
#     for j in range(num_word, len(wordDict)):
#         if check(i,wordDict[j]):
#             search_word(j+1,i)
#             i += len(wordDict[j])
#             if i == len(s):
#                 return True
            
#             search_word(0, i)


# s = "catsandog" 
# wordDict = ["cats","dog","sand","and","cat"]

# wordDict.sort(reverse=True)

# print(wordDict)
# print(search_word(0,0))

from queue import Queue


s = "catsandog" 
wordDict = ["cats","dog","sand","and","cat","san"]

q = Queue()
q.put(s)
new_s = " "

while not q.empty():
    s1 = q.get()
    for word in wordDict:
        if s1.startswith(word):
            new_s = s1[len(word):]
            if new_s == "":
                break
            q.put(new_s)

    if new_s == "":
        print(True)
        break

if new_s != "":
    print(False)