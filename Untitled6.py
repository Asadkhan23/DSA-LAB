#!/usr/bin/env python
# coding: utf-8

# In[ ]:



    


# In[ ]:





# In[31]:


class py_solution:
   def is_valid_parenthese(self, str1):
    #starting the program
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        #putting parenthesis
        for parenthese in str1:
            #using loop and if/else
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
#finishing line
print("program finished")


# In[ ]:




