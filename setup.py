import setuptools
 
 
setuptools.setup(
    name="cztest",
    version="0.0.1",
    author="Paul Jaworski",
    author_email="ronlesteve@ronlesteve.com",
    description="Package to create commitzien",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)