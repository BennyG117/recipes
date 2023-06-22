from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    # use schema name (my db)
    DB = 'recipes_db'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30_minutes = data['under_30_minutes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']



    #Classmethod to save a submitted new Recipe by adding it to our DB
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, date_cooked, under_30_minutes, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30_minutes)s, %(user_id)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    



    #classmethod to get all recipes from a specific user
    @classmethod
    def get_user_recipes(cls, data):
        query = """
        SELECT *
        FROM recipes
        WHERE user_id = %(id)s;
        """

        result = connectToMySQL(cls.DB).query_db(query, data)

        user_recipes = []

        for recipe in result:
            user_recipes.append( cls(recipe))
        return user_recipes


    #classmethod to get all recipes from all users
    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT * 
        FROM recipes;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        # use to check if working...
        print(results)

        all_recipes = []

        for recipe in results:
            all_recipes.append( cls(recipe))
        return all_recipes


    #classmethod to get one recipe
    @classmethod
    def get_one_recipe(cls, data):
        query="""SELECT * 
        FROM recipes
        WHERE id = %(id)s;        
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        singleRecipe = cls(results[0])

        return singleRecipe