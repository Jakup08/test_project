from pathlib import Path

root = Path('sample_files')
root.mkdir(exist_ok=True)
files = [
    'video1.mp4', 'video2.mkv', 'video3.avi', 'video4.mov', 'video5.flv', 'video6.dav',
    'video7.webm', 'video8.m4v', 'video9.wmv', 'video10.3gp', 'video11.m3u8',
    'audio1.mp3', 'audio2.wav', 'audio3.aac', 'audio4.flac', 'audio5.m4a', 'audio6.ogg',
    'audio7.wma', 'audio8.opus', 'audio9.alac', 'audio10.aiff',
    'img1.jpg', 'img2.jpeg', 'img3.png', 'img4.gif', 'img5.bmp', 'img6.webp',
    'img7.tiff', 'img8.heic', 'img9.raw', 'img10.svg', 'img11.ico', 'img12.psd',
    'doc1.pdf', 'doc2.docx', 'doc3.doc', 'doc4.xlsx', 'doc5.xls', 'doc6.pptx',
    'doc7.ppt', 'doc8.txt', 'doc9.odt', 'doc10.rtf', 'doc11.csv', 'doc12.json', 'doc13.xml',
    'arc1.zip', 'arc2.rar', 'arc3.7z', 'arc4.tar', 'arc5.gz', 'arc6.bz2', 'arc7.iso', 'arc8.dmg',
    'code1.py', 'code2.js', 'code3.ts', 'code4.java', 'code5.cpp', 'code6.c', 'code7.h',
    'code8.html', 'code9.css', 'code10.php', 'code11.go', 'code12.rs', 'code13.rb', 'code14.sh'
]
for name in files:
    path = root / name
    if not path.exists():
        path.write_text(f'Test file {name}\n')
print(f'Created {len(files)} test files in {root}')
