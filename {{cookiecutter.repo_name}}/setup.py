from setuptools import setup, find_packages

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
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # add required packages here...
    ],
    extras_require={
        # add optional packages here...
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    test_suite='tests',
    zip_safe=False)
