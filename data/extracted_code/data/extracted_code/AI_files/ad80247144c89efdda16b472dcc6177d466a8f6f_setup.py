from setuptools import setup, find_packages

setup(
    name='engicalc',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # e.g. 'numpy', 'pandas',
    ],
    entry_points={
        'console_scripts': [
            # Add command-line scripts here if needed
            # e.g. 'engicalc=engicalc.main:main',
        ],
    },
    author='Pascal Gitz',
    author_email='pascal.gitz@hotmail.ch',
    description='A Python package for engineering calculations and Jupyter cell outputs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PascalGitz/engicalc',  # Replace with your package's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)