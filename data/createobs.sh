#!/bin/bash
export OMP_NUM_THREADS=4


target=0.0
RUNDIR="./t${target}_base"
#RUNDIR="."

mkdir $RUNDIR
for i in {4..10}
do
    fname=run-vracer-continuous-t${target}-$i.py
    #fname=run-vracer-$i.py
    sed "5 a run = $i\ntarget = ${target}" run-vracer.py > "${RUNDIR}/${fname}"
    pushd .
    cd $RUNDIR
    python3 $fname
    popd
done
