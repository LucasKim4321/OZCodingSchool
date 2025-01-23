// 한줄 주석
// db.getCollection("system.version").find({});
/*
여러줄
주석
*/

// DB전환 (없으면 새로 만들어서 전환)
use testmongodb;
// 현재 활성화 된 DB 확
db;
// 현재 생성된 DB 목록 (컬렉션을 만들기 전까진 실제로 생성되지 않은 상태)
show dbs;
// 활성화 된 db 정보
db.stats();
// 컬렉션 만들기 (생성 후 실제로 DB도 같이 생
db.createCollection("users",{capped:false});
// 이미 생성된 컬렉션 이름 수정
db.users.renameCollection("customers");
// 컬렉션 지우기
db.customers.drop();
// DB 지우기
db.dropDatabase();

/*

## 1. 쿼리 복사 및 저장
IntelliShell 자체에는 쿼리를 파일로 저장하는 기능이 없습니다. 대신 작성한 쿼리를 복사하여 외부 파일로 저장해야 합니다:

IntelliShell에서 작성한 쿼리를 선택하고 복사합니다.
쿼리를 저장할 텍스트 편집기(예: VS Code, Notepad++, Sublime Text 등)를 엽니다.
파일에 저장:
파일 이름을 지정할 때 확장자를 .js로 저장하면 JavaScript 쿼리로 관리하기 쉽습니다.
예: myQuery.js

## 2. 몽고 쉘(Mongo Shell) 또는 IntelliShell에서 실행
저장한 .js 파일을 다시 실행하려면 Mongo Shell이나 IntelliShell에서 다음 방법을 사용합니다:

IntelliShell에서 스크립트 실행
파일 로드: IntelliShell에서 load() 명령을 사용하여 저장된 JavaScript 파일을 실행합니다:

javascript
복사
편집
load('/path/to/myQuery.js')
경로 설정: 파일 경로는 절대 경로 또는 IntelliShell가 실행 중인 현재 디렉토리에 상대적인 경로를 지정합니다.

## 3. MongoDB Compass에서 IntelliShell 대신 스크립트 관리
MongoDB Compass 자체에는 쿼리를 저장하는 기능이 없으므로 IntelliShell에서 스크립트를 효율적으로 관리하려면 별도의 디렉토리를 만들어 자주 사용하는 스크립트를 저장하고 관리하는 것이 좋습니다.

예:

디렉토리 이름: mongo-scripts
파일 이름: aggregateQuery.js, findQuery.js 등.



javascript 친환경적

MongoDB는 JavaScript를 기반으로 동작한다고 볼 수 있습니다. MongoDB의 쿼리 언어와 스크립트 실행 환경은 JavaScript에 기반을 두고 설계되었습니다.
이 점이 MongoDB의 유연성과 개발자 친화적인 경험을 제공하는 주요 이유 중 하나입니다.
MongoDB와 JavaScript의 연관성


1. Mongo Shell

MongoDB는 기본적으로 Mongo Shell이라는 대화형 JavaScript 실행 환경을 제공합니다.
Mongo Shell에서 JavaScript 구문을 사용하여 데이터베이스 작업을 수행할 수 있습니다.

예:
javascript
복사
편집
db.collection.find({ age: { $gt: 25 } }).forEach(doc => {
    print(doc.name);
});


2. JavaScript 기반 쿼리 문법

MongoDB의 쿼리 문법은 JSON 포맷에 기반하며, 이는 JavaScript Object Notation의 약자입니다.
쿼리는 사실상 JavaScript 객체로 표현되며, JavaScript의 메서드와 함수가 MongoDB와 긴밀히 통합되어 있습니다.


3. Node.js 및 JavaScript 클라이언트

MongoDB는 JavaScript로 작성된 서버 환경인 Node.js와 함께 사용되며, 이를 위해 mongodb와 같은 공식 Node.js 클라이언트를 제공합니다.
Node.js 환경에서 MongoDB와 상호작용할 때도 JavaScript를 사용합니다. 

예:
const { MongoClient } = require('mongodb');
const uri = "mongodb+srv://username:password@cluster.mongodb.net";
const client = new MongoClient(uri);

async function run() {
    try {
        await client.connect();
        const db = client.db("testDB");
        const result = await db.collection("users").findOne({ name: "Alice" });
        console.log(result);
    } finally {
        await client.close();
    }
}
run().catch(console.dir);


4. JavaScript 지원 확장

MongoDB의 서버 측 JavaScript 기능을 활용해 데이터 처리 로직을 작성할 수도 있습니다.

예: mapReduce 함수나 데이터베이스 커맨드에서 JavaScript를 사용할 수 있습니다.
db.collection.mapReduce(
    function () { emit(this.category, 1); },
    function (key, values) { return Array.sum(values); },
    { out: "category_totals" }
);

주의점
MongoDB 서버 자체가 JavaScript로 작성된 것은 아닙니다. MongoDB는 **C++**로 작성된 데이터베이스 엔진을 사용하며,
JavaScript는 주로 클라이언트와 상호작용하거나 특정 서버 작업에 사용됩니다.

*/