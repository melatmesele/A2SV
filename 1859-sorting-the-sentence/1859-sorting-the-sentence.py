class Solution:
    def sortSentence(self, s: str) -> str:
        
        # [1] split into words
        spl = s.split(" ")
        
        # [2] sort by last symbol (i.e., word number)
        srt = sorted(spl, key=lambda w: w[-1])
        
        # [3] extract a word (i.e., remove word number)
        wrd = [w[:-1] for w in srt]
        
        # [4] join words into a sentence
        return " ".join(wrd)
        