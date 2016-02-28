var request = require('request');
var async = require('async');



/*
 *  Function : Makes GET request for user defined URL
 */
var makeGet = function(getUrl) {
    
    printLog("Making Get Request for URL ");
    printLog("URL :: " + getUrl);

	request(getUrl, function(error, response, body) {
			if (!error && response.statusCode == 200) {
			console.log("GOT THIS RESPONSE :: \n" + body); // Print the body of response.
            return body ;
		}
	})
};

/*
 *  Prints Console Log.
 */
var printLog = function(logToPrint) {
    console.log("\n" + logToPrint);
};


/**
 * 
 * Main Method
 */
function likeMe() {
    printLog("ok I have started ");
    var resp = makeGet("http://www.google.com");
    console.log('all dropped' + resp); 

    // makeGet("http://www.google.com").then(function(body) { 
    //     console.log('all dropped' + body); 
    // });
    

};






exports.handler = function(req, res) {
  async.parallel([
    /*
     * First external endpoint
     */
    function(callback) {
      var url = "http://www.google.com";

      request(url, function(err, response, body) {
        // JSON body
        if(err) { console.log(err); callback(true); return; }
        obj = JSON.parse(body);
        callback(false, obj);
      });
    },



    /*
     * Second external endpoint
     */
    function(callback) {
      var url = "http://external2.com/api/some_endpoint";
      request(url, function(err, response, body) {
        // JSON body
        if(err) { console.log(err); callback(true); return; }
        obj = JSON.parse(body);
        callback(false, obj);
      });
    },
  ],


  /*
   * Collate results
   */
  function(err, results) {
    if(err) { console.log(err); res.send(500,"Server Error"); return; }
    res.send({api1:results[0], api2:results[1]});
  }
  );


};






































likeMe();

