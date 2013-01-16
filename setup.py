from setuptools import setup, find_packages

version = '2013.01.16'

setup(name='js.jquery_iframe_transport',
      version=version,
      description="jQuery Ajax transport plugin for iframe-based file uploads.",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christoph Handel',
      author_email='',
      url='',
      license='MIT or GPL2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools-git'],
      install_requires=[
          'fanstatic',
          'setuptools',
          'js.jquery',
      ],
      entry_points={
          'fanstatic.libraries': ['jquery_iframe_transport = js.jquery_iframe_transport:library', ],
      }
      )
