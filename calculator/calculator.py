import logging
from singleton import singleton

import corrector
import parser
import converter
import evaluator

@singleton
class Calculator(object):
    def __init__(self):
        self.corrector = corrector.Corrector()
        self.parser = parser.Parser()
        self.converter = converter.Converter()
        self.evaluator = evaluator.Evaluator()

    def calculate(self, iExpr, logLevel = 'info'):
        logLevel = logLevel.lower()
        if logLevel == 'debug':
            logging.basicConfig(level=logging.DEBUG)
        elif logLevel == 'info':      
            logging.basicConfig(level=logging.INFO)
        elif logLevel == 'warning':
            logging.basicConfig(level=logging.WARNING)
        else:
            logging.basicConfig(level=logging.ERROR)

        logging.info('Calculator started.')
        logging.info('Starting corrector...')
        correctedExpr = self.corrector.correct(iExpr)
        logging.info('Starting parser...')
        parsedExpr = self.parser.parse(correctedExpr)
        logging.info('Starting converter...')
        convertedExpr = self.converter.convert(parsedExpr)
        logging.info('Starting evaluator...')
        evaluatedExpr = self.evaluator.evaluate(convertedExpr)
        statMsg = 'Calculated successfully! '
        statMsg += 'Result: ' + str(evaluatedExpr) + '.\n'
        statMsg += '----------------------------------------'
        logging.info(statMsg)

        return evaluatedExpr
