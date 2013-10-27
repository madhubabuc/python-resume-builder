PYTHON-RESUME-BUILDER
=====================
This project uses a python template system to produce many output formats of the same resume.  The resume is stored directly in python source code and pushed through the jinja template system (similar to Django) to plain text, html and tex source.  The tex source can then be compiled to PDF using pdflatex.  
  
REQUIREMENTS
------------

For HTML and TXT exports:
- python 2.7
- jinja2

For PDF:
- pdflatex                    (tested with debian package texlive-full)  
- a *LOT* of LaTeX packages.  (tested with debian package texlive-full package)  
  
INSTRUCTIONS
------------
From the project directory, run:
```
~$ sudo pip install requirements.txt
~$ ./build_resume.py [source_file.py]
```
For pdf export:
```
~$ pdflatex [source_file.tex]
```
  
TO-DO
-----
- Update main script to validate arguments  
- Add usage statement to main script
- add support for JSON resumes
