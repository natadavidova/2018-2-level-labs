echo "$LABS_TO_BUILD"
WAS_FAILED=false
for i in ${LABS_TO_BUILD[@]}; do
	if ! python3 -m unittest discover -p *_test.py -s lab_${i};  then
    	WAS_FAILED=true
	fi
done

if [ "$WAS_FAILED" = true ]; then
	echo tests failed
	exit 1
fi
