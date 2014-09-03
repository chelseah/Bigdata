#get frequency count for different word length
DICT=/usr/share/dict/words
for i in {1..20}; 
do
  for x in {a..z} 
  do 
      echo -n $x' '$i' ' >> temp1.txt && grep '.\{'$i'\}' $DICT | grep $x -i -o | wc -l >> temp1.txt
  done
done
#sort temp.txt -k 2 -n | gawk '{print $1}'
