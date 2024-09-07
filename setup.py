from setuptools import find_packages,setup


setup(
    name="Book summarizer",
    version='0.0.1',
    author="Piyush Thakur",
    author_email="piyushthakur3613@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)