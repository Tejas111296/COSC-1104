import boto3
import pandas as pd

def fetch_cost_data():
    """Fetch cost and usage data from AWS Cost Explorer."""
    client = boto3.client('ce', region_name='us-east-1')
    response = client.get_cost_and_usage(
        TimePeriod={'Start': '2023-11-01', 'End': '2023-11-30'},
        Granularity='MONTHLY',
        Metrics=['BlendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )
    return response

def generate_cost_report(cost_data):
    """Generate a CSV report of AWS cost breakdown."""
    services = [item['Keys'][0] for item in cost_data['ResultsByTime'][0]['Groups']]
    costs = [float(item['Metrics']['BlendedCost']['Amount']) for item in cost_data['ResultsByTime'][0]['Groups']]
    
    df = pd.DataFrame({'Service': services, 'Cost (USD)': costs})
    df.to_csv('cost_report.csv', index=False)
    print("Cost report generated: cost_report.csv")
