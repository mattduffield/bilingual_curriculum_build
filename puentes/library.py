"""Content library. All original. Each activity: ages=(min,max), bilingual fields as {es, en}."""
def b(es, en): return {"es": es, "en": en}

LIBRARY = {
 "my-garden": {
  "theme": b("Mi huerto", "My garden"),
  "title": b("Mi huerto: sembramos y aprendemos", "My Garden: We Plant and Learn"),
  "objectives": [
    b("Contar hasta 5 objetos del huerto.", "Count up to 5 garden objects."),
    b("Nombrar cosas del huerto en dos idiomas.", "Name garden things in two languages."),
    b("Usar las manos y los dedos para explorar, pintar y recoger.", "Use hands and fingers to explore, paint and pick up."),
  ],
  "vocabulary": [
    b("huerto","garden"), b("semilla","seed"), b("tierra","soil"), b("zanahoria","carrot"),
    b("flor","flower"), b("hoja","leaf"), b("raíz","root"), b("regar","to water"), b("gusano","worm"),
  ],
  "activities": {
   "math": [{
    "name": b("Contar zanahorias","Counting carrots"), "skill_area": {"key":"math", **b("matemáticas","math")},
    "ages": (3,4), "safety_ok_under_3": False,
    "materials": [b("5 zanahorias de papel naranja","5 orange paper carrots"), b("un balde o caja","a bucket or box")],
    "steps": [
      b("Esconde las zanahorias por el salón.","Hide the carrots around the room."),
      b("Busquen juntos y pongan cada una en el balde.","Look together and put each one in the bucket."),
      b("Cuenten en voz alta: una, dos, tres...","Count out loud: one, two, three..."),
      b("Pregunta: \"¿Cuántas encontramos?\"","Ask: \"How many did we find?\""),
    ],
    "supervision": b("Un adulto cerca para guiar el conteo.","An adult nearby to guide the counting."),
    "say_this": b("¡Cinco zanahorias en el balde!","Five carrots in the bucket!"),
   }],
   "language": [{
    "name": b("¿Qué hay en el huerto?","What is in the garden?"), "skill_area": {"key":"language", **b("lenguaje","language")},
    "ages": (3,5), "safety_ok_under_3": False,
    "materials": [b("5 tarjetas con dibujos: semilla, flor, hoja, tierra, gusano","5 picture cards: seed, flower, leaf, soil, worm")],
    "steps": [
      b("Muestra una tarjeta a la vez.","Show one card at a time."),
      b("Di la palabra en español y luego en inglés.","Say the word in Spanish, then in English."),
      b("Pide al niño que repita contigo.","Ask the child to say it with you."),
      b("Esconde una tarjeta y pregunta: \"¿Cuál falta?\"","Hide one card and ask: \"Which one is missing?\""),
    ],
    "supervision": b("Un adulto con el niño todo el tiempo.","An adult with the child the whole time."),
    "say_this": b("Esta es una semilla. ¡Semilla! / Seed!","This is a seed. ¡Semilla! / Seed!"),
   }],
   "art": [{
    "name": b("Flores con tenedor","Fork flowers"), "skill_area": {"key":"art", **b("arte","art")},
    "ages": (3,5), "safety_ok_under_3": False,
    "materials": [b("papel","paper"), b("pintura lavable no tóxica","washable non-toxic paint"), b("un plato de papel","a paper plate"), b("tenedores de plástico","plastic forks")],
    "steps": [
      b("Pon un poco de pintura en el plato.","Put a little paint on the plate."),
      b("Moja los dientes del tenedor en la pintura.","Dip the fork's tines in the paint."),
      b("Presiona el tenedor en el papel para hacer pétalos.","Press the fork on the paper to make petals."),
      b("Dibuja un tallo verde con el dedo.","Draw a green stem with a finger."),
    ],
    "supervision": b("Un adulto cerca. Usa tenedores de plástico con puntas romas; el adulto los revisa antes.","An adult nearby. Use plastic forks with blunt tines; the adult checks them first."),
    "say_this": b("¡Mira cuántos pétalos tiene tu flor!","Look how many petals your flower has!"),
   }],
   "sensory": [{
    "name": b("Tierra de avena","Oat soil"), "skill_area": {"key":"sensory", **b("sensorial","sensory")},
    "ages": (3,5), "safety_ok_under_3": False,
    "materials": [b("avena seca en una caja grande","dry oats in a large box"), b("cacao en polvo (opcional)","cocoa powder (optional)"), b("cucharas y tazas","spoons and cups"), b("insectos de papel o un juguete grande (más grande que un tubo de papel higiénico)","paper bugs or one large toy (bigger than a toilet-paper tube)")],
    "steps": [
      b("Mezcla la avena con un poco de cacao para que parezca tierra.","Mix the oats with a little cocoa so it looks like soil."),
      b("Esconde los insectos dentro.","Hide the toy bugs inside."),
      b("Cava con las manos y las cucharas.","Dig with hands and spoons."),
      b("Habla de lo que sienten: suave, seca, esponjosa.","Talk about how it feels: soft, dry, fluffy."),
    ],
    "supervision": b("Un adulto con el grupo todo el tiempo; que nadie coma la mezcla. Revisa alergias a la avena, al gluten y al cacao. Si hay alergia, usa papel triturado o la versión sin cacao.","An adult with the group the whole time; no one eats the mix. Check for oat, gluten and cocoa allergies. If there is an allergy, use shredded paper or the version without cocoa."),
    "say_this": b("La tierra se siente suave.","The soil feels soft."),
   }],
   "motor": [{
    "name": b("Sembrar con pinzas","Planting with tongs"), "skill_area": {"key":"motor", **b("motricidad","motor")},
    "ages": (3,5), "safety_ok_under_3": False,
    "materials": [b("una caja de huevos","an egg carton"), b("pompones grandes o bolas de papel arrugado (más grandes que un tubo de papel higiénico)","large pom-poms or crumpled paper balls (bigger than a toilet-paper tube)"), b("pinzas de cocina","kitchen tongs")],
    "steps": [
      b("Pon las \"semillas\" en un plato.","Put the \"seeds\" on a plate."),
      b("Agarra una semilla con las pinzas.","Pick up a seed with the tongs."),
      b("Siémbrala en un hueco de la caja.","Plant it in a hole of the carton."),
      b("Sigue hasta llenar todos los huecos.","Keep going until every hole is full."),
    ],
    "supervision": b("Un adulto sentado al lado todo el tiempo; que nada se vaya a la boca.","An adult sitting beside the child the whole time; make sure nothing goes in the mouth."),
    "say_this": b("¡Una semilla en cada huequito!","One seed in each little hole!"),
   }],
  },
 }
}

# ---- Week 2: water, sun and growing (new title/objectives/vocabulary + 5 new activities) ----
LIBRARY["my-garden"]["weeks"] = {2: {
  "title": b("Mi huerto: agua, sol y crecer", "My Garden: Water, Sun and Growing"),
  "objectives": [
    b("Comparar tamaños: grande y pequeño.", "Compare sizes: big and small."),
    b("Aprender palabras de la lluvia, el sol y el crecimiento.", "Learn words about rain, sun and growing."),
    b("Moverse y explorar con agua, pintura y saltos.", "Move and explore with water, paint and hopping."),
  ],
  "vocabulary": [
    b("lluvia","rain"), b("gota","drop"), b("sol","sun"), b("nube","cloud"), b("agua","water"),
    b("grande","big"), b("pequeño","small"), b("brote","sprout"), b("crecer","to grow"), b("regadera","watering can"),
  ],
}}
_w2 = {
 "math": {
  "name": b("Flores grandes y pequeñas","Big and small flowers"), "skill_area": {"key":"math", **b("matemáticas","math")},
  "ages": (3,4), "safety_ok_under_3": False,
  "materials": [b("6 flores de papel: 3 grandes y 3 pequeñas","6 paper flowers: 3 big and 3 small"), b("2 platos de papel","2 paper plates")],
  "steps": [
    b("Pon todas las flores en la mesa.","Put all the flowers on the table."),
    b("Muestra una flor grande y una pequeña.","Show one big flower and one small flower."),
    b("Pongan las grandes en un plato y las pequeñas en el otro.","Put the big ones on one plate and the small ones on the other."),
    b("Cuenten cuántas hay en cada plato.","Count how many are on each plate."),
  ],
  "supervision": b("Un adulto cerca para guiar y hacer preguntas.","An adult nearby to guide and ask questions."),
  "say_this": b("¡Esta flor es grande y esta es pequeña!","This flower is big and this one is small!"),
 },
 "language": {
  "name": b("Canto de la lluvia","Rain chant"), "skill_area": {"key":"language", **b("lenguaje","language")},
  "ages": (3,5), "safety_ok_under_3": False,
  "materials": [b("una hoja grande de papel verde","a big green paper leaf")],
  "steps": [
    b("Muestra la hoja de papel y di: \"Hoy hablamos de la lluvia.\"","Show the paper leaf and say: \"Today we talk about rain.\""),
    b("Di el canto despacio. Haz caer los dedos como gotas.","Say the chant slowly. Let your fingers fall like drops."),
    b("Haz un círculo grande con los brazos para el sol.","Make a big circle with your arms for the sun."),
    b("Repitan el canto juntos dos o tres veces.","Say the chant together two or three times."),
  ],
  "supervision": b("Un adulto con los niños todo el tiempo.","An adult with the children the whole time."),
  "say_this": b("Gota, gota, cae la lluvia; sol, sol, crece mi plantita.","Drop, drop, the rain falls; sun, sun, my little plant grows."),
 },
 "art": {
  "name": b("Gotas con esponja","Sponge raindrops"), "skill_area": {"key":"art", **b("arte","art")},
  "ages": (3,5), "safety_ok_under_3": False,
  "materials": [b("papel","paper"), b("pintura azul lavable no tóxica","washable non-toxic blue paint"), b("un plato de papel","a paper plate"), b("trozos grandes de esponja de cocina (más grandes que un tubo de papel higiénico)","big pieces of kitchen sponge (bigger than a toilet-paper tube)")],
  "steps": [
    b("Pon un poco de pintura azul en el plato.","Put a little blue paint on the plate."),
    b("Moja un trozo de esponja en la pintura.","Dip a piece of sponge in the paint."),
    b("Presiona la esponja en el papel para hacer una gota.","Press the sponge on the paper to make a drop."),
    b("Haz muchas gotas: ¡una lluvia!","Make lots of drops: a rainstorm!"),
  ],
  "supervision": b("Un adulto cerca; revisa que los trozos de esponja sean grandes y que nadie los muerda.","An adult nearby; check that the sponge pieces are big and that no one chews them."),
  "say_this": b("¡Mira cuántas gotas de lluvia!","Look how many raindrops!"),
 },
 "sensory": {
  "name": b("Lluvia en la bandeja","Rain in the tray"), "skill_area": {"key":"sensory", **b("sensorial","sensory")},
  "ages": (3,5), "safety_ok_under_3": False,
  "materials": [b("una bandeja o tina baja con borde","a shallow tray or tub with a rim"), b("agua (dos dedos de profundidad)","water (about two fingers deep)"), b("vasos de plástico con agujeros hechos por un adulto","plastic cups with holes made by an adult"), b("una toalla","a towel")],
  "steps": [
    b("Pon la bandeja sobre la toalla.","Put the tray on the towel."),
    b("El adulto echa un poco de agua en la bandeja.","The adult pours a little water into the tray."),
    b("Llenen un vaso y dejen que el agua caiga por los agujeros, como lluvia.","Fill a cup and let the water fall through the holes, like rain."),
    b("Hablen de lo que ven y sienten: fría, mojada, gotas.","Talk about what you see and feel: cold, wet, drops."),
  ],
  "supervision": b("Un adulto al alcance de la mano todo el tiempo. Agua muy poco profunda. Seca el piso al terminar.","An adult within arm's reach the whole time. Very shallow water. Dry the floor when done."),
  "say_this": b("La lluvia cae, gota a gota.","The rain falls, drop by drop."),
 },
 "motor": {
  "name": b("Piedras del huerto","Garden stones"), "skill_area": {"key":"motor", **b("motricidad","motor")},
  "ages": (3,5), "safety_ok_under_3": False,
  "materials": [b("6 platos de papel","6 paper plates"), b("cinta adhesiva","tape")],
  "steps": [
    b("Pega los platos al piso con cinta, en fila, a un paso de distancia.","Tape the plates to the floor in a row, one step apart."),
    b("Muestra cómo pisar de plato en plato.","Show how to step from plate to plate."),
    b("Salten juntos de \"piedra\" en \"piedra\".","Hop together from \"stone\" to \"stone\"."),
    b("Cuenten cada salto en voz alta.","Count each hop out loud."),
  ],
  "supervision": b("Un adulto al lado. Piso limpio y firme; con zapatos o descalzos, no solo con calcetines.","An adult beside the child. Clean, firm floor; wear shoes or go barefoot, not just socks."),
  "say_this": b("¡Salto, salto, salto a la piedra!","Hop, hop, hop to the stone!"),
 },
}
for _skill, _act in _w2.items():
    _act["week"] = 2
    LIBRARY["my-garden"]["activities"][_skill].append(_act)
