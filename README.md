# OCR
학생증인식

https://drive.google.com/file/d/1VPKzY06xnAi3Q15FNPqcqzsovA1Jjrf_/view?usp=sharin

1. 링크가서 pth파일(craft) 다운
2. 깃클론하고
3. OCR/OCR에 pth 넣고
4. 테서렉트 korean추가해서 다운해서 OCR/OCR에 넣고
5. image, image_localized, image_result 디렉토리를 만든다(빈 디렉토리는 깃헙에 안올라가나봅니다)
6. image 폴더에 인식할 학생증 사진 넣고
7. OCR.py 실행
8. 실행하면 image_result를 거쳐 image_localized에 recognition할 이미지들이 생기고
9. result.txt에 recognition한 결과나와있음
10. result.txt를 읽어서 필요한 데이터만 추출하여 info.txt에 저장

OCR.py -> test.py -> localize -> tesseract.py -> extraction.py

모든 작업은 OCR/OCR디렉토리 상에서 하면 됨

모델 개선해야함.
