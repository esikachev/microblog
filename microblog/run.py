#!flask/bin/python

from microblog.app import app


def run_app():
    app.run(debug=True)


if __name__ == '__main__':
    run_app()
