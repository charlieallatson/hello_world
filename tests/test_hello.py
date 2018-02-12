"""
Tests the hello module
"""
import pytest
import hello


def test_hello_no_name():
    """
    Checks if no name is passed we get hello world
    """
    assert hello.hello() == 'Hello, world'
    
def test_hello_with_name():
    """
    If passed a name return 'hello {name}'
    """
    assert hello.hello('Charlie') == 'Hello, Charlie'
