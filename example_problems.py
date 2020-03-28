"""
Below are some example problems to give you some extra practice and also to get you used to processes that are commonly used to
solve programming problems. You should attempt to solve these questions yourself before viewing the solutions.
"""

"""
1. Write a function that takes a number x as input and returns a tuple with the first element being 3*x and the second element
being x^2 + 1.

2. Write a function that takes as input 3 numbers, x, y, and z. If z > y > x, return z. Otherwise, return x

3. Write a function that takes a list of numbers l as input, and returns the sum of that list. Do not use the built in sum()
method.

4. Write a function that takes a list of numbers l as input and returns the number of elements in that list that are a multiple
of 3.

5. Write a function that takes a list of lists of numbers (eg [[1,2],[3,4]]) and returns a new list where the elements in that
list are the sums of the sublists. In the case of the list mentioned earlier, the function should return [3,7]

6. Write a function that takes 2 lists of numbers that are assumed to be the same length, l1 and l2. It should return a new
list L where L[i] is equal to l1[i] + l2[i]. This is called elementwise addition and is significantly easier to do with the
numpy library.

7. Write a function that takes a sentence as a string as input. It should remove all the spaces in the string and combine all
the words into one big word. For example f7('Hello beautiful world') should return 'Hellobeautifulworld'. The built in replace()
function can do this pretty easily. For an extra challenge, try using the split() method to split the sentence by the spaces into
a list of words and then adding the words together with a for loop.

8. Write a function that takes 2 dictionaries as input d1 and d2. It should return a new dictionary where the key value pairs of
d2 are 'added' onto d1. For example suppose d1 = {'a':1, 'b':2} and d2 = {'a':-1, 'c':3}. Then f8(d1, d2) should return {'a':0, 'b':2, 'c': 3}.

9. Write a function that takes 2 numbers as input a and b. Have the function return a / b if b is not equal to zero and the
string 'Cannot divide by zero' if b is 0. You can either use an if statement or a try/except statement to do this problem. For
extra practice try the problem using both methods.

10. Write a function that takes a list of numbers l as input. It should return the sum from i = 0 to the length of l of l[i] * i.
For example suppose l = [4,2,7,3]. Then f10(l) should return 4 * 0 + 2 * 1 + 7 * 2 + 3 * 3 = 0 + 2 + 14 + 9 = 25.
"""




"""
Answers
"""

def f1(x):
    return (3*x, x**2 + 1)
    """
    When returning a tuple of a fixed number of elements like in this case, the parentheses are often left out so
    return 3*x, x**2 + 1 is also acceptable
    """

def f2(x, y, z):
    """
    In this case, 2 boolean conditions z > y and y > x have to be satisfied at the same time in order for z to be returned. The 'and'
    operator can be used in this case to combine the conditions, so that True and True returns True, True and False (or vise versa)
    returns False, and False and False returns False.
    """
    if (z > y) and (y > x):
        return z
    else:
        return x

def f3(l):
    """
    A common strategy for these types of problems is to initialize a variable as a 'result' variable that will eventually be returned
    and then iterating over your list, making incremental changes to the result variable as each element is visited. In this case, you
    should initialize a variable called res = 0, and then as you iterate over the elements in l, add each element to res. Since res
    started out as 0, if should be equal to the sum of the list after all the elements have been iterated over.
    """
    res = 0
    for x in l:
        res = res + x #res += x can be used as a shorthand for this
    return res

def f4(l):
    """
    We want to be able to test each element to see if it is a multiple of 3 and then if it is, take note of each case so that what we return
    is the number of cases in the list where this happened. Create a result variable called res, iterate over the elements in l and with
    each element, increment res by 1 if the element is a multiple of 3 (this can be tested with the boolean condition x % 3 == 0).
    """
    res = 0
    for x in l:
        if x % 3 == 0:
            res += 1
    return res

def f5(l):
    """
    We should take the same approach creating a result variable and modifying it as we iterate over l. In this case though the result variable
    will be a list that we append values to. And when we use a for loop such as for x in l, x is now a list instead of a number so we will want to
    take the sum of x, the iteration variable and add these results to the result variable. But what should we initialize the result variable as?
    It should start out as an empty space that we can add to so the the result will be a lists of the sums of the sublists. In this case, an empty
    list [] would be the answer, since this can be appended to.
    """
    res = []
    for x in l:
        res.append(sum(x))
    return res

def f6(l1,l2):
    """
    In this case, we should iterate over the lists, but we need to do it in a way where we can track the index location of wherever we're at in
    the lists and then add l1[i] + l2[i] to the result list. A common way to iterate over lists where we not only need the value of the iteration
    variable but also the index location of where we're at is to iterate over a range from 0 to the length of the list. For example the loop
    for i in range(5) has the same effect as doing for i in [0,1,2,3,4]. This is helpful because if we are iterating over a list using this range
    method, we could say

    for i in range(len(l)):
        x = l[i]

    We now have access to the iteration variable x as well as the index location of x which is i. In this case there are 2 iteration variables l1[i]
    and l2[i] that we need to add together and append to the result list.
    """

    res = []
    for i in range(len(l1)): #l1 and l2 have the same length so id doesn't matter which list you use
        res.append(l1[i] + l2[i])
    return res

def f7(s):
    """
    return s.replace(' ', '') makes use of the replace method. We are going to use the second method here. You can use the built in split() method
    to split a space separated sentence into a list of individual words. Then we can initialize a result variable and add the words to that result variable.
    In this case, the result variable should be initialized as an empty string so that we can add the words one by one as we iterate over the list.
    """
    res = ''
    words = s.split()
    for word in words:
        res = res + word
    return res

def f8(d1, d2):
    """
    An approach here would be to initialize a result dictionary D as a copy of d1, and then iterate over the key value pairs in d2. With each key in d2, if the
    key does not exist in D then create a new key value pair in D so that the key is the key that you are currently on in the iteration and the value is the
    corresponding value d2[key]. If the key already is in D, then the value in d2 that corresponds to that key should be added to the existing value for
    the corresponding key in D. Notice there is symmetry in this problem. You could swap the roles of d1 and d2 and you would have the same result afterwards.
    A subtle note is that if you initialize D as d1 then by changing D, you would also be changing d1 even if you are not explicitly doing so in the code. This is
    because D and d1 are located at the same spot in memory so by changing one, you will inadvertently change the other. You can get around this by saying
    D = d1.copy(). This makes it so D is identical to d1 but is not located in the same space in memory, so you can change D without changing d1.
    """
    D = d1.copy()
    for k in d2:
        if k not in D:
            D[k] = d2[k]
        else:
            D[k] += d2[k]

    """
    Notice that when you iterate over a dictionary, you are actually iterating over the keys in the dictionary. The statement k in D is the same thing as
    k in D.keys()
    """

def f9(a,b):
    #METHOD 1
    if b != 0:
        return a / b
    else:
        return 'cannot divide by zero'

def F9(a,b):
    #METHOD 2
    try:
        return a / b
    except ZeroDivisionError:
        return 'cannot divide by zero'
    """
    Note: you could just say

    except:
        return 'cannot divide by zero'

    And it would have the same effect. In practice though if you're using try/except statements, it is best to address the specific error that you are
    anticipating. Otherwise you can have situations where your code is silently running even if it encounters an error that you were not expecting. This
    makes it hard to tell when things have gone wrong if they have.
    """

def f10(l):
    """
    This is another case where you will want to keep track of the index location as well as the value of your iteration variable.
    """
    res = 0
    for i in range(len(l)):
        res += i * l[i]
    return res

print(f1(2))
print(f2(1,2,3))
print(f3([4,3,6]))
print(f4([6,4,1,4,7,8,3]))
print(f5([[1,2],[3,4]]))
print(f6([1,2],[3,4]))
print(f7('Hello Beautiful World'))
print(f8({'a':1, 'b':2}, {'a':-1, 'c':4}))
print(f9(5,3))
print(F9(5,0))
print(f10([4,2,7,3]))
