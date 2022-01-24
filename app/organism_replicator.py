from tracemalloc import start


class OrganismReplicator:
    
    def get_user_input_for_variables(self):
        number_of_days = input('Number of days to run simulation: ')
        rate_of_replication = input('What is the rate of replication?: ')
        starting_organisms = input('How many organisms to start with: ')
        return {'number_of_days': number_of_days, 'rate_of_replication': rate_of_replication, 'starting_organisms': starting_organisms}

    def validate_user_input_variables(self, user_input_variables):
        number_of_days = user_input_variables.get('number_of_days')
        rate_of_replication = user_input_variables.get('rate_of_replication')
        starting_organsisms = user_input_variables.get('starting_organisms')

        if not number_of_days.isnumeric():
            print('Wrong input entered for Number of Days, please enter a whole number: ')
            return False

        if not rate_of_replication.isnumeric():
            print('Wrong input entered for Rate of Replication, please enter a whole number: ')
            return False
        
        if not starting_organsisms.isnumeric():
            print('Wrong input entered for Starting Organisms, please enter a whole number: ')
            return False
        return True

        

