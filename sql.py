from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#config api key

genai.configure(api_key=os.getenv("Key"))

#function to load google model and provide queries as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

# Function to retrive query from the database 

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Prompt

prompt = ["""
    You are an Expert in converting English Question to SQL query!
    The SQL Database has name STUDENT and has the following columns - NAME, CLASS
    ,SECTION \n\nFor Example\nExample 1 - How many entries of records are present?,
    The SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the  students studying in COMP class ?,
    The SQL command will be something like this SELECT * FROM STUDENT where CLASS="COMP" ;
    also the sql code should not have ''' in beginning or end and sql word in output
"""
          
]

#Setting up Streamlit app

st.set_page_config(page_title="Retrieving SQL queries")
st.header("Queries Executer")

question = st.text_input("Input: ",key = "input")

submit = st.button("Ask The Question Regarding DataBase")

#  is submit is clicked
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("Your Answer is ")
    for row in response:
        print(row)
        st.header(row)