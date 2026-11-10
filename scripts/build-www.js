const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const wwwDir = path.join(rootDir, 'www');

// Clean and create www
if (fs.existsSync(wwwDir)) {
  fs.rmSync(wwwDir, { recursive: true, force: true });
}
fs.mkdirSync(wwwDir, { recursive: true });

// Copy file helper
function copyFile(src, dest) {
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, dest);
  }
}

// Copy directory recursively helper
function copyDir(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// Copy essential files
copyFile(path.join(rootDir, 'index.html'), path.join(wwwDir, 'index.html'));
copyFile(path.join(rootDir, 'manifest.json'), path.join(wwwDir, 'manifest.json'));
copyFile(path.join(rootDir, '.nojekyll'), path.join(wwwDir, '.nojekyll'));

// Copy assets
copyDir(path.join(rootDir, 'assets'), path.join(wwwDir, 'assets'));

console.log('✓ www directory built successfully for Android Capacitor package');
