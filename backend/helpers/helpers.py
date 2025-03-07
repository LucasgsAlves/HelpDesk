import mysql.connector

def standardize_text(text):
    return text.strip().title()

def space_remover(text):
    return text.strip()

def convert_uppercase(text):
    return text.upper()

def convert_lowercase(text):
    return text.lower()