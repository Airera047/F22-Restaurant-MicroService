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
    def get_restaurant_top5(cuisine):

        sql = "SELECT * FROM f22_databases.restaurants where cuisine=%s ORDER BY rating DESC LIMIT 5"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=cuisine)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_all_restaurants(offset=0, limit=10):

        sql = "SELECT * FROM f22_databases.restaurants"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()
        offset = int(offset)
        limit = int(limit)

        ret = result[0:len(result)]
        start = offset*limit
        end = start+limit

        if len(result) > start:
            ret = result[start:end]

        output = {
            "count": len(result),
            "restaurants": ret
        }
        return output

    @staticmethod
    def get_restaurant_by_query(query, offset, limit):
        '''
            SELECT * FROM f22_databases.restaurants
            WHERE LOWER( cuisine ) LIKE %s
            OR LOWER( name ) LIKE %s
            OR LOWER( address ) LIKE %s
            OR LOWER( zip_code ) LIKE %s
            OR LOWER( phone ) LIKE %s
        '''
        q = '%'+query+'%'
        sql = "SELECT * FROM f22_databases.restaurants WHERE LOWER( name ) LIKE %s OR LOWER( address ) LIKE %s OR LOWER( cuisine ) LIKE %s OR LOWER( phone ) LIKE %s OR LOWER( zip_code ) LIKE %s"
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=(q,q,q,q,q))
        result = cur.fetchall()
        offset = int(offset)
        limit = int(limit)

        ret = result[0:len(result)]
        start = offset*limit
        end = start+limit

        if len(result) > start:
            ret = result[start:end]
            
        output = {
            "count": len(result),
            "restaurants": ret
        }
        return output

    @staticmethod
    def create_restaurant_by_key(rid, cuisine, name, rating, address, zip_code, phone, url):
        
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()

        sql = "INSERT INTO f22_databases.restaurants VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"   
        res = cur.execute(sql, args = (rid, cuisine, name, rating, address, zip_code, phone, url))
        if res > 0:
            return "success"
        else:
            return "fail"    

    @staticmethod
    def update_restaurant_by_key(rid, cuisine, name, rating, address, phone):
        conn = RestaurantResource._get_connection()
        cur = conn.cursor()

        sql = "SELECT rid FROM f22_databases.restaurants where rid=%s"
        res = cur.execute(sql, args=(rid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "restaurant doesn't exist"
        
        sql = "UPDATE f22_databases.restaurants SET cuisine=%s, name=%s, rating=%s, address=%s, phone=%s WHERE rid=%s"
        val = (cuisine, name, rating, address, phone, rid)
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
    

    