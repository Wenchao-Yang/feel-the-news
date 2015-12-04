var bodyParser = require('body-parser');
var csrf = require('csurf');
var express = require('express');
var mysql = require('mysql');
var session = require('client-sessions');

var path = require('path');
//var favicon = require('serve-favicon');
var logger = require('morgan');
var middleware = require('./middleware');



/**
 * Returns user object
 */
module.exports.createUserSession = function(req, res, user) {
    var cleanUser = {
        firstName:  user.firstName,
        lastName:   user.lastName,
        email:      user.email,
        age:        user.age,
        data:       user.data || {},
    };

    req.session.user = cleanUser;
    req.user = cleanUser;
    res.locals.user = cleanUser;
};


/**
 * Create and initialize express app
 */
module.exports.createApp = function() {
    var app = express();
    // view engine setup
    app.set('views', path.join(__dirname, 'views'));
    app.set('view engine', 'jade');
    
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({ extended: false }));
    app.use(session({
        cookieName: 'session',
        secret:     'cs411',
        duration:   30 * 60 * 1000,
        activeDuration: 5 * 60 * 1000,
    }));
    app.use(logger('dev'));
    app.use(csrf());
    app.use(middleware.simpleAuth);
    app.use(express.static(path.join(__dirname, 'public')));
    // uncomment after placing your favicon in /public
    //app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));

    app.use('/', require('./routes/index'));
    app.use('/users', require('./routes/users'));
    app.use(require('./routes/auth'));

    // catch 404 and forward to error handler
    app.use(function(req, res, next) {
      var err = new Error('Not Found');
      err.status = 404;
      next(err);
    });
    
    // error handlers
    
    // development error handler
    // will print stacktrace
    if (app.get('env') === 'development') {
      app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
          message: err.message,
          error: err
        });
      });
    }
    
    // production error handler
    // no stacktraces leaked to user
    app.use(function(err, req, res, next) {
      res.status(err.status || 500);
      res.render('error', {
        message: err.message,
        error: {}
      });
    });

    return app;
};

/**
 * Ensure user is logged in
 *
 * if not logged in, redirect to login page
 */
module.exports.requireLogin = function(req, res, next) {
    if (!req.user) {
        res.redirect('/login');
    } else {
        next();
    }
};
