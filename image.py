import sqlite3

# SQLite DB 연결
conn = sqlite3.connect('mydatabase.db')

# 커서 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS Images
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  image BLOB NOT NULL)''')

# 이미지 데이터를 DB에 삽입
def insert_image(name, image_data):
    cursor.execute("INSERT INTO Images (name, image) VALUES (?, ?)", (name, image_data))
    conn.commit()
    print("이미지가 성공적으로 삽입되었습니다.")

# 모든 이미지 데이터를 DB에서 조회
def fetch_all_images():
    cursor.execute("SELECT * FROM Images")
    rows = cursor.fetchall()
    images_html = ''
    for row in rows:
        image_id, name, image_data = row
        # 이미지 데이터 처리 작업을 수행 (예: 저장, 표시 등)
        image_html = f'<img src="data:image/jpeg;base64,{image_data}" alt="{name}" /><br>'
        images_html += image_html
    return images_html

# 예시: 이미지 데이터 삽입
with open('청소기.jpg', 'rb') as file:
    image_data = file.read()
    insert_image('Image 1', image_data)

# 예시: 모든 이미지 데이터 조회 및 HTML 코드 생성
html = fetch_all_images()

# 연결 종료
conn.close()

# 생성된 HTML 코드 출력
print(html)
