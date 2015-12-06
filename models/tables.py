from datetime import datetime

db.define_table('pets',
                Field("name", requires = IS_NOT_EMPTY),
                Field("author", db.auth_user, default = auth.user_id),
                Field("description", "text", requires = IS_NOT_EMPTY),
                Field("posted", 'datetime'),
                Field("pet_image", 'upload', default = 'path/'),
                Field("Cat_or_Dog", requires=IS_IN_SET(['Cat', 'Dog'])),
                Field("gender", requires=IS_IN_SET(['Male', 'Female'])),
                Field("house_trained", 'boolean', default = False),
                Field("kid_friendly", 'boolean', default = False),
                Field("pet_friendly", 'boolean', default = False),
                Field("outdoor_pet", 'boolean', default = False),
                Field("indoor_pet", 'boolean', default = False),
                Field("frequent_exercise", 'boolean', default = False),
                Field("infrequent_exercise", 'boolean', default = False),
                Field("young_pet", 'boolean', default = False),
                Field("older_pet", 'boolean', default = False)
                )

db.pets.posted.readable = db.pets.posted.writable = False
db.pets.posted.default = datetime.utcnow()

#stream = open(filename, 'rb')
#db.pets.insert(image=db.pets.pet_image.store(stream, filename))