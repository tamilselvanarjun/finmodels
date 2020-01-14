from setuptools import setup, find_packages

<<<<<<< HEAD
setup(
    name='quantmodels',  # Replace with your package name
    version='1.0.0',  # Replace with your package version
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your script might have
        # For this example, there are no additional dependencies
    ],
    entry_points={
        'console_scripts': [
            'quantmodels = quantmodels.opm:binomial_option_pricing',  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='A python based financial models simulation to estimate the value of π',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arjunlimat/quantmodels',  # Update with your GitHub repository URL
=======
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='finmodels',
    version='2.0.3',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'cvxpy',
    ],
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='finmodels is a Python package that provides various financial models for analysis and optimization.',
    long_description=long_description,  # Add this line
    long_description_content_type='text/markdown',  # Specify the content type if using Markdown
    url='https://github.com/arjunlimat/finmodels',
>>>>>>> 726b3315a24d8f382b3b486500d2fcddce8e5b4d
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
<<<<<<< HEAD
    python_requires='>=3.6',
=======
>>>>>>> 726b3315a24d8f382b3b486500d2fcddce8e5b4d
)
