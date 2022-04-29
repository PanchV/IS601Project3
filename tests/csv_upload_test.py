def _test_upload_songs(application, add_db_user_fixture):
    """ unit test file upload """

    # from https://blog.entirely.digital/flask-pytest-testing-uploads/
    root = config.Config.BASE_DIR
    filename = 'sample.csv'
    filepath = root + '/../tests/' + filename
    user = add_db_user_fixture

    upload_folder = config.Config.UPLOAD_FOLDER
    upload_file = os.path.join(upload_folder, filename)
    if os.path.exists(upload_file):
        os.remove(upload_file)

    assert resp.status_code == 302

    assert db.session.query(Song).count() == 1 # pylint: disable=no-member
    song1 = Song.query.filter_by(artist="Eminem").first()
    assert song1.title == "Without Me"

    assert os.path.exists(upload_file)
    os.remove(upload_file)