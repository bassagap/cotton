from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Test Results API', description='API for submitting test results and evidences')


# Define a model for the test data
test_model = api.model('Test', {
    'projectId': fields.String(required=True, description='Project ID'),
    'companyId': fields.String(required=True, description='Company ID'),
    'junitResults': fields.String(required=True, description='JUnit Test Results in XML format'),
    'testEvidences': fields.List(fields.String(), description='List of test evidences (e.g., screenshots)')
})


class TestResource(Resource):
    # Class attributes for storing test results and evidences
    test_results = []
    evidences = []

    @api.expect(test_model)
    def post(self):
        """
        Submit a test result
        """
        data = request.json

        # Extract data from the request
        project_id = data.get('projectId')
        company_id = data.get('companyId')
        junit_results = data.get('junitResults')
        test_evidences = data.get('testEvidences')

        # Save test results to class attribute
        test_result = {
            'projectId': project_id,
            'companyId': company_id,
            'junitResults': junit_results
        }
        TestResource.test_results.append(test_result)

        # Save test evidences to class attribute
        evidence = {
            'projectId': project_id,
            'companyId': company_id,
            'testEvidences': test_evidences
        }
        TestResource.evidences.append(evidence)

        return {'message': 'Test submitted successfully.', 'testResult': test_result, 'evidence': evidence}

    def get(self):
        """
        Get test results and evidences
        """
        return {'testResults': TestResource.test_results, 'evidences': TestResource.evidences}


# Add the resource to the API
api.add_resource(TestResource, '/api/test')

if __name__ == '__main__':
    app.run(debug=True)
