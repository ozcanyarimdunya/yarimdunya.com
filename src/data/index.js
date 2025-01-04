import {GithubLogoIcon, LinkedinLogoIcon} from "@radix-icons/vue";

export const resumeData = {
  name: "Özcan Yarımdünya",
  about: "Simple Python Developer",
  avatarUrl: "https://avatars.githubusercontent.com/u/12237463?v=4",
  location: {
    city: "İstanbul",
    country: "Türkiye",
    link: "https://www.google.com/maps/place/Istanbul",
  },
  company: {
    name: "Sahibinden.com",
    link: "https://sahibinden.com",
  },
  contact: {
    email: "ozcanyd@gmail.com",
    tel: "+905310821028",
    social: [
      {
        name: "GitHub",
        url: "https://github.com/ozcanyarimdunya",
        icon: GithubLogoIcon,
      },
      {
        name: "LinkedIn",
        url: "https://www.linkedin.com/in/ozcanyarimdunya/",
        icon: LinkedinLogoIcon,
      },
    ],
  },
  resumeLink: "https://ozcan.yarimdunya.com",
};

const blogs = import.meta.glob("@/data/blog-files/*.md", {query: "raw"});

export const blogFiles = Object.entries(blogs).map(([path, content]) => {
  const [, number, slug, date] = path.match(/(\d+)_(.*)_(\d{4}-\d{2}-\d{2})\.md$/)
  return {
    title: slug.replace(/-/g, ' '),
    date: date,
    slug: `${number}_${slug}_${date}`,
    content: content,
  }
});
