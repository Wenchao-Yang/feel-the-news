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
    var py = spawn('python', ['../crawler/singleURLAdd.py', req.body.url]);
    py.stdout.on('data', function(data) {
        res.json(JSON.parse(data));
    });
});

/* Receive POST crawl BBC World */
router.post('/crawlBBCWorld', function(req, res, next) {
    console.log('Received: BBC Crawl');
    var py = spawn('python', ['../crawler/BBCCrawlAdd.py']);
    py.stdout.on('data', function(data) {
        res.json(JSON.parse(data));
    });
});

/* Receive POST delete */
router.post('/remove', function(req, res, next) {
    console.log('Received: Remove Request ' + req.body.url);
    //DO REMOVE HERE
    var py = spawn('python', ['../crawler/deleteURL.py', req.body.url]);
    res.send('Removed');
});

/* Receive POST update Read */
router.post('/updateRead', function(req, res, next) {
    console.log('Received: Update Read Request ' + req.body.url);
    //DO UPDATE HERE
    var py = spawn('python', ['../crawler/updateRead.py', req.body.url]);
    res.send('Read Updated');
});

/* Receive POST Query */
router.post('/readQuery', function(req, res, next) {
    console.log('Received: Readability Query Request ' + req.body.type);
    //DO UPDATE HERE
    var py = spawn('python', ['../crawler/readQuery.py', req.body.type]);
    py.stdout.on('data', function(data) {
        console.log(JSON.parse(data));
        res.json(JSON.parse(data));
    });
});

module.exports = router;
