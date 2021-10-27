while read line; do
	echo $line
		for file in $line*.mp4; do ffprobe $file >> $line.txt 2>&1; done
done < list