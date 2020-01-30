import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer
#from nltk.corpus import stopwords
import re
import logging

class preprocessing:
    def __init__(self):
        #nltk.download('stopwords')
        logging.basicConfig(level=logging.INFO, format='%(filename)s %(levelname)s: %(asctime)s: %(message)s')
        self.logger = logging.getLogger('utils')
        self.stemer = PorterStemmer()
        self.tokenizer = TweetTokenizer()

        self.ENGLISH_STOP_WORDS=[
            "a", "about", "above", "across", "after", "afterwards", "again", "against",
            "all", "almost", "alone", "along", "already", "also", "although", "always",
            "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
            "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
            "around", "as", "at", "back", "be", "became", "because", "become",
            "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
            "below", "beside", "besides", "between", "beyond", "bill", "both",
            "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
            "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
            "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
            "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
            "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
            "find", "fire", "first", "five", "for", "former", "formerly", "forty",
            "found", "four", "from", "front", "full", "further", "get", "give", "go",
            "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
            "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
            "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
            "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
            "latterly", "least", "less", "ltd", "made", "many", "may", "me",
            "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
            "move", "much", "must", "my", "myself", "name", "namely", "neither",
            "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
            "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
            "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
            "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
            "please", "put", "rather", "re", "same", "see", "seem", "seemed",
            "seeming", "seems", "serious", "several", "she", "should", "show", "side",
            "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
            "something", "sometime", "sometimes", "somewhere", "still", "such",
            "system", "take", "ten", "than", "that", "the", "their", "them",
            "themselves", "then", "thence", "there", "thereafter", "thereby",
            "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
            "third", "this", "those", "though", "three", "through", "throughout",
            "thru", "thus", "to", "together", "too", "top", "toward", "towards",
            "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
            "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
            "whence", "whenever", "where", "whereafter", "whereas", "whereby",
            "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
            "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
            "within", "without", "would", "yet", "you", "your", "yours", "yourself",
            "yourselves"]

    def stem(self, tokens=''):
        return [self.stemer.stem(w) for w in tokens]

    def tokenize(self, text=''):
        return self.tokenizer.tokenize(text)

    def remove_stopwords(self, tokens=[]):
        #stop_words = set(stopwords.words('english'))
        return [w for w in tokens if not w in self.ENGLISH_STOP_WORDS]

    def remove_capitalization(self, tokens=[]):
        return [w.lower() for w in tokens]

    def remove_punctuation(self, text=''):
        return re.sub(r'[^\w\s]', '', text)
    
    def the_works(self, text=''):
        text = self.remove_punctuation(text=text)
        tokens = self.tokenize(text=text)
        tokens = self.stem(tokens=tokens)
        tokens = self.remove_stopwords(tokens=tokens)
        tokens = self.remove_capitalization(tokens=tokens)
        return tokens
