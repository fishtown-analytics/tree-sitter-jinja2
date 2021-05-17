import os
from platform import system
from setuptools import Extension, setup

setup(
    name="tree-sitter-jinja2",
    version="0.0.1",
    platforms=["any"],
    python_requires=">=3.6",
    packages=[os.path.abspath("bindings/python3/tree-sitter-jinja2")],
    install_requires=[
        'tree_sitter==0.19.0'
    ],
    ext_modules=[
        Extension(
            "tree-sitter-jinja2",
            [os.path.abspath("./bindings/python3/include/tree-sitter-jinja2.c")],
            [os.path.abspath("./bindings/python3/include")],
            extra_compile_args=(
                ["-std=c99", "-fPIC"] if system() != "Windows" else None
            ),
        )
    ],
)
