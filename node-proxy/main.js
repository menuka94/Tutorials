var Http = require('http');

var req = Http.request({
        host: '192.168.5.8',
        port: 3128,
        method: 'GET',
        path: 'http://www.espn.com/' // full URL as path
    }, function (res) {
        console.log('function(res)');
        res.on('data', function (data) {
            console.log("res.on('data')");
            console.log(data.toString());
        });

        res.on('error', function (err) {
            console.log('Error:', err.toString());
        });

    }
);

req.end();