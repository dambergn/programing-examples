#!/bin/bash

START=$(date +%T)
NOW=$(date +"%Y-%m-%d-${START}")


(
echo 'this will be saved in the log'
sleep 5
echo 'this is another log entry'
) 2>&1 | tee log-${NOW}.txt
