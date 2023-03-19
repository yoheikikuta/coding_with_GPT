from datetime import datetime


def build_query(category, start_year, end_year, keyword):
    query = f"cat:{category}"

    if start_year and end_year:
        query += f" AND submittedDate:[{start_year}0101 TO {end_year}1231]"

    if keyword and keyword.strip():
        query += f' AND (ti:"{keyword}" OR abs:"{keyword}")'
    
    return query
