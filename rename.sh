 for f in $(ls); do new=$(echo $f | sed -e 's/\.html/.txt/g'); mv $f $new; done
