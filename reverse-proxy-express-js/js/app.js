var express = require('express');
var app = express();
var httpProxy = require('http-proxy');
var apiProxy = httpProxy.createProxyServer();

var serverOne = 'http://localhost:3001';
var serverTwo = 'http://localhost:3002';
var serverThree = 'http://localhost:3003';

app.all("/app1/*", function (req, res) {
    console.log("Redirecting to server 1");
    apiProxy.web(req, res, {target: serverOne});
});

app.all("/app2/*", function (req, res) {
    console.log("Redirecting to server 2");
    apiProxy.web(req, res, {target: serverTwo});
});

app.all("/app3/*", function (req, res) {
    console.log("Redirecting to server 3");
    apiProxy.web(req, res, {target: serverThree});
});

app.listen(3000);
