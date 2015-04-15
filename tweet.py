#-*-encoding: utf-8 -*-

import nltk

def etiquetados(lista, clase):
    """TODO: Docstring for etiquetados.

    :lista: TODO
    :clase: TODO
    :returns: TODO

    """
    for tweet in lista:
        yield (tweet.strip(), clase)


def ngramas(iterable, n=3):
    """TODO: Docstring for ngramas.

    :iterable: TODO
    :n: TODO
    :returns: TODO

    """
    i = 0
    while i <= len(iterable) - n:
        yield iterable[i: i + n]
        i += 1


# def extract_features(document):
#     document_words = set(document[0])
# 
#     features = {}
#     for word in document[1]:
#         features['contiene(%s)' % word] = word in document_words
# #    for word in word_features:
# #        features['contiene(%s)' % word] = (word in document_words)
# 
#     return features

with open("positivos.txt","r") as pos:
    pos_tweets = [tweet for tweet in etiquetados(pos, "positivo")]

with open("negativos.txt","r") as neg:
    neg_tweets = [tweet for tweet in etiquetados(neg, "negativo")]

tweets = []
for tweet, clas in pos_tweets + neg_tweets:
    tweet_segmentado = [ngram.lower() for ngram in ngramas(tweet)]
    tweets.append((tweet_segmentado, clas))

word_f = []
for ngram, clas in tweets:
    word_f.extend(ngram)

word_features = nltk.FreqDist(w for w in word_f).keys()
def extract_features(document):
    document_words = set(document)

    features = {}
#     for word in document[1]:
#         features['contiene(%s)' % word] = word in document_words
    for word in word_features:
        features['contiene(%s)' % word] = (word in document_words)

    return features

print(tweets[:2])
featuresets = [(extract_features(t), c) for t,c in tweets[:50]]
training_set = nltk.classify.apply_features(extract_features, featuresets)
x = training_set.count(True)
print(x); quit()

classifier = nltk.NaiveBayesClassifier.train(training_set)

print classifier.show_most_informative_features(10)
while True:
    tweet = raw_input('entra tweet: ')
    print tweet
    tweet = [e.lower() for e in trigramas(tweet) if len(e) >= 1]
    #print tweet
    print classifier.classify(extract_features(tweet))

