function getLocation() {
        
    navigator.geolocation.getCurrentPosition(function(position){
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        document.getElementById('map').src = "https://maps.google.com/maps?q=" + lat + "%2C%20" + lon + "&t=&z=13&ie=UTF8&iwloc=&output=embed";

    });
};
    