<template>
  <router-view/>
</template>

<script setup>
import {onBeforeMount} from "vue";
import {resumeData} from '@/data'

onBeforeMount(() => document.title = resumeData.name);
</script>

<style>
body {
  background-color: #f3f4f6;
}
</style>

