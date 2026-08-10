const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, '..', 'src', 'assets');
const DEST = path.join(__dirname, '..', 'public', 'assets');

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else if (entry.isFile()) {
      fs.copyFileSync(srcPath, destPath);
      console.log('copied', srcPath, '->', destPath);
    }
  }
}

try {
  copyRecursive(SRC, DEST);
  console.log('Assets sync complete');
} catch (err) {
  console.error('Assets sync failed:', err);
  process.exit(1);
}
