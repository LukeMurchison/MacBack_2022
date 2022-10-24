from django.shortcuts import render
from dataclasses import dataclass
@dataclass
# Create your views here.
class Cats:
    name: str
    home: str
    decs: str
    pop: str




def home(request, input):
    context = {
        'caracal': Cats('Caracal', 'Most of Africa', 'Typically nocturnal, the caracal is highly secretive and difficult to observe. It is territorial, and lives mainly alone or in pairs. The caracal is a carnivore that typically preys upon small mammals, birds, and rodents. It can leap higher than 3.0 m (10 ft) and catch birds in midair. It stalks its prey until it is within 5 m (16 ft) of it, after which it runs it down and kills its prey with a bite to the throat or to the back of the neck.', '5,000,000'),
        'serval': Cats('Serval', 'Most of Africa', 'The serval is a solitary carnivore and active both by day and at night. It preys on rodents, particularly vlei rats, small birds, frogs, insects, and reptiles, using its sense of hearing to locate prey. It leaps over 2 m (6 ft 7 in) above the ground to land on the prey on its forefeet, and finally kills it with a bite on the neck or the head. ', '250'),
        'cougar': Cats('Cougar', 'All of North America', 'The cougar is an ambush predator that pursues a wide variety of prey. Primary food sources are ungulates, particularly deer, but it also hunts smaller prey such as rodents. It prefers habitats with dense underbrush and rocky areas for stalking, but also lives in open areas. Cougars are territorial and lives at low population densities. Individual home ranges depend on terrain, vegetation and abundance of prey.', '30,000'),
        'leopard': Cats('Leopard', 'Africa, Central Asia, India, and China', 'Compared to other wild cats, the leopard has relatively short legs and a long body with a large skull. Its fur is marked with rosettes. It is similar in appearance to the jaguar (Panthera onca), but has a smaller, lighter physique, and its rosettes are generally smaller, more densely packed and without central spots.', '700,000'),
        'key': input
}
    return render(request, "details.html", context)

def land(request):
    return render(request, "land.html")

