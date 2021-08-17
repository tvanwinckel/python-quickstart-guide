import src.hello_world as hello_world_module

def test_hello_world():
    assert hello_world_module.hello_world() == "hello world"