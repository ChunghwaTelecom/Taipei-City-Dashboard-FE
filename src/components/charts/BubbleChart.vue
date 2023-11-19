<script setup>
import {  defineProps, onUpdated } from "vue";
import { useMapStore } from "../../store/mapStore";

const props = defineProps(["chart_config", "activeChart", "series", "map_config"]);
const mapStore = useMapStore();

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

function generateRandomBubble(maxWidth, maxHeight, category) {
	let radius = Math.random() * 20 + 5; // Random radius between 5 and 25
	let x = Math.random() * (maxWidth - 2 * radius) + radius;
	let y = Math.random() * (maxHeight - 2 * radius) + radius;
	return { x: x, y: y, radius: radius, text: category };
}

function addBubble(bubbles, maxWidth, maxHeight, maxAttempts, category) {
	for (let attempts = 0; attempts < maxAttempts; attempts++) {
		let newBubble = generateRandomBubble(maxWidth, maxHeight, category);
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
	circle.setAttribute("fill", "rgba(0, 0, 255, 0.5)"); // Semi-transparent blue
	circle.setAttribute("stroke", "black");
	let text = document.createElementNS("http://www.w3.org/2000/svg", "text");
	text.setAttribute("x", bubble.x+1);
	text.setAttribute("y", bubble.y+1);
	text.setAttribute("text-anchor", "middle");
	text.setAttribute("fill", "white");
	let textContent = document.createTextNode(bubble.text);
	text.appendChild(textContent);
	svg.appendChild(circle);
	svg.appendChild(text);
}

function createBubbleChart() {
	if (document.getElementById("bubbleChart")) {
		let svg = document.getElementById("bubbleChart");

		let bubbles = [];
		let maxAttempts = 100;
		let numberOfBubbles = props.chart_config.categories.length;
		let chartWidth = svg.getAttribute("width");
		let chartHeight = svg.getAttribute("height");

		for (let i = 0; i < numberOfBubbles; i++) {
			addBubble(bubbles, chartWidth, chartHeight, maxAttempts, props.chart_config.categories[i]);
		}

		for (let bubble of bubbles) {
			drawBubble(bubble, svg);
		}
	}

}

onUpdated(() => {
	createBubbleChart();
});

</script>

<template>
	<div v-if="activeChart === 'BubbleChart'">
		<div>
			<svg id="bubbleChart" width="300" height="280"></svg>
		</div>
	</div>
</template>
