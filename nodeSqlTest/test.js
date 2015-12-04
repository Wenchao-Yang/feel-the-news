var mysql = require('mysql');
var connection = mysql.createConnection({
    host    : 'localhost',
    user    : 'root',
    password: '1111',
    database: 'start'
});

var johnSmith = {firstName: 'John', lastName: 'Smith', email: 'jsmith@gmail.com', password: '1234'};
var query = connection.query('INSERT INTO user SET ?', johnSmith, function(err, result) {
    if (err) {
        console.log(err);
    }
});
console.log(query.sql);

connection.query('SELECT * FROM user WHERE ?', {email:'jsmith@gmail.com'}, function(err, result) {
    if (result[0])
        console.log(result[0]);
});
