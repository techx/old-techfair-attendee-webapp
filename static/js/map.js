var TECHFAIRMAP_DEBUG=false;
function techfairmap_aftersearch(response)
{
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
}
function techfairmap_beforesearch(query)
{
	$.mobile.loading('show', {});
	$('#q').val(query);
}

$(document).ready(function() {
	$(window).hashchange(function() {
		// Alerts every time the hash changes!
		if(location.hash.length>1) {
			if(location.hash.substr(1) == 'TECHFAIRMAPDEBUG-IDONOTTHINKSOMEONECANACCIDENTALLYTYPETHISSENTENSEWITHOUTVIEWINGTHESOURCECODEORWITHLINK') {
				TECHFAIRMAP_DEBUG = true;
			} else {
				techfairmap_search(location.hash.substr(1));
			}
		}
		else
			techfairmap_search('');
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
	techfairmap_init('map');
	$("#search-form").submit(function(event) {
		/* stop form from submitting normally */
		event.preventDefault();
		
		location.hash = '#'+$('#q').val();

		return false;
	});
});
