def get_fuels(collection, country):
   """
   Accumulate capacities for each fuel type for a given country
   """
   result = collection.aggregate([
      {
         # Search country
         '$search': {
            'index': 'default',
            'text': {
               'query': country,
               'path': 'country_long'
            }
         }
      },
      {
         # Accumulate capacity by fuel type
         '$group':
         {
            '_id': '$primary_fuel',
            'totCapacity': {
               '$sum': {'$toDecimal': '$capacity_mw'}
            }
         }
      }
   ])
   return result


def top_five_byfuel(collection, fuel):
   """
   Find the top five countries by fuel type capacity
   """
   result = collection.aggregate([
      {
         '$match': {
            'primary_fuel': fuel
         }
      },
      {
         # Accumulate capacity by fuel type
         '$group':
         {
            '_id': '$country_long',
            'totCapacity': {
               '$sum': {'$toDecimal': '$capacity_mw'}
            }
         }
      },
      {
         '$sort': {'totCapacity': -1}
      },
      {
         '$limit': 5
      }
   ])
   return result