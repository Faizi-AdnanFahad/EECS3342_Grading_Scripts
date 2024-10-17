#!/bin/bash
true="True"
validate_script="./validate.py"
feedback_script="./generate_feedback.py"

python3 $validate_script

all_assumptions_passed=$(python3 $validate_script | tail -n 1)

if echo $all_assumptions_passed | grep -q $true; then
    # run the feedback marking strings only if all assumptions have been validated
    python3 $feedback_script
else
    echo "Please make sure that all assumptions are satisifed first"
fi

