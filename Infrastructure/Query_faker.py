from faker import Faker
from Infrastructure.db.Postgres import  PostgressDatabaseConnector
from loguru import logger
class InitDB(PostgressDatabaseConnector):
    @staticmethod
    def initial_connection(self):
        dataBaseQuery = PostgressDatabaseConnector()
        queryDb = dataBaseQuery.cursor()
        table_users = """
         CREATE TABLE IF NOT EXISTS users (
             id Integer NOT NULL AUTO_INCREMENT primary key ,
             name varchar(255) NOT NULL,
             email varchar(255) NOT NULL,
             address varchar(255) NOT NULL
         )
        """
        logger.success("Creating table users")
        queryDb.execute(table_users)
        #valide la transaction
        """
        Generate the faker data for the users
        """
        query_insert = """
        INSERT INTO users (name, email, address)
        VALUES (%s, %s, %s)
        """
        faker = Faker()
        queryDb.execute("SELECT COUNT(*) FROM users")
        counter  = queryDb.fetchone()[0]
        print(counter)
        if counter== 0:
          for _ in range(100):
            queryDb.execute(
               query_insert,
               args=(
                 faker.first_name(),
                 faker.email(),
                 faker.address()
               )
            )
        logger.success("Insertion data")
        dataBaseQuery.commit()
queryDb = InitDB.initial_connection(PostgressDatabaseConnector)



