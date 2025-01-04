<template>
  <main class="sm:py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2 text-muted-foreground">
        <router-link :to="{name: 'home'}">
          <ArrowLeftIcon class="size-6"/>
        </router-link>
        <h1 class="text-md">
          Blog Posts
        </h1>
        <router-link :to="{name: 'home'}" class="ml-auto">
          <Button variant="outline" class="text-muted-foreground" size="sm">
            <HomeIcon class="size-4"/>
            <span class="hidden md:block">Home</span>
          </Button>
        </router-link>
      </div>
      <span class="text-muted-foreground">
        These are some of the blog posts I have written.
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
import {ArrowLeftIcon, HomeIcon} from "@radix-icons/vue";
import {blogFiles} from "@/data";
import {Button} from "@/components/ui/button";
</script>

<style scoped></style>