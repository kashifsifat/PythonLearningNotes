#NumPy 00
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

#np_height
np_height = np.array(height)

#np_weight
np_weight = np.array(weight)

#BMI = weight / height ** 2
BMI = np_weight / np_height ** 2

print (BMI)

#NumPy 01
import numpy as np

python_list = [1, 2, 3]
print (python_list + python_list)
#This outputs [1, 2, 3, 1, 2, 3]. As the normal lists do

numpy_array = np.array([1, 2, 3])
print (numpy_array + numpy_array)
#This outputs [2 4 6]. Sequentially adding the elements of both lists

#NumPy 02
import numpy as np

BMI = np.array([21.852, 20.975, 21.75, 24.747, 21.441])
print (BMI>23)
print (BMI[BMI>23])

#This program outputs as follows:
#[False False False  True False]
#[24.747]

#Such operations can NOT be done in plain Python. There it shows error like below:
#BMI = [21.852, 20.975, 21.75, 24.747, 21.441]
#print (BMI>23)
#print (BMI[BMI>23])
#TypeError: '>' not supported between instances of 'list' and 'int'

#Note that, when trying to know how many items in a list meet the condition, it requires just using condition.
#For example, print (list_name, condition like <,>,== etc.)

#Types of NumPy Array 00
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print (type(np_height))
print (type(np_weight))

#This program outputs:
#"<class 'numpy.ndarray'>"
#"<class 'numpy.ndarray'>"

#Note that, an array can only contain a single type.
#If you change one float to be string, all the array elements will be coerced to strings,
#To end up with a homogeneous array. 

#Types of NumPy Array 01
import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                [65.4, 59.2, 63.6, 88.4, 68.7]])

print (np_2d.shape)
#This program outputs: (2, 5). That means, 2 rows, 5 columns
#Shape attribute can be used to get more information about what the data structure looks like
#However, the indentation is NOT the matter for writing the array
#But, the brackets matter
#See the format: np.array([[fisrt_list],[second_list]])

#Subsetting NumPy Array 00
import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                [65.4, 59.2, 63.6, 88.4, 68.7]])

print (np_2d[1,-1])
print (type(np_2d))
#This program outputs:
#68.7
#<class 'numpy.ndarray'>
#To print a specific item of a specific list use the format as below:
#print (array_name [list_number_in_array, item_number_in_that_list])

print (np_2d[0,:])
#This program outputs all items in first list (index 0)
#[1.73 1.68 1.71 1.89 1.79]

print (np_2d[1,:])
#This program outputs all items in first list (index 1)
#[65.4 59.2 63.6 88.4 68.7]

print (np_2d[:,2])
#This program outputs the third items (index 2) from both lists
#[1.71 63.6]

print (np_2d [:,1:4])
#This program outputs second to fourth items (index 1 to 3) of both lists
#[[ 1.68  1.71  1.89]
#[59.2  63.6  88.4 ]]

print (np_2d[:])
#This program outputs all items of both lists
#[[ 1.73  1.68  1.71  1.89  1.79]
#[65.4  59.2  63.6  88.4  68.7 ]]

#Each sublist in a list, corresponds to a row in a two dimensional numpy array