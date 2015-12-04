var bcrypt = require('bcryptjs');
var express = require('express');

var models = require('../models');
var utils = require('../utils');

var router = express.Router();

/**
 * Render the registration page.
 */
router.get('/register', function(req, res) {
  res.render('register.jade', { csrfToken: req.csrfToken() });
});

/**
 * Create a new user account.
 *
 * Once a user is logged in, they will be sent to the interface page.
 */
router.post('/register', function(req, res) {
  var salt = bcrypt.genSaltSync(10);
  var hash = bcrypt.hashSync(req.body.password, salt);

  var userInfo = {
    firstName:  req.body.firstName,
    lastName:   req.body.lastName,
    email:      req.body.email,
    password:   hash,
  };
  models.registerUser(userInfo, function(err) {
    if (err) {
      var error = 'Something bad happened! Please try again.';

      if (err.code == 'ER_DUP_ENTRY') {
        error = 'That email is already taken, please try another.';
      }

      res.render('register.jade', { error: error });
    } else {
      utils.createUserSession(req, res, userInfo);
      res.redirect('/');
    }
  });
});

/**
 * Render the login page.
 */
router.get('/login', function(req, res) {
  res.render('login.jade', { csrfToken: req.csrfToken() });
});

/**
 * Log a user into their account.
 *
 * Once a user is logged in, they will be sent to the interface page.
 */
router.post('/login', function(req, res) {
  models.findUser({ email: req.body.email }, function(err, user) {
    if (!user) {
      res.render('login.jade', { error: "Incorrect email / password.", csrfToken: req.csrfToken() });
    } else {
      if (bcrypt.compareSync(req.body.password, user.password)) {
        utils.createUserSession(req, res, user);
        res.redirect('/interface');
      } else {
        res.render('login.jade', { error: "Incorrect email / password.", csrfToken: req.csrfToken() });
      }
    }
  });
});

/**
 * Log a user out of their account, then redirect them to the home page.
 */
router.get('/logout', function(req, res) {
  if (req.session) {
    req.session.reset();
  }
  res.redirect('/');
});

/**
 * Render the My Account page
 */
router.get('/myAccount', function(req, res) {
  res.render('myaccount.jade', { csrfToken: req.csrfToken() });
});

/**
 * Allow User to Change information.
 *
 */
router.post('/myAccount', function(req, res) {
  models.findUser({ email: req.user.email }, function(err, user) {
    if (!user) {
      res.render('login.jade', { error: "Incorrect email / password.", csrfToken: req.csrfToken() });
    } else {
      if (bcrypt.compareSync(req.body.oldPassword, user.password)) {
        var salt = bcrypt.genSaltSync(10);
        var hash = bcrypt.hashSync(req.body.newPassword, salt);
        var userInfo = {
            firstName: req.body.firstNameBlah,
            lastName: req.body.lastNameBlah,
            password: hash
        };
        var userEmail = {email: req.user.email};
        models.updateUser(userInfo, userEmail, function(err) {
            if (err)
                res.render('myaccount.jade', { error: err,  csrfToken: req.csrfToken() });
            else
                res.render('myaccount.jade', { updateStatus: 'Successfully Updated',  csrfToken: req.csrfToken() });
        });
      } else {
        res.render('myaccount.jade', { error: "Incorrect Password", csrfToken: req.csrfToken() });
      }
    }
    });
});

module.exports = router;
