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
      <div class="flex flex-col md:flex-row gap-2 items-center justify-between">
        <span class="text-muted-foreground">
          These are some of the blog posts I have written.
        </span>
        <div class="relative w-full max-w-sm items-center">
          <Input
              v-model="searchQuery"
              id="search"
              type="search"
              placeholder="Type / to search"
              class="pl-10 h-8"
          />
          <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
            <MagnifyingGlassIcon class="size-5 text-muted-foreground"/>
          </span>
        </div>
      </div>
      <ul class="space-y-3 pt-2">
        <li v-for="(blog, index) in filteredBlogFiles" :key="index">
          <div class="flex flex-col mb-4">
            <span class="text-muted-foreground text-xs">
              {{ blog.date }}
            </span>
            <router-link :to="{name: 'blog-detail', params: {slug: blog.slug}}">
              <span class="hover:underline hover:underline-offset-4">{{ blog.title }}</span>
            </router-link>
          </div>
        </li>
        <li v-if="filteredBlogFiles.length === 0">
          <div class="p-4 rounded-sm text-muted-foreground text-center">
            No blog post found.
          </div>
        </li>
      </ul>
    </div>
  </main>
</template>

<script setup>
import {computed, onMounted, onUnmounted, ref} from "vue";
import {ArrowLeftIcon, HomeIcon, MagnifyingGlassIcon} from "@radix-icons/vue";
import {blogFiles} from "@/data";
import {Button} from "@/components/ui/button";
import {Input} from "@/components/ui/input";

const searchQuery = ref('');
const filteredBlogFiles = computed(() => {
  return blogFiles.filter(blog => {
    return blog.title.toLowerCase().includes(searchQuery.value.toLowerCase());
  });
});


const handleSearch = (event) => {
  if (event.key === '/') {
    event.preventDefault();
    document.getElementById('search')?.focus();
  }
};

onMounted(() => {
  window.addEventListener('keydown', handleSearch);
});


onUnmounted(() => {
  window.removeEventListener('keydown', handleSearch);
});

</script>

<style scoped></style>