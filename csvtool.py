import sys, csv

def getrowstr(row):
    return ", ".join(["'%s'" % i for i in row])

def csvtool(fname, table_name):
    f = open(fname, "rb")
    reader = csv.reader(f, delimiter=',', skipinitialspace=True)
    rownum = 0
    query = "INSERT INTO %s " % table_name
    res = []
    for row in reader:
        if row:
            if rownum == 0:
                query += "(%s) VALUES" % getrowstr(row)
            else:
                res.append("(%s)" % getrowstr(row))
            rownum += 1
    f.close()
    print query
    print ',\n'.join(res)

if __name__ == "__main__":
    try:
        fromfile, table_name = sys.argv[1:]
    except:
        sys.exit()
    csvtool(fromfile, table_name)

