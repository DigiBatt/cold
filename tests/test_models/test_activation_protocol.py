import pytest,os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(),'..',"..", 'examples')))
print(sys.path)
from examples.test_protocols import activation_test_protocol


def test_activation_protocol():
    result= activation_test_protocol.activation_test_protocol()
    assert isinstance(result, dict), "Expected a dictionary but got a different type"