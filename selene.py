import nltk 
from nltk.tokenize import word_tokenize

class Cogw(object):
    
    def __init__(self, dataFrame):
        
        self.df = dataFrame
        self.unique = []
        self.apperances = []
        self.wordsDict = {}

    def setUniqueWords(self):
        
        phrases = list(self.df['Phrase'])
        
        for i in range(len(phrases)):
            word_tokens = word_tokenize(phrases[i])
            for w in word_tokens:
                flag = 0
                for l in w:
                    if (l.isdigit()) or (l == '.') or (w[0] == '-'):
                        flag = 1
                if (w not in self.unique) and (len(w) > 2) and (not w.isdigit()) and (not flag):
                    self.unique.append(w)
                    
        print("There are {} unique words in this data.".format(len(self.unique)))

    def setApperances(self):
        
        phrases = list(self.df['Phrase'])
        
        for word in self.unique:
            currWord = word
            counter = 0
            for i in range(len(phrases)):
                counter += phrases[i].count(currWord)
            self.apperances.append(counter)
            
        max_app = max(self.apperances)
        max_ind = self.apperances.index(max_app)
        
        print("The word with the most apperances is {} with {} "
              "apperances.".format(self.unique[max_ind], max_app))

    def setWordsDict(self):
        
        index = 0
        for word in self.unique:
            self.wordsDict[word] = self.apperances[index]
            index += 1
            
        print("Here is all the unique words and their number of occurances:")
        
        for key, value in self.wordsDict.items():
            print(key, ": ", value)

    def extractUniqueWords(self):
        
        self.setUniqueWords()
        self.setApperances()
        self.setWordsDict()