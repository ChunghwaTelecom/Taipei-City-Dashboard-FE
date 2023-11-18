<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref } from "vue";

const props = defineProps(["chart_config", "activeChart", "series"]);

const chartOptions = ref({
	chart: {
		toolbar: {
			show: false,
			tools: {
				zoom: false,
			},
		},
	},
	colors: props.chart_config.color,
	dataLabels: {
		enabled: false,
	},
	grid: {
		show: false,
	},
	legend: {
		show: props.series.length > 1 ? true : false,
	},
	markers: {
		hover: {
			size: 5,
		},
		size: 3,
		strokeWidth: 0,
	},
	stroke: {
		colors: props.chart_config.color,
		curve: "smooth",
		show: true,
		width: 2,
	},
	forecastDataPoints: {
		count: forecastDataPoints()
	},
	fill: {
		type: 'gradient',
		gradient: {
			shade: 'dark',
			gradientToColors: [ '#FDD835'],
			shadeIntensity: 1,
			type: 'horizontal',
			opacityFrom: 1,
			opacityTo: 1,
			stops: [0, 100, 100, 100]
		},
	},
	tooltip: {
		custom: function ({ series, seriesIndex, dataPointIndex, w }) {
			// The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css
			return (
				'<div class="chart-tooltip">' +
				"<h6>" +
				`${parseTime(
					w.config.series[seriesIndex].data[dataPointIndex].x
				)}` +
				` - ${w.globals.seriesNames[seriesIndex]}` +
				"</h6>" +
				"<span>" +
				series[seriesIndex][dataPointIndex] +
				` ${props.chart_config.unit}` +
				"</span>" +
				"</div>"
			);
		},
	},
	annotations: {
		xaxis: [{
			x: new Date().getTime(),
			strokeDashArray: 0,
			borderColor: '#775DD0',
			label: {
				borderColor: '#775DD0',
				style: {
					color: '#fff',
					background: '#775DD0',
				}
			}
		}]
	},
	xaxis: {
	axisBorder: {
		color: "#555",
		height: "0.8",
	},
	axisTicks: {
		show: false,
	},
	crosshairs: {
		show: false,
	},
	tooltip: {
		enabled: false,
	},
	type: "datetime",
}
	,yaxis: [{
		title: {
			text: props.series[0].name,
		},


	}],
});

function forecastDataPoints() {
	let count = 0;
	const now = new Date();
	props.series[0].data.forEach(obj=> {
		if (new Date(obj.x) > now) {
			count = count+1;
		}
	});
	return (count-1);
}

function parseTime(time) {
	return time.replace("T", " ").replace("+08:00", " ");
}
</script>

<template>
	<div v-if="activeChart === 'TimelineSeparateChartWithForecast'">
		<apexchart
			type="line"
			width="100%"
			height="260px"
			:options="chartOptions"
			:series="series"
		></apexchart>
	</div>
</template>
