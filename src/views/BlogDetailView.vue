<template>
  <main class="px-4 sm:px-0 py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2">
        <router-link to="/blog">
          <ArrowLeftIcon class="size-8 text-primary"/>
        </router-link>
        <h1 class="text-2xl font-semibold w-full ">
          {{ blog.title }}
        </h1>
        <p class="text-muted-foreground text-sm text-end text-nowrap">
          {{ blog.date }}
        </p>
      </div>
      <div v-html="blog.html" class="prose prose-sm prose-code:text-xs prose-img:rounded min-w-full"></div>
      <p class="text-muted-foreground text-sm text-end">
        Published on {{ blog.date }}
      </p>

    </div>
  </main>
</template>

<script setup>
import {ArrowLeftIcon} from "@radix-icons/vue";
import {onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import blogFiles from "@/data/blog-files";
import {marked} from "marked";

const route = useRoute()
const blog = ref({})

onMounted(() => {
  blog.value = blogFiles.find(b => b.slug === route.params.slug)
  blog.value.content().then(t => blog.value.html = marked(t.default))
})

</script>

<style scoped></style>