from .utils.reader import readerProduct, readerSearch
from .utils.recommend import *

products = readerProduct("src/data/product.txt")
purchased = readerProduct("src/data/purchased.txt")
search = readerSearch("src/data/search.txt")

processRecommend(products, search, purchased)
recommend = recommendProduct(products)

print("RECOMMENDED PRODUCT")
for item in recommend:
    item.info()