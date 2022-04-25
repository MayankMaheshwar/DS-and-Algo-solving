class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        set_banned = set(banned)
        
        # paragraph lowercase and without punctuation symbols
        # replace it with white space
        para_lower = paragraph.lower()
        para_lower = re.sub(r"[!?',;.]+",' ',para_lower)
        #print(para_lower)
        
        # get the word list now by split method
        # from the word list, which occurs how much time
        # a dictionary, easy way is using a counter 
        word_list = para_lower.split()
        counter = Counter(word_list).most_common()
        # now return the first most common that is not in the
        # banned set
        for word,_ in counter:
            if word not in set_banned:
                result = word
                break
        return result