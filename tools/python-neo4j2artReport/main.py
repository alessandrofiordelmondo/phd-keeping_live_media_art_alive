from neo4j import GraphDatabase
import pandas as pd

# Connect to Neo4j database
uri = "bolt://localhost:7687"  # Neo4j URI, change if needed
username = "neo4j"  # Your Neo4j username
password = "password"  # Your Neo4j password

# Initialize the driver
driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to execute a query and return the results
def execute_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()  # returns data as a list of dictionaries

query ="""
MATCH (a:ARTWORK)
RETURN a
"""

ARTWORK = execute_query(query)

