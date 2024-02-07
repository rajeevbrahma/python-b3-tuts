# check if he/she is eligible to write the exam if 
    # he/she meets following criteria
    # 1. should pass 12th with minimum 65% (not graduates) - Company A
    # 2. should be a graduate with 90% - Company B (not post graduates)
    # 3  should be a grduate with 85% or post graduate pass / fail - Company C 
         # even if  postgrad pass / fail in undergrad he should have more than 85
    # 4. either 12th pass with 90% or graduate with 75% - - Company D

# qulified / not qualified / over qualified

# 1. should pass 12th with minimum 65% (not graduates) - Company A
dataset = {
    "highschool":{
        "status": True,
        "score": 64.9
    },
    "undergrad":{
        "status": True,
        "score": 45
    },
    "postgrad":{
        "status": False,
        "score": 0
    }
}

# business logic

if (dataset["highschool"]["status"] and dataset["highschool"]["score"] >= 65 ):
    print ("The Candidate is Eligible to apply to Company A")
elif dataset["undergrad"]["status"]:
    print ("Over qulified")
elif not dataset["undergrad"]["status"]:
    print ("The Candidate is Eligible to apply to Company A")
elif dataset["postgrad"]:
    print ("Over qulified")
else:
    print ("")

# company A - optimized business logic

if dataset["postgrad"]:
    print ("The candidate is Over qualified")
elif dataset["undergrad"]["status"]:
    print ("The candidate is Over qualified")
elif ( not dataset["undergrad"]["status"] and
         dataset["highschool"]["status"] and
         dataset["highschool"]["score"] >= 65
    ):
    print ("The Candidate is Eligible to apply to Company A")
else:
    print ("Not Qualified for this Company")




# company B - optimized logic
if dataset["postgrad"]["status"]:
    print ("The candidate is Over qualified")
elif ( not dataset["postgrad"]["status"] and
         dataset["undergrad"]["status"] and
         dataset["undergrad"]["score"] >= 90
    ):
    print ("The Candidate is Eligible to apply to Company B")
else:
    print ("Not Qualified for this Company")

# company C

if dataset["postgrad"] and (  dataset["undergrad"]["status"] and
         dataset["undergrad"]["score"] >= 85
    ):
    print ("The Candidate is Eligible to apply to Company C")
elif (  dataset["undergrad"]["status"] and
         dataset["undergrad"]["score"] >= 85
    ):
    print ("The Candidate is Eligible to apply to Company C")
else:
    print ("Not Qualified for this Company")



# company D


if 1 == 1:
    print ("Yes")
# --------------
if 1==1:
    print ("Yes")
else:
    print ("No")
# ---------------
if 1 ==1:
    print ("Yes")
elif 1 == 2:
    print ("May be")
else:
    print ("No")
