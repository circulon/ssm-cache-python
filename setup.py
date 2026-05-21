""" Setup command """
from setuptools import setup, find_packages


LONG_DESCRIPTION = open('README.md').read()

setup(
    name='ssm-cache',
    version='2.11',
    description='AWS System Manager Parameter Store caching client for Python',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords=['aws', 'amazon-web-services', 'aws-lambda', 'aws-ssm', 'parameter-store'],
    license="MIT",
    author='Alex Casalboni',
    author_email='alex@alexcasalboni.com',
    url='https://github.com/alexcasalboni/ssm-cache-python',
    download_url='https://github.com/alexcasalboni/ssm-cache-python/archive/2.11.tar.gz',
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    install_requires=['boto3'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
