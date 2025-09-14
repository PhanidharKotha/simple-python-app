#!/usr/bin/env python3
"""
Simple Quote Display Web App
A Flask web application that displays inspirational quotes.
"""

from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime
import os

app = Flask(__name__)

class QuoteApp:
    def __init__(self):
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Life is what happens to you while you're busy making other plans. - John Lennon",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "It is during our darkest moments that we must focus to see the light. - Aristotle",
            "The way to get started is to quit talking and begin doing. - Walt Disney",
            "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "The only impossible journey is the one you never begin. - Tony Robbins",
            "Believe you can and you're halfway there. - Theodore Roosevelt"
        ]
    
    def get_random_quote(self):
        """Get a random quote"""
        return random.choice(self.quotes)
    
    def get_all_quotes(self):
        """Get all quotes"""
        return self.quotes
    
    def get_quote_of_the_day(self):
        """Get quote of the day (deterministic based on date)"""
        day_of_year = datetime.now().timetuple().tm_yday
        quote_index = day_of_year % len(self.quotes)
        return self.quotes[quote_index]
    
    def add_quote(self, new_quote):
        """Add a new quote to the collection"""
        if new_quote.strip():
            self.quotes.append(new_quote.strip())
            return True
        return False

# Initialize the quote app
quote_app = QuoteApp()

@app.route('/')
def index():
    """Main page displaying a random quote"""
    quote = quote_app.get_random_quote()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', quote=quote, timestamp=timestamp)

@app.route('/random')
def random_quote():
    """API endpoint to get a random quote"""
    quote = quote_app.get_random_quote()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'quote': quote,
        'timestamp': timestamp
    })

@app.route('/daily')
def daily_quote_page():
    """Page displaying quote of the day"""
    quote = quote_app.get_quote_of_the_day()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('daily_quote.html', quote=quote, timestamp=timestamp)

@app.route('/api/daily')
def daily_quote():
    """API endpoint to get quote of the day"""
    quote = quote_app.get_quote_of_the_day()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'quote': quote,
        'timestamp': timestamp,
        'type': 'daily'
    })

@app.route('/all')
def all_quotes():
    """Page displaying all quotes"""
    quotes = quote_app.get_all_quotes()
    return render_template('all_quotes.html', quotes=quotes)

@app.route('/api/all')
def api_all_quotes():
    """API endpoint to get all quotes"""
    quotes = quote_app.get_all_quotes()
    return jsonify({'quotes': quotes})

@app.route('/add', methods=['GET', 'POST'])
def add_quote():
    """Page to add a new quote"""
    if request.method == 'POST':
        new_quote = request.form.get('quote', '')
        if quote_app.add_quote(new_quote):
            return render_template('add_quote.html', success=True, quote=new_quote)
        else:
            return render_template('add_quote.html', error=True)
    
    return render_template('add_quote.html')

@app.route('/api/add', methods=['POST'])
def api_add_quote():
    """API endpoint to add a new quote"""
    data = request.get_json()
    new_quote = data.get('quote', '') if data else ''
    
    if quote_app.add_quote(new_quote):
        return jsonify({
            'success': True,
            'message': 'Quote added successfully!',
            'total_quotes': len(quote_app.quotes)
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Please enter a valid quote.'
        })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("🌟 Starting Quote Display Web App...")
    print("📱 Open your browser and go to: http://localhost:5001")
    print("🌐 App will be accessible on all network interfaces (0.0.0.0:5001)")
    print("🛑 Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
