### Crawl_video_down_ts

### ts web data video down

1. ts, jpeg 등 통신으로 주고 받는 비디오 파일 다운받기
2. F12 -> Network -> record -> filter -> ts or jpeg.. etc.. -> URL copy
3. URL insert (37 line) : {i}.(file extension)
4. 다운 받아지는 확장자 변경 (38 line)
5. 실행

#### 추가사항
- 다운로드가 다끝나면 cmd command 까지 실행됨
- time.sleep 을 넣은 이유는 너무 잦은 통신으로 연결이 끊기기 때문에 설정
