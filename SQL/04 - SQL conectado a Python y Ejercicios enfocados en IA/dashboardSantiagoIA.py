import mysql.connector
import pandas as pd
import plotly.express as px

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="santiagoIA"
)

df = pd.read_sql("SELECT * FROM santiago_sensores", conn)
conn.close()

fig = px.line(df, x="fecha", y="humedad", color="cultivo_id",
              title="Humedad de cultivos en tiempo real")
fig.show()
