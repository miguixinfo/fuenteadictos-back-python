import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.fountain import Fountain
from app.models.base_object import BaseObject

class TestFountain(unittest.TestCase):

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

    def test_create_fountain(self):
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
        self.assertIsNotNone(fountain.id)

    def test_unique_name(self):
        fountain1 = Fountain(
            name="Unique Fountain",
            description="First fountain",
            image=b"image data",
            operative=True,
            average_points=5,
            latitude=40.7128,
            longitude=-74.0060
        )
        self.session.add(fountain1)
        self.session.commit()

        fountain2 = Fountain(
            name="Unique Fountain",
            description="Second fountain",
            image=b"image data",
            operative=True,
            average_points=5,
            latitude=40.7128,
            longitude=-74.0060
        )
        self.session.add(fountain2)
        with self.assertRaises(Exception):
            self.session.commit()

    def test_not_null_constraints(self):
        with self.assertRaises(Exception):
            fountain = Fountain(
                name=None,
                description="A fountain without a name",
                image=b"image data",
                operative=True,
                average_points=5,
                latitude=40.7128,
                longitude=-74.0060
            )
            self.session.add(fountain)
            self.session.commit()

    def test_relationships(self):
        fountain = Fountain(
            name="Fountain with relationships",
            description="A fountain with reviews and warnings",
            image=b"image data",
            operative=True,
            average_points=5,
            latitude=40.7128,
            longitude=-74.0060
        )
        self.session.add(fountain)
        self.session.commit()
        self.assertEqual(len(fountain.reviews), 0)
        self.assertEqual(len(fountain.warnings), 0)

if __name__ == '__main__':
    unittest.main()