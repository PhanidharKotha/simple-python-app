#!/usr/bin/env python3
"""
Simple Quote Display App
A Python application that displays inspirational quotes.
"""

import random
import time
from datetime import datetime

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
    
    def display_random_quote(self):
        """Display a random quote with timestamp"""
        quote = random.choice(self.quotes)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("=" * 80)
        print(f"📅 {timestamp}")
        print("=" * 80)
        print(f"💭 {quote}")
        print("=" * 80)
    
    def display_all_quotes(self):
        """Display all quotes in the collection"""
        print("\n📚 ALL QUOTES COLLECTION")
        print("=" * 80)
        for i, quote in enumerate(self.quotes, 1):
            print(f"{i:2d}. {quote}")
        print("=" * 80)
    
    def add_quote(self, new_quote):
        """Add a new quote to the collection"""
        if new_quote.strip():
            self.quotes.append(new_quote.strip())
            print(f"✅ Quote added successfully! Total quotes: {len(self.quotes)}")
        else:
            print("❌ Please enter a valid quote.")
    
    def interactive_mode(self):
        """Run the app in interactive mode"""
        print("🌟 Welcome to the Quote Display App! 🌟")
        print("\nChoose an option:")
        print("1. Display random quote")
        print("2. Display all quotes")
        print("3. Add new quote")
        print("4. Display quote of the day")
        print("5. Exit")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == "1":
                    self.display_random_quote()
                elif choice == "2":
                    self.display_all_quotes()
                elif choice == "3":
                    new_quote = input("Enter your new quote: ")
                    self.add_quote(new_quote)
                elif choice == "4":
                    self.display_quote_of_the_day()
                elif choice == "5":
                    print("👋 Thank you for using the Quote App! Goodbye!")
                    break
                else:
                    print("❌ Invalid choice. Please enter 1-5.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
    
    def display_quote_of_the_day(self):
        """Display a quote based on the current day (deterministic)"""
        day_of_year = datetime.now().timetuple().tm_yday
        quote_index = day_of_year % len(self.quotes)
        quote = self.quotes[quote_index]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("=" * 80)
        print(f"📅 QUOTE OF THE DAY - {timestamp}")
        print("=" * 80)
        print(f"🌟 {quote}")
        print("=" * 80)

def main():
    """Main function to run the quote app"""
    app = QuoteApp()
    
    # Check if running with command line arguments
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--random":
            app.display_random_quote()
        elif sys.argv[1] == "--all":
            app.display_all_quotes()
        elif sys.argv[1] == "--daily":
            app.display_quote_of_the_day()
        else:
            print("Usage: python quote_app.py [--random|--all|--daily]")
    else:
        # Run in interactive mode
        app.interactive_mode()

if __name__ == "__main__":
    main()
