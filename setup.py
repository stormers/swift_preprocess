from setuptools import setup, find_packages

version = "0.1"

setup(
    name="swift_preprocess",
    version=version,
    description='OpenStack Swift middleware to preprocess objects',
    license='Apache License (2.0)',
    author='Alan Vitor S. Anselmo',
    author_email='avanselmo@gmail.com',
    url='https://github.com/stormers/swift_preprocess',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7'],
    install_requires=["swift"],
    test_suite='py.test',
    tests_require=["pytest"],
    scripts=[],
    entry_points={
        'paste.filter_factory': ['preprocess=swift_preprocess:filter_factory']})
