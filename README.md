# Project Title

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)

## About <a name = "about"></a>

Good Vision API Project. Simple. Reads and extracts text from electronic components. 

## Getting Started <a name = "getting_started"></a>

Ensure Conda environment manages virutalization
Python 3.13
Install via requirements.txt '''pip install -r Requirements.txt'''

Sequential order: 
1) Test google api access with local workstation in test.py
2) run image_processor.py ... confirm you have a high res image with a single component to reduce overhead or api extraction difficulty
3) run extraction.py to retrieve web information and print to link.txt

If you receive gRCP errors on this then proceed to weep bitterly and be frustrated for several hours as a complete reinstallation was the only possibilty to resolve. Dependency Walker will NOT help you here...


### Prerequisites

4GB RAM
Windows 11
VMWare 
Docker


### Installing


'''conda create -n <name>=python3.13'''
'''conda activate <name>'''
'''pip install -r Requirements.txt'''
'''python test.py'''
'''python image_processor.py'''
'''python.extraction.py'''


