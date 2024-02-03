#!/bin/bash

## Dependencies
# sudo apt-get install jq
# sudo apt-get install sensors

# File to store persistant data
json_file="/tmp/system_info.json"
log_file="/tmp/system_info.log"

# Get Timestamps
timestamp=$(date +"%Y%m%d%H%M%S")
timestamp2=$(date "+%b %e %H:%M:%S")

# Get system information
hostname_var=$(hostname)

# Get system load
load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}')

# CPU functions
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')

# Check if the 'sensors' command is available
if command -v sensors &> /dev/null; then
    # Get CPU temperature
    cpu_temperature=$(sensors | awk '/Core 0/ {print $3}' | tr -d '+°C')
    # echo "CPU Temperature: $cpu_temperature"
else
    cpu_temperature="N/A"
    echo "sensors command not found. Unable to retrieve CPU temperature."
fi

# memory_usage=$(free -m | awk '/Mem:/ {print $3}')
disk_usage=$(df -h / | awk 'NR==2 {print $5}')

# Get used and total memory in MB
used_memory=$(free -m | awk '/Mem:/ {print $3}')
total_memory=$(free -m | awk '/Mem:/ {print $2}')

# Calculate the percentage of used memory
memory_percentage=$(( (used_memory * 100) / total_memory ))

# Set the path to the filesystem you want to check
filesystem_path="/"

# Get the used and total inodes
used_inodes=$(df -i $filesystem_path | awk 'NR==2 {print $3}')
total_inodes=$(df -i $filesystem_path | awk 'NR==2 {print $2}')

# Calculate the percentage of used inodes
inode_percentage=$(( (used_inodes * 100) / total_inodes ))

# Create JSON response
new_json_data=$(cat <<-EOF
{
  "system_information": {
    "timestamp" : "$timestamp",
    "load": "$load",
    "cpu_usage": "$cpu_usage%",
    "cpu_temp": "$cpu_temperature",
    "memory_usage": "$memory_percentage%",
    "disk_usage": "$disk_usage",
    "i_node_usage": "$inode_percentage%"
  }
}
EOF
)

# Check if the JSON file exists
if [ -e "$json_file" ]; then
  # Read the existing JSON content
  existing_json_data=$(cat "$json_file")

  # Check if the existing content is empty
  if [ -z "$existing_json_data" ]; then
    # If it's empty, create a new JSON array
    updated_json_data=$(echo "[$new_json_data]" | jq '.')
  else
    # If it's not empty, append the new data to the existing array
    updated_json_data=$(echo "$existing_json_data" | jq --argjson new_data "$new_json_data" '. += [$new_data]')
  fi
else
  # If the file doesn't exist, create a new JSON array
  updated_json_data=$(echo "[$new_json_data]" | jq '.')
fi

# Write the updated JSON back to the file
echo "$updated_json_data" > "$json_file"
echo "Data added to $json_file"

# Write to logfile
logfile="$timestamp2 $hostname_var load:$load cpu_usage:$cpu_usage cpu_temp:$cpu_temperature memory_usage:$memory_percentage disk_usage:$disk_usage i_node_usage:$inode_percentage"
echo "$logfile" >> "$log_file"

echo $logfile