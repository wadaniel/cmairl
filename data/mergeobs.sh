#!/bin/bash
target=0.0
RUNDIR="./t${target}_base"

outfile="observations-t-${target}.json"

flist=""
for i in {1..3}
do
    fname="${RUNDIR}/observations-vracer-${i}-t-${target}.json"
    flist="${flist} ${fname}"
    #echo $fname
done

echo $outfile
echo $flist
python mergeobsfile.py --obsfiles $flist --outfile $outfile
