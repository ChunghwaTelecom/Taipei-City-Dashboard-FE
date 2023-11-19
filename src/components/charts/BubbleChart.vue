<script setup>
import { defineProps, onMounted, onUpdated } from "vue";

const props = defineProps(["chart_config", "activeChart", "series"]);
const svgId = "bubbleChart" + Math.random().toString(36).substr(2, 9);

function isOverlapping(newBubble, bubbles) {
	for (let bubble of bubbles) {
		let dx = newBubble.x - bubble.x;
		let dy = newBubble.y - bubble.y;
		let distance = Math.sqrt(dx * dx + dy * dy);

		if (distance < newBubble.radius + bubble.radius) {
			return true;
		}
	}
	return false;
}

function generateRandomBubble(maxWidth, maxHeight, category, value) {
	let radius = Math.sqrt(value) * 5; // Calculate radius based on the square root of the value
	let x = Math.random() * (maxWidth - 2 * radius) + radius;
	let y = Math.random() * (maxHeight - 2 * radius) + radius;

	// Ensure x is within bounds
	x = Math.max(radius, Math.min(x, maxWidth - radius));

	// Ensure y is within bounds
	y = Math.max(radius, Math.min(y, maxHeight - radius));
	return { x: x, y: y, radius: radius, text: category };
}

function addBubble(bubbles, maxWidth, maxHeight, maxAttempts, category, value) {
	for (let attempts = 0; attempts < maxAttempts; attempts++) {
		let newBubble = generateRandomBubble(maxWidth, maxHeight, category, value);
		if (!isOverlapping(newBubble, bubbles)) {
			bubbles.push(newBubble);
			return;
		}
	}
	throw new Error("Failed to place a bubble after max attempts");
}

function drawBubble(bubble, svg) {
	let circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
	circle.setAttribute("cx", bubble.x);
	circle.setAttribute("cy", bubble.y);
	circle.setAttribute("r", bubble.radius);
	circle.setAttribute("fill", "rgba(255, 192, 203, 0.6)"); // Semi-transparent blue
	circle.setAttribute("stroke", "rgba(255, 192, 203, 1)");
	let text = document.createElementNS("http://www.w3.org/2000/svg", "text");
	text.setAttribute("x", bubble.x + 1);
	text.setAttribute("y", bubble.y + 1);
	text.setAttribute("text-anchor", "middle");
	text.setAttribute("fill", "white");
	let textContent = document.createTextNode(bubble.text);
	text.appendChild(textContent);
	svg.appendChild(circle);
	svg.appendChild(text);
}

function createBubbleChart() {
	if (document.getElementById(svgId)) {
		let svg = document.getElementById(svgId);

		let bubbles = [];
		let maxAttempts = 100;
		let numberOfBubbles = props.chart_config.categories.length;
		let chartWidth = svg.getAttribute("width");
		let chartHeight = svg.getAttribute("height");

		const maxValue = props.series[0].data.reduce((a, b) => Math.max(a, b));

		for (let i = 0; i < numberOfBubbles; i++) {
			let category = props.chart_config.categories[i];
			let value = props.series[0].data[i];
			let radius = (value / maxValue) * 30;
			addBubble(bubbles, chartWidth, chartHeight, maxAttempts, category, radius);
		}

		for (let bubble of bubbles) {
			drawBubble(bubble, svg);
		}
	}
}
onMounted(() => {
	setTimeout(() => {
		createBubbleChart();
	}, 100);
});
onUpdated(() => {
	createBubbleChart();
});

</script>

<template>
	<div v-if="activeChart === 'BubbleChart'">
		<div>
			<svg :id="svgId" width="360" height="240"></svg>
		</div>
	</div>
</template>
