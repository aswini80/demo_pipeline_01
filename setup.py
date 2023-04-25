from setuptools import setup, find_packages

setup(
    name ="census_income",
    version='0.0.1',
    author='aswini',
    author_email = "aswinikk@gmail.com",
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn','flask']
)