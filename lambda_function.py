import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [2, 4], 'col2': [6, 12]}
    df = pd.DataFrame(data=d)
    print(df)
    print("Hello, its a test for Blog")
