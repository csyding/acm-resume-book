import os
from neo4j.v1 import GraphDatabase, basic_auth

graphenedb_url = os.environ.get("GRAPHENEDB_BOLT_URL")
graphenedb_user = os.environ.get("GRAPHENEDB_BOLT_USER")
graphenedb_pass = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")

driver = GraphDatabase.driver(graphenedb_url, auth=basic_auth(graphenedb_user, graphenedb_pass))

session = driver.session()

session.run("CREATE (n:Person {name:'Billy Bob'})")
result = session.run("MATCH (n:Person) RETURN n.name AS name")
for record in result:
    print(record["name"])
    session.close()
