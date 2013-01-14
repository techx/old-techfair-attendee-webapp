
function techfairmap_init(map_id,url_prefix) {
	var map = L.map(map_id, {
            crs: L.CRS.Simple
	}).setView([0, 0], 2);
	L.tileLayer((typeof url_prefix !== 'undefined'? url_prefix : '')+ '/static/map/{z}/{x}/{y}.png', {
		maxZoom : 4,
		continuousWorld : false,
		attribution : '',
		continuousWorld : true,
		noWrap : true
	
	}).addTo(map);
	layergroup = L.layerGroup();
	layergroup.addTo(map);
	map.on('click', function(e) {
		if(TECHFAIRMAP_DEBUG) {
			pnt =e.latlng;
			alert(pnt.lat+','+pnt.lng);
		}
	});
}
function techfairmap_search(query,url_prefix) {
	techfairmap_beforesearch(query);
	$.post((typeof url_prefix !== 'undefined'? url_prefix : '')+'/map/search/', {
		q : query
	}, function(response) {
		layergroup.clearLayers();
		var alreadyopen = false;
		for (var id in response) {
			item = response[id];
			layergroup.addLayer( l = L.rectangle(item.pos).bindPopup("<strong>" + item.title + "</strong><br/>"+item.description+"<br/>"+"<a href='" + item.url + "'>Details</a>"));
			if (query != "" && !alreadyopen) {
				l.openPopup();
				alreadyopen = true;
			}
		}
		techfairmap_aftersearch(response);
	}, 'json');
}