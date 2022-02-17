#!/bin/bash
# The purpose of this is an example of calling an external script and retreving the results.

# MATH= source ./main_sub1.sh 2 2
SCRIPT_PATH="./main_sub1.sh"
OUTPUT="RESULT: $("$SCRIPT_PATH" "2" "2")"

# printf "\n"
echo $OUTPUT