SELECT StudentGroup.name, count(*) 
FROM StudentGroup JOIN MemberOf 
ON StudentGroup.name=MemberOf.studentgroup_id 
GROUP BY StudentGroup.name;