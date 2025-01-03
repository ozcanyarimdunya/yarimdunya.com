const blogs = import.meta.glob("./*.md", {query: "raw"});

const blogFiles = Object.entries(blogs).map(([path, content]) => {
  const [, number, slug, date] = path.match(/(\d+)_(.*)_(\d{2}-\d{2}-\d{4})\.md$/)
  return {
    title: slug.replace(/-/g, ' '),
    date: new Date(date).toDateString(),
    slug: `${number}_${slug}_${date}`,
    content: content,
  }
});

export default blogFiles;