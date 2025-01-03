<template>
  <main class="px-4 sm:px-0 py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2">
        <router-link to="/">
          <ArrowLeftIcon class="size-8 text-primary"/>
        </router-link>
        <h1 class="text-2xl font-semibold">
          Blog
        </h1>
      </div>
      <span>
        These are some of the blogs I have written.
      </span>
      <ul class="space-y-3">
        <li v-for="(blog, index) in blogFiles" :key="index">
          <router-link :to="{name: 'blog-detail', params: {slug: blog.slug}}">
            <div
                class="flex items-center justify-between gap-2 p-4 border rounded-sm hover:shadow-md transition duration-300 ease-in-out">
              <span>
                {{ index + 1 }}. {{ blog.title }}
              </span>
              <span class="text-muted-foreground text-sm text-nowrap">
                {{ blog.date }}
              </span>
            </div>
          </router-link>
        </li>
      </ul>
    </div>
  </main>
</template>

<script setup>
import {ArrowLeftIcon} from "@radix-icons/vue";
import blogFiles from "@/data/blog-files";
</script>

<style scoped></style>