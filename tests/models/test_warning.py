import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.warning import Warning
from app.models.user import User
from app.models.fountain import Fountain
from app.models.base_object import Base

# Setup test database
@pytest.fixture(scope='module')
def test_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_warning(test_db):
    user = User(name="Test User")
    fountain = Fountain(name="Test Fountain")
    test_db.add(user)
    test_db.add(fountain)
    test_db.commit()

    warning = Warning(operative=True, user=user, fountain=fountain)
    test_db.add(warning)
    test_db.commit()

    assert warning.id is not None
    assert warning.operative is True
    assert warning.user == user
    assert warning.fountain == fountain

def test_warning_relationships(test_db):
    user = User(name="Test User 2")
    fountain = Fountain(name="Test Fountain 2")
    test_db.add(user)
    test_db.add(fountain)
    test_db.commit()

    warning = Warning(operative=False, user=user, fountain=fountain)
    test_db.add(warning)
    test_db.commit()

    assert warning.user_id == user.id
    assert warning.fountain_id == fountain.id
    assert warning.user.warnings[0] == warning
    assert warning.fountain.warnings[0] == warning

def test_warning_operative_field(test_db):
    user = User(name="Test User 3")
    fountain = Fountain(name="Test Fountain 3")
    test_db.add(user)
    test_db.add(fountain)
    test_db.commit()

    warning = Warning(operative=False, user=user, fountain=fountain)
    test_db.add(warning)
    test_db.commit()

    assert warning.operative is False

    warning.operative = True
    test_db.commit()

    assert warning.operative is True