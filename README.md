# Useful-Python-Tools
A collection of tools I have created for working in python.


<h3>ClassGenerator</h3>


  
A python scripts which generates a basic start to a class structure in python: __init__ and getters and setters for a list of attributes passed in. Though most uses of it will need adjustment afterward, such as assigning default values if not passed in with the list of attributes and custom methods.
    
Also included test_create_class.py to demonstrate usage.
    




<h3>dependency</h3>


  
A method to check a given python script and produce a list of all imported libraries.
    
The intended usage of this is to ease the task of labelng non-core-Python-API dependencies in a project manifest.
    
Coming Soon: a way to compare this list against a particular version of Python to determine what may need installed along with the release of the project, though it will be quite some time before this need actually makes it into my current project.
    


<h3>webgen</h3>

A script to add docstring comments into a python script so that it's ready to run through a documentation generator. The course where I created this for had students using pdoc3, but it generates the docstrings in "Google Notation" for python documentation generators.

Here's a video walkthrough for WebGen I made for the students in the course it was originally created for: https://www.youtube.com/watch?v=ccnf5onD540 




