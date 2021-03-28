from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

def preprocess(sentence : str, stop_words=stop_words) -> str:
    sentence=str(sentence)
    sentence = sentence.lower()
    # remove non numeric and other tokens
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stop_words]
    return " ".join(filtered_words)