# cosy_project_chatbot
## 문장 감성 분석 후 랜덤으로 문장(답변) 추출 
<li> goodSentence.csv </li>
  사용자가 입력한 문장이 0 과 1.0 사이일 때의 답변 : 기분 좋은 답변 
<li> sadSentence.csv </li>
  사용자가 입력한 문장이 -1.0 과 0 사이일 때의 답변 : 위로하는 답변 
<li> sentiment_analysis.py </li>
  사용자 문장 감성분석 및 답변을 불러오는 코드가 들어있는 파일
<li> sentText.txt </li>
  사용자 문장을 입력하는 텍스트파일 : 실제 프로젝트에선 이 파일을 사용하지 않음
  

## 결과 보는 방법 
1. sentText.txt에 사용자 문장을 입력한다.
2. cmd 창 또는 Anaconda Prompt에서 
`set GOOGLE_APPLICATION_CREDENTIALS=Goole_Cloud_Platform에서 받은 json파일 실행경로`를 입력한다.  
ex ) set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\happy\Desktop\Goole_Cloud_Platform\My First Project-01e4a5c0f738.json


3. `python sentiment_analysis.py sentText.txt` 명령어를 실행한다



## 결과화면
![image01](https://user-images.githubusercontent.com/29648470/39761815-05920efe-5314-11e8-9efe-a00d3df2ce0f.png)
* 명령어를 실행할 때마다 문장 감성 점수에 맞는 다른 답변이 선택되어 출력된다


### 더 자세한 사용방법은 아래를 참고

1. 문장 감성 분석 및 랜덤 문장 추출 사용법<p> 
http://www.evernote.com/l/Abd8JcZAlsdGha_cB9GkjWm-DgiDEYT2nAk/ <p>
2. Google Sentiment API 사용하기 - json파일 <p>
http://www.evernote.com/l/AbeNk97xzNhGZ5iTi1RV5WLRh_gdqS1P54M/ <p>
