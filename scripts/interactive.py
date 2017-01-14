from scripts.core.common import ex_

db = input('Choose DB ("`test` or `bank`").'
           'By default uses `test` >')

if db == 'bank':
    from scripts.core.common import con_bank as con
else:
    from scripts.core.common import con_test as con


def take_until(previous_line=None,
               end=';',
               input_mark='--> ',
               exit_cmd=('q', 'exit')):
    """Takes lines from command line until one of them ends with
    value of :end: parameter.
    Returns lines joined by empty spaces.
    """

    def check_prev_line(prev, line):
        if prev:
            line = ' '.join((prev, line))
        return line

    line = input(input_mark)
    if line in exit_cmd:
        return 'E_X_I_T'
    if line and (line[-1] == end):
        return check_prev_line(previous_line, line)
    else:
        return take_until(previous_line=check_prev_line(previous_line, line))


while 1:
    sql = take_until()
    if sql == 'E_X_I_T':
        break
    try:
        for line in ex_(sql, con=con):
            print(line)
    except Exception as err:
        print(err)
