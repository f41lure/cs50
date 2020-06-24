import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        self.positives_list = []
        f = open(positives, "r")
        for line in file:
            if line.startswith(';') == False:
                self.positives_list.append(line.rstrip("\n"))
        f.close()
        
        self.negatives_list = []
        f = open(negatives, "r")
        for line in file:
            if line.startswith(';') == False:
                self.negatives_list.append(line.rstrip("\n"))
        file.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        sum = 0
        for word in tokens:
            if word.lower() in self.positives_set:
                sum += 1
            elif word.lower() in self.negatives_set:
                sum -= 1
            else:
                continue
        
        return sum