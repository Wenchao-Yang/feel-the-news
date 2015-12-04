var mysql = require('mysql');
var connection = mysql.createConnection({
    host    : 'localhost',
    user    : 'root',
    password: '1111',
    database: 'feelthenews'
});

/**
 * Finds User
 */
module.exports.findUser = function(UserID, callback) {
    connection.query('SELECT * FROM user WHERE ?', UserID, function(err, result) {
        callback(err, result[0]);
    });
};

/**
 * Register User
 */
module.exports.registerUser = function(UserInfo, callback) {
    connection.query('INSERT INTO user SET ?', UserInfo, function(err) {
        callback(err);
    });
};

/**
 * Update User Information
 */
module.exports.updateUser = function(UserInfo, email, callback) {
    console.log(UserInfo);
    connection.query('UPDATE user SET ? WHERE ?', [UserInfo, email], function(err) {
        callback(err);
    });
};

/**
 * Checks for Empty Object
 */
function isEmptyObject(obj) {
    return !Object.keys(obj).length;
}

/**
 * Generates the WHERE of MySQL query
 */
function generateWhere(queryObject) {
    if (isEmptyObject(queryObject))
        return '';
    var query = ' WHERE'; 
    var firstCond = true;
    if (queryObject.readRateLow) {
        if (firstCond) {
            query += ' readRate > ' + connection.escape(queryObject.readRateLow);
            firstCond = false;
        } else {
            query += ' AND readRate > ' + connection.escape(queryObject.readRateLow);
        }
    }
    if (queryObject.readRateHigh) {
        if (firstCond) {
            query += ' readRate <= ' + connection.escape(queryObject.readRateHigh);
            firstCond = false;
        } else {
            query += ' AND readRate <= ' + connection.escape(queryObject.readRateHigh);
        }
    }
    if (queryObject.senRate) {
        if (firstCond) {
            query += ' senRate = ' + connection.escape(queryObject.senRate);
            firstCond = false;
        } else {
            query += ' AND senRate = ' + connection.escape(queryObject.senRate);
        }
    }
    if (queryObject.category) {
        if (firstCond) {
            query += ' category = ' + connection.escape(queryObject.category);
            firstCond = false;
        } else {
            query += ' AND category = ' + connection.escape(queryObject.category);
        }
    }
    return query;
}

/**
 * Normal Query
 */
module.exports.articlesQuery = function(queryWhere, callback) {
    queryString = 'SELECT * FROM articles';
    if (!isEmptyObject(queryWhere))
        queryString += generateWhere(queryWhere);
    queryString +=' ORDER BY date';
    connection.query(queryString, function(err, result) {
        callback(err, result.slice(0, 9));
    });
};

/**
 * Like an Article
 */
module.exports.like = function(url, email, callback) {
    connection.query('INSERT INTO likes SET url = ?, email = ?', [url, email], function(err) {
        callback(err);
    });
};
    
/**
 * Remove Like on an Article
 */
module.exports.removeLike = function(url, email, callback) {
    connection.query('DELETE FROM likes WHERE url = ? AND email = ?', [url, email], function(err) {
        callback(err);
    });
};
    
/**
 * Get all Liked Articles URL
 */
module.exports.getLikesURL = function(email, callback) {
    connection.query('SELECT url FROM likes WHERE email = ?', email, function(err, result) {
        callback(err, result);
    });
};

/**
 * Get all Liked Articles with Statistics
 */
module.exports.getLikes = function(email, callback) {
    connection.query("SELECT * FROM articles, likes WHERE articles.url = likes.url AND email = ?", email, function(err, result) {
        callback(err, result);
    });
};

/**
 * Get User Added articles
 */
module.exports.getUserAddedArticles = function(email, callback) {
    connection.query("SELECT * FROM articles, owner WHERE articles.url = owner.url AND email = ?", email, function(err, result) {
        callback(err, result);
    });
};
