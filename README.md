# Team Hail Marys

## Project Little John
---
### We presented in terminal on 8/20/2020!

[https://github.com/hail-marys/little-john]

---
## Web Application
***[Explain your app, should be at least a paragraph. What does it do? Why should I use? Sell your product!]***

As a group we created an AI stock market trading bot using python. Customers will be able to log into their account to view current trades and balances through the terminal along with past trading history. Customers will also be able to search for a companies stock price and history by searching either the companies name or symbol. Customers will be able to turn the auto trading bot on and off. 

---

## Tools Used
VS Code

- Python
- Django
- Docker
- MVC
- xUnit
- Bootstrap
- Azure
- Pytest

---

## Recent Updates

#### V 1.4
*Added OAuth for MySpace* - 23 Jan 2003

---

## Getting Started

Clone this repository to your local machine.

```
$ git clone https://github.com/hail-marys/little-john
```
Once downloaded, activate your virtual environment and run by ____________
```
cd YourRepo/YourProject
dotnet build
```
The poetry tools will automatically install any dependencies. Before running the application, setup your DB by doing ________
```
Update-Database
```
Once the database has been created, the application can be run. Options for running and debugging the application using can be found via your coding tools of ___________. From the command line, the following will start an instance of the Postgresql server to host the application:
```
cd YourRepo/YourProject
dotnet run
```
Unit testing is included in the __________________ project using the pytest test framework. Tests have been provided for models, view models, controllers, and utility classes for the application.

---

## Usage
***[Provide some images of your app with brief description as title]***

### Overview of Recent Posts
![Overview of Recent Posts](https://via.placeholder.com/500x250)

### Creating a Post
![Post Creation](https://via.placeholder.com/500x250)

### Enriching a Post
![Enriching Post](https://via.placeholder.com/500x250)

### Viewing Post Details
![Details of Post](https://via.placeholder.com/500x250)

---
## Data Flow (Frontend, Backend, REST API)
***[Add a clean and clear explanation of what the data flow is. Walk me through it.]***
![Data Flow Diagram](/assets/img/Flowchart.png)

---
## Data Model

### Overall Project Schema
***[Add a description of your DB schema. Explain the relationships to me.]***
![Database Schema](/assets/img/ERD.png)

---
## Model Properties and Requirements

### Blog

| Parameter | Type | Required |
| --- | --- | --- |
| ID  | int | YES |
| Summary | string | YES |
| Content | string | YES |
| Tags | string(s) | NO |
| Picture | img jpeg/png | NO |
| Sentiment | float | NO |
| Keywords | string(s) | NO |
| Related Posts | links | NO |
| Date | date/time object | YES |


### User

| Parameter | Type | Required |
| --- | --- | --- |
| ID  | int | YES |
| Name/Author | string | YES |
| Posts | list | YES |

---

## Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***
1.4: *Added OAuth for MySpace* - 23 Jan 2003
1.3: *Changed email handler to Alta Vista, fixed issue with styling on Netscape Navigator browser.* - 21 Dec 1999
1.2: *Fixed bug where pages would not load due to temp data* - 16 Jun 1998
1.1: *Added ability for user to change photos on a post* - 12 May 1998

---

## Authors
Adam Owada 
Natalie Sinner
Richard Whitehead
Will Koger

---

For more information on Markdown: https://www.markdownguide.org/cheat-sheet