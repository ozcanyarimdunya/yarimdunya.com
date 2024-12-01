<template>
  <main class="px-4 sm:px-0 flex items-center h-[80vh]">
    <div class="mx-auto w-full max-w-xl bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm">
      <!-- Header -->
      <div class="flex items-center justify-between">
        <div class="flex-1 space-y-1.5">
          <h1 class="text-2xl font-bold">{{ data.name }}</h1>
          <p class="max-w-md text-pretty font-mono text-sm text-muted-foreground print:text-[12px]">
            {{ data.about }}
          </p>
          <p class="max-w-md items-center text-pretty font-mono text-xs text-muted-foreground">
            <a
                class="inline-flex gap-x-1.5 align-baseline leading-none hover:underline"
                :href="data.company.link"
                target="_blank"
            >
              <BackpackIcon class="size-3"/>
              {{ data.company.name }}
            </a>
          </p>
          <p class="max-w-md items-center text-pretty font-mono text-xs text-muted-foreground">
            <a
                class="inline-flex gap-x-1.5 align-baseline leading-none hover:underline"
                :href="data.location.link"
                target="_blank"
            >
              <GlobeIcon class="size-3"/>
              {{ data.location.city }} / {{ data.location.country }}
            </a>
          </p>
          <div class="flex gap-x-1 pt-1 font-mono text-sm text-muted-foreground ">
            <Button
                class="size-8"
                variant="outline"
                size="icon"
                asChild
                v-if="data.contact.email"
            >
              <a :href="`mailto:${data.contact.email}`">
                <EnvelopeClosedIcon class="size-4"/>
              </a>
            </Button>
            <Button
                class="size-8"
                variant="outline"
                size="icon"
                asChild
                v-for="social in data.contact.social"
                :key="social.name"
            >
              <a :href="social.url">
                <component :is="social.icon" class="size-4"/>
              </a>
            </Button>
            <a :href="data.resumeLink" target="_blank">
              <Button variant="outline" class="text-muted-foreground px-3" size="sm">
                Resume
                <ExternalLinkIcon class="size-4"/>
              </Button>
            </a>
          </div>
        </div>
        <Avatar class="size-24 sm:size-36 rounded-xl">
          <AvatarImage :alt="data.name" :src="data.avatarUrl"/>
          <AvatarFallback>{{ data.name }}</AvatarFallback>
        </Avatar>
      </div>
    </div>
  </main>
</template>

<script setup>
import {onBeforeMount} from "vue";
import {BackpackIcon, EnvelopeClosedIcon, ExternalLinkIcon, GlobeIcon} from "@radix-icons/vue";
import {Button} from "@/components/ui/button";
import {Avatar, AvatarFallback, AvatarImage} from "@/components/ui/avatar";
import data from '@/data'

onBeforeMount(() => document.title = data.name);
</script>

