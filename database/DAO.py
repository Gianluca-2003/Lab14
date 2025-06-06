from database.DB_connect import DBConnect
from model.ordine import Ordine


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes(storeId):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []
        query = """SELECT o.*
                FROM  orders o 
                WHERE o.store_id = %s"""
        cursor.execute(query,(storeId,))
        for row in cursor:
            res.append(Ordine(**row))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAlleEdges(storeId, k, idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []
        query = """Select DISTINCT o1.order_id as id1, o2.order_id as id2, count(oi.quantity+ oi2.quantity) as cnt
                from orders o1, orders o2, order_items oi, order_items oi2 
                where o1.store_id=%s
                and o1.store_id=o2.store_id 
                and o1.order_date > o2.order_date
                and oi.order_id = o1.order_id
                and oi2.order_id  = o2.order_id
                and DATEDIFF(o1.order_Date, o2.order_date) < %s
                group by o1.order_id, o2.order_id"""
        cursor.execute(query, (storeId, k,))
        for row in cursor:
            res.append((idMap[row['id1']], idMap[row['id2']], row['cnt']))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllStores():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []
        query = """SELECT s.store_id as id
                FROM stores s """
        cursor.execute(query,)
        for row in cursor:
            res.append(row['id'])
        cursor.close()
        cnx.close()
        return res





