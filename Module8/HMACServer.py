import	socketserver
import sqlite3 as sql
import hmac, hashlib
from TestResult import enc, dec
from HospitalApp import strseparator

# instead of importing secret, have the secret here for testing authentication
secret = b'1234'
#secret = b'12345'  # uncomment for invalid authentication

class HMACAuth(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("8888{}	sent message:	".format(self.client_address[0]))
        print(self.data)
        self.data = dec(self.data)
        print(self.data)

        # split recieved string into its pieces for computing
        strs = str.split(self.data, strseparator)
        computedSig = hmac.new(secret, bytes(strs[0]+strseparator+strs[1]+strseparator,'utf-8'),
                               digestmod=hashlib.sha3_512).digest()

        print(strs[2])
        print(computedSig)
        # if hmac signature is authenticated
        if strs[2] == str(computedSig):
            con = sql.connect('HospitalDB.DB')

            cur = con.cursor()
            cur.execute('SELECT * FROM UserTestResults WHERE testresultid=?',
                        (strs[0],))
            if cur.fetchone() is not None:
                cur.execute('UPDATE UserTestResults SET TestResult=? WHERE testresultid=?',
                            (enc(strs[1]), strs[0]))

                print('Update recieved successfully!')
            else:
                print('Update recieved unsuccessfully (cannot find testresultid)')


            con.commit()
            con.close()
        # if hmac fails
        else:
            print('Unauthentic Test Result Update recieved! Be on alert! Watch out for bad guys !!!')

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