// use mongodbtest;
db.createCollection('user' ,{capped:false});

// 넣는데로 다 들어가네
db.users.insertOne({name:"Alice", age:30, address:"123 Maple St"});
db.users.insertOne({name:"Alice", age:30, address:["123 Maple St","124 Maple St","125 Maple St"]});
db.users.insertOne({name:"Alice", age:30, address2:["123 Maple St","124 Maple St","125 Maple St"]});

// 여러개 추가
db.users.insertMany([
{name:"Bob", age:25, address:"456 Oak St"},
{name:"Charlie", age:35, address:"789 Pine St"}
]);
db.users.insertMany([
{name:"Bob", age:25, address:"456 Oak St"},
{name:"Charlie", age:35, city:"California"}
]);

// 컬렉션내 모든 문서 조회
db.users.find();

// 특정 필드 조회
db.users.find({},{name:1, address:1});
// 이렇게 하면 특정 필드에 값을 대입해서 보여줌
db.users.find({},{age:1, address:"oak12344"});

// 조건에 맞는 문서 조회
// 정확히 일치하는 값을 찾아줌
db.users.find({address:"123 Maple St"});
// 안찾아짐
db.users.find({address:"Maple"});

// 하나의 필드만 변경
db.users.updateOne({name:'Alice'},{$set:{age:31}});

// 검색된 모든 필드 변경
db.users.updateMany({name:'Alice'},{$set:{age:31}});

// 하나의 필드 삭제
db.users.deleteOne({name:'Alice'});
// 여러 필드 삭제
db.users.deleteMany({name:'Bob'});
