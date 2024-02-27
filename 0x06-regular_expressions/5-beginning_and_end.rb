#!/usr/bin/env ruby
# Get the argument passed to the script
 input_string = ARGV[0]

# Define the regular expression pattern
 pattern = /^h.n$/

 # Check if the input string matches the pattern
 if input_string.match?(pattern)
   puts input_string
 end
