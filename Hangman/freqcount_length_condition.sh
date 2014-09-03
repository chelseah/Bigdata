#!/usr/bin bash
DICT=/usr/share/dict/words
tempsave=temp2.txt
#for i in {1..20} 
for i in {1..20} 
do
  if [ -e $tempsave ]; then
    rm $tempsave
  fi
  for x in {a..z} 
  do 
      echo -n $x' '$i' ' >> $tempsave && grep '.\{'$i'\}' $DICT | grep $x -i -o | wc -l >> $tempsave
  done
  FIRST_CALL=$(sort $tempsave -k 3 -n -r | head -n 1 | cut -d ' ' -f 1)
  
  if [ -e $tempsave ]; then
    rm $tempsave
  fi
  for x in {a..z} 
  do 
      echo -n $x' '$i' ' >> $tempsave && grep '.\{'$i'\}' $DICT | grep -i -v $FIRST_CALL | grep $x -i -o | wc -l >> $tempsave
  done

  SECOND_CALL=$(sort $tempsave -k 3 -n -r | head -n 1 | cut -d ' ' -f 1)
  echo $FIRST_CALL,$SECOND_CALL
done
#sort temp.txt -k 2 -n | gawk '{print $1}'
