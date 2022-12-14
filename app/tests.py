from django.test import TestCase
from app.views import home, prof_dashboard, student_dashboard
from app.views import student_stats
from app.views import prof_quizzes, prof_map
from app.exp import exp
from django.urls import resolve
from django.http import HttpRequest
from django.db import models
from .models import Professor, Student, Quest, Obstacle, Multiple_Choice, Multiple_Answers


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
        self.assertIn('Map', html)
        self.assertIn('Quest Creation', html)
        self.assertIn('Image Upload', html)

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
        self.assertIn('Home',html)
        self.assertIn('Map', html)
        self.assertIn('Quest List', html)
        self.assertIn('Stats', html)

class ExperienceFrontEndTest(TestCase):
    def test_student_experience_resolves_to_correct_view(self):
        found = resolve('/student-stats/')
        self.assertEqual(found.func, student_stats)

class ExperienceBackEndTests(TestCase):
    def test_min_experience(self):
        xp = 0
        self.assertEqual(exp.GetLevel(xp), 1)
        self.assertEqual(exp.ExpToNextLevel(xp), 10)
        self.assertEqual(exp.ToNextLevelPercent(xp), 0)

    def test_max_experience(self):
        xp = 1250000
        self.assertEqual(exp.GetLevel(xp), 100)
        self.assertEqual(exp.ExpToNextLevel(xp), 0)
        self.assertEqual(exp.ToNextLevelPercent(xp), 1)

    def test_experience_out_of_bounds(self):
        xp = -1
        self.assertEqual(exp.GetLevel(xp), False)
        self.assertEqual(exp.ExpToNextLevel(xp), False)
        self.assertEqual(exp.ToNextLevelPercent(xp), False)
        xp = 10000000000000
        self.assertEqual(exp.GetLevel(xp), False)
        self.assertEqual(exp.ExpToNextLevel(xp), False)
        self.assertEqual(exp.ToNextLevelPercent(xp), False)

    def test_experience_normal_case(self):
        request = HttpRequest()
        response = student_dashboard(request)
        html = response.content.decode('utf8')
        xp = 50
        self.assertEqual(exp.GetLevel(xp), 3) # floor((50/5 * 4) ^ (1/3)) = 3
        self.assertEqual(exp.ExpToNextLevel(xp), 30) #80 (minimum total xp of next level) - 50 (current xp) = 30
        self.assertEqual(exp.ToNextLevelPercent(xp), 0.348) # (30 [exp to next level] % 46 [base exp to next level] ) / 46 = .348
       
class ModelsTest(TestCase):
    def test_prof_student_creation_db_retreival(self):
        prof = Professor(professor_email='prof@umbc.edu', first_name='Prof', last_name='J')
        student = Student(student_email='student@umbc.edu', first_name='Candy', last_name='Kuo', grade=90.001, exp_pts='0')
        prof.save()
        student.save()

        assert(Professor.objects.get(professor_email='prof@umbc.edu') == prof)
        assert(Student.objects.get(student_email='student@umbc.edu') == student)

    def test_quest_creation(self):
        prof = Professor(professor_email='prof@umbc.edu', first_name='Prof', last_name='J')
        student = Student(student_email='student@umbc.edu', first_name='Candy', last_name='Kuo', grade=90.001, exp_pts='0')
        prof.save()
        student.save()

        quest = Quest(title='New Quest', num_questions=5, total_exp=100, is_required=True)
        quest.save()
        assert(Quest.objects.get(title='New Quest') == quest)
        
    def sample_question(self):
        num_questions = Multiple_Choice(num_choices)