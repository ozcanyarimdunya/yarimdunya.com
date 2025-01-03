<template>
  <router-view/>
</template>

<script setup>
import {onBeforeMount} from "vue";
import data from '@/data'

onBeforeMount(() => document.title = data.name);
</script>

<style>
body {
  background-color: #f3f4f6;
}
</style>

