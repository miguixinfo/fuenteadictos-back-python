import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.review import Review
from app.models.base_object import BaseObject
from app.models.fountain import Fountain
from app.models.user import User

class TestReview(unittest.TestCase):

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

    def test_create_review(self):
        review = Review(
            header="Great Fountain",
            description="This fountain is amazing!",
            jet_points=5,
            cold_points=4,
            pretty_points=5,
            flavor_points=3,
            user_id=1,
            fountain_id=1
        )
        self.session.add(review)
        self.session.commit()
        self.assertIsNotNone(review.id)

    def test_relationship_with_fountain(self):
        fountain = Fountain(
            name="Test Fountain",
            description="A beautiful test fountain",
            image=b"image data",
            operative=True,
            average_points=5,
            latitude=40.7128,
            longitude=-74.0060
        )
        self.session.add(fountain)
        self.session.commit()

        review = Review(
            header="Great Fountain",
            description="This fountain is amazing!",
            jet_points=5,
            cold_points=4,
            pretty_points=5,
            flavor_points=3,
            user_id=1,
            fountain_id=fountain.id
        )
        self.session.add(review)
        self.session.commit()
        self.assertEqual(review.fountain.id, fountain.id)

    def test_relationship_with_user(self):
        user = User(
            username="testuser",
            email="testuser@example.com",
            password="password"
        )
        self.session.add(user)
        self.session.commit()

        review = Review(
            header="Great Fountain",
            description="This fountain is amazing!",
            jet_points=5,
            cold_points=4,
            pretty_points=5,
            flavor_points=3,
            user_id=user.id,
            fountain_id=1
        )
        self.session.add(review)
        self.session.commit()
        self.assertEqual(review.user.id, user.id)

    def test_not_null_constraints(self):
        with self.assertRaises(Exception):
            review = Review(
                header=None,
                description="This fountain is amazing!",
                jet_points=5,
                cold_points=4,
                pretty_points=5,
                flavor_points=3,
                user_id=1,
                fountain_id=1
            )
            self.session.add(review)
            self.session.commit()

if __name__ == '__main__':
    unittest.main()