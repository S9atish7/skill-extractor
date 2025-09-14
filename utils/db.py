import pymysql
import streamlit as st
from pymysql.cursors import DictCursor

def get_connection():
    return pymysql.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        cursorclass=DictCursor,
    )

def save_result(resume_name, matched_role, score, skills):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO results (resume_name, matched_role, score, detected_skills)
                VALUES (%s, %s, %s, %s)
                """,
                (resume_name, matched_role, score, ",".join(skills)),
            )
        conn.commit()