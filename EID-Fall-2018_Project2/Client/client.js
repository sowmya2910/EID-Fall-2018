/*
# Javascript to ensure connection, exchange of data between client and server and allocate functions for button presses
#
# Authors: Sowmya Ramakrishnan and Vinayak Srivatsan Kovalam Mohan
#
*/
	
//Log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

//Initialisation variables
$(document).ready(function () {
  var websocket;
  var temperature = 0;
  var fahrenheit = 0;
  var switch_current_data;
  var switch_avg_data;
  var switch_min_data;
  var switch_max_data;
  var error;
  
    // create websocket instance
    websocket = new WebSocket("ws://10.0.0.37:8888/ws");

    websocket.onerror = function(error){
      alert("Error Connecting to Server")
    }
    websocket.onclose = function(evt) {
      alert("Retry Refreshing the Webpage!");
    }
    
    //Callback function
    websocket.onmessage = function(evt) {
		
	        //Using - delimiter to split and get data values
		var data = evt.data.split("-")
     
		//For graphs, open new window
		if(data[0] == "graph_temp"){
			window.open(data[1]);
		}

		if(data[0] == "graph_hum"){
			window.open(data[1]);
		}

	    	//Current Temperature
		if(data[0] == "current_temp"){
			if(fahrenheit){
				var temperature = parseFloat(data[1])
				temperature = ((temperature * 9.0)/5.0)+32
				$("#Current_Temperature_Output").val(temperature.toFixed(2)+ "\u00b0F Time Stamp: " + data[2] );
			}
			else{
				$("#Current_Temperature_Output").val(data[1] + "\u00b0C Time Stamp: " + data[2]);
			}
		}
		
	    	//Maximum Temperature
		if(data[0] == "max_temp"){
			if(fahrenheit){
				var temperature = parseFloat(data[1])
				temperature = ((temperature * 9.0)/5.0)+32
				$("#Maximum_Temperature_Output").val(temperature.toFixed(2)+ "\u00b0F Time Stamp: " + data[2]);
			}
			else{
				$("#Maximum_Temperature_Output").val(data[1] + "\u00b0C Time Stamp: " + data[2]);
			}
		}
		
	    	//Minimum Temperature
		if(data[0] == "min_temp"){
			if(fahrenheit){
				var temperature = parseFloat(data[1])
				temperature = ((temperature * 9.0)/5.0)+32
				$("#Minimum_Temperature_Output").val(temperature.toFixed(2)+ "\u00b0F Time Stamp: " + data[2]);
			}
			else{
				$("#Minimum_Temperature_Output").val(data[1] + "\u00b0C Time Stamp: " + data[2]);
			}
		}
		
	    	//Average Temperature
		if(data[0] == "avg_temp"){
			if(fahrenheit){
				var temperature = parseFloat(data[1])
				temperature = ((temperature * 9.0)/5.0)+32
				$("#Average_Temperature_Output").val(temperature.toFixed(2)+ "\u00b0F Time Stamp: " + data[2]);
			}
			else{
				$("#Average_Temperature_Output").val(data[1] + "\u00b0C Time Stamp: " + data[2]);
			}
		}

	    	//Current Humidity
		if(data[0] == "current_hum"){
			$("#Current_Humidity_Output").val(data[1] + "% Time Stamp: " + data[2]);
		}
		
	    	//Maximum Humidity
		if(data[0] == "max_hum"){
			$("#Maximum_Humidity_Output").val(data[1] + "% Time Stamp: " + data[2]);
		}
		
	    	//Minimum Humidity
		if(data[0] == "min_hum"){
			$("#Minimum_Humidity_Output").val(data[1] + "% Time Stamp: " + data[2]);
		}
		
	    	//Average Humidity
		if(data[0] == "avg_hum"){
			$("#Average_Humidity_Output").val(data[1] + "% Time Stamp: " + data[2]);
		}		
	};

    //On button presses, send appropriate data
    $("#Current_Temperature_Button").click(function(evt){
      websocket.send("current_temp");
    });

    $("#Maximum_Temperature_Button").click(function(evt) {
      websocket.send("max_temp");
    });
	
    $("#Minimum_Temperature_Button").click(function(evt) {
      websocket.send("min_temp");
    });
	
    $("#Average_Temperature_Button").click(function(evt) {
      websocket.send("avg_temp");
    });

    $("#Current_Humidity_Button").click(function(evt) {
      websocket.send("current_hum");
    });
	
    $("#Maximum_Humidity_Button").click(function(evt) {
      websocket.send("max_hum");
    });

    $("#Minimum_Humidity_Button").click(function(evt) {
      websocket.send("min_hum");
    });

    $("#Average_Humidity_Button").click(function(evt) {
      websocket.send("avg_hum");
    });

    //Clearing values for the functionality of Clear Button
    $("#Clear").click(function(evt) {
      $("#Current_Temperature_Output").val(" ");
      $("#Average_Temperature_Output").val(" ");
      $("#Minimum_Temperature_Output").val(" ");
      $("#Minimum_Temperature_Output").val(" ");
      $("#Current_Humidity_Output").val(" ");
      $("#Average_Humidity_Output").val(" ");
      $("#Minimum_Humidity_Output").val(" ");
      $("#Maximum_Humidity_Output").val(" ");
    });

    //Redirecting user to Login page for the functionality of Logout Button
    $("#Logout").click(function(evt) {
      websocket.send("Logged Out");
      window.location.replace("login.html");
    });
	
    //Graph data (images) are sent for plots
    $("#graph_temp").click(function(evt) {
      websocket.send("graph_temp");
    });

    $("#graph_hum").click(function(evt) {
      websocket.send("graph_hum");
    });

    //If user asks for a Unit Switch
    $("#SwitchUnit").click(function(evt){
      var data1;

      //If Fahrenheit is asked
      if(fahrenheit){
		  
	switch_current_data = $("#Current_Temperature_Output").val()
        var data1 = switch_current_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature-32)*5.0)/9.0
        if(Number.isNaN(temperature) == false){
          $("#Current_Temperature_Output").val(temperature.toFixed(2)+"\u00b0C");
        }
        else{
          $("#Current_Temperature_Output").val("Error: No data");
        }
		
	switch_max_data = $("#Maximum_Temperature_Output").val()
        var data1 = switch_max_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature-32)*5.0)/9.0
        if(Number.isNaN(temperature) == false){
          $("#Maximum_Temperature_Output").val(temperature.toFixed(2)+"\u00b0C");
        }
        else{
          $("#Maximum_Temperature_Output").val("Error: No data");
        }
		
        switch_min_data = $("#Minimum_Temperature_Output").val()
        var data1 = switch_min_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature-32)*5.0)/9.0
        if(Number.isNaN(temperature) == false){
          $("#Minimum_Temperature_Output").val(temperature.toFixed(2)+"\u00b0C");
        }
        else{
          $("#Minimum_Temperature_Output").val("Error: No data");
        }
		
        switch_avg_data = $("#Average_Temperature_Output").val()
        var data1 = switch_avg_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature-32)*5.0)/9.0
        if(Number.isNaN(temperature) == false){
          $("#Average_Temperature_Output").val(temperature.toFixed(2)+"\u00b0C");
        }
        else{
          $("#Average_Temperature_Output").val("Error: No data");
        }

        fahrenheit = 0;
        $("#SwitchUnit").fadeOut(300).val("Switch Scale: C to F").fadeIn(300)
      }

      //Celcius values
      else{
		  
        switch_current_data = $("#Current_Temperature_Output").val()
        var data1 = switch_current_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature*9.0)/5.0)+32
        if(Number.isNaN(temperature) == false){
          $("#Current_Temperature_Output").val(temperature.toFixed(2)+"\u00b0F");
        }
        else{
          $("#Current_Temperature_Output").val("Error: No data");
        }
		
        switch_max_data = $("#Maximum_Temperature_Output").val()
        var data1 = switch_max_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature*9.0)/5.0)+32
        if(Number.isNaN(temperature) == false){
          $("#Maximum_Temperature_Output").val(temperature.toFixed(2)+"\u00b0F");
        }
        else{
          $("#Maximum_Temperature_Output").val("Error: No data");
        }
		
        switch_min_data = $("#Minimum_Temperature_Output").val()
        var data1 = switch_min_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature*9.0)/5.0)+32
        if(Number.isNaN(temperature) == false){
          $("#Minimum_Temperature_Output").val(temperature.toFixed(2)+"\u00b0F");
        }
        else{
          $("#Minimum_Temperature_Output").val("Error: No data");
        }

        switch_avg_data = $("#Average_Temperature_Output").val()
        var data1 = switch_avg_data.split("\u00b0")
        var temperature = parseFloat(data1[0])
        temperature = ((temperature*9.0)/5.0)+32
        if(Number.isNaN(temperature) == false){
          $("#Average_Temperature_Output").val(temperature.toFixed(2)+"\u00b0F");
        }
        else{
          $("#Average_Temperature_Output").val("Error: No data");
        }
		
        fahrenheit = 1;
        $("#SwitchUnit").fadeOut(300).val("Switch Scale: F to C").fadeIn(300)
      }
    });
});
