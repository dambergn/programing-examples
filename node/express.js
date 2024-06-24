const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a simple API endpoint that returns some JSON data
app.get('/api', (req, res) => {
    res.json({ message: 'Hello from your Express server!' });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});