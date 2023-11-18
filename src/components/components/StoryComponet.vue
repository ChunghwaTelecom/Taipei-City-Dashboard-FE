<template>
	<div
		:class="{
			storycontainer: true,
		}">
		<section>
			<h2>準爸媽：月子中心價格、預約方式</h2>
			<p>了解月子中心的價格和預約方式，為即將成為父母的您提供相關資訊。</p>
			<p>

			</p>
		</section>

		<section>
			<h2>新生兒出生：育兒津貼申請、媽媽手冊領取、新生兒疫苗接種</h2>
			<p>瞭解如何申請育兒津貼、領取媽媽手冊以及新生兒疫苗接種的相關資訊。</p>
			<p>

			</p>
		</section>

		<section>
			<h2>嬰兒40天、滿周歲：公私立托嬰(保母)</h2>
			<p>探索公私立托嬰機構和保母的選擇，為您的寶寶提供適當的照顧和教育。</p>
			<p>
				<ComponentContainer
					:content="contentStore.components['202']"
					:notMoreInfo="false"
					:key="`story-202`" />
			</p>
			<p>
				<ComponentContainer
					:content="contentStore.components['203']"
					:notMoreInfo="false"
					:key="`story-203`" />
			</p>
		</section>

		<section>
			<h2>小朋友就學：遷戶口、公私立幼稚園評價(& 價格)</h2>
			<p>了解遷戶口的相關事項以及公私立幼稚園的評價和價格，為您的孩子提供良好的教育環境。</p>
			<p>
				<ComponentContainer
					:content="contentStore.components['204']"
					:notMoreInfo="false"
					:key="`story-204`" />
			</p>
		</section>
	</div>
</template>

<script setup>
import { useDialogStore } from "../../store/dialogStore";
import { useContentStore } from "../../store/contentStore";

import ComponentContainer from "./ComponentContainer.vue";

const dialogStore = useDialogStore();
const contentStore = useContentStore();
</script>

<style scoped lang="scss">
.storycontainer {

}
</style>