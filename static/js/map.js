function loadScript(url, callback) {
	var script = document.createElement("script");

	if (script.readyState) {
		script.onreadystatechange = function () {
			if (script.readyState === "loaded" ||
				script.readyState === "complete") {
				script.onreadystatechange = null;
				callback();
			}
		};
	} else {
		script.onload = function () {
			callback();
		};
	}

	script.src = url;
	document.getElementsByTagName("head")[0].appendChild(script);
}

function initYandexMap() {
	ymaps.ready(function () {

		$('.js-map').each(function() {
			let $this = $(this);
			let locationLat = 55.030204; // координаты по умолчанию
			let locationLong = 82.920430; // координаты по умолчанию
			let zoom = $this.attr('data-zoom');

			if (zoom === '' || zoom === undefined) {
				zoom = 13;
			}
			
			if ($this.attr('data-lat') !== '' && $this.attr('data-long') !== '') {
				locationLat = JSON.parse($this.attr('data-lat'));
				locationLong = JSON.parse($this.attr('data-long'));
			}

			let mapInstance = new ymaps.Map($this.get(0), {
				center: [locationLat, locationLong],
				zoom: zoom,
				controls: ['zoomControl', 'typeSelector']
			}, {
				searchControlProvider: 'yandex#search'
			});

			let balloon = mapInstance.geoObjects.add(new ymaps.Placemark([locationLat, locationLong], {}, {
				iconLayout: 'default#image',
				iconImageHref: mapBalloonPath,
				iconImageSize: [82, 108], // размер балуна
				iconImageOffset: [-41, -54], // размер балуна / 2
			}));

		});
	});
}

document.addEventListener("DOMContentLoaded", function () {

	setTimeout(function () {
		loadScript(mapURL, initYandexMap);
	}, 1500);
});
