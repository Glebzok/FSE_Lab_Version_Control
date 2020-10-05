from storage import Storage


def test_add():
    st = Storage({})
    key_1, value_1 = 'a', 1
    st.add(key_1, value_1)
    assert key_1 in st.data.keys(), "Pair not added"
    assert st.data[key_1] == value_1, "Added wrong value"
    try:
        st.add(key_1, value_1)
    except KeyError:
        pass
    else:
        assert False, "Exeption about existing key not raised"


def test_remove():
    pass


def test_set():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = 3
    st.set(key,val)
    assert st.data[key] == val, "Value for the key {} was not changed".format(key) 
    key = 'c'
    val = 4
    try:
        st.set(key,val)
    except KeyError as e:
        pass
    else:
        assert True  == False, "Keyerror exception was not raised for invalid key"



def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"


def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()


if __name__ == "__main__":
    run_tests()
