var map = L.map('map').setView([51.505, -0.09], 13);
var tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var data = JSON.parse(data);
var nb = data.length;
var listPoint = Array();
for (let i=0; i<nb; i++){
    if(data[i].latitude != null && data[i].longitude != null){
        listPoint.push(L.marker([data[i].latitude, data[i].longitude]).addTo(map));
    }
}