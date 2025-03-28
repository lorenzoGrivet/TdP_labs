from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAlbums(d):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.*, sum(t.Milliseconds) as totD
                    FROM album a , track t
                    WHERE a.AlbumId = t.AlbumId 
                    GROUP by a.AlbumId
                    having totD > %s"""

        cursor.execute(query, (d,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinctrow t.AlbumId as a1, t2.AlbumId as a2
                    FROM playlisttrack p , track t , playlisttrack p2 , track t2 
                    WHERE p2.PlaylistId = p.PlaylistId
                    and p2.TrackId = t2.TrackId 
                    and p.TrackId = t.TrackId
                    and t.AlbumId < t2.AlbumId """

        cursor.execute(query)

        for row in cursor:
            if row["a1"] in idMap and row["a2"] in idMap:
                result.append( (idMap[row["a1"]] , idMap[row["a2"]] ) )

        cursor.close()
        conn.close()
        return result
