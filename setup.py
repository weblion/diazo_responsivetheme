from setuptools import find_packages
from setuptools import setup


setup(
    author="Rob Porter",
    author_email="robzonenet@gmail.com",
    classifiers=[
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python :: 2.7',
    ],
    description="collective.responsivetheme reimplemented with Diazo.",
    keywords='Diazo Modern Plone Sunburst Theme Theming Responsive',
    include_package_data=True,
    long_description=(
        open("README.rst").read() + '\n' +
        open("HISTORY.txt").read()
    ),
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    license="GPL2",
    name='plonetheme.diazo_responsivetheme',
    namespace_packages=[
        'plonetheme',
    ],
    packages=find_packages(),
    url="",
    version="1.1",
    zip_safe=False,
    install_requires=[
          'setuptools',
          'plone.app.theming',
          'kreagroup.jsi18n',
          # -*- Extra requirements: -*-
      ],
)
