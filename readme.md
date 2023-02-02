# Null Drive

**Currently In Development**

## About

Command Line Interface tool that serves the contents of a directory as a web page. The program auto-generates the HTML and CSS for a stylish and visually appealing presentation of the files. It is designed to be run from the command prompt and provides a quick and convenient way to serve local files as a website.

## Example

`$ python ~/null-drive/serve.py --directory=~/Pictures --port=8000 --server=python`

![null drive serving ~/Files](images/example-new.png)

`$ python ~/null-drive/serve.py -d ~/Movie-Posters`

![null drive serving ~/Movie-Posters](images/example-movie-posters.png)

> Note: this looks unimpressive as is, but more advanced styling is forthcoming. 

## Dependencies 

- node.js http-server, available globally (optional)
- python 3
