var express = require('express');
var utils = require('../utils');
var router = express.Router();
/* GET home page. */
router.get('/', function(req, res, nex) {
  res.render('index', { title: 'FeelTheNews' });
});

/* Render interface */
router.get('/interface', utils.requireLogin, function(req, res) {
    res.render('interface.jade',  { csrfToken: req.csrfToken() });
});

/* Render myLikes */
router.get('/mylikes', utils.requireLogin, function(req, res) {
    res.render('mylikes.jade',  { csrfToken: req.csrfToken() });
});

/* Render myLikes */
router.get('/myarticles', utils.requireLogin, function(req, res) {
    res.render('myarticles.jade',  { csrfToken: req.csrfToken() });
});
module.exports = router;
