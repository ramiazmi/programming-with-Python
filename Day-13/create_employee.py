import pandas as pd
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/api/employees', methods=['POST'])
def list_employees_by_department():

    # Reading employees data (Employee Resource)
    employees_df = pd.read_csv('data/employees.csv')

    data = request.data
    employee = json.loads(data)

    if employees_df.append(pd.DataFrame(employee, index=[0])).duplicated().sum() == 0:
        with open('data/employees.csv', 'a') as f:
            f.write('\n')
            f.write('{},{},{}'.format(employee['Name'], employee['Department'], employee['Salary']))
        return {'data': employee}, 201  # status code when a resource created successfully
    else:
        return {'data': 'Resource already exists!'}, 409


if __name__ == '__main__':
    app.run()
