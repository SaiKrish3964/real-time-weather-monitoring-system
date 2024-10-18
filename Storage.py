import psycopg2

def store_daily_summary(summary):
    conn = psycopg2.connect("dbname=weather user=yourusername password=yourpassword")
    cursor = conn.cursor()

    for _, row in summary.iterrows():
        cursor.execute(
            "INSERT INTO daily_weather (city, date, avg_temp, max_temp, min_temp, dominant_condition) VALUES (%s, %s, %s, %s, %s, %s)",
            (row['city'], row['date'], row['avg_temp'], row['max_temp'], row['min_temp'], row['dominant_condition'])
        )
    conn.commit()
    cursor.close()
    conn.close()