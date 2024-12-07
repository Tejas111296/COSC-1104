import pandas as pd
import matplotlib.pyplot as plt

# Load simulated data from the CSV file
def load_cost_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading the data: {e}")
        return None

# Function to generate a cost summary report
def generate_cost_report(data):
    total_cost = data['total_cost'].sum()
    service_costs = data.groupby('service')['total_cost'].sum()
    return total_cost, service_costs

# Function to generate a cost distribution graph
def generate_cost_graph(service_costs, output_image):
    service_costs.plot(kind='bar', color='skyblue')
    plt.title('Cloud Service Cost Distribution')
    plt.xlabel('Cloud Service')
    plt.ylabel('Total Cost ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_image)
    plt.close()

def main():
    # Load data (using the simulated CSV file)
    cost_data = load_cost_data('cost_report.csv')

    if cost_data is not None:
        # Generate the cost report
        total_cost, service_costs = generate_cost_report(cost_data)
        print(f"Total Cloud Cost: ${total_cost:.2f}")
        print("Cost by Service:")
        print(service_costs)

        # Generate the graph and save it as a PNG
        generate_cost_graph(service_costs, 'cost_report.png')

if __name__ == "__main__":
    main()
