<template>
  <main class="px-4 sm:px-0 flex items-center h-[80vh]">
    <div class="mx-auto w-full max-w-xl bg-white print:space-y-4 border p-4 sm:p-6 rounded shadow-sm">
      <!-- Header -->
      <div class="flex items-center justify-between">
        <div class="flex-1 space-y-1.5">
          <h1 class="text-2xl font-bold">{{ resumeData.name }}</h1>
          <p class="max-w-md text-pretty font-mono text-sm text-muted-foreground print:text-[12px]">
            {{ resumeData.about }}
          </p>
          <p class="max-w-md items-center text-pretty font-mono text-xs text-muted-foreground">
            <a
                class="inline-flex gap-x-1.5 align-baseline leading-none hover:underline"
                :href="resumeData.company.link"
                target="_blank"
            >
              <BackpackIcon class="size-3"/>
              {{ resumeData.company.name }}
            </a>
          </p>
          <p class="max-w-md items-center text-pretty font-mono text-xs text-muted-foreground">
            <a
                class="inline-flex gap-x-1.5 align-baseline leading-none hover:underline"
                :href="resumeData.location.link"
                target="_blank"
            >
              <GlobeIcon class="size-3"/>
              {{ resumeData.location.city }} / {{ resumeData.location.country }}
            </a>
          </p>
          <div class="flex gap-x-1 pt-1 font-mono text-sm text-muted-foreground print:hidden">
            <Button
                class="size-8"
                variant="outline"
                size="icon"
                asChild
                v-if="resumeData.contact.email"
            >
              <a :href="`mailto:${resumeData.contact.email}`">
                <EnvelopeClosedIcon class="size-4"/>
              </a>
            </Button>
            <Button
                class="size-8"
                variant="outline"
                size="icon"
                asChild
                v-for="social in resumeData.contact.social"
                :key="social.name"
            >
              <a :href="social.url">
                <component :is="social.icon" class="size-4"/>
              </a>
            </Button>
            <a :href="resumeData.resumeLink" target="_blank">
              <Button variant="outline" class="text-muted-foreground px-2 md:px-3" size="sm">
                <ReaderIcon class="size-4"/>
                <span class="hidden md:block">Resume</span>
              </Button>
            </a>
          </div>
          <div class="hidden print:flex flex-col gap-y-2 text-xs text-muted-foreground">
            <a class="flex items-center gap-2" :href="`mailto:${resumeData.contact.email}`">
              <EnvelopeClosedIcon class="size-3"/>
              {{ resumeData.contact.email }}
            </a>
            <a class="flex items-center gap-2"
               v-for="social in resumeData.contact.social" :key="social.name"
               :href="social.url" target="_blank">
              <component :is="social.icon" class="size-3"/>
              {{ social.url }}
            </a>
            <a class="flex items-center gap-2"
               :href="resumeData.resumeLink" target="_blank">
              <ReaderIcon class="size-3"/>
              {{ resumeData.resumeLink }}
            </a>
          </div>
        </div>
        <Avatar class="size-24 sm:size-36 rounded-xl print:size-48">
          <AvatarImage :alt="resumeData.name" :src="resumeData.avatarUrl"/>
          <AvatarFallback>{{ resumeData.name }}</AvatarFallback>
        </Avatar>
      </div>
    </div>
  </main>
</template>

<script setup>
import {BackpackIcon, EnvelopeClosedIcon, GlobeIcon, ReaderIcon} from "@radix-icons/vue";
import {Button} from "@/components/ui/button";
import {Avatar, AvatarFallback, AvatarImage} from "@/components/ui/avatar";
import {resumeData} from '@/data'
</script>

<style scoped></style>

