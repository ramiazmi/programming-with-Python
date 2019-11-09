import pandas as pd
from flask import Flask, request
import json

app = Flask(__name__)

# Read employees data from a csv file when server starts
employees_df = pd.read_csv('data/employees.csv')

########################################################################################################################
# Solution-1: Sending the department name parameter in the request body
# @app.route('/api/employees', methods=['GET'])
# def list_employees_by_department():
#     req_body = request.json
#     department = req_body['department']
#     return '{"employees": ' + employees_df[employees_df['Department'] == department].to_json(orient='records') + '}'

# Solution-2: Showing the department name parameter in the URL
# @app.route('/api/employees/<department>', methods=['GET'])
# def list_employees_by_department(department):
#     return '{"employees": ' + employees_df[employees_df['Department'] == department].to_json(orient='records') + '}'
########################################################################################################################
'''Solution-3: this accepts both ways, however, this is not good practice. The best is to use one approach in which 
   we send the data of the department name attribute in the request body'''


# @app.route('/api/employees/<dept_name>', methods=['GET'])
# @app.route('/api/employees', methods=['GET'])
# def list_employees_by_department(dept_name=None):
#     department_name = dept_name
#     if not dept_name:
#         try:
#             req_body = request.data
#             department_name = json.loads(req_body)
#             department_name = department_name['department']
#         except:
#             department_name = None
#
#     df_ = employees_df[employees_df['Department'] == department_name] if department_name else employees_df
#     return '{"employees": ' + df_.to_json(orient='records') + '}
########################################################################################################################
# Solution-4: This is the best practice
@app.route('/api/employees', methods=['GET'])
def list_employees_by_department():
    try:
        data = request.data  # this is the data in the request body
        department_name = json.loads(data)
        department_name = department_name['department_name']
        df_ = employees_df[employees_df['Department'] == department_name]
    except:
        df_ = employees_df

    return '{"employees": ' + df_.to_json(orient='records') + '}'


########################################################################################################################

if __name__ == '__main__':
    app.run()
