#!/bin/bash
# Version: 1.0
# Updated: 2020-02-22
# Written by: Nick Damberg
# Perfected by: No one
# Tested OS: Ubuntu 16.04, 18.04, 20.04

START=$(date +%T)
NOW=$(date +"%Y-%m-%d-$START")
NAME="log"
DIR="logs/"


(
echo 'this will be saved in the log'
sleep 5
echo 'this is another log entry'
) 2>&1 | tee -a "$DIR$NAME-$NOW.txt"
