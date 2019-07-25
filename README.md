# MetaChallenge

## Challenge objective
This challenge aims to solve 4 questions:
First question: given an array of integer and a integer which is the target, return the indices of the integers that together results in the target.

Second question: given a string of braces, brackets and parentheses, return Yes if the string is balanced and no if it isn't. 
An example of balanced string: "{[(())]}"
An example of an umbalanced string: "[({)}]"

Third question: Let's say you have an array for which the i element is the price of a particular stock on day i.
If you were allowed to complete at most one transaction (ie buy one and sell one share), create an algorithm to find the maximum profit.

Forth question: Given n nonnegative integer representing an elevation map where the width of each bar is 1, calculate how much water it can hold after rain.

## Technologies used
This challange needed to be solved in the form of a REST API and because it's a challange to a role as a python developer, i chose django and django rest framework to develop this solution. 

##System requirements
To use this repository you'll need python 3.x installed on your local machine.
This project was developed using python 3.7.3

## Installation
The simplest way to get this repository running on your computer is using pipenv.

First download this repository or clone it to a directory on your computer using git.
Then you run ```pipenv install```
After this step pipenv will install the requirements and create a virtual environment. 
To use this virtual environment created by pipenv, run ```pipenv shell```
And to start this project, just run ```python manage.py runserver```

### Is the server running?
After getting the server running, open the browser and type **127.0.0.1:[PORT RUNNING]/**
You will see **Page not found (404)**. Below this title you'll see 
>Using the URLconf defined in Desafio.urls, Django tried these URL patterns, in this order:
>
>questao01/
>questao02/
>questao03/
>questao04/
>The empty path didn't match any of these.

### pipenv didn't work
If pipenv didn't work you can use **pip** and **venv**.
first create your virtual environment.
run ```venv [name of the virtual environment]```
After creating your venv, activate it.
Then, in order to install the requirements, run ```pip install -r requirements.txt```

##Testing the api
I use postman to send requests to my api.
The api just receive POST requests in all 4 endpoints.

###Question 01
The URL to this endpoint is 127.0.0.1:[PORT RUNNING]/questao01/
Send a POST request with this structure in the body:
```
{
    "lista": [here goes the array of integer],
    "alvo": [here goes the target]
}
```
You'll receive a respose with this structure:

```
{
    "lista": [the array of integer sent to the server],
    "alvo": [the target sent to the server],
    "resposta": [the indices requested]
}
```

###Question 02
The URL to this endpoint is 127.0.0.1:[PORT RUNNING]/questao02/
Send a POST request with this structure in the body:
```
{
    "input": [here goes the string]
}
```
You'll receive a respose with this structure:

```
{
    "input": [the string sent to the server],
    "output": [the response requested]
}
```
###Question 03
The URL to this endpoint is 127.0.0.1:[PORT RUNNING]/questao03/
Send a POST request with this structure in the body:
```
{
    "input": [here goes the array]
}
```
You'll receive a respose with this structure:

```
{
    "input": [the array sent to the server],
    "output": [the response]
}
```

###Question 04
The URL to this endpoint is 127.0.0.1:[PORT RUNNING]/questao01/
Send a POST request with this structure in the body:
```
{
    "input": [here goes the array of integer]
}
```
You'll receive a respose with this structure:

```
{
    "input": [the array of integer sent to the server],
    "Volume de chuva retida": [the volume of rain]
}
```
