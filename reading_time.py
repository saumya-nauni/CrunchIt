import spacy 
nlp = spacy.load("en_core_web_sm")
def readingTime(mytext):
	total_words = len([ token.text for token in nlp(mytext)])
	estimatedTime = total_words/250.0
	return estimatedTime