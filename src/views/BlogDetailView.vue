<template>
  <main class="sm:py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2 text-muted-foreground">
        <router-link to="/blog">
          <ArrowLeftIcon class="size-6"/>
        </router-link>
        <h1 class="text-md">
          {{ blog.title }}
        </h1>
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
import {useRoute, useRouter} from "vue-router";
import {marked} from "marked";
import {blogFiles} from "@/data";

const route = useRoute()
const router = useRouter()
const blog = ref({})

onMounted(() => {
  const found = blogFiles.find(b => b.slug === route.params.slug)
  if (!found) {
    router.push({name: 'not-found'})
    return
  }
  blog.value = found
  blog.value.content().then(t => blog.value.html = marked(t.default))
})

</script>

<style scoped></style>