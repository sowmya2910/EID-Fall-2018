// Initialize SQS and variables
var AWS = require('aws-sdk');
AWS.config.update({region: 'REGION'});
var sqs = new AWS.SQS();
var averagetemperature = 0.00;
var averagehumidity = 0.00;
var totaltemperature = 0.00;
var totalhumidity = 0.00;
var maximumtemperature = 0.00;
var maximumhumidity = 0.00;
var minimumtemperature = 100.00;
var minimumhumidity = 100.00;
var count = 1.0;

    //Function that is called every time a message is received (event happens)
    exports.handler = (event, context, callback) => {
    var eventText = JSON.stringify(event, null, 2);
    console.log("Received event:", eventText);
    //Taking values received from the IoT topic
    var currenttemperature = parseFloat(event.Temperature);
    var currenthumidity = parseFloat(event.Humidity);
    //Computing min, max and average values
    maximumtemperature = Math.max(maximumtemperature, currenttemperature);
    maximumhumidity = Math.max(maximumhumidity, currenthumidity);
    minimumtemperature = Math.min(minimumtemperature, currenttemperature);
    minimumhumidity = Math.min(minimumhumidity, currenthumidity);
    totaltemperature += currenttemperature;
    totalhumidity += currenthumidity;
    averagetemperature = (totaltemperature/count);
    averagehumidity = (totalhumidity/count);
    averagetemperature = averagetemperature.toFixed(2);
    averagehumidity = averagehumidity.toFixed(2);
    maximumtemperature = maximumtemperature.toFixed(2);
    maximumhumidity = maximumhumidity.toFixed(2);
    minimumtemperature = minimumtemperature.toFixed(2);
    minimumhumidity = minimumhumidity.toFixed(2);

    //Message to be transferred to SQS Queue
    var params = {
     DelaySeconds: 0,
     MessageBody: "{ \"curr_temp\": " + currenttemperature +", " + " \"avg_temp\": " + averagetemperature + "," + "\"max_temp\": " + maximumtemperature + "," + "\"min_temp\": " + minimumtemperature + "," +"\"curr_humid\": " + currenthumidity + "," + "\"avg_humid\": " + averagehumidity + "," + "\"max_humid\": " + maximumhumidity + "," + "\"min_humid\": " + minimumhumidity + "}",
     QueueUrl: "https://sqs.us-east-1.amazonaws.com/434557601411/EIDProject3_Queue"
    };

    //Sending message to SQS queue every time an event is generated
    sqs.sendMessage(params, function(err,data){
    if(err) {
      console.log('error:',"Fail Send Message" + err);
    }else{
      console.log('data:',data.MessageId);
    }
});
    //Logging values
    console.log(maximumtemperature, minimumtemperature, maximumhumidity, minimumhumidity, averagetemperature, averagehumidity, count);
    count++;
    callback(null, currenthumidity);
};
