from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(    
        name="SAFD", 
        version="0.0.1",
        author="Shayan Shafaghi",
        author_email="shayandesh@gmail.com",
        description="Simple As Fuck Dispatcher",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/nothingrealm/SAFD",
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "Environment :: Web Environment",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Internet :: WWW/HTTP :: WSGI",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
            "Topic :: Software Development"
        ],
        packages=find_packages(exclude=['tests'])
    )
