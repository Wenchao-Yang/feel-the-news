var models = require('./models');
var utils = require('./utils');

/**
 * Authentication Middleware for Express
 *
 * Only checks if valid email
 */
module.exports.simpleAuth = function(req, res, next) {
    if (req.session && req.session.user) {
        models.findUser({ email: req.session.user.email }, function(err, user) {
            if (user) {
                utils.createUserSession(req, res, user);
            }
            next();
        });
    } else {
        next();
    }
};
