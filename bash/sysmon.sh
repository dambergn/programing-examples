#!/bin/bash

# Dependencies
# sudo apt-get install jq

# File to store the JSON data
json_file="system_info.json"

# Get system information
timestamp=$(date +"%Y%m%d%H%M%S")
load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}')
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
memory_usage=$(free -m | awk '/Mem:/ {print $3}')
disk_usage=$(df -h / | awk 'NR==2 {print $5}')

# Create JSON response
new_json_data=$(cat <<-EOF
{
  "system_information": {
    "timestamp" : "$timestamp",
    "load": "$load",
    "cpu_usage": "$cpu_usage%",
    "memory_usage": "${memory_usage}MB",
    "disk_usage": "$disk_usage"
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