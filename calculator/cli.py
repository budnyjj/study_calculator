#!/usr/bin/python2

import calculator as calc

def main():
	print "This is calculator for basic math expressions."
	print "Input correct expression and hit <ENTER>."
	print "Hit <ENTER> twice to quit."

	c = calc.Calculator()
        try:
                iExpr = raw_input('> ')

                while (iExpr != ''):
                        try:
                                oExpr = c.calculate(iExpr, 'warning')
                        except calc.parser.ParseError as e:
                                print "ParseError:", e
                        except calc.converter.ConvertError as e:
                                print "ConvertError:", e
                        except calc.evaluator.EvaluateError as e:
                                print "EvaluateError:", e
                        except ArithmeticError as e:
                                print "ArithmeticError:", e
                        except ValueError as e:
                                print "ValueError:", e
                        else:
                                print oExpr

                        iExpr = raw_input('> ')
        except EOFError:
                pass

	print 'Quitting...'
