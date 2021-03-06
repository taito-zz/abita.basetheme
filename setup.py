from setuptools import find_packages
from setuptools import setup


setup(
    name='abita.basetheme',
    version='0.6',
    description="ABITA Base Theme",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='ABITA',
    author_email='taito.horiuchi@abita.fi',
    url='http://abita.fi/',
    license='Non-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['abita'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.base',
        'setuptools',
        'z3c.jbot'],
    extras_require={'test': ['Products.CMFPlacefulWorkflow', 'hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
