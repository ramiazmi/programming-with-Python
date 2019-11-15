# In this example we are experiencing a different way using flask_restful library.
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

"""
Here we are making a class for a particular resource; 
Employee for an example. The get and post methods correspond to the get and post requests.
The methods are automatically mapped by convention by flask_restful library. You can also use other methods such as put and delete.
"""


class Employee(Resource):
    def get(self):
        """
        This method corresponds to the GET request.
        It is called whenever there is a GET request on this resource "Employee"
        """
        # Reading employees data (Employee Resource)
        employees_df = pd.read_csv('data/employees.csv')

        try:
            data = request.data  # this is the data in the request body
            department_name = json.loads(data)
            department_name = department_name['department_name']
            df_ = employees_df[employees_df['Department'] == department_name]
        except:
            df_ = employees_df

        return {"employees": df_.to_dict('records')}

    def post(self):
        """
        This method corresponds to the POST request.
        It is called whenever there is a POST request to this resource "Employee"
        This is just a basic example to show how to create a resource.
        """
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


# Actually setup the Api resource routing here
api.add_resource(Employee, '/api/employees')

if __name__ == '__main__':
    app.run()
