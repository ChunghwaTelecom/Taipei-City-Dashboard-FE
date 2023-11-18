<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { useDialogStore } from "../../store/dialogStore";
import { useContentStore } from "../../store/contentStore";

import DialogContainer from "./DialogContainer.vue";
import { chartTypes } from "../../assets/configs/apexcharts/chartTypes.js";
import ComponentContainer from "../components/ComponentContainer.vue";
import ReportIssue from "./ReportIssue.vue";
import MoreInfo from "./MoreInfo.vue";

const dialogStore = useDialogStore();
const contentStore = useContentStore();

function changeActiveChart(chartName) {
	activeChart.value = chartName;
}
</script>

<template>
	<DialogContainer
		:dialog="`story`"
		@on-close="dialogStore.hideAllDialogs"
	>
		<div v-if="dialogStore.storyContent.content.story.length !== 0" >
			<ComponentContainer
				v-for="item in dialogStore.storyContent.content.story"
				:content="contentStore.components[item]"
				:notMoreInfo="false"
				:key="item.index" />
		</div>
	</DialogContainer>
</template>

<style scoped lang="scss">
.dashboard {
	//max-height: calc(100vh - 127px);
	//max-height: calc(var(--vh) * 100 - 127px);
	//display: grid;
	//row-gap: var(--font-s);
	//column-gap: var(--font-s);
	margin: var(--font-m) var(--font-m);
	overflow-y: scroll;

	@media (min-width: 720px) {
		grid-template-columns: 1fr 1fr;
	}

	@media (min-width: 1150px) {
		grid-template-columns: 1fr 1fr 1fr;
	}

	@media (min-width: 1800px) {
		grid-template-columns: 1fr 1fr 1fr 1fr;
	}

	@media (min-width: 2200px) {
		grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
	}

	&-nodashboard {
		grid-template-columns: 1fr;

		&-content {
			width: 100%;
			//height: calc(100vh - 127px);
			//height: calc(var(--vh) * 100 - 127px);
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;

			span {
				margin-bottom: 1rem;
				font-family: var(--font-icon);
				font-size: 2rem;
			}

			button {
				color: var(--color-highlight)
			}

			div {
				width: 2rem;
				height: 2rem;
				border-radius: 50%;
				border: solid 4px var(--color-border);
				border-top: solid 4px var(--color-highlight);
				animation: spin 0.7s ease-in-out infinite;
			}
		}
	}
}

@keyframes spin {
	to {
		transform: rotate(360deg);
	}
}
</style>
