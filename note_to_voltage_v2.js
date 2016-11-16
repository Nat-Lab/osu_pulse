var shock_time = 200;

if(!process.argv[2]) {
	console.error('usage: node ' + process.argv[1] + ' <osu_file>');
	process.exit(1);
}

var osu_parser = require('osu-parser');
osu_parser.parseFile(process.argv[2], function(err, osu) { 
	var ms_pre_beat = osu.timingPoints[0].beatLength;
	osu.hitObjects.forEach(function(hit) {
		switch(hit.objectName) {
			case 'spinner':
			case 'slider':
				for(var i = hit.startTime; i <= hit.endTime; i += ms_pre_beat) {
					console.log(Math.round(i) + ":" + 255);
					console.log(Math.round(i + shock_time) + ":" + 0);
				}
				break;
			case 'circle':
				console.log(hit.startTime + ":" + 255)
				console.log((hit.startTime+shock_time) + ":" + 0)
				break;
		}
	});
});
