#!/bin/bash


for i in {1..10}
do
    run=${i}
    outfile="policies_l2error_${i}.eps"

    
    policies="_korali_result_${run}-t-1.0 _korali_result_${run}-t-0.5 _korali_result_${run}-t-0.25 _korali_result_${run}-t-0.125 _korali_result_${run}-t-0.0625 _korali_result_${run}-t-0.03125 _korali_result_${run}-t-0.0"
    
    obsfiles="observations-vracer-1-t-0.0.json observations-vracer-2-t-0.0.json observations-vracer-3-t-0.0.json observations-vracer-4-t-0.0.json observations-vracer-5-t-0.0.json observations-vracer-6-t-0.0.json observations-vracer-7-t-0.0.json observations-vracer-8-t-0.0.json observations-vracer-9-t-0.0.json observations-vracer-10-t-0.0.json"

    python comparepolicy.py --policies $policies --obsfile $obsfiles --outfile $outfile --comparison "action"

done
