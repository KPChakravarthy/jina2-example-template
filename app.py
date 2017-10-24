#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Jinja2 static site renderer using Flask
    @author   Tarun Bhardwaj
    @license  FreeBSD Licence
"""
from flask import Flask, abort, render_template
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route("/")
@app.route("/<path>")
def main(path=None):
    if not path:
        path = 'index.html'
    try:
        return render_template(path)
    except TemplateNotFound:
        abort(404)

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', 5000)
