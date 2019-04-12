# LOGS ANALYSIS

This project is a part of [FullStack Web Developer Nanodegree][u1] by Udacity.

The objective of the Logs Analysis Project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

 

# Steps to execute

# 1. Setup: Configure VM & Database
**Step 1:** Download and install Vagrant and VirtualBox. We’ll need these tools to setup and manage the Virtual Machine (VM).

**Step 2:** [Download][u9] the VM configuration from the downloads folder or clone from this [github repo][u8]. Note the path where you downloaded it as it will be used in other steps.

The configuration file specifies the arrangement of resources (processors, memory, disks, network adapters, etc) assigned to a virtual machine.

**Step 3:** Download the database dump from the downloads folder or this [link][u5].

Then, copy the database dump newsdata.sql to the vagrant/ (one of the folders you downloaded in step 2).

**Step 4:** Download the python programs ([source.py][u6] and [dataSource.py][u7]) from the current folder. Then, copy them to the vagrant/ (one of the folders you downloaded in step 2).

**Step 5:** Open the terminal. Then, run the following commands:

```sh
# Install & Configure VM
cd /path/to/vagrant
vagrant up

# Log into machine
vagrant ssh

# Populate database using dump in shared folder 
cd /vagrant 
psql -d news -f newsdata.sql
```
# 2. Run the Reporting Tool
Open the terminal. Then, run the following commands:
```sh
# Launch & Login to machine
cd /path/vagrant
vagrant up
vagrant ssh

# Run the program
python source.py
```

# QUESTIONS TO ANSWER

##### What are the most popular three articles of all time? Which articles have been accessed the most?

**Example:**

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
##### Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? 

**Example:**

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
##### On which days did more than 1% of requests lead to errors? 

**Example:**

July 29, 2016 — 2.5% errors

## References
[Writing code with DB-API][u2]
[Aggregate Fuctions][u3]
[PSQL CLI commands][u4]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [u1]: <https://classroom.udacity.com/nanodegrees/nd004/syllabus/core-curriculum>
   [u2]: <https://classroom.udacity.com/courses/ud197/lessons/3483858580/concepts/35153985360923>
   [u3]: <https://www.postgresql.org/docs/9.5/functions-aggregate.html>
   [u4]: <https://www.postgresql.org/docs/9.2/app-psql.html>
   [u5]: <https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91>
   [u6]: <https://github.com/RoboTechB/LogAnalysis/blob/master/source.py>
   [u7]: <https://github.com/RoboTechB/LogAnalysis/blob/master/dataSource.py>
   [u8]: <https://github.com/udacity/fullstack-nanodegree-vm>
   [u9]: <https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0>
   