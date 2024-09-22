# functions.py
import pytest


def q1(message, k):
    # find simple solution
    cut_message = message.rstrip(" ")
    if len(message) <= k:
        return message

    # Need to cut words
    cut_message = cut_message[:k-4]
    # Not finish with a space - we are in middle of word that should be cut
    if cut_message and cut_message[len(cut_message)-1] != " ":
        last_space_index = len(cut_message)-1
        while last_space_index > 0 and cut_message[last_space_index] != " ":
            last_space_index -= 1
        cut_message = cut_message[:last_space_index]
        # We found whole word
    return cut_message + " ..."

def q2(input_list):
    return input_list

def q3(input_list):
    return input_list

# test_functions.py

@pytest.mark.q1
def test_q1_short_message():
    message = "Hello, world!"
    k = 15
    expected_output = "Hello, world!"
    assert q1(message, k) == expected_output

@pytest.mark.q1
def test_q1_long_message():
    message = "This is a very long message that needs to be truncated."
    k = 20
    expected_output = "This is a very ..."
    assert q1(message, k) == expected_output

@pytest.mark.q1
def test_q1_exact_length_message():
    message = "Exactly 20 characters."
    k = 20
    expected_output = "Exactly 20 characters."
    assert q1(message, k) == expected_output

@pytest.mark.q1
def test_q1_empty_message():
    message = ""
    k = 10
    expected_output = ""
    assert q1(message, k) == expected_output

@pytest.mark.q1
def test_q1_long_word():
    message = "This is an extremelylongwordthatneedstobetruncated."
    k = 20
    expected_output = "This is an ..."
    assert q1(message, k) == expected_output


@pytest.mark.q2
def test_q2():
    input_data = [1, 2, 3, 4, 5]
    assert q2(input_data) == input_data

@pytest.mark.q2
def test_q2_varied():
    input_data = [0, -1, -2]
    assert q2(input_data) == input_data

@pytest.mark.q3
def test_q3():
    input_data = [1, 2, 3, 4, 5]
    assert q3(input_data) == input_data

@pytest.mark.q3
def test_q3_varied():
    input_data = ['a', 'b', 'c']
    assert q3(input_data) == input_data

