const http = require('http');
let fs = require('fs');
let xml2js = require('xml2js');
let builder = new xml2js.Builder();
const payload = require('./payload.js');
const soapHandler = require('./soap_handler.js');

const port = 8000;

// Create a server object
http.createServer(function (req, res) {
    let data = [];
    req.on('data', chunk => {
        console.log('Data chunk available:', chunk);
        data.push(chunk);
    });
    req.on('end', () => {
        console.log('end of data');
        if (data !== '') {
            console.log(data.toString('UTF-8'));
        } else {
            console.log('No response body found.');
        }
    });
    req.on('error', err => {
        console.log('Error:', err);
    });

    // handle response
    res.writeHead(200, {'Content-Type': 'text/xml'});
    let xml = builder.buildObject(payload);
    res.write(xml);
    res.end();
}).listen(port);

console.log("Listening on", port);
console.log();
