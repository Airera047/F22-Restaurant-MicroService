from unittest import result
import pymysql
import os

class RestaurantResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        user = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=user,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_restaurant_by_key(key):

        sql = "SELECT * FROM f22_databases.restaurants where rid=%s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_restaurant_by_query(query, offset, limit):
        '''
            SELECT * FROM f22_databases.restaurants
            WHERE LOWER( name ) LIKE %s
            OR LOWER( address ) LIKE %s
            OR LOWER( email ) LIKE %s
            OR LOWER( phone ) LIKE %s
            OR LOWER( category ) LIKE %s
        '''
        q = '%'+query+'%'
        sql = "SELECT * FROM f22_databases.restaurants WHERE LOWER( name ) LIKE %s OR LOWER( address ) LIKE %s OR LOWER( email ) LIKE %s OR LOWER( phone ) LIKE %s OR LOWER( category ) LIKE %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(q,q,q,q,q))
        result = cur.fetchall()

        ret = result[0:len(result)]
        if len(result) > offset:
            ret = ret[offset:len(ret)]

        if len(ret) > limit:
            ret = ret[0:limit]

        return ret

    @staticmethod
    def create_restaurant_by_key(rid, name, address, email, phone, category):
        
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()

        sql = "INSERT INTO f22_databases.restaurants VALUES (%s, %s, %s, %s, %s, %s)"
        res = cur.execute(sql, args = (rid, name, address, email, phone, category))
        if res > 0:
            return "success"
        else:
            return "fail"    

    @staticmethod
    def update_restaurant_by_key(rid, name, address, email, phone, category):
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()

        sql = "SELECT rid FROM f22_databases.restaurants where rid=%s"
        res = cur.execute(sql, args=(rid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "restaurant doesn't exist"
        
        sql = "UPDATE f22_databases.restaurants SET name=%s, address=%s, email=%s, phone=%s, category=%s WHERE rid=%s"
        val = (name, address, email, phone, category, rid)
        cur.execute(sql, val)

        if cur.rowcount > 0:
                return "success"
        else:
            return "fail"
    
    @staticmethod
    def delete_restaurant_by_key(rid):
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
    
        sql = "SELECT rid FROM f22_databases.restaurants where rid=%s"
        res = cur.execute(sql, args=(rid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "restaurant doesn't exist"
        
        sql = "DELETE FROM f22_databases.restaurants WHERE rid = %s"
        val = (rid)
        cur.execute(sql, val)
        
        if cur.rowcount > 0:
                return "success"
        else:
            return "fail"
    

    