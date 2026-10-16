import os

os.environ.setdefault('SECRET_KEY', 'test-only-key')
os.environ['DATABASE_URL'] = 'sqlite://'

import pytest  # noqa: E402

from app import create_app, db  # noqa: E402
from app.models import Kid, Task, Reward  # noqa: E402


@pytest.fixture
def client():
    app = create_app()
    with app.app_context():
        db.session.add_all([
            Kid(name='Alex', points=0),
            Task(name='Brush teeth', points=5, icon='brush_teeth.svg'),
            Reward(name='New toy', cost=5, icon='toy.svg'),
        ])
        db.session.commit()
    return app.test_client()


def test_pages_load(client):
    for url in ('/', '/add_kid', '/kid/1'):
        assert client.get(url).status_code == 200
    assert client.get('/kid/999').status_code == 404


def test_points_and_redeem(client):
    client.post('/add_points/1/1')
    page = client.get('/kid/1').get_data(as_text=True)
    assert 'Total Points: 5' in page
    client.post('/redeem_reward/1/1')
    assert 'Total Points: 0' in client.get('/kid/1').get_data(as_text=True)


def test_static_icons_exist(client):
    assert client.get('/static/assets/kids/default_kid.svg').status_code == 200
    assert client.get('/static/assets/tasks/brush_teeth.svg').status_code == 200


def test_missing_secret_key_fails(monkeypatch):
    import importlib
    import config
    monkeypatch.delenv('SECRET_KEY')
    with pytest.raises(RuntimeError, match='SECRET_KEY'):
        importlib.reload(config)
    monkeypatch.setenv('SECRET_KEY', 'x')
    importlib.reload(config)
