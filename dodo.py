def task_coverage():
    """Generate test coverage.xml."""
    return {
        "actions": [
            'coverage run --source=. -m unittest discover '
            '-s tests -p "*_test.py"',
            'coverage xml'
        ]
    }


def task_ut():
    """Execute all unit tests."""
    return {
        "actions": [
            'python -m unittest discover -s tests -p "*_test.py"'
        ]
    }


def task_lint():
    """Lint the code with flake8."""
    return {
        "actions": [
            'flake8'
        ]
    }


def task_html():
    """Create a html version of the documentation."""
    return {
        "actions": [
            'pdoc --html --output-dir documentation code --force'
        ]
    }


def task_pdf():
    """Create a markdown version of the documentation."""
    return {
        "actions": [
            'pdoc --force --output-dir=documentation/docs code'
        ]
    }


def task_dependency():
    """Create a dependency graph as .png."""
    return {
        "actions": [
            'pydeps --noshow -T png -o '
            'documentation/UML/DependencyGraphUML.png code'
        ]
    }
