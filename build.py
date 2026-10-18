# يبني index.html (نسخة GitHub Pages القابلة للتثبيت) من app.html (مصدر الـ Artifact)
s = open('app.html', encoding='utf-8').read()
head, rest = s.split('<style>', 1)
style, body = rest.split('</style>', 1)
pwa_head = '''<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#0f766e">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="بوصلة">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
'''
pwa_body = '''<script>
  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
    window.addEventListener('load', () => navigator.serviceWorker.register('sw.js'));
  }
</script>
'''
full = ('<!DOCTYPE html>\n<html lang="ar" dir="rtl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head.strip() + '\n' + pwa_head + '<style>' + style + '</style>\n</head>\n<body>\n'
        + body.strip() + '\n' + pwa_body + '</body>\n</html>\n')
open('index.html', 'w', encoding='utf-8').write(full)
