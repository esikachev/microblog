import imp

from migrate.versioning import api
from microblog.app import db_object
from microblog.config import SQLALCHEMY_DATABASE_URI
from microblog.config import SQLALCHEMY_MIGRATE_REPO


def main():
    migration = '{}/versions/{:03d}_migration.py'.format(
        SQLALCHEMY_MIGRATE_REPO, api.db_version(SQLALCHEMY_DATABASE_URI,
                                                SQLALCHEMY_MIGRATE_REPO) + 1)
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI,
                                 SQLALCHEMY_MIGRATE_REPO)
    exec old_model in tmp_module.__dict__
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                              SQLALCHEMY_MIGRATE_REPO,
                                              tmp_module.meta,
                                              db_object.metadata)
    open(migration, "wt").write(script)
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

    print 'New migration saved as {}'.format(migration)
    print 'Current database version: {}'.format(api.db_version(
        SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))


if __name__ == '__main__':
    main()
