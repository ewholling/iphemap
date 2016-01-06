#!/bin/bash
FILES="$@"
for i in ./*.pdf; do
	echo "Prcoessing image $i ..."
	/usr/bin/convert -thumbnail x80 "$i" "$i.png"
done
