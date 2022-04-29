from app.db.models import User
from app import db

def _test_dashboard(application, add_db_user_fixture):
    """ GET to dashboard as logged in user """
    # pylint: disable=redefined-outer-name
    user = add_db_user_fixture

    with application.test_client(user=user) as client:
        resp = client.get('dashboard')

    # check if successful at getting /dashboard
    assert resp.status_code == 200
    assert b'<h2>Dashboard</h2>' in resp.data
    assert b'<p>Welcome: testuser@test.com</p>' in resp.data
    assert b'<h2>Browse: Your Songs</h2>' in resp.data