# MongoDB

database control

```sh
# switch to my_db
use my_db

# show all databses
show databases
```

collection control

```javascript
// drop a collection
db.users.drop()
```

docuemnt control

```javascript
//  insert a document
db.users.insertOne({name: "foo"})

// insert many documents
db.users.insertMany([
    {name: "foo"},
    {name: "bar"}
])

// find all document
db.users.find()
// find one document
db.users.findOne()
// or
db.users.find().limit(1)

// sort asc by level
db.users.find().sort({level: 1})
// sort desc by level
db.users.find().sort({level: -1})

// skip the first 1 record
db.users.find().skip(1)

// query users who meet certain criteria
// user with name 'foo'
db.users.find({name: "foo"})
// regex search, and ignore case
db.users.find({name: {$regex: /\w{0,2}/, $options: 'i'}})
// get adult user
db.users.find({age: {$gt: 18}})
// get chinese-speaking user
db.users.find({country: {$in: ['china', 'taiwan']}})
// get non-korean user
db.users.find({country: {$nin: ['korea']}})
// or
db.users.find({country: {$not: {$in: ['korea']}}})
// get user with email field
// all users with the "email" field will be retrieved, even if that field is null.
db.users.find({email: {$exists: true}})

// return only wanted field
db.users.find({name: "foo"}, {_id: 0, name: 1})

// or logic
// retrive young or old people
db.users.find({$or: [{age: {$gte: 70}}, {age: {$lte: 10}}]})
```

aggregation

```javascript
db.users.countDocuments()
```

update document

```javascript
// update one record
db.users.updateOne({name: "foo"}, {$set: {name: "bar"}})
// update many records
db.users.updateMany({name: "foo"}, {$set: {name: "bar"}})
```

delete document

```javascript
// delete one document
db.users.deleteOne({name: "foo"})
// delete many documents
db.users.deleteMany({name: "foo"})
```
