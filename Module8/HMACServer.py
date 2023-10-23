import	socketserver
import sqlite3 as sql
from TestResult import enc, dec
from HospitalApp import strseparator


class HMACAuth(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("8888{}	sent message:	".format(self.client_address[0]))
        self.data = dec(self.data)

        # split recieved string into its pieces for computing
        strs = str.split(self.data, strseparator)
        con = sql.connect('HospitalDB.DB')

        cur = con.cursor()
        cur.execute('UPDATE UserTestResults SET TestResult=? WHERE testresultid=?',
                    (strs[1], strs[0]))

        con.commit()
        con.close()

if __name__  ==	"__main__":
    try:
        print("running")
        #	Create	the	server,	binding	to	localhost	on	port	9999
        HOST, PORT = 'localhost', 8888
        server = socketserver.TCPServer((HOST, PORT), HMACAuth)
        # Activate	the	server;	this	will	keep	running	until	you
        #	interrupt	the	program	with	Ctrl-C
        server.serve_forever()
    except server.error as e:
        print("Error:",e)
        exit(1)
    finally:
        server.close()


""" example output: Console View
running
"""