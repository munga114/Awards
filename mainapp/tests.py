from django.test import TestCase
from .models import *


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='pendo', password='mineme')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='pendo')
        self.projects = Projects.objects.create(id=1, title='test post', projectimage='https//gt.com/0ccf61ff-50fe-32c6-b713-db51dbg6626f', description='desc', user=self.user, url='http://ur.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.projects, Projects))

    def test_save_projects(self):
        self.projects.save_projects()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_get_projects(self):
        self.projects.save()
        projects = Projects.all_projects()
        self.assertTrue(len(projects) > 0)

    def test_search_projects(self):
        self.projects.save()
        projects = Projects.search_projects('test')
        self.assertTrue(len(projects) > 0)

    def test_delete_projects(self):
        self.projects.delete_projects()
        projects = Projects.search_projects('test')
        self.assertTrue(len(projects) < 1)


class ReviewwTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='maitha')
        self.projects = Projects.objects.create(id=1, title='testing', projectimage='https:/xyxz.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='ok', user=self.user, url='http://ur.com')
        self.rating = Revieww.objects.create(id=1, design=6, usability=7, content=9, user=self.user, projects=self.projects)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Revieww))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Revieww.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_project_rating(self, id):
        self.rating.save()
        rating = Revieww.get_ratings(project_id=id)
        self.assertTrue(len(rating) == 1)