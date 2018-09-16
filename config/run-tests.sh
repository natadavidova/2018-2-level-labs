echo running tests
WAS_FAILED=false
echo "$1"
for i in $1; do
	echo "$i"
	if ! python3 -m unittest discover -p *_test.py -s lab_${i};  then
    	WAS_FAILED=true
	fi
done

if [ "$WAS_FAILED" = true ]; then
	echo tests failed
	return 1
fi
