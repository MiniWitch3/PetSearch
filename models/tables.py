from datetime import datetime

db.define_table('pets',
                Field("name", requires = IS_NOT_EMPTY),
                Field("author", db.auth_user, default = auth.user_id),
                Field("description", "text", requires = IS_NOT_EMPTY),
                Field("posted", 'datetime'),
                Field("pet_image", 'upload', default = 'path/'),
                Field("house_trained", default = False),
                Field("kid_friendly", default = False),
                Field("pet_friendly", default = False),
                Field("outdoor_pet", default = False),
                Field("indoor_pet", default = False),
                Field("frequent_exercise", default = False),
                Field("infrequent_exercise", default = False),
                Field("young_pet", default = False),
                Field("older_pet", default = False)
                )

db.pets.posted.readable = db.pets.posted.writable = False
db.pets.posted.default = datetime.utcnow()

#stream = open(filename, 'rb')
#db.pets.insert(image=db.pets.pet_image.store(stream, filename))