# Filename: provisioning.py
# Author: Vaibhav Chitte
# Date: 27 September 2024
# Purpose: This program simulates a cloud resource allocation system. It checks if the requested CPU cores
#          and memory are available and lets you know whether the request can be fulfilled or not.

# Constants
MAX_CPU_CORES = 16  
MAX_MEMORY_GB = 64.0 

# Prompt user for resource demands
cpu_cores_needed = int(input("Please enter the number of CPU cores required: "))
memory_needed_gb = float(input("Please enter the required memory in GB: "))

# Check if user inputs are valid (non-negative values)
if cpu_cores_needed < 0 or memory_needed_gb < 0:
    print("Error: Requested CPU cores and memory must be non-negative.")
else:
    # Check if the system can fulfill the request
    if cpu_cores_needed <= MAX_CPU_CORES and memory_needed_gb <= MAX_MEMORY_GB:
        print("Resources allocated successfully.")
        available_cpu_cores = MAX_CPU_CORES - cpu_cores_needed
        available_memory_gb = MAX_MEMORY_GB - memory_needed_gb
    else:
        print("Request exceeds available resources. Allocation failed.")
        available_cpu_cores = MAX_CPU_CORES
        available_memory_gb = MAX_MEMORY_GB

    # Output
    print(f"Remaining CPU cores: {available_cpu_cores}")
    print(f"Remaining memory (GB): {available_memory_gb}")