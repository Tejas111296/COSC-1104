import json

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_option(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            return None  
        try:
            return int(value)  
        except ValueError:
            print("Please enter a valid integer or leave blank.")

def load_ec2_instances(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def filter_instances(instances, min_vcpu, max_vcpu, min_memory, max_memory):
    filtered_instances = []
    for instance in instances:
        vcpu = int(instance['vcpu'].split()[0])  
        memory = float(instance['memory'].split()[0])  
        
        if ((min_vcpu is None or vcpu >= min_vcpu) and 
            (max_vcpu is None or vcpu <= max_vcpu) and 
            (min_memory is None or memory >= min_memory) and 
            (max_memory is None or memory <= max_memory)):
            filtered_instances.append(instance['name'])  
    return filtered_instances

def main():
    min_vcpu = get_valid_integer("Enter minimum required CPU cores: ")
    max_vcpu = get_valid_option("Enter maximum required CPU cores (leave blank for no maximum): ")

    min_memory = get_valid_integer("Enter minimum required memory in GiB: ")
    max_memory = get_valid_option("Enter maximum required memory in GiB (leave blank for no maximum): ")

    instances = load_ec2_instances('ec2_instance_types.json')

    filtered_instances = filter_instances(instances, min_vcpu, max_vcpu, min_memory, max_memory)

    if filtered_instances:
        print("\nEC2 Instance Types that meet your requirements:")
        for instance in filtered_instances:
            print(f"- {instance}")
    else:
        print("No EC2 instance types found that meet your requirements.")

if __name__ == "__main__":
    main()
