# String_Matching_Recommender_System

## Created by Antonio Natthan Krishna 13521162

This project is a simple recommender system prototype using string matching algorithm. I use Boyer-Moore string searching algorithm and Levenshtein string similarity algorithm to calculate match score. This program would recommend 10 products with highest match score from 100 products available. If you wish, you can modify purchased and search data in `src/data/purchased.txt` and `src/data/search.txt`

All codes are written in Python.

## **How to Run The Program**
Clone this repository </br>
```sh
git clone https://github.com/natthankrish/String_Matching_Recommender_System.git
```

Change the current directory into the cloned repository </br>
```sh
python -m src.main
```
or <br/>
```sh
python3 -m src.main
```

## **Data Format**
1. Product (in `src/data/purchased.txt` and `src/data/product.txt`)
```
<product name>_<product category>
```
2. Search History (`src/data/search.txt`)
```
<search content>
```
**WARNING** : Make sure to press enter in the end of data (.txt) file