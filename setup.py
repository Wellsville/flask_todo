from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='A To-Do List built with Flask',
    author='&lt;Your actual name here&gt;',
    author_email='&lt;Your actual e-mail address here&gt;',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)