"""This module is a simple unit testing framework for better_addition.py"""

class UnitTest(object):

    """The call of this class UnitTest(better_addition, [a, b],
    {'num_rechecks': n}, r) tests better_addition.py. a and b are function
    parameters, n is the number or rechecks to be done and r is what 
    better_addition.py should have returned."""

    def __init__(self, func, args, kwargs, res):    # make test
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res    

    def __call__(self):                             # run test
        func = self.func
        args = self.args
        kwargs = self.kwargs
        res = self.res
       	
       	try:
       		  better_result = func(args[0], args[1], kwargs.get("num_rechecks"))
       	except IndexError:
       		  return False

       	if res != better_result:
       		  return False

        return True

