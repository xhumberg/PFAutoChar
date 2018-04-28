if [ "$1" = "" ]
then
	pip install --user -U numpy
	pip install --user -U scipy
	pip install --user -U scikit-learn
fi

echo "."
echo "."
echo "."

echo "Done! You should now be able to run our program with 'python DecisionTree.py'"

echo ""

echo "Would you like to do that now? [y/n]"

read RESPONSE

if [ "$RESPONSE" = "y" ]
then
	echo "python DecisionTree.py"
	python DecisionTree.py
fi

echo ""
echo ""
echo "Would you like to uninstall the packages, now? [y/n]"

read UNINSTALL

if [ "$UNINSTALL" = "y" ]
then
	pip uninstall -y numpy
	pip uninstall -y scipy
	pip uninstall -y scikit-learn
fi
