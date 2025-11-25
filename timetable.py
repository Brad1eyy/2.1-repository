import csv
from tabulate import tabulate 

course = "BSSE Y2 S1"
class_size = "63"  

rows = [
    [course, "UNIT CODE", "UNIT NAME", class_size, "LECTURER", "DAY", "TIME", "MODE OF STUDY", "ROOM"],
    [course, "BCSE 2104", "DATA COMMUNICATION NETWORKS", class_size, "DR Charles Katila", "WEDNESDAY", "7:00AM-10:OOAM", "Online", "Zoom"],
    [course, "BCSE 2105", "FOUNDATIONS OF SOFTWARE ENGINEERING", class_size, "DR  Kenedy Hadullo", "THURSDAY", "4.00pm-7.00PM", "Physical", "NB RM E"],
    [course, "BNCS 2103", "FUNDAMENTALS OF CLOUD COMPUTING AND VIRTUALIZATION", class_size, "Doreen Mango", "FRIDAY", "10.00AM-1.00PM", "Physical", "LTA 16"],
    [course, "BMAT 2109", "LINEAR ALGEBRA", class_size, "DR. Emma Anyika", "WEDNESDAY", "10:00AM-1:00PM", "Online", "Zoom"],
    [course, "BCIT 2112", "SYSTEM ANALYSIS AND DESIGN", class_size, "Edna Chepkemoi", "TUESDAY", "4:00PM-7:00PM", "Physical", "LTA 16"],
    [course, "BSTA 2104", "PROBABILITY AND STATISTICS II", class_size, "Samuel Gathuka", "TUESDAY", "10:00AM-1:00PM", "Physical", "NB RM B"],
    [course, "BMAT 2111", "CALCULUS II", class_size, "DR Fidelis Mukundi", "MONDAY", "10:00PM-1:00PM", "Physical", "LTA 2"]
]

header = rows[0]
data = rows[1:]

print(tabulate(data, headers=header, tablefmt="fancy_grid"))



