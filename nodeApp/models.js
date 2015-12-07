var mysql = require('mysql');
var pool = mysql.createPool({
    connectionLimit: 10,
    host    : 'localhost',
    user    : 'root',
    password: '1111',
    database: 'feelthenews'
});

/**
 * Finds User
 */
module.exports.findUser = function(UserID, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('SELECT * FROM user WHERE ?', UserID, function(err, result) {
            callback(err, result[0]);
            connection.release();
        });
    });
};

/**
 * Register User
 */
module.exports.registerUser = function(UserInfo, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('INSERT INTO user SET ?', UserInfo, function(err) {
            callback(err);
            connection.release();
        });
    });
};

/**
 * Update User Information
 */
module.exports.updateUser = function(UserInfo, email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('UPDATE user SET ? WHERE ?', [UserInfo, email], function(err) {
            callback(err);
            connection.release();
        });
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
            query += ' readRate > ' + pool.escape(queryObject.readRateLow);
            firstCond = false;
        } else {
            query += ' AND readRate > ' + pool.escape(queryObject.readRateLow);
        }
    }
    if (queryObject.readRateHigh) {
        if (firstCond) {
            query += ' readRate <= ' + pool.escape(queryObject.readRateHigh);
            firstCond = false;
        } else {
            query += ' AND readRate <= ' + pool.escape(queryObject.readRateHigh);
        }
    }
    if (queryObject.senRate) {
        if (firstCond) {
            query += ' senRate = ' + pool.escape(queryObject.senRate);
            firstCond = false;
        } else {
            query += ' AND senRate = ' + pool.escape(queryObject.senRate);
        }
    }
    if (queryObject.category) {
        if (firstCond) {
            query += ' category = ' + pool.escape(queryObject.category);
            firstCond = false;
        } else {
            query += ' AND category = ' + pool.escape(queryObject.category);
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
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query(queryString, function(err, result) {
            callback(err, result.slice(0, 19));
            connection.release();
        });
    });
};

/**
 * Like an Article
 */
module.exports.like = function(url, email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('INSERT INTO likes SET url = ?, email = ?', [url, email], function(err) {
            callback(err);
            connection.release();
        });
    });
};
    
/**
 * Remove Like on an Article
 */
module.exports.removeLike = function(url, email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('DELETE FROM likes WHERE url = ? AND email = ?', [url, email], function(err) {
            callback(err);
            connection.release();
        });
    });
};
    
/**
 * Get all Liked Articles URL
 */
module.exports.getLikesURL = function(email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('SELECT url FROM likes WHERE email = ?', email, function(err, result) {
            callback(err, result);
            connection.release();
        });
    });
};

/**
 * Get all Liked Articles with Statistics
 */
module.exports.getLikes = function(email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query("SELECT * FROM articles, likes WHERE articles.url = likes.url AND email = ? ORDER BY date", email, function(err, result) {
            callback(err, result);
            connection.release();
        });
    });
};

/**
 * Get User Added articles
 */
module.exports.getUserAddedArticles = function(email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query("SELECT * FROM articles, owner WHERE articles.url = owner.url AND email = ? ORDER BY date", email, function(err, result) {
            callback(err, result);
            connection.release();
        });
    });
};

/**
 * Add Article
 */
module.exports.addArticle = function(articleInfo, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query("INSERT INTO articles SET ?", articleInfo, function(err) {
            callback(err);
            connection.release();
        });
    });
};

/**
 * Add Ownership to Article
 */
module.exports.ownArticle = function(url, email, callback) {
    pool.getConnection(function(err, connection) {
        if (err) throw err;
        connection.query('INSERT INTO owner SET url = ?, email = ?', [url, email], function(err) {
            callback(err);
            connection.release();
        });
    });
};
