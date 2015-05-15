from setuptools import setup

setup(
    name='flask-sqlalchemy-booster',
    version='0.1.3',
    long_description='A wrapper around Flask-SQLalchemy',
    packages=['flask_sqlalchemy_booster'],
    include_package_data=True,
    install_requires=[
        "toolspy>=0.1.",
        "Flask>=0.10.1",
        "SQLAlchemy>=0.9.8",
        "Flask-SQLAlchemy>=2.0"
        ],
    license='MIT',
    author='SuryaSankar',
    author_email='suryashankar.m@gmail.com')
