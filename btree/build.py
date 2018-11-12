from btree import BTree
import csv

tree = BTree()
reader = csv.reader('../data/poke.csv', delimeter=',')

#build up the BTree
#Pull up data file and BTree.insert()
