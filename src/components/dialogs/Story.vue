<!-- Developed by Taipei Urban Intelligence Center 2023 -->

<script setup>
import { useDialogStore } from "../../store/dialogStore";
import { useContentStore } from "../../store/contentStore";

import DialogContainer from "./DialogContainer.vue";
import ComponentContainer from "../components/ComponentContainer.vue";
import HistoryChart from "../utilities/HistoryChart.vue";
import DownloadData from "./DownloadData.vue";

const { BASE_URL } = import.meta.env;

const dialogStore = useDialogStore();
const contentStore = useContentStore();

function getLinkTag(link, index) {
	if (link.includes("data.taipei")) {
		return `資料集 - ${index + 1} (data.taipei)`;
	} else if (link.includes("tuic.gov.taipei")) {
		return `大數據中心專案網頁`;
	} else if (link.includes("github.com")) {
		return `GitHub 程式庫`;
	} else {
		return `資料集 - ${index + 1} (其他)`;
	}
}
</script>

<template>
	<DialogContainer
		:dialog="`story`"
		@on-close="dialogStore.hideAllDialogs"
	>
		<ComponentContainer
			:content="dialogStore.storyContent.content"
			:not-more-info="false"
		/>
	</DialogContainer>
</template>

<style scoped lang="scss">
.moreinfo {
	height: fit-content;
	width: auto;
	display: grid;

	@media (min-width: 820px) {
		height: 410px;
		grid-template-columns: 3fr 2fr;
	}

	@media (min-width: 1200px) {
		height: 440px;
	}

	@media (min-width: 2200px) {
		height: 550px;
	}

	//&-info {
	//	display: flex;
	//	flex-direction: column;
	//	padding: 1rem;
	//	border-top: solid 1px var(--color-border);
	//
	//	p {
	//		margin-bottom: 0.75rem;
	//		color: var(--color-complement-text);
	//		text-align: justify;
	//	}
	//
	//	h4 {
	//		color: var(--color-complement-text);
	//		font-weight: 400;
	//		font-size: 10px;
	//	}
	//
	//	@media (min-width: 820px) {
	//		border-left: solid 1px var(--color-border);
	//		border-top: none;
	//	}
	//
	//	&-data {
	//		max-height: calc(100% - 2.5rem);
	//		overflow-y: scroll;
	//		padding-right: 8px;
	//
	//		&::-webkit-scrollbar {
	//			width: 4px;
	//		}
	//		&::-webkit-scrollbar-thumb {
	//			background-color: rgba(136, 135, 135, 0.5);
	//			border-radius: 4px;
	//		}
	//		&::-webkit-scrollbar-thumb:hover {
	//			background-color: rgba(136, 135, 135, 1);
	//		}
	//	}
	//
	//	&-contributors {
	//		display: grid;
	//		grid-template-columns: 1fr 1fr;
	//		row-gap: 4px;
	//		margin: 4px 0 var(--font-s);
	//
	//		a {
	//			display: flex;
	//			align-items: center;
	//
	//			p {
	//				margin: 0;
	//				transition: color 0.2s;
	//			}
	//
	//			img {
	//				height: var(--font-xl);
	//				margin-right: 4px;
	//			}
	//
	//			&:hover p {
	//				color: var(--color-highlight);
	//			}
	//		}
	//	}
	//
	//	&-links {
	//		display: grid;
	//		grid-template-columns: 1fr 1fr;
	//
	//		a {
	//			font-size: var(--font-s);
	//			color: var(--color-complement-text);
	//			transition: color 0.2s;
	//
	//			&:hover {
	//				color: var(--color-highlight);
	//			}
	//		}
	//	}
	//
	//	&-control {
	//		display: flex;
	//		align-items: flex-end;
	//		justify-content: flex-end;
	//		flex: 1;
	//
	//		span {
	//			margin-right: 4px;
	//			font-family: var(--font-icon);
	//			font-size: calc(var(--font-m) * var(--font-to-icon));
	//		}
	//
	//		button {
	//			display: flex;
	//			align-items: center;
	//			margin-left: 8px;
	//			padding: 2px 4px;
	//			border-radius: 5px;
	//			background-color: var(--color-highlight);
	//			font-size: var(--font-m);
	//			transition: opacity 0.2s;
	//
	//			&:hover {
	//				opacity: 0.8;
	//			}
	//		}
	//	}
	//}
}
</style>
