my_str="I like apple"
sub_str="orange"
new_value=my_str.replace("apple","orange")
print(new_value)

my_str= "blue sky"
sub_str="red"
sub_str1="sky blue"


new_value=my_str.replace("sky",sub_str1)
modified_value= new_value.replace("blue","red",1)


print(modified_value)

my_str="Hello world"
sub_str="_"
new_value=my_str.replace(" ","_")
print(new_value)


my_str="1.2.3"
sub_str="-"
new_value=my_str.replace(".","-")
print(new_value)