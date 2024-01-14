from setuptools import setup, find_packages

setup(
    name='document_text_extractor',
    version='1.0.0',
    author='Harshad Yadav',
    author_email='harshadyadav20@gmail.com',
    description='Extracts text from the file that is image or pdf type',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'uvicorn>=0.25.0',
        'fastapi>=0.109.0',
        'python-multipart>=0.0.6',
        'pytesseract>=0.3.10',
        'Pillow>=10.2.0',
        'PyMuPDF>=1.23.12',
    ],
    package_data={
      'document_text_extractor': ['data/*.ini'],
   },
   include_package_data=True,
)
