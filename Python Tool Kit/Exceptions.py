# error handeling:
def someExpressionOrFunc():
    pass

try:
    someExpressionOrFunc()
except:
    print("now we handling the error, any error")
else:
    print("if no exception is raised, we can add else block that will deal with this case.")
finally:
    print("no matter what the finally part will be executed")

try:
    someExpressionOrFunc()
except StopIteration:
    print("Raised when the next() method of an iterator does not point to any object.")
except (SystemExit, ArithmeticError):
    print("one of this error occured: (SystemExit, ArithmeticError)")
    print("SystemExit: Raised by the sys.exit() function.")
    print("ArithmeticError: Base class for all errors that occur for numeric calculation.")
except OverflowError:
    print("Raised when a calculation exceeds maximum limit for a numeric type.")
except ZeroDivisionError:
    print("Raised when division or modulo by zero takes place for all numeric types.")
except AssertionError:
    print("Raised in case of failure of the Assert statement")
except AttributeError:
    print("Raised in case of failure of attribute reference or assignment")
except EOFError:
    print("Raised when there is no input from either the raw_input() or input() function and the end of file is reached")

try:
    someExpressionOrFunc()
except LookupError:
    print("Base class for all lookup errors.")
except IndexError:
    print("Raised when an index is not found in a sequence")
except KeyError:
    print("Raised when the specified key is not founc in the dictionary")

# there are more error types!!

try:
    raise ValueError
except ValueError:
    print("when a func is called with wrong values")
    print("Raised when the built-in function for a data type has the valid type of arguments, but the arguments have"
          " invalid values specified.")


