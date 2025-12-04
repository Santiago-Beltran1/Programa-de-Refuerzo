import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

conn = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="santiagoIA"
)

df = pd.read_sql("""
SELECT humedad, temperatura, luminosidad,
CASE 
    WHEN humedad < 20 AND temperatura > 29 THEN 1
    ELSE 0
END AS enfermo
FROM santiago_sensores
""", conn)

conn.close()

X = df[['humedad', 'temperatura', 'luminosidad']]
y = df['enfermo']

modelo = LogisticRegression()
modelo.fit(X, y)

print("Predicción enfermedad:", modelo.predict([[18, 31, 850]]))
print(classification_report(y, modelo.predict(X)))
