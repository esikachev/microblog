import os.path

from migrate.versioning import api

from microblog.config import SQLALCHEMY_DATABASE_URI
from microblog.config import SQLALCHEMY_MIGRATE_REPO
from microblog.app import db_object


def main():
    db_object.create_all()

    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                            api.version(SQLALCHEMY_MIGRATE_REPO))


if __name__ == '__main__':
    main()
