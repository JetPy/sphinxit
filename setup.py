from setuptools import setup, find_packages


setup(
    name='sphinxit',
    version='0.3.2',
    author='Roman Semirook',
    author_email='semirook@gmail.com',
    packages=find_packages(),
    license='BSD',
    url='https://github.com/semirook/sphinxit',
    description='Lite and powerful SphinxQL query constructor',
    long_description='Lite and powerful SphinxQL query constructor',
    install_requires=[
        "six >= 1.1.0",
        "oursql3 @ git+https://github.com/sqlobject/oursql.git@b5f3be2d92671b41856f2933790b2f32814b1c10#egg=oursql3",
        "ordereddict >= 1.1",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
