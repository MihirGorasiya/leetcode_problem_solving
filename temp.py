words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
answer = []

temp_words = []  # To store words for the current line
current_length = 0  # Current length of words without spaces

for word in words:
    # Check if adding the next word exceeds maxWidth
    if current_length + len(word) + len(temp_words) > maxWidth:
        # Calculate the number of spaces to add
        total_spaces = maxWidth - current_length
        if len(temp_words) == 1:
            # If only one word in the line, left-justify it by adding spaces to the right
            answer.append(temp_words[0] + " " * total_spaces)
        else:
            # Distribute spaces between words
            space_between_words = total_spaces // (len(temp_words) - 1)
            extra_spaces = total_spaces % (len(temp_words) - 1)

            for i in range(extra_spaces):
                temp_words[i] += " "  # Add extra space to the first few words

            # Join the words with evenly distributed spaces
            answer.append((" " * space_between_words).join(temp_words))

        # Reset for the next line
        temp_words = []
        current_length = 0

    # Add the current word to the line
    temp_words.append(word)
    current_length += len(word)

# Handle the last line (left-justified)
last_line = " ".join(temp_words)
answer.append(last_line + " " * (maxWidth - len(last_line)))

# Print the justified text
for line in answer:
    print(f"'{line}'")
