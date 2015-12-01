from datetime import datetime

db.define_table(pets,
                Field("name", requires = IS_NOT_EMPTY),
                Field("author", db.auth_user, default = auth.user_id),
                Field("description", "text"),
                Field("posted", datetime),
                Field("house-trained", default = false),
                Field("kid-friendly", default = false),
                Field("pet-friendly", default = false),
                Field("outdoor-pet", default = false),
                Field("indoor-pet", default = false),
                Field("frequent-exercise", default = false),
                Field("infrequent-exercise", default = false),
                Field("young-pet", default = false),
                Field("older-pet", default = false)
                )

db.pets.posted.readable = db.pets.posted.writable = False
db.pets.posted.default = datetime.utcnow()