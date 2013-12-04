#!/usr/bin/python2

import logging
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
                                oExpr = c.calculate(iExpr, 'error')
                        except calc.parser.ParseError as e:
                                logging.error("ParseError: " + str(e))
                        except calc.converter.ConvertError as e:
                                logging.error("ConvertError: " + str(e))
                        except calc.evaluator.EvaluateError as e:
                                logging.error("EvaluateError: " + str(e))
                        except ArithmeticError as e:
                                logging.error("ArithmeticError: " + str(e))
                        except ValueError as e:
                                logging.error("ValueError: " + str(e))
                        else:
                                print oExpr

                        iExpr = raw_input('> ')
        except EOFError:
                pass

	print 'Quitting...'
