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
  	const IMAGES_DIR = path.join(DEST, 'images');
  	if (!fs.existsSync(IMAGES_DIR)) 
		fs.mkdirSync(IMAGES_DIR, { recursive: true });

  	const SRC_IMAGES_DIR = path.join(SRC, 'images');
  	if (!fs.existsSync(SRC_IMAGES_DIR)) 
		fs.mkdirSync(SRC_IMAGES_DIR, { recursive: true });
	// Ensure source root has secplus images so Astro content imports can resolve '/assets/secplus_*.png'
	const srcRootLight = path.join(SRC, 'secplus_light.png');
	const srcRootDark = path.join(SRC, 'secplus_dark.png');
	const srcImageLight = path.join(SRC_IMAGES_DIR, 'secplus_light.png');
	const srcImageDark = path.join(SRC_IMAGES_DIR, 'secplus_dark.png');
	if (fs.existsSync(srcImageLight) && !fs.existsSync(srcRootLight)) {
		fs.copyFileSync(srcImageLight, srcRootLight);
		console.log('copied', srcImageLight, '->', srcRootLight);
	}
	if (fs.existsSync(srcImageDark) && !fs.existsSync(srcRootDark)) {
		fs.copyFileSync(srcImageDark, srcRootDark);
		console.log('copied', srcImageDark, '->', srcRootDark);
	}
  
	const pubLight = path.join(IMAGES_DIR, 'secplus_light.png');
  	const pubDark = path.join(IMAGES_DIR, 'secplus_dark.png');
  	const srcLight = path.join(SRC_IMAGES_DIR, 'secplus_light.png');
  	const srcDark = path.join(SRC_IMAGES_DIR, 'secplus_dark.png');
  	if (fs.existsSync(pubLight) && !fs.existsSync(srcLight)) {
    	fs.copyFileSync(pubLight, srcLight);
    	console.log('copied', pubLight, '->', srcLight);
  	}
  	if (fs.existsSync(pubDark) && !fs.existsSync(srcDark)) {
    	fs.copyFileSync(pubDark, srcDark);
    	console.log('copied', pubDark, '->', srcDark);
  	}
	// Mirror images into public/assets root so /assets/secplus_*.png are available
	const pubRootLight = path.join(DEST, 'secplus_light.png');
	const pubRootDark = path.join(DEST, 'secplus_dark.png');
	if (fs.existsSync(pubLight) && !fs.existsSync(pubRootLight)) {
		fs.copyFileSync(pubLight, pubRootLight);
		console.log('copied', pubLight, '->', pubRootLight);
	}
	if (fs.existsSync(pubDark) && !fs.existsSync(pubRootDark)) {
		fs.copyFileSync(pubDark, pubRootDark);
		console.log('copied', pubDark, '->', pubRootDark);
	}
  	console.log('Assets sync complete');
} catch (err) {
  	console.error('Assets sync failed:', err);
  	process.exit(1);
}
