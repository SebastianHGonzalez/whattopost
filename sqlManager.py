#!/usr/bin/python
import mysql.connector
import logging

class SqlManager:

    def configure(self, host, user, psw, _db):
        self.cnx = mysql.connector.connect(host=host,
                             user=user,
                             passwd=psw,
                             db=_db)
        self.createTableIfNot(_db)

    def createTableIfNot(self, db):
        cursor = self.cnx.cursor()
        query = "SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'picData' AND table_schema = '{0}';".format(db)
        cursor.execute(query)

        result = (cursor.fetchone()[0])
        if result == 0:
            cursor.execute("CREATE TABLE picData(LABEL VARCHAR(50), AMOUNT INT);")
            print('picData table created!')

        cursor.close()

    def updateRecords(self, label):

        cursor = self.cnx.cursor()

        cursor.execute("SELECT * FROM picData;")

        results = cursor.fetchall()
        updated = False

        for pair in results:
            if pair[0] == label:
                query = "UPDATE picData SET AMOUNT = AMOUNT + 1 WHERE LABEL = '{0}';".format(label)
                cursor.execute(query)
                self.cnx.commit()
                updated = True
                print(label + ' updated!')

        if not updated:
            query = "INSERT INTO picData (LABEL, AMOUNT) VALUES ('{0}', 1);".format(label)
            cursor.execute(query)

            self.cnx.commit()
            print(label + ' inserted!')

        cursor.close()

    def disconnect(self):
        self.cnx.close()
