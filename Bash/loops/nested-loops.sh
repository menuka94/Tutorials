declare -a arrA=("1", "2", "3", "4", "5")
declare -a arrB=("A", "B", "C", "D", "E")

for i in "${arrA[@]}"
do
    for j in "${arrB[@]}"
	do
	    echo "$i-$j\n"
	done
done


