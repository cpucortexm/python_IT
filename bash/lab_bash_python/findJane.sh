
#!/bin/bash
> oldFiles.txt   # create a new file called oldFiles.txt. This file will be the input for the python script

# collect files which have only 'jane' as part of their name. Other files will be excluded and -f 3 is used as field=3 for file names in the list.txt
files=$(grep ' jane ' ../data/list.txt | cut -d ' ' -f 3)   

for file in $files
 do
   echo $file
   if test -e ~/$file # check if the file actually exists in the location
   then
      echo "File exists"
      echo $HOME$file>>oldFiles.txt   # copy the file path to the temp file created above
   else echo "File doesn't exist"
   fi
done

