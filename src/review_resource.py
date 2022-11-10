from unittest import result
import pymysql
import os

class ReviewResource:

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
    def get_review_by_key(key):

        sql = "SELECT * FROM f22_databases.reviews where rrid=%s"
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_review_by_user_id(key):

        sql = "SELECT * FROM f22_databases.reviews R, f22_database.write_reviews W where W.rrid=R.rrid and W.uid=%s"
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_review_by_restaurant_id(key):

        sql = "SELECT * FROM f22_databases.reviews R, f22_database.write_reviews W where W.rrid=R.rrid and W.rid=%s"
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def create_review_by_key(rrid, rating, content):
        
        conn = ReviewResource._get_connection()
        cur = conn.cursor()

        sql = "INSERT INTO f22_databases.reviews VALUES (%s, %s, %s)"
        res = cur.execute(sql, args = (rrid, rating, content))
        if res > 0:
            return "success"
        else:
            return "fail"    

    @staticmethod
    def update_review_by_key(rrid, rating, content):
        conn = ReviewResource._get_connection()
        cur = conn.cursor()

        sql = "SELECT rrid FROM f22_databases.reviews where rrid=%s"
        res = cur.execute(sql, args=(rrid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "review doesn't exist"
        
        sql = "UPDATE f22_databases.reviews SET rrid=%s, rating=%s, content=%s"
        val = (rrid, rating, content) #(name, address, email, phone, category, rid)
        cur.execute(sql, val)

        if cur.rowcount > 0:
                return "success"
        else:
            return "fail"
    
    @staticmethod
    def delete_review_by_key(rid):
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
    
        sql = "SELECT rrid FROM f22_databases.reviews where rrid=%s"
        res = cur.execute(sql, args=(rid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "review doesn't exist"
        
        sql = "DELETE FROM f22_databases.reviews WHERE rrid = %s"
        val = (rid)
        cur.execute(sql, val)
        
        if cur.rowcount > 0:
                return "success"
        else:
            return "fail"

    @staticmethod
    def create_write_review_by_key(rrid, uid, rid):
        
        conn = ReviewResource._get_connection()
        cur = conn.cursor()

        sql = "INSERT INTO f22_databases.write_reviews VALUES (%s, %s, %s)"
        res = cur.execute(sql, args = (rrid, uid, rid))
        if res > 0:
            return "success"
        else:
            return "fail"    

    @staticmethod
    def delete_write_review_by_key(rid):
        conn = ReviewResource._get_connection()
        cur = conn.cursor()
    
        sql = "SELECT rrid FROM f22_databases.write_reviews where rrid=%s"
        res = cur.execute(sql, args=(rid))
        result = cur.fetchall()
        if len(result) <= 0:
            return "review doesn't exist"
        
        sql = "DELETE FROM f22_databases.write_reviews WHERE rrid = %s"
        val = (rid)
        cur.execute(sql, val)
        
        if cur.rowcount > 0:
                return "success"
        else:
            return "fail"
    
