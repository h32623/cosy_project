/*
 * 설정 파일
 *
 * @date 2016-11-10
 * @author Mike
 */

module.exports = {
	server_port: 44444,
	db_url: 'mongodb://localhost:27017/cosy_db',
	db_schemas: [
	    {file:'./user_schema', collection:'users', schemaName:'UserSchema', modelName:'UserModel'}
	],
    // 라우터 모듈들 여기다가 저장함
	route_info: [
	]
};
