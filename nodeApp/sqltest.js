var mysql = require('mysql');
var connection = mysql.createConnection({
    host    : 'localhost',
    user    : 'root',
    password: '1111',
    database: 'feelthenews'
});

queryWhere = "senRate = 'Positive' AND readRate > 5";
queryWhere2 = "readRate > 5";
queryString = 'SELECT title, description, senRate, readRate, category FROM articles WHERE ' + queryWhere2;

//console.log(connection.escape(' WHERE senRate = 0.5'));
//
//console.log(queryString);
//
//connection.query(queryString, function(err, result) {
//        console.log(err, result);
//});
//
connection.query("SELECT title, description, senRate, readRate, category FROM articles, likes WHERE articles.url = likes.url AND email = 'pingkochiu@gmail.com'", function(err, result) {
        console.log(err, result);
});
