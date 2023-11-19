<script setup>
import { computed, defineProps, ref } from 'vue';

const props = defineProps(['chart_config', 'activeChart', 'series', 'map_config']);

const tableData = ref({});

tableData.value = {
	data: props.series,
};

const filterText = ref('');

const filteredData = computed(() => {
	if (!filterText.value) {
		return tableData.value.data;
	}
	return tableData.value.data.filter(row => {
		return Object.values(row).some(value => {
			return String(value).toLowerCase().includes(filterText.value.toLowerCase());
		});
	});
});
</script>

<template>
	<div v-if="activeChart === 'DataTableChart'">
		<div class="filter">
			<input type="text" v-model="filterText" placeholder="請輸入要篩選的資料值" />
			<span>共有 <code>{{filteredData.length}}</code> 筆符合的資料</span>
		</div>
		<table v-if="filteredData">
			<thead>
				<tr>
					<th v-for="(value, key) in props.chart_config.categories" :key="key">
						{{ value }}
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(row, index) in filteredData" :key="index">
					<td v-for="(value, key) in row" :key="key">
						{{ value }}
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<style scoped lang="scss">
.filter {
	display: flex;
	justify-content: space-between;
	align-items: center;
	column-count: 2;
	flex-direction: row;
	margin-bottom: 4px;
	font-size: small;
	
	input {
		font-size: small;
	}

	span {
		color: gray;
	}
}

table {
	font-size: small;
	border-collapse: collapse;
	width: 100%;
}

th,
td {
	text-align: left;
	padding: 8px;
}

th {
	background-color: rgba(255, 255, 255, 0.2);
	color: white;
}

tr:nth-child(even) {
	background-color: rgba(255, 255, 255, 0.05);
}
</style>
