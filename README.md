# Expense Tracker

## Overview

The Expense Tracker is a desktop application built using Python, SQLite, and Tkinter. The application provides an intuitive interface for users to manage their finances. It allows users to record income and expenses, categorize transactions, visualize data through graphs, and export data to CSV.

## Features

- **Record Income and Expenses**: Users can add transactions by specifying the category, description, and amount.
- **Categorize Transactions**: Each transaction can be categorized for better organization and analysis.
- **Visual Analytics**: Provides pie charts and line graphs to help users understand their spending patterns.
- **Export Data**: Users can export all transaction data to a CSV file for external use.
- **Budget Alerts**: Notifies the user when they are close to exceeding their budget (feature to be added).

## Tech Stack

- **Python**: The backend logic is written in Python.
- **SQLite**: Used for storing transaction data.
- **Tkinter**: Provides the graphical user interface.

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run `python main.py`.

## Files

- `main.py`: The main application file containing both backend logic and frontend GUI.
- `expense_tracker.db`: SQLite database file that stores all transaction data.
- `expenses.csv`: A CSV file that holds exported transaction data.

## Future Enhancements

- Add budgeting features to alert users when they're about to exceed their budget.
- Implement user authentication for added security.
- Add more advanced data visualizations like trend analysis.

## Screenshots

![Alt text](<App Interface.png>)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
