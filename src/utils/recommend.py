from ..struct.product import Product
from .distance import distance
from .search import search

def evaluateData(text, pattern):
    val = 0
    if (search(text, pattern) != -1):
        val = val + 1
    similarity = distance(text, pattern)
    if (len(text) > len(pattern)):
        val = val + (len(text) - similarity) / len(text)
    else: 
        val = val + (len(pattern) - similarity) / len(pattern)
    return val


def processRecommend(products, search, purchased):
    for x in products:
        newmatch = 0
        for y in search:
            newmatch += evaluateData(y, x.getName())
            newmatch += evaluateData(y, x.getCategory())
    
        for y in purchased:
            newmatch += evaluateData(y.getName(), x.getName())
            newmatch += evaluateData(y.getCategory(), x.getCategory())

        x.updateMatch(newmatch)

def recommendProduct(products):
    recommend = sorted(products, key=lambda x: x.getMatch(), reverse=True)
    recommend = recommend[:10]
    return recommend
