let map;
let marker;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: -33.4332521, lng: -70.6156447},
      zoom: 17,
    });
    marker = new google.maps.Marker({
        position: { lat: -33.4332521, lng: -70.6156447},
        map: map,
    });
  }