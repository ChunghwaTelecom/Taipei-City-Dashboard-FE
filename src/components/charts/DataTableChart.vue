<script setup>
import { computed, defineProps, ref } from 'vue';


const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);

function getDistrict() {
	const result = [];
	props.series.forEach(data => {
		result.push(data.name);
	});
	return result;
}

const tableData = ref({  });
function onSelectChange($event) {
	const filtered = props.series.filter(data=> {
		return (data.name === $event.target.value);
	})
	tableData.value = filtered[0];
}

</script>



<template>
	<div v-if="activeChart === 'DataTableChart'" >
		行政區: <select @change="onSelectChange($event)">
				<option v-for="option in getDistrict()" v-bind:value="option" >
					{{ option }}
				</option>
			</select>
		<table v-if="tableData">
			<thead>
			<tr>
				<th v-for="(value, key) in props.chart_config.categories" :key="key">
					{{ value }}
				</th>
			</tr>
			</thead>
			<tbody>
			<tr v-for="(row, index) in tableData.data" :key="index">
				<td v-for="(value, key) in row" :key="key">
					{{ value }}
				</td>
			</tr>
			</tbody>
		</table>
	</div>

</template>
