# Gym class scheduling app

My first week 6 solo project of my academey journey at QA due on Mon, 23rd March.

## Table of Contents
[Objective](#objective)
   * [Solution](#solution)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   
[Testing](#testing)

[Deployment](#depl)
   * [Technologies Used](#tech)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)


<a name="objective"></a>
## Objective

To create CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.


<a name="solution"></a>
### Solution

I have created a gym class scheduling application that would allow the user to book activities/classes at a gym, as well as add, update and delete.
There is a many to many relationship between gym and classes, therefore I added a joining table as explained and shown the the ERD below

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagram
![ERD](/Project1-Documentation/gym-erd.jpeg)

<a name="testing"></a>
## Testing
Unit Testing has been used

<a name="depl"></a>
## Deployment

The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event.

This application can be deployed both locally and externally through a virtual machine.
![Deployment Pipeline](/Project1-Documentation/CI_pipeline.odp)
<a name="tech"></a>
### Technologies Used

* Project Tracking - [Trello](https://trello.com/b/M97Vmn5V/devops-project)
* Version Control - [Git](https://github.com/nidakhawar/gym-schedule)
* Database - SQL
* Front-end - Flask(HTML)
* Programming Language - Python
* Unit Testing - Pytest
* CI Server - Jenkins 
* Live Environment - GCP

<a name="improve"></a>
## Improvements for the Future

In future I would like to clear my concepts furhter and add further functionalities to my app. 

<a name="auth"></a>
## Author

Nida Khawar

<a name="ack"></a>
## Acknowledgements

* QA consulting and our amazng trainers
* The rest of my wonderful team on the programme

