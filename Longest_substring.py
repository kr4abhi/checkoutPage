def longest_substring(s: str) -> str:
    # Initialize variables to track the start and end of the longest substring
    start = 0
    end = 0
    # Initialize a dictionary to store the last seen index of each character
    char_index = {}
    # Initialize the length of the longest substring
    max_length = 0
    # Initialize the start index of the longest substring
    max_start = 0

    for i, char in enumerate(s):
        # If the character is already in the dictionary and its index is after the start of the current substring
        if char in char_index and char_index[char] >= start:
            # Update the start index of the current substring to the index after the last occurrence of the character
            start = char_index[char] + 1
        # Update the last seen index of the character
        char_index[char] = i
        # Update the end index of the current substring
        end = i
        # Update the length of the current substring
        length = end - start + 1
        # If the current substring is longer than the longest substring found so far
        if length > max_length:
            # Update the length and start index of the longest substring
            max_length = length
            max_start = start

    return s[max_start:max_start + max_length]

# Example usage:
input_str = "uusiovjojdoidijdojo"
print("Longest substring without repeating characters:", longest_substring(input_str))
