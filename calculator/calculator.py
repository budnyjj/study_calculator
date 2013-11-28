import corrector
import parser
import converter
import evaluator

class Calculator(object):
    def __init__(self):
        self.corrector = corrector.Corrector()
        self.parser = parser.Parser()
        self.converter = converter.Converter()
        self.evaluator = evaluator.Evaluator()

    def calculate(self, iExpr):
        correctedExpr = self.corrector.correct(iExpr)
        parsedExpr = self.parser.parse(correctedExpr)
        convertedExpr = self.converter.convert(parsedExpr)
        evaluatedExpr = self.evaluator.evaluate(convertedExpr)
        return evaluatedExpr

    def debug(self, iExpr):
        print "input:", iExpr

        correctedExpr = self.corrector.correct(iExpr)
        print "corrected:", correctedExpr

        parsedExpr = self.parser.parse(correctedExpr)
        print "parsed:",  " ".join([ str(ident.val) for ident in parsedExpr ])

        convertedExpr = self.converter.convert(parsedExpr)
        print "converted:", " ".join([ str(ident.val) for ident in convertedExpr ])

        evaluatedExpr = self.evaluator.evaluate(convertedExpr)

        return evaluatedExpr
