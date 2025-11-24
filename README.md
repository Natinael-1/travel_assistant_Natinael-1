             ====✈️ Your Travel Assistant===

A Python-based CLI(Command Line Interface) travel assistant that helps users discover destinations and search for hotels using real-time data from the Booking.com API (via RapidAPI).

This application can be accessed and used in two ways:

Local CLI: A purely interactive command-line tool for local execution.

Deployed one: A Load-Balanced one deployed across two servers, accessible via a browser.

## 📂 Project Structure

```text
travel_assistant_Natinael-1/
├── local_version_CLI/      # Contains logic for the local command-line tool
│   ├── destinationInfo.py
│   └── hotelsInfo.py
├── deployed_version_CLI/   # Contains logic modified for deployment
│   ├── destinations_deplo.py
│   ├── hotels_deplo.py
│   └── main_deplo.py
├── README.md               # Documentation
└── main.py                 # Entry point for the Local CLI


       ⁉️HOW to Access Travel Assistant
Part 1: How to Run Locally (CLI)
To use the application interactively in your terminal (Shell):

Prerequisites
Python 3.x

pip (Python Package Manager)

Installation
Clone the repository:

Bash

git clone https://github.com/Natinael-1/travel_assistant_Natinael-1.git
cd travel_assistant_Natinael-1
Install dependencies:

Bash

pip install requests flask
Set  API Key(Provided in the comment section on Canvas):

Linux/Mac: export RAPID_BOOKING_API_KEY="api_key_here"

Windows: set RAPID_BOOKING_API_KEY=api_key_here

Usage
Run the main script:

Bash

python3 main.py
Follow the on-screen prompts to search for cities or hotels by(city, district, or airport).  

Note: When searching for hotels, insert the destination Id found in the  
      destination you searched for.
      For example, search for London or Kigali, then when searching for hotels by city,  
      put "-2601889"   for London and "-2181358" for Kigali.

🌐 Part 2: Deployment (Web Architecture)
The travel assistant is deployed to a cloud infrastructure consisting  of two web servers  
and one load balancer.

Live URL: https://www.natiboda.tech
Load Balancer (Lb-01): configured with HAProxy. It handles SSL termination (HTTPS) and distributes  
incoming traffic using a Round Robin algorithm.

Web Servers (Web-01 & Web-02): Both servers run the Python Flask application (main_deplo.py)  
in the background using nohup.

Domain: The domain (natiboda.tech) points to the Load Balancer's public IP.

   ⁉️How to Access Remotely.
In the browser,

1. Search for a City:  
For example, details about london


[https://www.natiboda.tech/city?name=London](https://www.natiboda.tech/city?name=London)
you can change "name" to any city you want
2. Search for Hotels(Destination Id is provided inside the city details):

<https://www.natiboda.tech/hotels?type=city&dest_id=-3712125&arrival=2025-11-27&departure=2025-11-29>

       Challenges Faced & Solutions: The CLI Deployment.

The most significant challenge I encountered was the architectural mismatch between a Command   Line Interface (CLI) and a Load Balanced Web Server.

The Problem: My original application (main.py) relied on Python's input() function,   
which is designed for interactive, local terminal execution.  
When deployed to a web server, there is no user to run it from inside the server or     
I must provide my RSA private_key but that is not recommended at all.    
Consequently, if the application were run directly, the server would hang indefinitely     
waiting for input from user, causing the Load Balancer to return error.

The Solution: To satisfy the requirement of deploying and to configure the Load Balancer   accordingly while preserving the nicely format output, I used Flask (main_deplo.py).

Input to parameters: I replaced input() prompts with URL query parameters   
(e.g., request.args.get('name')). This allows the Load Balancer to pass user  
input via HTTP requests.

Maintained output format: I utilized contextlib.redirect_stdout.   
This allowed me to format the response using print() statements to print  
nicely formated response for user.

This approach helped me to deploy the CLI into servers and access it via browser.

   Credits to:
API: Booking API via RapidAPI

Web-infrasture used

HAProxy, Nginx (for SSL), Ubuntu Servers