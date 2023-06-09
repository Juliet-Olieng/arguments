# A function named concatenate_args that takes any
#  number of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_args(*args,text=" "):
    return text.join(args)

# A function named concatenate_kwargs that takes any 
# number of string arguments in keyword arguments 
#  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    return ''.join(kwargs.values())
