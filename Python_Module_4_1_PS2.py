
# coding: utf-8

# In[2]:


def filter_long_words(list_strings, n):
    list_long_words = []
    for s in list_strings:
        if(len(s) > n):
            list_long_words.append(s)
    return list_long_words

input_l = input("Please enter a list of strings separated by commas: ")
num = int(input("Please enter the length to filter by: "))
input_list = []

for str in (input_l.split(",")):
    input_list.append(str)
     
print("The list of words entered whose length is greater than ", num, " is: ", filter_long_words(input_list, num))

        

