from ..struct.product import Product

# Reader for Product 
def readerProduct(path):
    f = open(path, "r")
    li = []
    for x in f:
        name = ""
        category = ""
        i = 0

        while (x[i] != "_"):
            name = name + x[i]
            i = i + 1

        i = i+1
        while (x[i] != "\n"):
            category = category + x[i]
            i = i + 1

        li.append(Product(name, category))
    f.close()
    return li

# Reader for Search History
def readerSearch(path):
    f = open(path, "r")
    li = []
    for x in f:
        li.append(x.splitlines()[0])
    f.close()
    return li


