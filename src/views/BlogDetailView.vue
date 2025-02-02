<template>
  <main class="sm:py-2 flex items-center">
    <div
        class="mx-auto w-full max-w-screen-lg bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm flex flex-col gap-4">
      <div class="flex items-center gap-4 border-b pb-2 text-muted-foreground print:hidden">
        <router-link to="/blog">
          <ArrowLeftIcon class="size-6"/>
        </router-link>
        <h1 class="text-md">
          {{ blog.title }}
        </h1>
        <router-link :to="{name: 'home'}" class="ml-auto">
          <Button variant="outline" class="text-muted-foreground" size="sm">
            <HomeIcon class="size-4"/>
            <span class="hidden md:block">Home</span>
          </Button>
        </router-link>
      </div>
      <div v-if="blog.html"
           v-html="blog.html"
           class="prose prose-sm prose-code:text-xs prose-img:rounded min-w-full"></div>
      <div v-else
           class="flex items-center justify-center h-32 text-muted-foreground animate-pulse">
        Loading...
      </div>
      <p class="text-muted-foreground text-xs text-end mt-2 italic">
        Published on {{ blog.date }}
      </p>
    </div>
  </main>
</template>

<script setup>
import {ArrowLeftIcon, HomeIcon} from "@radix-icons/vue";
import {onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";
import {marked} from "marked";
import Prism from "prismjs";
import {blogFiles} from "@/data";
import {Button} from "@/components/ui/button";

import 'prismjs/themes/prism-okaidia.css';
import 'prismjs/components/prism-python.min.js';
import 'prismjs/components/prism-bash.min.js';
import 'prismjs/components/prism-javascript.min.js';
import 'prismjs/components/prism-json.min.js';
import 'prismjs/components/prism-yaml.min.js';
import 'prismjs/components/prism-markup.min.js';

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
  blog.value.content().then(t => {
    const content = t.default
    const renderer = new marked.Renderer()
    renderer.code = ({text, lang}) => {
      const validLanguage = Prism.languages[lang] ? lang : 'plaintext';
      const highlighted = Prism.highlight(text, Prism.languages[validLanguage], validLanguage);
      return `<pre><code class="language-${lang}">${highlighted}</code></pre>`;
    };
    blog.value.html = marked(content, {renderer})
  })
})

</script>

<style scoped></style>