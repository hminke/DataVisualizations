import networkx as nx
import matplotlib.pyplot as plt

airportGraph = nx.Graph()
chicagoIl = 'MDW'
austinTx = 'AUS'
baltimoreMd = 'BWI'
charlotteDouglasNc = 'CLT'
clevelandOh = 'CLE'
denverCo = 'DEN'
jacksonvilleFl = 'JAX'
manchesterNh = 'MHT'
memphisTn = 'MEM'
nashvilleTn = 'BNA'
oaklandCa = 'OAK'
orlandoFl = 'MCO'
philadelphiaPa = 'PHL'
sacramentoCa = 'SMF'
saltLakeCityUt = 'SLC'
sanDiegoCa = 'SAN'
tucsonAz = 'TUS'

labels = {'Chicago, IL': 'MDW', 'Austin, TX': 'AUS', 'Baltimore, MD': 'BWI', 'Charlotte-Douglas, NC': 'CLT',
          'Cleveland, OH': 'CLE', 'Denver, CO': 'DEN', 'Jacksonville, FL': 'JAX', 'Manchester, NH': 'MHT',
          'Memphis, TN': 'MEM', 'Nashville, TN': 'BNA', 'Oakland, CA': 'OAK', 'Orlando, FL': 'MCO',
          'Philadelphia, PA': 'PHL', 'Sacramento, CA': 'SMF', 'Salt Lake City, UT': 'SLC', 'San Diego, CA': 'SAN',
          'Tucson, AZ': 'TUS'}

airportGraph.add_edges_from([(chicagoIl, austinTx, {'weight': 11.6}), (chicagoIl, baltimoreMd, {'weight': 7.0}),
                             (chicagoIl, charlotteDouglasNc, {'weight': 7.5}),
                             (chicagoIl, clevelandOh, {'weight': 3.4}),
                             (chicagoIl, denverCo, {'weight': 10.0}), (chicagoIl, jacksonvilleFl, {'weight': 10.6}),
                             (chicagoIl, manchesterNh, {'weight': 10.1}), (chicagoIl, memphisTn, {'weight': 5.3}),
                             (chicagoIl, nashvilleTn, {'weight': 4.7}), (chicagoIl, oaklandCa, {'weight': 21.2}),
                             (chicagoIl, orlandoFl, {'weight': 11.5}), (chicagoIl, philadelphiaPa, {'weight': 7.5}),
                             (chicagoIl, sacramentoCa, {'weight': 20.4}), (chicagoIl, saltLakeCityUt, {'weight': 13.9}),
                             (chicagoIl, sanDiegoCa, {'weight': 20.7}), (chicagoIl, tucsonAz, {'weight': 17.4}),
                             (austinTx, baltimoreMd, {'weight': 15.6}), (austinTx, charlotteDouglasNc, {'weight': 12.0}),
                             (austinTx, clevelandOh, {'weight': 13.7}), (austinTx, denverCo, {'weight': 9.2}),
                             (austinTx, jacksonvilleFl, {'weight': 10.3}), (austinTx, manchesterNh, {'weight': 19.9}),
                             (austinTx, memphisTn, {'weight': 6.4}), (austinTx, nashvilleTn, {'weight': 8.5}),
                             (austinTx, oaklandCa, {'weight': 17.4}), (austinTx, orlandoFl, {'weight': 11.2}),
                             (austinTx, philadelphiaPa, {'weight': 16.6}), (austinTx, sacramentoCa, {'weight': 17.6}),
                             (austinTx, saltLakeCityUt, {'weight': 12.8}), (austinTx, sanDiegoCa, {'weight': 13.0}),
                             (austinTx, tucsonAz, {'weight': 8.9}), (baltimoreMd, charlotteDouglasNc, {'weight': 4.4}),
                             (baltimoreMd, clevelandOh, {'weight': 3.7}), (baltimoreMd, denverCo, {'weight': 16.6}),
                             (baltimoreMd, jacksonvilleFl, {'weight': 7.5}), (baltimoreMd, manchesterNh, {'weight': 4.3}),
                             (baltimoreMd, memphisTn, {'weight': 9.1}), (baltimoreMd, nashvilleTn, {'weight': 7.0}),
                             (baltimoreMd, oaklandCa, {'weight': 28.0}), (baltimoreMd, orlandoFl, {'weight': 8.9}),
                             (baltimoreMd, philadelphiaPa, {'weight': 1.0}), (baltimoreMd, sacramentoCa, {'weight': 27.2}),
                             (baltimoreMd, saltLakeCityUt, {'weight': 20.8}), (baltimoreMd, sanDiegoCa, {'weight': 26.3}),
                             (baltimoreMd, tucsonAz, {'weight': 23.1}), (charlotteDouglasNc, clevelandOh, {'weight': 5.1}),
                             (charlotteDouglasNc, denverCo, {'weight': 15.6}),
                             (charlotteDouglasNc, jacksonvilleFl, {'weight': 3.8}),
                             (charlotteDouglasNc, manchesterNh, {'weight': 8.7}),
                             (charlotteDouglasNc, memphisTn, {'weight': 6.1}),
                             (charlotteDouglasNc, nashvilleTn, {'weight': 4.0}),
                             (charlotteDouglasNc, oaklandCa, {'weight': 26.9}),
                             (charlotteDouglasNc, orlandoFl, {'weight': 5.2}),
                             (charlotteDouglasNc, philadelphiaPa, {'weight': 5.3}),
                             (charlotteDouglasNc, sacramentoCa, {'weight': 27.0}),
                             (charlotteDouglasNc, saltLakeCityUt, {'weight': 20.6}),
                             (charlotteDouglasNc, sanDiegoCa, {'weight': 23.8}),
                             (charlotteDouglasNc, tucsonAz, {'weight': 19.7}), (clevelandOh, denverCo, {'weight': 13.3}),
                             (clevelandOh, jacksonvilleFl, {'weight': 8.9}), (clevelandOh, manchesterNh, {'weight': 6.7}),
                             (clevelandOh, memphisTn, {'weight': 7.3}), (clevelandOh, nashvilleTn, {'weight': 5.2}),
                             (clevelandOh, oaklandCa, {'weight': 24.5}), (clevelandOh, orlandoFl, {'weight': 10.3}),
                             (clevelandOh, philadelphiaPa, {'weight': 4.3}), (clevelandOh, sacramentoCa, {'weight': 23.6}),
                             (clevelandOh, saltLakeCityUt, {'weight': 17.2}), (clevelandOh, sanDiegoCa, {'weight': 23.6}),
                             (clevelandOh, tucsonAz, {'weight': 20.0}), (denverCo, jacksonvilleFl, {'weight': 17.4}),
                             (denverCo, manchesterNh, {'weight': 20.0}), (denverCo, memphisTn, {'weight': 10.4}),
                             (denverCo, nashvilleTn, {'weight': 11.5}), (denverCo, oaklandCa, {'weight': 12.4}),
                             (denverCo, orlandoFl, {'weight': 18.4}), (denverCo, philadelphiaPa, {'weight': 17.2}),
                             (denverCo, sacramentoCa, {'weight': 11.6}), (denverCo, saltLakeCityUt, {'weight': 5.1}),
                             (denverCo, sanDiegoCa, {'weight': 10.7}), (denverCo, tucsonAz, {'weight': 8.9}),
                             (jacksonvilleFl, manchesterNh, {'weight': 11.7}),
                             (jacksonvilleFl, memphisTn, {'weight': 7.3}), (jacksonvilleFl, nashvilleTn, {'weight': 5.9}),
                             (jacksonvilleFl, oaklandCa, {'weight': 27.8}), (jacksonvilleFl, orlandoFl, {'weight': 1.4}),
                             (jacksonvilleFl, philadelphiaPa, {'weight': 8.4}),
                             (jacksonvilleFl, sacramentoCa, {'weight': 27.9}),
                             (jacksonvilleFl, saltLakeCityUt, {'weight': 22.5}),
                             (jacksonvilleFl, sanDiegoCa, {'weight': 23.3}), (jacksonvilleFl, tucsonAz, {'weight': 19.3}),
                             (manchesterNh, memphisTn, {'weight': 13.4}), (manchesterNh, nashvilleTn, {'weight': 11.3}),
                             (manchesterNh, oaklandCa, {'weight': 31.2}), (manchesterNh, orlandoFl, {'weight': 13.2}),
                             (manchesterNh, philadelphiaPa, {'weight': 3.4}), (manchesterNh, sacramentoCa, {'weight': 30.4}),
                             (manchesterNh, saltLakeCityUt, {'weight': 23.9}), (manchesterNh, sanDiegoCa, {'weight': 30.2}),
                             (manchesterNh, tucsonAz, {'weight': 26.6}), (memphisTn, nashvilleTn, {'weight': 2.1}),
                             (memphisTn, oaklandCa, {'weight': 20.8}), (memphisTn, orlandoFl, {'weight': 8.3}),
                             (memphisTn, philadelphiaPa, {'weight': 10.1}), (memphisTn, sacramentoCa, {'weight': 20.8}),
                             (memphisTn, saltLakeCityUt, {'weight': 15.5}), (memphisTn, sanDiegoCa, {'weight': 18.1}),
                             (memphisTn, tucsonAz, {'weight': 14.0}), (nashvilleTn, oaklandCa, {'weight': 22.9}),
                             (nashvilleTn, orlandoFl, {'weight': 6.8}), (nashvilleTn, philadelphiaPa, {'weight': 8.0}),
                             (nashvilleTn, sacramentoCa, {'weight': 22.9}), (nashvilleTn, saltLakeCityUt, {'weight': 16.6}),
                             (nashvilleTn, sanDiegoCa, {'weight': 20.2}), (nashvilleTn, tucsonAz, {'weight': 16.1}),
                             (oaklandCa, orlandoFl, {'weight': 28.8}), (oaklandCa, philadelphiaPa, {'weight': 28.6}),
                             (oaklandCa, sacramentoCa, {'weight': 0.8}), (oaklandCa, saltLakeCityUt, {'weight': 7.2}),
                             (oaklandCa, sanDiegoCa, {'weight': 4.9}), (oaklandCa, tucsonAz, {'weight': 8.5}),
                             (orlandoFl, philadelphiaPa, {'weight': 9.8}), (orlandoFl, sacramentoCa, {'weight': 28.9}),
                             (orlandoFl, saltLakeCityUt, {'weight': 23.4}), (orlandoFl, sanDiegoCa, {'weight': 24.2}),
                             (orlandoFl, tucsonAz, {'weight': 20.2}), (philadelphiaPa, sacramentoCa, {'weight': 27.8}),
                             (philadelphiaPa, saltLakeCityUt, {'weight': 21.4}),
                             (philadelphiaPa, sanDiegoCa, {'weight': 26.9}), (philadelphiaPa, tucsonAz, {'weight': 23.3}),
                             (sacramentoCa, saltLakeCityUt, {'weight': 6.4}), (sacramentoCa, sanDiegoCa, {'weight': 5.0}),
                             (sacramentoCa, tucsonAz, {'weight': 8.6}), (saltLakeCityUt, sanDiegoCa, {'weight': 7.5}),
                             (saltLakeCityUt, tucsonAz, {'weight': 7.7}), (sanDiegoCa, tucsonAz, {'weight': 4.0})])
spot = nx.kamada_kawai_layout(airportGraph, weight='weight')
nx.draw_networkx(airportGraph, spot, node_color='yellow', node_size=700, edge_color='black')
plt.show()
