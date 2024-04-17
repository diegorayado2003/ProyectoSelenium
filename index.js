const express = require("express");
const app = express()
const path = require('path');
const port = 8080

app.use(express.static(path.join(__dirname,'public')));

    app.get('/', async(req, res) => 
    {
      res.sendFile(path.join(__dirname, 'public','ThomYorke.html'));
    });
    

//listen
app.listen(port , () =>{
console.log('Escuchando del puerto ' + port)
});
