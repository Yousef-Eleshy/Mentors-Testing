# -*- coding: utf-8 -*-

from odoo.tests import common


Class TestModule(common.TransactionCase):
    def setUp(self):
        super(TestModule, self).setUp()
        #Add Test Setup Code Here
        
        
    def test_data(self):
        #Add Test Code Here
        
        # Create a New Project with the Test
        test_project = self.env['project.project'].create({
            'name': 'TestProject'
        })

        # Add a Test Task to the Project
        test_project_task = self.env['project.task'].create({
            'name': 'ExampleTask',
            'project_id': test_project.id
        })
        

        # Check if the project name and the task name match
        self.assertEqual(test_project.name, 'TestProject')
        self.assertEqual(test_project_task.name, 'ExampleTask')
        
        # Check if the project assigned to the task is in fact the correct id
        self.assertEqual(test_project_task.project_id.id, test_project.id)
        
        # Print to show it visually
        print('Your Test Was Succesfull!')