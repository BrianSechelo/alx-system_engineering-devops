#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: ruby script.rb <phone_number>"
  exit
end

phone_number = ARGV[0]

# Define the regular expression pattern for a 10-digit phone number
pattern = /^\d{10}$/

# Use the match method to search for the pattern in the phone number
match_data = phone_number.match(pattern)

# Check if a match is found
if match_data
  puts "Phone number: #{match_data[0]}"
else
  puts "Invalid phone number format. Please provide a 10-digit phone number."
end
