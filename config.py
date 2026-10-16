import os

basedir = os.path.abspath(os.path.dirname(__file__))


def _require_secret_key():
    key = os.environ.get('SECRET_KEY')
    if not key:
        raise RuntimeError(
            'SECRET_KEY environment variable is not set. Generate one with '
            '"python -c \'import secrets; print(secrets.token_hex(32))\'" '
            'and export it (see .env.example and README.md).')
    return key


class Config:
    SECRET_KEY = _require_secret_key()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'anak_baik.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'assets', 'kids')
