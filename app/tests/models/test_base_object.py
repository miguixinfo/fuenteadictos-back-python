import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base_object import BaseObject
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TestBaseObject(BaseObject):
    __tablename__ = 'test_base_object'

class TestBaseObjectModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_uuid_generation(self):
        obj1 = TestBaseObject()
        obj2 = TestBaseObject()
        self.session.add(obj1)
        self.session.add(obj2)
        self.session.commit()
        self.assertIsNotNone(obj1.uuid)
        self.assertIsNotNone(obj2.uuid)
        self.assertNotEqual(obj1.uuid, obj2.uuid)

    def test_default_values(self):
        obj = TestBaseObject()
        self.session.add(obj)
        self.session.commit()
        self.assertIsNotNone(obj.created_date)
        self.assertFalse(obj.voided)

    def test_primary_key_autoincrement(self):
        obj1 = TestBaseObject()
        obj2 = TestBaseObject()
        self.session.add(obj1)
        self.session.add(obj2)
        self.session.commit()
        self.assertIsNotNone(obj1.id)
        self.assertIsNotNone(obj2.id)
        self.assertNotEqual(obj1.id, obj2.id)

if __name__ == '__main__':
    unittest.main()