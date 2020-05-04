MATCH (s:Student)-[i:InterestedIn]->(x:Interest)
WHERE x.value = "Artificial Intelligence"
RETURN s.uuid