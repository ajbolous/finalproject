from operator import itemgetter

def negotiation(agents, missions, date):
    for mission in missions:
        offers = []
        for agent in agents:
            offers.append((agent, agent.makeOffer(task)))
        bestOffer = max(offers, key=itemgetter(1))
        print bestOffer
