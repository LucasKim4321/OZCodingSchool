
db.createCollection("sports",{capped:false});

db.sports.insertOne({name:"Football", players: 11});

db.sports.find();

// products컬렉션의 price가 500보다 작거나 같은 문서
db.products.find({price:{$lte:500}});

// books컬렉션의 author가 John Doe인 문서
db.books.find({author:'John Doe'});

// orders컬렉션에서 status가 'pending'인 모든 문서를 'complete'로 변경하세요.
db.orders.updateMany({status:'pending'},{$set: {status:"complete"}});

// movies컬렉션에서 genre가 'comedy'인 모든 문서의 rating을 5로 변경
db.movies.updateMany({genre:"comedy"},{$set:{rating:5}});

// customers 컬렉션에서 age가 30미만인 모든 문서를 삭제
db.customers.deleteMany({age:{$lt:30}});

db.myCollection.insertOne({name:"Gadget",type:"Electronics", price: 300, rating: [4,5,5]});
db.myCollection.find();

db.stats();

db.employees.find({department:'Sales', age: {$gte: 30}});

db.employees.find({salary:{$gte:50000}}, {name:1, title:1});

db.products.insertMany({stock:{$exists:false}},{$set:{stock:10}});

db.vehicles.updateMany({type:'car'},{$set:{wheels:4}});

db.orders.deleteMany({orderDate:{$lt: new Date('2023-01-01')}});

db.restaurants.deleteMany({rating:{$lt:3}});

db.customers.find({age:{$gte:30}}.sort({name:1}));

db.users.aggregate([{ $match: { birthdate: { $lt: new Date('1990-01-01') } } }, { $group: { _id: null, avgAge: { $avg: "$age" } } }]);

db.employees.updateMany({department:"HR"},{$set:{department:"HumanResources", title: "HR Manager"}});

db.orders.insertMany({delivered:false},{$set:{deliveryDate: new Date()}});

// 30일이 지나야하니까 
db.products.deleteMnay({lastModified: {$lt: new Date(new Date() - 30 * 24 * 60 * 60 *1000)}});

