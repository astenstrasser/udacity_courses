import movies

star_wars = movies.Movie("Star Wars - Episode I: The Phantom Menace",
                         "The Trade Federation upsets order in the Galactic Republic by blockading the planet Naboo in preparation for a full-scale invasion. The Republic's leader, Supreme Chancellor Valorum, dispatches Jedi Master Qui-Gon Jinn and his apprentice, Obi-Wan Kenobi, to negotiate with Trade Federation Viceroy Nute Gunray. Darth Sidious, a Sith Lord and the Trade Federation's secret benefactor, orders the Viceroy to kill the Jedi and begin their invasion with an army of battle droids.",
                         "https://m.media-amazon.com/images/M/MV5BYTRhNjcwNWQtMGJmMi00NmQyLWE2YzItODVmMTdjNWI0ZDA2XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=bD7bpG-zDJQ")


black_panther = movies.Movie("Black Panther",
                             "After the events of Captain America: Civil War, Prince T'Challa returns home to the reclusive, technologically advanced African nation of Wakanda to serve as his country's new king. However, T'Challa soon finds that he is challenged for the throne from factions within his own country. When two foes conspire to destroy Wakanda, the hero known as Black Panther must team up with C.I.A. agent Everett K. Ross and members of the Dora Milaje, Wakandan special forces, to prevent Wakanda from being dragged into a world war.",
                             "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                             "https://www.youtube.com/watch?v=xjDjIWPwcPU")

logan = movies.Movie("Logan",
                     "In a dystopian 2029, no mutants have been born in 25 years. Logan's healing ability has weakened and he has physically aged. The adamantium coating on his skeleton has begun to leak into his body, poisoning him. Hiding in plain sight, Logan spends his days working as a limo driver in El Paso, Texas. In an abandoned smelting plant in northern Mexico, he and mutant tracker Caliban care for 90-year-old Charles Xavier, Logan's mentor and founder of the X-Men. Gabriela Lopez, a former nurse for biotechnology corporation Alkali-Transigen, tries to hire Logan to escort her and an 11-year-old girl, Laura, to Eden, a refuge in North Dakota.",
                     "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                     "https://www.youtube.com/watch?v=Div0iP65aZo")


print(star_wars.title)
print(black_panther.title)
print(logan.title)
star_wars.show_trailer()
