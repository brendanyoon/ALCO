from django.test import TestCase
from app.views import home
from app.views import prof_dashboard
from django.urls import resolve
from django.http import HttpRequest

# Create your tests here.

class HomePageTests(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<h1>ALCO RPG Login</h1>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_student_professor_login_buttons_exists(self):
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('Student Login', html)
        self.assertIn('Student Login', html)
        self.assertTrue(html.endswith('</html>'))


class ProfDashboardTests(TestCase):
    def test_prof_dashboard_resolves_to_correct_view(self):
        found = resolve('/prof-dashboard/')
        self.assertEqual(found.func, prof_dashboard)

    def test_prof_dashboard_page_returns_correct_html(self):
        request = HttpRequest()
        response = prof_dashboard(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<h3>Welcome to the dashboard!</h3>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_buttons(self):
        request = HttpRequest()
        response = prof_dashboard(request)
        html = response.content.decode('utf8')
        self.assertIn('<button type="button" class="btn btn-primary">Quizzes</button>', html)
        self.assertIn('<button type="button" class="btn btn-primary">Assignments</button>', html)
        self.assertIn('<button type="button" class="btn btn-primary">Tests</button>', html)

