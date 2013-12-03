import re
import definitions

def ParserError(Exception):
    def __init__(self, expr, pos):
        self.expr = expr
        self.pos = pos

class Parser(object):
    def __init__(self):
        self.numberM = definitions.Identifier(
            type = 'num', val = re.compile(definitions._number.regex))
        
        self.functionM = definitions.Identifier(type = 'func', val = re.compile( '|'.join( 
            [re.escape(func) for func in sorted(definitions._functions, key=lambda func: len(func), reverse=True) ] )))

        self.operatorM = definitions.Identifier(type = 'op', val = re.compile( '|'.join( 
            [re.escape(op) for op in sorted(definitions._operators, key=lambda func: len(func), reverse=True)] )))
        
        self.lBracketM = definitions.Identifier(type = 'lb', val = re.compile('\('))
        self.rBracketM = definitions.Identifier(type = 'rb', val = re.compile('\)'))

        self.matchers = (self.numberM, self.functionM, self.operatorM, self.lBracketM, self.rBracketM)


    def parse(self, iExpr):
        '''
        @iExpr -- string to parse
        @parsedExpr -- output parsed expression
        '''
        parsedExpr = []
        curPos = 0

        while curPos < len(iExpr):
            for matcher in self.matchers:
                result = matcher.val.match(iExpr, curPos)
                if result:
                    if result.re == self.numberM.val:
                        parsedExpr.append( \
                            definitions.Identifier(type = matcher.type, val = float(result.group(0))))
                    else:
                        parsedExpr.append( \
                            definitions.Identifier(type = matcher.type, val = result.group(0)))
                    curPos = result.end()
                    break
            # need to place error raising here!
            raise ParserError(iExpr, curPos)
        return parsedExpr
