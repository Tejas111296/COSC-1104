import matplotlib.pyplot as plt

def generate_visualizations(cost_data):
    """Generate a bar chart visualizing AWS costs by service."""
    services = [item['Keys'][0] for item in cost_data['ResultsByTime'][0]['Groups']]
    costs = [float(item['Metrics']['BlendedCost']['Amount']) for item in cost_data['ResultsByTime'][0]['Groups']]
    
    plt.figure(figsize=(10, 6))
    plt.bar(services, costs, color='skyblue')
    plt.title("AWS Cost Breakdown by Service")
    plt.ylabel("Cost (USD)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("cost_chart.png")
    print("Visualization generated: cost_chart.png")
