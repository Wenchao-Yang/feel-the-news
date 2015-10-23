var express = require('express');
var router = express.Router();
var spawn = require('child_process').spawn;


/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* Receive POST analyze URL */
router.post('/analyzeURL', function(req, res, next) {
    console.log('Received: ' + req.body.url);
    var py = spawn('python', ['./scripts/test.py']);
    py.stdout.on('data', function(data) {
        console.log(JSON.parse(data.toString()));
        res.json(JSON.parse(data.toString()));
    });
});

/* Receive POST crawl BBC World */
router.post('/crawlBBCWorld', function(req, res, next) {
    console.log('Received: BBC Crawl');
    var dummy = [{'title': 'beeboo', 'description': 'blublu', 'senRate': '-', 'readRate': '0.2', 'url': 'blayyy', 'read': 'Unread'}, {'title': 'babbu', 'description': 'a15462', 'senRate': '-', 'readRate': '0.6', 'url': 'asdfasdfa', 'read': 'Unread'},{'title': 'bibibibib', 'description': 'lalallaa', 'senRate': '-', 'readRate': '0.9', 'url': 'huhuhuhuh', 'read': 'Unread'}]; 
    res.json(dummy);
});

/* Receive POST delete */
router.post('/remove', function(req, res, next) {
    console.log('Received: Remove Request ' + req.body.url);
    //DO REMOVE HERE
    res.send('Removed');
});

/* Receive POST update Read */
router.post('/updateRead', function(req, res, next) {
    console.log('Received: Update Read Request ' + req.body.url);
    //DO UPDATE HERE
    res.send('Read Updated');
});

/* Receive POST Query */
router.post('/readQuery', function(req, res, next) {
    console.log('Received: Readability Query Request ' + req.body.type);
    //DO UPDATE HERE
    res.send([]);
});

module.exports = router;
