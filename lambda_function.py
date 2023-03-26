import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1, 4], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print("Hello, its a final test")
