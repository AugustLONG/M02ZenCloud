# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from ZenCloud import create_app

app = create_app()
manager = Manager(app)

@manager.command
def run():
    """Run in local machine."""
    
    app.run

    
if __name__ == "__main__":
    manager.run()
"""
(venv)shiyanlou:shiyanlou_cs354/ (master*) $ python manage.py run    [22:08:13]
/home/shiyanlou/Code/shiyanlou_cs354/venv/local/lib/python2.7/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
  warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')
"""