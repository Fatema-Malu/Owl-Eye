var latlng;
var address;
geocoder = new google.maps.Geocoder();
function success(position) {
  var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  geocoder.geocode({'latLng': latlng}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      if (results[1]) {
        address = results[1].formatted_address;
        console.log(results[1]);
        // Render Stuff
      }else{
        error("Unable to reverse Geocode");
      }
    }
  });
}

function error(msg) {
  console.log(msg);
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(success, error);
} else {
  error('HTML 5 Geolocation not supported');
}