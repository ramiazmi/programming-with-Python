import pandas as pd
from flask import Flask, request
import json

app = Flask(__name__)

data_path = '../../'  # You can choose a more specific path


@app.route('/api/employee/create', methods=['POST'])
def list_employees_by_department():
    req_body = request.json
    employee = dict(req_body)
    pd.DataFrame(employee, index=[0]).to_csv(data_path + 'employees.csv', mode='a', header=False, index=False)
    return '{"employee":' + str(json.dumps(employee)) + ', "Status": "A new employee was created successfully"}', 201


if __name__ == '__main__':
    app.run()
