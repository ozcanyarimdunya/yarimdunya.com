<template>
  <main class="sm:py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2 text-muted-foreground">
        <router-link :to="{name: 'home'}">
          <ArrowLeftIcon class="size-6"/>
        </router-link>
        <h1 class="text-md">
          Not Found
        </h1>
      </div>
      <div class="flex flex-col items-center justify-center gap-2">
        <ExclamationTriangleIcon class="size-10 text-muted-foreground"/>
        <span class="text-muted-foreground text-center">
          The page you are looking for does not exist.
        </span>
      </div>
    </div>
  </main>
</template>

<script setup>
import {ArrowLeftIcon, ExclamationTriangleIcon} from "@radix-icons/vue";
</script>

<style scoped>

</style>