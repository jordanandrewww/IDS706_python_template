from hello import say_hello, add

# Checks that the appropriate hello message is printed for Annie
def test_say_hello():
    assert (
        say_hello("Annie")
        == "Hello, Annie, welcome to Data Engineering Systems (IDS 706)!"
    )

# adds 2 and 3 together and checks if it equals 5
def test_add():
    assert add(2, 3) == 5
