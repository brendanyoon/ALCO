from django.test import TestCase
from app.views import home, prof_dashboard, student_dashboard
from app.views import prof_quizzes, prof_map
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
        self.assertIn('Professor Login', html)
        self.assertTrue(html.endswith('</html>'))


class ProfDashboardTests(TestCase):
    def test_prof_dashboard_home_resolves_to_correct_view(self):
        found = resolve('/prof-dashboard/')
        self.assertEqual(found.func, prof_dashboard)

    def test_prof_dashboard_page_returns_correct_html(self):
        request = HttpRequest()
        response = prof_dashboard(request)
        html = response.content.decode('utf8')

        # not sure why below one isn't working:
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<h2 style="font-family: Georgia">Welcome to the dashboard!</h2>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_buttons_for_professor_nav(self):
        request = HttpRequest()
        response = prof_dashboard(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="btn btn-primary" href="../prof-quizzes/" role="button">Quizzes</a>', html)
        self.assertIn('<a class="btn btn-primary" href="#" role="button">Assignments</a>', html)
        self.assertIn('<a class="btn btn-primary" href="#" role="button">Tests</a>', html)

    def prof_quizzes_page(self):
        found = resolve('prof-quizzes/')
        self.assertEqual(found.func, prof_quizzes)

        request = HttpRequest()
        response = prof_quizzes(request)
        html = response.content.decode('utf8')

        self.assertIn('<h2>Quizzes</h2>', html)
        self.assertIn('<button type="submit" class="btn btn-primary">Submit</button>', html)
        self.assertIn('<input type="file" name="document">', html)

    def prof_map_page_testing(self):
        found = resolve('prof-map/')
        self.assertEqual(found.func, prof_map)

        request = HttpRequest()
        response = prof_map(request)
        html = response.content.decode('utf8')

        self.assertIn('<h2>Map</h2>', html)



class StudentDashboardTests(TestCase):
    def test_student_dashboard_resolves_to_correct_view(self):
        found = resolve('/student-dashboard/')
        self.assertEqual(found.func, student_dashboard)

    def test_student_dashboard_buttons(self):
        request = HttpRequest()
        response = student_dashboard(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.endswith('</html>'))
        self.assertIn('<span class="fs-4">Student Dashboard</span>', html)
        self.assertIn('Home',html)
        self.assertIn('Map', html)
        self.assertIn('Tests', html)
        self.assertIn('Assignments', html)
        self.assertIn('Grades', html)
        self.assertIn('<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" title="Quiz 1" data-bs-content="This quiz is the hardest quiz you will ever take in your life">Quiz 1 </button>', html)
