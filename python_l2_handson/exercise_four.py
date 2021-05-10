import re

# digit at the beginning of the string and a digit at the end of the string
pattern_one = r'^\d+.+\d$'

# A string that contains only whitespace characters or word characters
pattern_two = r'[\s\w]+'

# A string containing no whitespace characters
pattern_three = r'[\S]+'
