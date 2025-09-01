import mysql.connector

DB_CREDENTIALS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "habi_db"
}

BASE_QUERY = """
    WITH LatestStatus AS (
        SELECT property_id, status_id,
        ROW_NUMBER() OVER(PARTITION BY property_id ORDER BY update_date DESC) as rn
        FROM status_history
    )
    SELECT p.address, p.city, s.name as status, p.price, p.description, p.year
    FROM property p
    JOIN LatestStatus ls ON p.id = ls.property_id AND ls.rn = 1
    JOIN status s ON ls.status_id = s.id
    WHERE s.name IN ('pre_venta', 'en_venta', 'vendido')
"""

COLUMN_MAPPING = {
        'city': 'p.city',
        'year': 'p.year',
        'status': 's.name'
}

def get_properties(filters={}):
    """Crea la conexión con la DB y ejectua la querie con filtros."""
    try:
        connector = mysql.connector.connect(**DB_CREDENTIALS)
        cursor = connector.cursor(dictionary=True)

        filter_query, params = add_filters_to_query(filters)
        full_query = BASE_QUERY + filter_query
        cursor.execute(full_query, tuple(params))
        
        results = cursor.fetchall()
        cursor.close()
        connector.close()
        return results
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None

def add_filters_to_query(filters):
    """
    Construye la parte de la consulta para los filtros y devuelve
    un string con placeholders (%s) y una lista con los valores.
    """
    where_clauses = []
    params = []
    for key, column in COLUMN_MAPPING.items():
        if key in filters:
            where_clauses.append(f"{column} = %s")
            params.append(filters[key])
    query_string = " AND " + " AND ".join(where_clauses) if where_clauses else ""
    return query_string, params