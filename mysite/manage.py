
"""Django's command-line utility for administrative tasks."""
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django
django.setup()

from django.db import connection



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1] == 'runserver':
        cursor = connection.cursor()
        tables = connection.introspection.get_table_list(cursor)
        if len(tables) == 0:
            execute_from_command_line(['manage.py','migrate'])
            execute_from_command_line(['manage.py','loaddata','users/fixtures/users.json'])
            execute_from_command_line(['manage.py','loaddata','posts/fixtures/posts.json'])
            # execute_from_command_line(['manage.py','loaddata','posts/fixtures/votes.json'])
        print('##################################################')
        print('admin: admin@locdedatcucapul.ro')
        print('pass: test12')
        print('##################################################')
        print('user: dsl400@gmail.com')
        print('pass: RandRand12')
        print('##################################################')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
