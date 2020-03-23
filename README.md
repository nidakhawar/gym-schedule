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
   
[Risk Assessment](#risk)

[Improvements for the Future](#improve)

[Authors](#auth)

[Special Thanks to](#thanks)


<a name="objective"></a>
## Objective

To create CRUD application using the feature branch model and with the utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.


<a name="solution"></a>
### Solution

I have created a gym class scheduling application that would allow the user to book activities/classes at a gym, as well as add, update and delete.
There is a many to many relationship between gym and classes, therefore I added a joining table as explained and shown the the ERD below

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagram
![ERD](/Project1-Documentation/new-erd.png)

<a name="testing"></a>
## Testing
Unit Testing has been used

<a name="depl"></a>
## Deployment

The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event.

This application can be deployed both locally and externally through a virtual machine.
![Deployment Pipeline](/Project1-Documentation/Screenshot-ci.png)

<a name="risk"></a>
## Risk Assessment

![Risk Assessment](/Project1-Documentation/risk-assessment.png)

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

In future I would like to clear my concepts further and add further functionalities to my app, , where users are able to perform these functionalities.

<a name="auth"></a>
## Author

Nida Khawar

<a name="thanks"></a>
## Special Thanks to

* Luke, Ben, Matt
* My wonderful team members on the programme
