from setuptools import setup

setup(name='petclassifier',
        version='0.1',
        description='Classify events from Positron Emission Tomography',
        url='http://github.com/daria137/petclassifier',
        author='Daria Kisielewska',
        author_email='dk.dariakisielewska@gmail.com	',
        license='MIT',
        packages=['petclassifier'],
        install_requires=[
            'uproot','numpy','matplotlib','tensorflow','pandas'
            ],
        zip_safe=False)
