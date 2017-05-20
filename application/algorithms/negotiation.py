from operator import itemgetter


def negotiation(agents, schedule):
    for task in schedule.tasks:
        offers = []
        for agent in agents:
            offers.append((agent, agent.makeOffer(task)))
        bestOffer = max(offers, key=itemgetter(1))
        print bestOffer
