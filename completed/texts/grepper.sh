for file in *.txt; do
	echo $file
	cat $file | grep "tbn" >> Grepped_$file
done