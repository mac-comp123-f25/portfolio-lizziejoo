def has_q(str):
    return 'q' in str


if __name__ == "__main__":
    assert has_q("quick") == True
    assert has_q("math") == False
    print("All tests passed!")
