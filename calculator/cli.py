#!/usr/bin/python2

import calculator as calc

def main():
	print "This is calculator for basic math expressions."
	print "Input correct expression and hit <ENTER>."
	print "Hit <ENTER> twice to quit."

	c = calc.Calculator()
	iExpr = raw_input('> ')

	while (iExpr != ''):
	#	oExpr = c.debug(iExpr)
		oExpr = c.calculate(iExpr)
		print oExpr
		iExpr = raw_input('> ')

	print 'Quitting...'
