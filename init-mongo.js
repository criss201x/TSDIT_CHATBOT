db.createUser(
    {
        user: "chatbotadmin",
        pwd: "123456",
        roles: [
            {
                role: "readWrite",
                db: "chatbot"
            }
        ]
    }
);
db.createCollection("conversaciones"); //MongoDB creates the database when you first store data in that database
