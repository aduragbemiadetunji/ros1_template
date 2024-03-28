Header header           # timestamp is the time the reading was made
float64 value     # Measurement of the reading
float64 variance        # 0 is interpreted as variance unknown

#Add this message name to the CMakeLists.txt file in the add_message_files functions and rebuild 
#add message_generation in the find package