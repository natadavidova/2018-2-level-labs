echo running check
echo "${LABS_TO_BUILD[*]}"
WAS_FAILED=false
for i in ${LABS_TO_BUILD[@]}; do
	if ! python3 config/plagiarism_check.py --source-dir lab_${i}/ --others-dir tmp/lab_${i};  then
    	WAS_FAILED=true
	fi
done

if [ "$WAS_FAILED" = true ]; then
	echo plagiarism failed
	return 1
fi
