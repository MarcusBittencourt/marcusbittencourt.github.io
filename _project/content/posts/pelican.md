Title: Flying with pelican project
Category: Development
Date: 22/05/2019 23:18
Tags: python, pelican
Slug: flying-with-pelican-project
Authors: Marcus Bittencourt
Summary: Flying with pelican project

# Flying with pelican project

### Install pelican 

    :::bash

    $ pip install pelican
    $ pip install markdown
    $ pip install typogrify

### create pelican project based on quickstart template scafold 

    :::bash
    
    $ pelican quickstart

### build html static pages and run on localhost:8000  

    :::bash
    
    $ cd /_project
    $ make html
    $ make serve
