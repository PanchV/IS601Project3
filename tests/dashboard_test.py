from app.db.models import User
from app import db

def _test_dashboard(application, add_db_user_fixture):
    user = add_db_user_fixture

    with application.test_client(user=user) as client:
        resp = client.get('dashboard')

    assert resp.status_code == 200
    assert b'Dashboard' in resp.data