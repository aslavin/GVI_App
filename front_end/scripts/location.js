function getLocation() {
    console.log("here");
    if (navigator.geolocation) {
        console.log("geolocation on");
    } else {
        console.log("geolocation off");
    }
        
    navigator.geolocation.getCurrentPosition(function(position){
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        console.log("lat: " + lat);
        console.log("lon: " + lon);
        /*
        var marker = new GMarker(new GLatLng(lat, lon));
       
        var jsMap = new GMap2(document.getElementById("jsMap"));
        jsMap.addOverlay(marker);
    },function(error){
        //use error.code to determine what went wrong
    });
    */
    });
    
}
