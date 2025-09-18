class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if len(words) == 0:
            return "#"

        newWords = list(map(lambda x: x.capitalize(), words))
        
        newWords[0] = newWords[0].lower() 
        
        tag = "#" + "".join(newWords)

        return tag if len(tag) < 100 else tag[:100]