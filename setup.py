from setuptools import setup, find_packages

    
setup(
    name='finmodels',
    version='2.0.4',
    packages=find_packages(),
    install_requires=[],
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='finmodels is a Python package that provides various financial models for analysis and optimization.',
    long_description=long_description,  # Add this line
    long_description_content_type='text/markdown',  # Specify the content type if using Markdown
    url='https://github.com/arjunlimat/finmodels',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)
