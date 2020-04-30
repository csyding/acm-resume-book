SELECT Internship.CompanyName, Company.Description, AVG(Internship.NumberRating), COUNT(Internship.CompanyName)
FROM Internship JOIN Company on Internship.CompanyName = Company.CompanyName
GROUP BY CompanyName;