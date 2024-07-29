var express = require('express');
var router = express.Router();

router.get('/api', function (req, res, next) {
  const message = 'API ready';
  res.json({ result: true, message });
});

module.exports = router;
