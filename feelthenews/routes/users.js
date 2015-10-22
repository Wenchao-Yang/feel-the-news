var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* Receive POST analyze URL */
router.post('/analyzeURL', function(req, res, next) {
    console.log('Received: ' + req.body.url);
    var data = {title: 'Booya',
                description: 'blahBlah',
                senRate: '0.67',
                techRate: '0.25',
                url: req.body.url,
                read: 'Unread'};
    res.json(data);
});

module.exports = router;
