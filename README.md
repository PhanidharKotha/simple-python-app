# Quote Display App

A Python application that displays inspirational quotes with both command-line and web interfaces.

## Features

### Command Line App (`quote_app.py`)
- 🎲 Display random quotes
- 📚 View all quotes in the collection
- ➕ Add new quotes
- 📅 Quote of the day (deterministic based on date)
- 🖥️ Interactive command-line interface
- ⚡ Command-line arguments support

### Web App (`web_app.py`)
- 🌐 Beautiful web interface
- 📱 Responsive design for mobile and desktop
- 🎲 Random quote display with auto-refresh
- 📅 Quote of the day page
- 📚 All quotes collection page
- ➕ Add new quotes form
- 🔄 Real-time updates with JavaScript
- 📡 REST API endpoints

## Requirements

### Command Line App
- Python 3.6 or higher
- No additional packages needed (uses only standard library)

### Web App
- Python 3.6 or higher
- Flask web framework

## Installation

### For Command Line App
No installation required beyond having Python 3.6+ installed on your system.

### For Web App
1. Install Flask:
   ```bash
   pip install Flask
   ```

2. Or install from requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line App

#### Interactive Mode (Default)
Run the app without any arguments to enter interactive mode:

```bash
python quote_app.py
```

This will show you a menu with the following options:
1. Display random quote
2. Display all quotes  
3. Add new quote
4. Display quote of the day
5. Exit

#### Command Line Arguments
You can also run the app with specific commands:

```bash
# Display a random quote
python quote_app.py --random

# Display all quotes
python quote_app.py --all

# Display quote of the day
python quote_app.py --daily
```

### Web App

1. Start the web server:
   ```bash
   python web_app.py
   ```

2. Open your browser and go to: http://localhost:5000

3. The web app provides:
   - **Home page**: Random quote with refresh button
   - **Quote of the Day**: Same quote for the entire day
   - **All Quotes**: View all quotes in a beautiful grid
   - **Add Quote**: Form to add new quotes

#### API Endpoints
The web app also provides REST API endpoints:

- `GET /random` - Get a random quote (JSON)
- `GET /api/daily` - Get quote of the day (JSON)
- `GET /api/all` - Get all quotes (JSON)
- `POST /api/add` - Add a new quote (JSON)

## Example Output

### Command Line
```
🌟 Welcome to the Quote Display App! 🌟

Choose an option:
1. Display random quote
2. Display all quotes
3. Add new quote
4. Display quote of the day
5. Exit

Enter your choice (1-5): 1

================================================================================
📅 2024-01-15 14:30:25
================================================================================
💭 The only way to do great work is to love what you do. - Steve Jobs
================================================================================
```

### Web Interface
The web app features a modern, responsive design with:
- Gradient backgrounds
- Card-based layout
- Smooth animations
- Mobile-friendly interface
- Auto-refreshing quotes

## Features Explained

- **Random Quote**: Displays a randomly selected quote from the collection
- **All Quotes**: Shows all quotes in a numbered list (CLI) or grid (Web)
- **Add Quote**: Allows you to add new quotes to the collection
- **Quote of the Day**: Shows the same quote for the entire day (based on day of year)
- **Interactive Mode**: User-friendly menu-driven interface (CLI only)
- **Command Line**: Quick access to specific functions (CLI only)
- **Web Interface**: Beautiful, responsive web interface (Web only)
- **REST API**: Programmatic access to quote data (Web only)

## Customization

You can easily customize the app by:

1. **Adding more quotes**: Modify the `quotes` list in the `QuoteApp` class
2. **Changing the display format**: Edit the print statements (CLI) or HTML templates (Web)
3. **Adding new features**: Extend the `QuoteApp` class with additional methods
4. **Styling**: Modify the CSS in the HTML templates for the web app

## File Structure

```
Docker/simple-python-app/
├── quote_app.py          # Command line application
├── web_app.py            # Web application (Flask)
├── requirements.txt      # Dependencies
├── README.md            # This file
└── templates/           # HTML templates for web app
    ├── index.html       # Main page
    ├── all_quotes.html  # All quotes page
    └── add_quote.html   # Add quote page
```

## License

This project is open source and available under the MIT License.
