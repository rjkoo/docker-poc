from flask import url_for

class TestPlanOfWork(object):
    def test_landing_page(self, client):
        """ Home page should respond with a 200 success code."""
        response = client.get(url_for('plan_of_work.show_plans'))
        assert response.status_code == 200
