var spawn = require('child_process').spawn;
var py = spawn('python', ['../src/merge.py', '-u', 'http://www.foxnews.com/us/2015/12/04/2-suspects-killed-shootout-san-bernardino-massacre-14-killed/']);
py.stdout.on('data', function(data) {
    console.log(JSON.stringify(data));
}); 

