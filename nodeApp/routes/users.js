var express = require('express');
var router = express.Router();
var spawn = require('child_process').spawn;
var models = require('../models');


/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* Receive POST analyze URL */
router.post('/analyzeURL', function(req, res, next) {
    console.log('Received for analysis:' + req.body.url);
    var py = spawn('python', ['../src/merge.py', '-u', req.body.url]);
    py.stdout.on('data', function(data) {
        //data = JSON.parse(data);
        console.log(data);
        models.addArticle(data, function(err) {
            console.log(err);
        });
        models.ownArticle(data.url, req.user.email, function(err) {
            console.log(err);
        });
        res.json(data);
    });
});

/* Receive POST like */
router.post('/like', function(req, res, next) {
    console.log('Received: Like ' + req.body.url + ' by ' + req.user.firstName);
    models.like(req.body.url, req.user.email, function(err) {
        if (err) {
            console.log(err);
        }
    });
});

/* Receive POST Remove like */
router.post('/removeLike', function(req, res, next) {
    console.log('Received: Remove Like ' + req.body.url + ' by ' + req.user.firstName);
    models.removeLike(req.body.url, req.user.email, function(err) {
        if (err) {
            console.log(err);
        }
    });
});

/* Receive POST Get likes URL */
router.post('/getLikesURL', function(req, res, next) {
    console.log('Received: Get Likes URL by ' + req.user.firstName);
    models.getLikes(req.user.email, function(err, result) {
        if (err) {
            console.log(err);
        }
        res.json(result);
    });
});

/* Receive POST Get likes URL */
router.post('/getLikes', function(req, res, next) {
    console.log('Received: Get Likes by ' + req.user.firstName);
    models.getLikes(req.user.email, function(err, result) {
        if (err) {
            console.log(err);
        }
        res.json(result);
    });
});

/* Receive POST Get User added articles */
router.post('/getUserAddedArticles', function(req, res, next) {
    console.log('Received: Get Articles Added by ' + req.user.firstName);
    models.getUserAddedArticles(req.user.email, function(err, result) {
        if (err) {
            console.log(err);
        }
        res.json(result);
    });
});

/* Receive POST Query */
router.post('/normalQuery', function(req, res, next) {
    console.log('Received: Normal Query Request ' + JSON.stringify(req.body));
    //WATCH OUT: res overwrite
    models.articlesQuery(req.body, function(err, result) {
        if (err) {
            console.log(err);
        }
        res.json(result);
    });
});

module.exports = router;
