from datetime import datetime
import abc


class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, text):
        with open(self.file_name, 'a') as f:
            f.write(text + '\n')


class LogFile(WriteFile):

    def __init__(self, file_name):
        super().__init__(file_name)

    def write(self, text):
        dt = datetime.now()
        date_strf = dt.strftime('%D-%M-%Y %H:%M')
        self.write_line('{}  {}'.format(date_strf, text))


class DelimFile(WriteFile):

    def __init__(self, file_name, delimeter):
        super().__init__(file_name)
        self.delim = delimeter

    def write(self, elements):
        line = self.delim.join(elements)
        self.write_line(line)


log = LogFile('logo.txt')
delim = DelimFile('text.csv', ',')

log.write('This is the first log')
log.write('This is the second log')

delim.write(['a', 'b', 'c', 'd'])
delim.write(['1', '2', '3', '4'])
