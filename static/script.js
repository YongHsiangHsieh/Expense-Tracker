
// JavaScript code to interact with the backend
document.addEventListener("DOMContentLoaded", function() {
    // Load existing expenses
    fetchExpenses();

    // Handle form submission
    const form = document.getElementById('expense-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const expenseData = {
            'category': formData.get('category'),
            'description': formData.get('description'),
            'amount': parseFloat(formData.get('amount')),
            'date': formData.get('date')
        };
        
        // Send POST request to add a new expense
        fetch('/expense', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(expenseData)
        }).then(response => response.json())
          .then(data => {
            if (data.status === 'success') {
                alert(data.message);
                // Reload expenses
                fetchExpenses();
            } else {
                alert(`Error: ${data.message}`);
            }
        });
    });
});

// Function to fetch all expenses
function fetchExpenses() {
    fetch('/expenses')
    .then(response => response.json())
    .then(data => {
        const tableBody = document.querySelector('#expense-table tbody');
        tableBody.innerHTML = '';
        data.expenses.forEach(expense => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${expense.id}</td>
                <td>${expense.category}</td>
                <td>${expense.description}</td>
                <td>${expense.amount}</td>
                <td>${expense.date}</td>
            `;
            tableBody.appendChild(row);
        });
    });
}
