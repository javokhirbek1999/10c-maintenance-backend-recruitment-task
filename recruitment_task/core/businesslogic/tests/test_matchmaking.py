from datetime import datetime

from django.test import TestCase

from core.models import Investor, Project


class MatchmakingTestCase(TestCase):

    def setUp(self) -> None:

        investor_payload = {'name':'Javokhirbek Khaydaraliev', 'total_amount':250000, 'individual_amount':5000, 'project_delivery_deadline':datetime(2022, 12, 15)}
        project_payload = {'name': 'Inventory Management System', 'description': 'Inventory Management System is used to manage manufactured products', 'amount':2000, 'delivery_date':datetime(2022, 10, 25), 'funded_by':None, 'funded':False}

        self.investor = Investor.objects.create(**investor_payload)
        self.projects = Project.objects.create(**project_payload)
        

    def test_matchmaking_for_project(self):

        matched_projects = self.investor.matching_projects()

        self.assertGreater(len(matched_projects), 0)


    def test_matchmaking_for_investor(self):
        
        matched_investors = self.projects.matching_investors()

        self.assertGreater(len(matched_investors), 0)