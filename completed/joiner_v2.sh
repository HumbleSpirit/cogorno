while read line; do
	echo $line
	ls fixed_$line*.mp4 | perl -ne 'print "file $_"' | ffmpeg -protocol_whitelist file,pipe -f concat -i - -c copy $line.mp4
done < list3
