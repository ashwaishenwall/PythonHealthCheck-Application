const express = require('express');
const app = express();
const port = 3000;

app.get('/ashu/status/morning', (req, res) => {
  // Check the health of your application here
  // You can add more sophisticated checks based on your application's requirements

  // For demonstration purposes, let's assume the application is always healthy
  const status = { status: 'OK', message: 'Application is healthy in the morning!' };
  res.json(status);
});

app.listen(port, () => {
  console.log(`Node.js app listening at http://localhost:${port}`);
});

