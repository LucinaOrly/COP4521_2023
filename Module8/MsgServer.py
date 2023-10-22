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

class	MyTCPHandler(socketserver.BaseRequestHandler):
    def	handle(self):
        #	self.request	is	the	TCP	socket	connected	to	the	client
        self.data	=	self.request.recv(1024).strip()
        print("9999{}	sent message:	".format(self.client_address[0]))
        print(self.data)
        self.data = dec(self.data)
        print(self.data)

        strs = str.split(self.data, strseparator)
        con = sql.connect('HospitalDB.db')

        print(strs)
        cur = con.cursor()
        cur.execute('SELECT COUNT(*) FROM UserTestResults')
        num_of_rows = cur.fetchone()
        print(num_of_rows[0])
        cur.execute("INSERT INTO UserTestResults (testresultid, userid, testname, testresult) VALUES (?,?,?,?)",
                    (num_of_rows[0] + 1,strs[0],enc(strs[1]),enc(strs[2])))
        con.commit()
        con.close()



if __name__  ==	"__main__":
    try:
        print("running")
        #	Create	the	server,	binding	to	localhost	on	port	9999
        server	=	socketserver.TCPServer(("localhost",	9999),	MyTCPHandler)
        server_HMAC = socketserver.TCPServer(("localhost", 8888), HMACAuth)
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