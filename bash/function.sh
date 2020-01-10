#!/bin/bash

# Passing arguments into function 
function func_toRun () {
    value1="${1}" # $1 represent first argument
    value2="${2}" # $2 represent second argument
    echo 'I have' ${value1}
    echo 'This is how to' ${value2}
}

func_toRun "suceeded" "pass arguments into a function"