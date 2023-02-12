import dis

def myfunc(alist):
    return len(alist)

dis.dis(myfunc)

# 0 LOAD_GLOBAL              0 (len)
# 2 LOAD_FAST                0 (alist)
# 4 CALL_FUNCTION            1
# 6 RETURN_VALUE

# myfunc.__code__.co_names
# ('len',)
# myfunc.__code__.co_varnames
# ('alist',)



# 0 LOAD_GLOBAL : Loads the global named co_names[namei>>1] onto the stack.
# tells Python to look up the global object referenced
# by the name at index 0 of co_names and push it onto the evaluation stack.

# 2 LOAD_FAST : Pushes a reference to the local co_varnames onto the stack.

# 4 CALL_FUNCTION : tells Python to call a function; it will need to pop one 
# positional argument off the stack, then the new top-of-stack will be the function to call.

# 6 RETURN_VALUE : returns with TOS (Top Of Stack) to the caller of the function.