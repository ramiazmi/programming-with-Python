import pandas as pd
from flask import Flask, request
import json


app = Flask(__name__)

# Read employees data from a csv file when server starts
employees_df = pd.read_csv('data/employees.csv')


@app.route('/api/employee/create', methods=['POST'])
def list_employees_by_department():
    req_body = request.json
    employee = json.dumps(dict(req_body))
    return '{"employee":' + str(employee) + ', "Status": "A new employee was created successfully"}', 201


if __name__ == '__main__':
    app.run()
