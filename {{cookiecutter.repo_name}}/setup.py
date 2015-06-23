from setuptools import setup

# ----------------------------------------------------------------------------
# {{ cookiecutter.project_name | capitalize }}
# ----------------------------------------------------------------------------
setup(
    name='{{ cookiecutter.project_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=open('README.md').read(),
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    packages=[
        '{{ cookiecutter.project_name }}',
    ],
    install_requires=[
        # add required packages here...
    ],
    extras_require={
        # add optional packages here...
    },
    test_suite='tests',
    zip_safe=False)
