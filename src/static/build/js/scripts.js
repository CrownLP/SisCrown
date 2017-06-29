$(function(){
  alert ('OK');
  
  if (navigator.geolocation)
  {
    navigator.geolocation.getCurrentPosition (getCoords, getError);
  }
  else {

  }
  function getCoords(position)
  {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    initialize(lat, lng)
  }

  function getError(err)
  {
    initialize(-16.540790, -68.090059);
  }
  function initialize(lat, lng)
  {
    var latlng = new google.maps.latLng(lat,lng);
    var mapSettings = {
      center: latLng,
      zoom: 15,
      mapsTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map($('#mapa').get(0), mapSettings);

    var marker = new google.maps.Marker ({
        position: latlng,
        map:map,
        draggable: true,
        title: 'Arrastrame'
    })
  }
}
)
