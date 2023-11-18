<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { ref, computed } from "vue";
import { useMapStore } from "../../store/mapStore";
import axios from "axios";
import { TaipeiVillage } from "../../assets/configs/mapbox/mapConfig.js";
import ComponentContainer from "../components/ComponentContainer.vue";
import { useDialogStore } from "../../store/dialogStore.js";
import { useContentStore } from "../../store/contentStore.js";

import StoryComponet from "../components/StoryComponet.vue";

const { BASE_URL } = import.meta.env;

const props = defineProps(["chart_config", "activeChart", "series", "map_config"]);
const mapStore = useMapStore();

const dialogStore = useDialogStore();
const contentStore = useContentStore();

const chartOptions = ref({
	chart: {
		offsetY: 15,
		stacked: true,
		toolbar: {
			show: false
		}
	},
	colors: props.chart_config.color,
	dataLabels: {
		offsetX: 20,
		textAnchor: "start"
	},
	grid: {
		show: false
	},
	legend: {
		show: false
	},
	plotOptions: {
		bar: {

			borderRadius: 2,
			distributed: true,
			horizontal: true
		}
	},
	stroke: {
		colors: ["#282a2c"],
		show: true,
		width: 0
	},
	// The class "chart-tooltip" could be edited in /assets/styles/chartStyles.css
	tooltip: {
		custom: function ({ series, seriesIndex, dataPointIndex, w }) {
			return '<div class="chart-tooltip">' +
				'<h6>' + w.globals.labels[dataPointIndex] + '</h6>' +
				'<span>' + series[seriesIndex][dataPointIndex] + ` ${props.chart_config.unit}` + '</span>' +
				'</div>';
		},
		followCursor: true,
	},
	xaxis: {
		axisBorder: {
			show: false,
		},
		axisTicks: {
			show: false,
		},
		labels: {
			show: false,
		},
		type: 'category',
	},
	yaxis: {
		labels: {
			formatter: function (value) {
				return value.length > 7 ? value.slice(0, 6) + "..." : value;
			},
		},
	},
});
</script>

<template>
	<div v-if="activeChart === 'StoryChart'">
		<StoryComponet />
	</div>
</template>