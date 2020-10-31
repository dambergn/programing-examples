# Bash Scripting

## Bash Navigation
- ls (Print a list of files and folders in directory)
- pwd (Print Working Directory - You are here)
- cd (change directory)
- cd .. (Move back one directory)
- cd ~ (Go to home folder)
- / (Root of operating system)
- ./ (execute from this location)
- touch name.sh (create new file)
- mkdir folder (creates a new directory named folder)
- cp name.sh name2.sh (Makes a copy of the file)
- mv name.sh Name.sh (Moves or re names a file or folder)
- rm name2.sh (deletes the file name2.sh)


## Getting Started
create a new file name.sh
Put the following line of code at the beginning of the bash script
```
#!/bin/bash
```
Make the bash script exicuteable
```
sudo chmod +x name.sh
```
To run the script from the directory where the script is contained
```
./name.sh
```

## Console output
```
echo "Hello World"
```

## Variables
"variable" "store"
```
name your-name-here

```

## Data types
- string
- intiger
- boolian

## User input
```
echo "type something in"
read variable
echo "you typed ${variable}"
```

## if statements
```
if [ <check for something> ]; then
  <do something>
elif [<check for something else>]; then
  <do something else>
else
  <do last thing>
fi
```

## for loops

## while loops

## functions
```
function toRun () {
    value1="${1}" # $1 represent first argument
    value2="${2}" # $2 represent second argument
    echo 'I have' ${value1}
    echo 'This is how to' ${value2}
}

toRun "suceeded" "pass arguments into a function"
```

## STDOut to LOG files
```
          || visible in terminal ||   visible in file   || existing
  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file   
==========++==========+==========++==========+==========++===========
    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    >>    ||    no    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
          ||          |          ||          |          ||
 | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
 | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
|& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite
|& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append
```

### Examples
```
command > output.txt
command >> output.txt
command 2> output.txt
command 2>> output.txt
command &> output.txt
command &>> output.txt
command | tee output.txt
command | tee -a output.txt
command |& tee output.txt
command |& tee -a output.txt
```

## System Information

### Check status of service
```
systemctl is-active --quiet <Service_Name> && echo Service is running
```

### This will check if the service is down and perform service restart
```
systemctl is-active --quiet <service name> || <service name> restart
```

### Get CPU temp
```
cat /sys/class/thermal/thermal_zone0/temp
watch -n.1 "cat /sys/class/thermal/thermal_zone0/temp"
# or
apt-get install lm-sensors
sensors-detect
watch -n 1 sensors
```

### Get CPU Frequency
```
watch -n.1 "cat /proc/cpuinfo | grep \"^[c]pu MHz\""
```