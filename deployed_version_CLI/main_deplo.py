from flask import Flask, request, Response
import sys
import os
import io
from contextlib import redirect_stdout

# Import your modules
import destinations_deplo
import hotels_deplo

app = Flask(__name__)

# This helper function captures your CLI print statements
def capture_cli_output(func, *args):
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            func(*args)
        except Exception as e:
            print(f"Error executing function: {e}")
    return f.getvalue()

@app.route('/')
def home():
    # Only showing basic instructions here
    return """
    <pre>
    Welcome to the Travel Assistant CLI (Web Version)
    
    Available Commands (Use these URLs):
    1. Check City:   /city?name=London
    2. Check Hotels: /hotels?type=city&dest_id=-3712125&arrival=2025-11-27&departure=2025-11-29
    </pre>
    """

@app.route('/city')
def city_route():
    city_name = request.args.get('name')
    if not city_name:
        return "<pre>Error: Please add ?name=CityName to the URL</pre>"
    
    # Run your function and capture the output
    output = capture_cli_output(destinations_deplo.getCityInfo, city_name)
    
    # Return as plain text to keep your formatting
    return Response(output, mimetype='text/plain')

@app.route('/hotels')
def hotels_route():
    # Get parameters from URL
    s_type = request.args.get('type', 'city')
    d_id = request.args.get('dest_id')
    arr = request.args.get('arrival')
    dep = request.args.get('departure')
    
    if not d_id or not arr or not dep:
        return "<pre>Error: Missing parameters. Need dest_id, arrival, and departure.</pre>"
        
    output = capture_cli_output(hotels_deplo.hotel_finder, s_type, d_id, arr, dep)
    return Response(output, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)