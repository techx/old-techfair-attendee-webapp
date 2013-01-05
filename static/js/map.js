function search(query) {
	$.mobile.loading('show', {});
	$('#q').val(query);
	$.post('/map/search/', {
		q : query
	}, function(response) {
		layergroup.clearLayers();
		var alreadyopen = false;
		for (var id in response) {
			item = response[id];
			layergroup.addLayer( l = L.marker(item.pos).bindPopup("<strong>" + item.title + "</strong><br/><a href='" + item.url + "'>Website</a>"));
			if (query != "" && !alreadyopen) {
				l.openPopup();
				alreadyopen = true;
			}
		}
		$.mobile.loading('hide', {});
		if (response.length == 0) {
			$.mobile.loading('show', {
				text : 'Location not found :(',
				textVisible : true,
				textonly : true,
				theme : 'e',
				html : ""
			});
			setTimeout($.mobile.hidePageLoadingMsg, 1500);
		}
	}, 'json');
}


$(document).ready(function() {
	$(window).hashchange(function() {
		// Alerts every time the hash changes!
		if(location.hash.length>1)
			search(location.hash.substr(1));
		else
			search('');
	})
	// Trigger the event (useful on page load).
	$(window).hashchange();
	// http://zsprawl.com/iOS/2012/05/completely-disabling-zoom-in-jquery-mobile-1-1-0/
	$(document).bind("mobileinit", function(event) {
		$.extend($.mobile.zoom, {
			locked : true,
			enabled : false
		});
		
	});

	var map = L.map('map').setView([0, 0], 2);
	L.tileLayer('/static/map/{z}/{x}/{y}.png', {
		maxZoom : 4,
		continuousWorld : false,
		attribution : '',
		continuousWorld : true,
		noWrap : true

	}).addTo(map);
	layergroup = L.layerGroup();
	layergroup.addTo(map);
	layergroup.addLayer(L.marker([20, 5]).bindPopup('a'));
	$("#search-form").submit(function(event) {
		/* stop form from submitting normally */
		event.preventDefault();
		
		location.hash = '#'+$('#q').val();

		return false;
	});
});
