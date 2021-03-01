import math
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def find_nearest_pair(data):
    data = np.array(data)
    N = len(data)
    dist = np.empty((N, N)) # Default is numpy.float64.
    for i in range(N):
        for j in range(N):
            g = sum([np.abs(data[i][a] - data[j][a]) for a in range(len(data[i]))])
            dist[i][j] = g if g > 0 else np.inf
    print(np.unravel_index(np.argmin(dist), dist.shape))

def main(text):
    tf,df,tfidf = {},{},[] #Term frequency, Document frequency, Term frequency inverse document frequency
    docs = [line.lower().split() for line in text.split('\n')]
    words = set(text.lower().split()) 
    for w in words:
        tf[w] = [d.count(w)/len(d) for d in docs]
        df[w] = sum([d.count(w) for d in docs])/len(docs)
    for i in range(len(docs)):
        tfidf.append([tf[word][i] * math.log(1/df[word],10) for word in words]) 
    find_nearest_pair(tfidf)

main(text)