//https://www.paulox.net/2021/07/19/maps-with-django-part-2-geodjango-postgis-and-leaflet/#showing-markers-in-the-map

const copy = '© <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
const url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const osm = L.tileLayer(url, { attribution: copy })
const map = L.map('map', { layers: [osm] })
const layerGroup = L.layerGroup().addTo(map)
map.locate()
  .on('locationfound', e => map.setView(e.latlng, 9))
  .on('locationerror', () => map.setView([41.8988, 12.5451], 9))

async function load_borders() {
  let border_url = ``
  const zoom = map.getZoom()
  //console.log(zoom)
  if (zoom<10){
    border_url = `/map-api/borders/lo/?in_bbox=${map.getBounds().toBBoxString()}`
  } else if (zoom<12){
    border_url = `/map-api/borders/md/?in_bbox=${map.getBounds().toBBoxString()}`
  } else if (zoom<15){
    border_url = `/map-api/borders/hi/?in_bbox=${map.getBounds().toBBoxString()}`
  } else {
    border_url = `/map-api/borders/full/?in_bbox=${map.getBounds().toBBoxString()}`
  }
  const response = await fetch(border_url)
  const geojson = await response.json()
  return geojson
}
async function render_borders() {
  const borders = await load_borders()
  layerGroup.clearLayers()
  L.geoJSON(borders).bindPopup(layer => layer.feature.properties.name).addTo(layerGroup)
}
map.on('moveend', render_borders)
