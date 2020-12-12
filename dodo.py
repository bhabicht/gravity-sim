def task_coverage():
    """generate test coverage.xml"""
    return {
        "actions": [
            'coverage run --source=. -m unittest discover '
            '-s tests -p "*_test.py"',
            'coverage xml'
        ]
    }


def task_ut():
    """execute all unit tests"""
    return {
        "actions": [
            'python -m unittest discover -s tests -p "*_test.py"'
        ]
    }


def task_lint():
    """lint the code with flake8"""
    return {
        "actions": [
            'flake8'
        ]
    }


def task_html():
    """create a html version of the documentation"""
    return {
        "actions": [
            'pdoc --html --output-dir documentation code --force'
        ]
    }
