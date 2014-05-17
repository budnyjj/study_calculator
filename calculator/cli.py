#!/usr/bin/python2

<<<<<<< HEAD
import curses
=======
import logging
>>>>>>> c8a6e489b4764ad2e947765209b654b5e758c32f
import calculator as calc

class Curses_screen:
    def __init__(self):
        self.__scr = curses.initscr()
    
    def __enter__(self):
        self.__scr.keypad(1)
        curses.noecho()
        return self
        
    def __exit__(self, t, value, trace):
        curses.nocbreak()
        curses.echo()
        self.__scr.keypad(0)
        curses.endwin()
        
    def getch(self):
        return self.__scr.getch()

    def addstr(self, string):
        self.__scr.addstr(string)

    def move_left(self):
        y,x = curses.getsyx()
        if x > 0:
            self.__scr.move(y,x-1)

    def move_left_border(self):
        y,_ = curses.getsyx()
        self.__scr.move(y,0)


    def move_right(self):
        _,MAX_X = self.__scr.getmaxyx()
        y,x = curses.getsyx()
        if x < MAX_X - 1:
            self.__scr.move(y,x+1)

    def move_next_line(self):
        MAX_Y,_ = self.__scr.getmaxyx()
        y,_ = curses.getsyx()
        if y < MAX_Y - 3:
            self.__scr.move(y+1,0)


# def show_help(scr):
#   scr.addstr(0, 0, "This is calculator for basic math expressions.")
#   scr.addstr(1, 0, "Input correct expression and press <ENTER>.")
#   scr.addstr(2, 0, "Write 'quit', 'exit' or 'q' to exit.")
#   scr.addstr(3, 0, "---")
#   scr.refresh()


def main():
    c = calc.Calculator()
    with Curses_screen() as scr:
        user_input = []
        while True:
            event = scr.getch()
            if event == curses.KEY_LEFT:
                scr.move_left()
            elif event == curses.KEY_RIGHT:
                scr.move_right()
            elif event == ord('\n'):
                scr.move_next_line()
                result = c.debug("".join(user_input))
                scr.addstr(str(e))

                scr.move_next_line()
                user_input = []

            elif (0 <= event <= 255):
                char = chr(event)
                try:
                    _,x = curses.getsyx()
                    user_input.insert(x, char)
                except IndexError:
                    user_input.append(char)
                scr.move_left_border()
                scr.addstr("".join(user_input))

                
        # clear(stdscr)
        # prompt(stdscr)
        # input_expr = []
        # while True:
        #   event = stdscr.getch()
        #   MAX_Y,MAX_X = stdscr.getmaxyx()
        #   y,x = curses.getsyx()
        #   if event == curses.KEY_LEFT:
        #       move_cursor_left(stdscr)
        #   elif event == curses.KEY_RIGHT:
        #       move_cursor_right(stdscr)
        #   elif event == ord("\n"):
        #       input_string = "".join(input_expr)
        #       if input_string.lower() in ("exit", "quit", "q");
        #       break
        #   else:
        #       if y >= MAX_Y - 2:
        #           clear(stdscr)
        #           answer(stdscr, input_string)
        #           input_expr = []
        #           prompt(stdscr)
        #       else:
        #           try:
        #               pass
        #               # if x < len(input_expr) - 1:
        #               #         input_expr[x-1] = chr(event)
        #               # else:
        #               #         input_expr.insert(x, chr(event))
        #           except ValueError:
        #               pass
        

        # stdscr = curses.initscr()

        # show_help(stdscr)

        # prompt(stdscr)
        # iExpr = []
        # while True:
        #         event = stdscr.getch()
        #         if event == ord("q"):
        #                 break
        #         elif event == curses.KEY_LEFT:
        #                 move_left(stdscr)
        #         elif event == curses.KEY_RIGHT:
        #                 move_right(stdscr)
        #         elif event == curses.KEY_ENTER or event == ord('\n'):
        #                 MAX_Y,MAX_X = stdscr.getmaxyx()
        #                 y,x = curses.getsyx()
        #                 if y >= MAX_Y - 2:
        #                         stdscr.cls()
        #                 print_result(stdscr, "".join(iExpr))
        #                 iExpr = []
        #                 prompt(stdscr)
        #         else:
        #                 iExpr.append(chr(event))
        



    # c = calc.Calculator()


    # iExpr = raw_input('> ')

    # while (iExpr != ''):
    # # oExpr = c.debug(iExpr)
    #   oExpr = c.calculate(iExpr)
    #   print oExpr
    #   iExpr = raw_input('> ')

<<<<<<< HEAD
        # iExpr = ""
        # while True:
        #         c = stdscr.getch()
        #         if c != curses.KEY_ENTER:
        #                 iExpr += c
        #         else:
        #                 # oExpr = c.debug(iExpr)
        #                 oExpr = c.calculate(iExpr)
        #                 curses.addstr(oExpr)

    # print 'Quitting...'
=======
	c = calc.Calculator(logLevel='error')
        try:
                iExpr = raw_input('> ')

                while (iExpr != ''):
                        try:
                                oExpr = c.calculate(iExpr)
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
                                print '=', oExpr

                        iExpr = raw_input('> ')
        except EOFError:
                pass
>>>>>>> c8a6e489b4764ad2e947765209b654b5e758c32f

        # curses.nocbreak()
        # stdscr.keypad(0)
        # # curses.echo()
        # curses.endwin()
