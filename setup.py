import os
import setuptools

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-relativedeltastore",
    version="0.9.0",
    author="anfema GmbH",
    author_email="contact@anfe.ma",
    description="Django model field to store relativedelta from python-dateutil",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/anfema/django-relativedeltastore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'python-dateutil',
        'Django>=2.2',
    ],
    # test_suite='runtests.run_tests',
    zip_safe=False,
)
