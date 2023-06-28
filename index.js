const express = require('express'); //Import the express dependency
const os = require('os');
const app = express();          //Instantiate an express app, the main work horse of this serve
const port = 5001;                  //Save the port number where your server will be listening
const ip = getIPaddress();
const bodyParser = require('body-parser');

function getIPaddress() {
  const interfaces = os.networkInterfaces();
  for (const devName in interfaces) {
    const iface = interfaces[devName];
    for (let i = 0; i < iface.length; i++) {
      const alias = iface[i];
      if (alias.family === 'IPv4' && alias.internal === false) {
        return alias.address;
      }
    }
  }
  return null;
}

app.use(bodyParser.json());

app.post('/NODESERVER/testapi', (req, res) => {
    
    console.log("New request arrived!");
    var name = '';
    let json = '';
    req.on('data', chunk => {
      json += chunk;
    });
    req.on('end', () => {
      const data = JSON.parse(json);
      name = data.name;
      console.log(name);
    });

    //if (name === "CPU-LOAD") {
      //generate cpu load
      console.log("Generating CPU load!")
      let keepRunning = true;
      let rightNow = Date.now();
      let result = 0;
      let ms = 1000 * 5;
  
      while (keepRunning) {
          result += Math.random() * Math.random();
  
          if (Date.now() > rightNow + ms) {
              break;
          }
      }
    // }else{
    //   console.log("We should not ve here!");
    // }
  
  console.log(req.body)
  res.send(req.body);

});

app.listen(port,ip,() => {            //server starts listening for any attempts from a client to connect at port: {port}
    console.log(`Now listening on port ${port}`);
});