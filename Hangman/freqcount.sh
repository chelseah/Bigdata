
DICT=/usr/share/dict/words
for x in {a..z}; do echo -n $x' ' >> temp.txt && grep $x -i -o $DICT | wc -l >> temp.txt; done
sort temp.txt -k 2 -n | gawk '{print $1}'
