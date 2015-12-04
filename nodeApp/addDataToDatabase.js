var mysql = require('mysql');
var connection = mysql.createConnection({
    host    : 'localhost',
    user    : 'root',
    password: '1111',
    database: 'feelthenews'
});

var newsBundles = [];
newsBundles.push(require('../src/04122015_abcnews.go.com.json'));
newsBundles.push(require('../src/04122015_america.aljazeera.com.json'));
newsBundles.push(require('../src/04122015_money.cnn.com.json'));
newsBundles.push(require('../src/04122015_www.aljazeera.com.json'));
newsBundles.push(require('../src/04122015_www.bbc.com.json'));
newsBundles.push(require('../src/04122015_www.cnn.com.json'));
newsBundles.push(require('../src/04122015_www.dogonews.com.json'));
newsBundles.push(require('../src/04122015_www.nbcnews.com.json'));
newsBundles.push(require('../src/04122015_www.newscientist.com.json'));
newsBundles.push(require('../src/04122015_www.reuters.com.json'));
newsBundles.push(require('../src/04122015_www.sportingnews.com.json'));
newsBundles.push(require('../src/04122015_www.time.com.json'));

function logError(err) {
    console.log(err);
}
for (i = 0; i < newsBundles.length; i++) {
    for (j = 0; j < newsBundles[i].length; j++) {
        connection.query('INSERT INTO articles SET ?', newsBundles[i][j], logError);
    }
}
