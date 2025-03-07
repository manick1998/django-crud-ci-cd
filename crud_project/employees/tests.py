from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from employees.models import Employee

class EmployeeAPITest(APITestCase):
    """
    Integration tests for the Employee API.
    """

    def setUp(self):
        """
        Set up a test employee for API testing.
        """
        self.employee = Employee.objects.create(
            name="John Doe",
            age=30,
            department="IT"
        )
        self.employee_url = reverse('get_employee', kwargs={'pk': self.employee.id})  # ✅ Use reverse() to get the correct URL
        self.create_employee_url = reverse('create_employee')  # ✅ Fix URL for POST request

    def test_get_employee(self):
        """
        Test the GET request for retrieving an employee.
        """
        response = self.client.get(self.employee_url)
        print(response.status_code, response.content)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "John Doe")  # ✅ Use .json() instead of response.data

    def test_create_employee(self):
        """
        Test the POST request for creating an employee.
        """
        data = {"name": "Jane Doe", "age": 28, "department": "HR"}
        response = self.client.post(self.create_employee_url, data)
        print(response.status_code, response.content)  # Debugging output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
