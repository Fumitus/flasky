import unittest
from app.models import Comment
from app import create_app, db


class UserViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_moderate_disable(self):
        c1 = Comment(body='pirmas', body_html='<a>cat</a>', author_id=1, post_id=1)
        c2 = Comment(body='antras', body_html='<a>dog</a>', author_id=1, post_id=1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        self.assertTrue(Comment.query.get(1))
        self.assertTrue(Comment.query.get(2))
        self.assertTrue(c1.body == 'pirmas')
        self.assertTrue(c2.body == 'antras')
        c1.disabled = True
        c2.disabled = False
        db.session.add(c1)
        db.session.commit()
        self.assertTrue(c1.disabled == True)
        self.assertTrue(c2.disabled == False)

