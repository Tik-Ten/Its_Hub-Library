from setuptools import setup, find_packages

setup(
    name="Its_Hub",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "Faker",
        "tkhtmlview",
        "opencv-python",
    ],
    author="Farbod Parkhooi(Tik Ten)",
    description="Its_Hub is a library for use Other Libraries! (;",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)