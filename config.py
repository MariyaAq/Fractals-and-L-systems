fractals = {
    #P1e
    "snowflake_P1e":{
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 150,
        "angle": 60,
        "start_point": (-50, -50),
        "start_angle": 0,
        "rules":{
            "F": "F",

        },
        "num_iter": 1,
    },

    #P1g
    "snowflake_P1g":{
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 20,
        "angle": 60,
        "start_point": (-50, -50),
        "start_angle": 0,
        "rules":{
            "F": "F[+F][-F]FF[+FF][-FF]F[+F][-F]F[+F][-F]F[+F][-F]F",

        },
        "num_iter": 1,
    },

    #собственно придуманая снежинка
    "snowflake_pridumalasama":{
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 5,
        "angle": 60,
        "start_point": (-50, -50),
        "start_angle": 0,
        "rules":{
            "F": "F[+F][-F]FF[++FF][--FF]F[+F][-F]F[+F][-F]F[+F][-F]F",

        },
        "num_iter": 2,
    },
    # type P2c
    "snowflake_P2c" : {
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 15,
        "angle": 60,
        "start_point": (0, 0),
        "start_angle": 0,
        "rules":
            ("F", "F[+FF][-FF]FF[+F][-F]FF"),
        
        "num_iter": 1,
    },

    # type P3a
      "snowflake_P3a" : {
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]+[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 25,
        "angle": 30,
        "start_point": (0, 0),
        "start_angle": 0,
        "rules":{
            "F": "FFXXX",
            "X": "[++F][--F]F",

        },
        "num_iter": 2,
    },
    
    # type P2a
    "snowflake_P2a":{
        "width": None,
        "axiom": "[F]+[F]+[F]",
        "len": 25,
        "angle": 120,
        "start_point": (-100, 100),
        "start_angle": 0,
        "rules":{
            "F": "FF[+F][-F]F[+F][-F]",

        },
        "num_iter": 2,
    },


    # type P1f
    "snowflake_P1f" : {
        "width": None,
        "axiom": "[F]+[F]+[F]+[F]+[F]+[F]",
        "len": 25,
        "angle": 60,
        "start_point": (-100, 100),
        "start_angle": 0,
        "rules":{
            "F": "FF[+F][-F]FF[+FF][-FF][++F][--F]FF[+F][-F]F",

        },
        "num_iter": 1,
    },

    "derevo_prob":{
        "len": 30,
        "angle": 33,
        "axiom": "A",
        "start_point": (-100, -200),
        "start_angle": 90,
        "rules":{
           "F": [("F", 0.5),
                 ("FF", 0.5)], 
           "A": [
               ("F[+A][A][-A]", 0.3),
               ("F[+A][-A]", 0.7),
           ]
        },
        "num_iter": 5,
    },

    "serpinsky": {
        "width": None, 
        "len": 5,
        "angle": 60,
        "axiom": "---FXF--FF--FF",
        "rules": [
            ("F", "FF"),
            ("X", "--FXF++FXF++FXF--"),
        ],
        "num_iter": 4,
        "start_point": (100, -100),
        "start_angle": 0,
    },

    "stairway": {
        "len": 10,
        "angle": 90,
        "axiom": "Y",
        "rules": [
            ("X", "F+F-"),
            ("Y", "YX"),
        ],
        "num_iter": 4,
        "start_point": (100, -100),
        "start_angle": 0,
    },

    "drakonXartera":{
        "len": 5,
        "angle": 90,
        "axiom": "FX",
        "rules":{
            ("FX", "FX+FY+"), 
            ("FY", "-FX-FY"),
        },
        "num_iter": 12,
        "start_point": (100, -100),
        "start_angle": 0,
    },

    "krivaiGilberta":{
        "len": 15,
        "angle": 90,
        "axiom": "X",
        "rules":{
            ("X", "-YF+XFX+FY-"), 
            ("Y", "+XF-YFY-FX+"),
        },
        "num_iter": 4,
        "start_point": (0, -200),
        "start_angle": 90,
    },

    "krivaiGospera":{
        "len": 20,
        "angle": 60,
        "axiom": "XF",
        "start_point": (0, -200),
        "start_angle": 0,
        "rules":{
            ("X", "X+YF++YF-FX--FXFX-YF+"), 
            ("Y", "-FX+YFYF++YF+FX--FX-Y"),
        },
        "num_iter": 3,

    },

    "kust":{
        "len": 10,
        "angle": 22.5,
        "axiom": "F",
        "rules":{
            ("F", "FF-[-F+F+F]+[+F-F-F]")
        },
        "num_iter": 4,
        "start_point": (0, -200),
        "start_angle": 90,
    },

    "krivaipeano":{
        "len": 5,
        "angle": 90,
        "axiom": "F",
        "start_point": (-200, -250),
        "start_angle": 90,
        "rules":{
            ("F", "F-F+F+F+F-F-F-F+F"), 
        },
        "num_iter": 4,
    },

    "krivaiSerpinskogo":{
        "len": 15,
        "angle": 90,
        "axiom": "F+XF+F+XF",
        "start_point": (170, -200),
        "start_angle": 45,
        "rules":{
            ("F", "F"),
            ("X", "XF-F+F-XF+F+XF-F+F-X"), 
        },
        "num_iter": 3,
    },

    "snezinkaKoha":{
        "len": 5,
        "angle": 60,
        "axiom": "F--F--F",
        "start_point": (-200, 100),
        "start_angle": 0,
        "rules":{
           ("F", "F+F--F+F"),
           
        },
        "num_iter": 4,
    },
    
    "cvetok":{
        "len": 15,
        "angle": 11.25,
        "axiom": "F[+F+F][-F-F][++F][--F]F",
        "start_point": (-100, -200),
        "start_angle": 90,
        "rules":{
           ("F", "FF[++F][+F][F][-F][--F]"),
        },
        "num_iter": 3,
    },

    "derevo_prob":{
        "len": 30,
        "angle": 33,
        "axiom": "A",
        "start_point": (-100, -200),
        "start_angle": 90,
        "rules":{
           "F": [("F", 0.5),
                 ("FF", 0.5)], 
           "A": [
               ("F[+A][A][-A]", 0.3),
               ("F[+A][-A]", 0.7),
           ]
        },
        "num_iter": 5,
    },

    "derevo_prostoe":{
        "len": 30,
        "angle": 33,
        "axiom": "A",
        "start_point": (-100, -200),
        "start_angle": 90,
        "rules":{
           ("F", "FF"),
           ("A", "F[+A][-A]"),
        },
        "num_iter": 4,
    },

    "snow_01":{
        "len": 5, 
        "angle": 60,
        "axiom": "[A]+[A]+[A]+[A]+[A]+[A]",
        "start_point": (-100, -200),
        "start_angle": 90,
        "rules":{
            "F": [("F")],
            "A": [("F[A]")]
        }
    },

    "snezinka_koha_random":{
        "len": 10,
        "angle": 60,
        "axiom": "F--F--F",
        "start_point": (-200, 100),
        "start_angle": 0,
        "rules":{
           "F": [("F+F--F+F", 0.7),
                 ("F-F++F-F", 0.3)],
           
        },
        "num_iter": 3,
    },
}


if __name__ == "__main__":
    print("HELLO")