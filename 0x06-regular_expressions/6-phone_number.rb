#!/usr/bin/env ruby
# Pass the argument to the script
p_number = ARGV[0]
# Define the pattern for the regular expression
pattern = /^\d{10}$/
# check if p_number matches the pattern
if p_number.match?(pattern)
    puts p_number
end
