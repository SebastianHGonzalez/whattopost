#!/usr/bin/python
import mysql.connector
import logging

class SqlManager:

    def configure(self, host, user, psw, db):
        self.cnx = mysql.connector.connect(host=host,
                             user=user,
                             passwd=psw,
                             db=db)

    def updateRecords(self, label, amount=1):

        cursor = self.cnx.cursor()

        cursor.execute("SELECT * FROM picData;")

        results = cursor.fetchall()
        updated = False

        for pair in results:
            if pair[0] == label:
                query = "UPDATE picData SET AMOUNT = AMOUNT + %s WHERE LABEL = %s;"
                data = (amount, label)
                cursor.execute(query, data)
                self.cnx.commit()
                updated = True
                print(label + ' updated!')

        if not updated:
            query = "INSERT INTO picData (LABEL, AMOUNT) VALUES (%s, %s);"
            data = (label, amount)
            cursor.execute(query, data)

            self.cnx.commit()
            print(label + ' inserted!')

        cursor.close()

    def disconnect(self):
        self.cnx.close()
