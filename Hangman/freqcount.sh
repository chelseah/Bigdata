#/usr/bin bash
#iterate from a to z, 
#count the number of frequencies a letter appears in the dictionary DICT
#attemped to get rid of those with caps but couldn't reproduce web result
DICT=/usr/share/dict/words
for x in {a..z} 
do 
    echo -n $x' ' >> temp.txt && grep -v '[^ ]*[A-Z][^ ]*' $DICT | grep $x -o | wc -l >> temp.txt 
done
sort temp.txt -k 2 -n | gawk '{print $1}'
