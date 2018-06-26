from datetime import datetime


class CSVFormatter(object):

    def __init__(self):
        self.delim = ','

    def formatter(self, elements):
        line = []
        [line.append('"{}"'.format(el)) if self.delim in el else line.append(
            el) for el in elements]
        return self.delim.join(line)


class LogFormatter(object):

    def formatter(self, text):
        dt = datetime.now()
        date_strf = dt.strftime('%D-%M-%Y %H:%M')
        return "{}:  {}".format(date_strf, text)


class WriteFile(object):

    def __init__(self, file_name, formatter):
        self.file_name = file_name
        self.formatter = formatter()

    def write(self, text):
        line = self.formatter.formatter(text)
        with open(self.file_name, 'a') as f:
            f.write(line + '\n')


writecsv = WriteFile('text2.csv', CSVFormatter)
writelog = WriteFile('logo2.txt', LogFormatter)


writecsv.write(['1', '2', '3', '4'])
writelog.write("This is the first log")

writecsv.write(['1', 'a,c', '3', '4'])
writelog.write("This is the second log")
