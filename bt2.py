import psycopg2 
DATABASE_URL = "postgresql://postgres:130104@localhost:5432/HoangMinhTri_bt2"
with psycopg2.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
      cur.execute('SELECT * FROM "Table_Tri";')
      rows = cur.fetchall()
      for row in rows:
        print(row)