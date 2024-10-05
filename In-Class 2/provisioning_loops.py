# Filename: provisioning_loops.py
# Author: Vaibhav Chitte
# Date: 27 September 2024
# Purpose: This program simulates a cloud resource allocation system that handles multiple requests. It checks if 
#          the requested CPU cores and memory are available and stores the requests in allocated or pending lists.

# Constants
MAX_CPU_CORES = 16 
MAX_MEMORY_GB = 64.0  

# Lists to store requests
allocated_resources = [] 
pending_requests = [] 

# Track resources used
used_cpu_cores = 0  
used_memory_gb = 0.0  

# Function to validate input
def get_valid_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Value must be non-negative.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")

# Function to validate input
def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value must be non-negative.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")

# Loop
while True:
    # Prompt user for resource demands
    username = input("Enter the username: ")
    cpu_cores_needed = get_valid_int_input("Please enter the number of CPU cores required: ")
    memory_needed_gb = get_valid_float_input("Please enter the required memory in GB: ")

    # Check if the system can fulfill the request
    if (cpu_cores_needed + used_cpu_cores <= MAX_CPU_CORES) and (memory_needed_gb + used_memory_gb <= MAX_MEMORY_GB):
        # Add successful request to allocated resources
        allocated_resources.append([username, cpu_cores_needed, memory_needed_gb])
        used_cpu_cores += cpu_cores_needed
        used_memory_gb += memory_needed_gb
        print("Resources allocated successfully.")
    else:
        # Add unsuccessful request to pending requests
        pending_requests.append([username, cpu_cores_needed, memory_needed_gb])
        print("Request exceeds available resources. Added to pending requests.")

    # Ask user if they want to continue
    another_request = input("Do you want to make another request? (yes/no): ").strip().lower()
    if another_request != 'yes':
        break

# Display the results
print("\nAllocated Resources")
print(f"{'Username':<15}{'CPU Cores':<15}{'Memory (GB)':<15}")
print('-' * 45)
for request in allocated_resources:
    print(f"{request[0]:<15}{request[1]:<15}{request[2]:<15}")
print('-' * 45)

print("\nPending Requests")
print(f"{'Username':<15}{'CPU Cores':<15}{'Memory (GB)':<15}")
print('-' * 45)
for request in pending_requests:
    print(f"{request[0]:<15}{request[1]:<15}{request[2]:<15}")
print('-' * 45)