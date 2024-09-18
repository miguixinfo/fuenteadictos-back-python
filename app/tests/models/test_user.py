import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.base_object import BaseObject

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database
        cls.engine = create_engine('sqlite:///:memory:')
        BaseObject.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        user = User(
            email="test@example.com",
            username="testuser",
            password="securepassword"
        )
        self.session.add(user)
        self.session.commit()
        self.assertIsNotNone(user.id)

    def test_unique_email(self):
        user1 = User(
            email="unique@example.com",
            username="uniqueuser1",
            password="securepassword"
        )
        self.session.add(user1)
        self.session.commit()

        user2 = User(
            email="unique@example.com",
            username="uniqueuser2",
            password="securepassword"
        )
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()

    def test_unique_username(self):
        user1 = User(
            email="user1@example.com",
            username="uniqueuser",
            password="securepassword"
        )
        self.session.add(user1)
        self.session.commit()

        user2 = User(
            email="user2@example.com",
            username="uniqueuser",
            password="securepassword"
        )
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()

    def test_not_null_constraints(self):
        with self.assertRaises(Exception):
            user = User(
                email=None,
                username="nonameuser",
                password="securepassword"
            )
            self.session.add(user)
            self.session.commit()

        with self.assertRaises(Exception):
            user = User(
                email="noname@example.com",
                username=None,
                password="securepassword"
            )
            self.session.add(user)
            self.session.commit()

        with self.assertRaises(Exception):
            user = User(
                email="noname@example.com",
                username="nonameuser",
                password=None
            )
            self.session.add(user)
            self.session.commit()

    def test_relationships(self):
        user = User(
            email="relationship@example.com",
            username="relationshipuser",
            password="securepassword"
        )
        self.session.add(user)
        self.session.commit()
        self.assertEqual(len(user.reviews), 0)
        self.assertEqual(len(user.warnings), 0)

if __name__ == '__main__':
    unittest.main()