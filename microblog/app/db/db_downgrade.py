import sys

from migrate.versioning import api

from microblog.config import SQLALCHEMY_DATABASE_URI
from microblog.config import SQLALCHEMY_MIGRATE_REPO


def main():
    downgrade_on = 1
    if len(sys.argv) > 1:
        downgrade_on = int(sys.argv[1])
    version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
                  version - downgrade_on)

    print 'Current database version: '.format(api.db_version(
        SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))


if __name__ == '__main__':
    main()
