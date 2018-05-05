# YAPP_Cosy


1. npm install 하시고

2. config/config.js 파일에 있는 환경설정 맞춰주기 위해 각자 로컬 몽고디비에 

	1) use cosy_db 로 cosy_db 만들어주고
	2) db.createCollection('users') 로 컬렉션 생성해줍니다


	(제가 만들어 놓은 db 스키마는 database/user_schema.js 에 있습니당)

3. 접속 포트는 44444 입니다
	(127.0.0.1:44444 로 접속)

* 패스포트 라우팅 함수들은 routes/user_passport.js 에 있습니다
