# the contruction of custom exception class can enrich our class design.A custom erro class couldlogs error,inspect an object.
'''Import inspect as ipt
def tree_class(cls,ind=0):
    print('-'* ind, ind =0):
    for k in cls.__subclasses__():
        tree_class(k, ind+3)
print("Inbuilt exception is:")
ipt.getclasstree( ipt.getmro(BaseException))
tree_class(BaseException)     '''

# ZeroDivision Error and Floating point error.
#number=6
#eroErro=6/0



# lookup error is raised when a wrong key is used to access a dictionary value.
x="python"
try:
    print(x[10])
except lookError as e:
    print(f"{e},{e.__class__}") 



# Import error occur when the python program trie to import modulewhich does not exist in the privete table.
# ModuleNotFoundErroe -this error is occurs when you are trying to access or use a module that cannot be found.


''' Expicit is better than implicit
Flat is better than nested 
keep your try/except blocksnarrow
remote on tools'''