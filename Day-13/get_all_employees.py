import pandas as pd
from flask import Flask

app = Flask(__name__)

# Read employees data from a csv file when server starts
employees_df = pd.read_csv('data/employees.csv')


@app.route('/api/employees', methods=['GET'])
def list_employees():
    return '{"employess": ' + employees_df.to_json(orient='records') + '}'


if __name__ == '__main__':
    app.run()
