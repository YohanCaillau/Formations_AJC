db.restaurants.update(
{"_id": ObjectId("6311d6b18971d17948b27d28")},
{$unset : {"commentaire":"1"}});

db.restaurants.find({
    "commentaire" : "NouveauCommentaire"});