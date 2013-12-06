import logging
from os import getcwd

from singleton import singleton

import corrector
import parser
import converter
import evaluator

@singleton
class Calculator(object):
    def __init__(self, **kwargs):
        LOG_FORMAT = "%(levelname)s: %(msg)s"

        LOG_LEVEL = kwargs.get('logLevel', logging.ERROR)
        if LOG_LEVEL == 'debug':
            LOG_LEVEL = logging.DEBUG
        elif LOG_LEVEL == 'info':
            LOG_LEVEL = logging.INFO
        elif LOG_LEVEL == 'warning':
            LOG_LEVEL = logging.WARNING
        elif LOG_LEVEL == 'error':
            LOG_LEVEL = logging.ERROR
        elif LOG_LEVEL == 'critical':
            LOG_LEVEL = logging.CRITICAL

        LOG_FILENAME = kwargs.get('logFilename', False)
        if LOG_FILENAME:
            if LOG_FILENAME[0] != '/':
                LOG_FILENAME = getcwd() + '/' + LOG_FILENAME
            logging.basicConfig(level=LOG_LEVEL, filename=LOG_FILENAME, format=LOG_FORMAT)
        else:
            logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
        
        self.corrector = corrector.Corrector()
        self.parser = parser.Parser()
        self.converter = converter.Converter()
        self.evaluator = evaluator.Evaluator()


    def calculate(self, iExpr):
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
