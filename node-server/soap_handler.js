var xml2js = require('xml2js');
var builder = new xml2js.Builder();

// const soap = `
// <?xml version="1.0" encoding="UTF-8"?>
// <env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
//     <env:Header/>
//     <env:Body optional="abc">
//         <Root>
//             <Abc attr="1">123456</Abc>
//         </Root>
//     </env:Body>
// </env:Envelope>
// `;

var options = {explicitArray: false, tagNameProcessors: [xml2js.processors.stripPrefix] };


let soapParser = function (soap) {
    xml2js.parseString(soap, options, (err, result) => {
        if (err) {
            console.log('An error has occurred: ' + err);
            return;
        }

        // Get the soap body object
        var soapBody = result.Envelope.Body;

        // Remove optional attribute(s) from <Body> element.
        if (soapBody.$) {
            delete soapBody.$;
        }

        // Get the body XML if needed
        var soapBodyXML = builder.buildObject(soapBody);

        console.log(soapBodyXML);
    });
};


module.exports = {
    soapParser
};