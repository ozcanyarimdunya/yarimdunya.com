import fs from 'fs';
import path from 'path';

const blogFilesPath = path.join(process.cwd(), 'src/data/blog-files');
const blogFiles = fs.readdirSync(blogFilesPath);
const nextBlogFileNumber = (blogFiles.length + 1).toString().padStart(3, '0');

const title = process.argv.slice(2).join(' ').replace(/\s/g, '-');
const date = new Date().toISOString().slice(0, 10);
const blogFile = path.join(blogFilesPath, `${nextBlogFileNumber}_${title}_${date}.md`);
fs.writeFileSync(blogFile, '');
console.log(`Created ${blogFile}`);
