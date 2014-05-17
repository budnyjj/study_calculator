import calculator as calc
import calculator.definitions as dfs

# define basic logical constants and operations
dfs._operators['not'] = dfs.Operator(leftAssoc = False, priority = 4, argCount = 1, alg = lambda args: not args[0])
dfs._operators['and'] = dfs.Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: args[0] and args[1])
dfs._operators['or'] = dfs.Operator(leftAssoc = True, priority = 3, argCount = 2, alg = lambda args: args[0] or args[1])

dfs._functions['t'] = dfs.Function(argCount = 0, alg = lambda args: True)
dfs._functions['f'] = dfs.Function(argCount = 0, alg = lambda args: False)

c = calc.Calculator(logLevel='debug', logFilename='calc.log') 
print c.calculate("sin(pi/2)") # == 1

# change function behavior
dfs._functions['sin'] = dfs.Function(argCount = 1, alg = lambda args: 0)
print c.calculate("sin(pi/2)") # == 0

# test logical functions
print c.calculate("t() and f()") # = False
print c.calculate("t() or f()") # == True
print c.calculate("t() and not f()") # == True
print c.calculate("(f() or t()) and (t() and not f())") # == True
