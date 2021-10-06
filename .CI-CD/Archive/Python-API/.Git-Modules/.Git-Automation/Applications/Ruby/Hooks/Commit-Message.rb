#!/usr/bin/env ruby
message_file = ARGV[0]
message = File.read(message_file)

 = /\[ref: (\d+)\]/

if !.match(message)
  puts "[POLICY] Your message is not formatted correctly"
  exit 1
end
