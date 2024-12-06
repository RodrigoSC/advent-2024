#!/bin/sh

awk '{print substr($0,0,5);}' input.txt | sort > col1.txt
awk '{print substr($0,8,6);}' input.txt | sort > col2.txt

python3 distance.py
python3 similarity.py
