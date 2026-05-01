DATA_TEXT = r'''
# Metro dataset (TXT version)
# Notes:
# 1) Use [SECTION_NAME] to separate sections
# 2) Each section contains a Python literal that can be parsed by ast.literal_eval
# 3) You can directly modify stations, fares, first/last train times,
#    crowding levels, landmarks, and other data
[METRO_LINES]
{
    "Line 1": {
        "stations": ["Kennedy Town", "HKU", "Sai Ying Pun", "Sheung Wan", "Central", "Admiralty", "Wan Chai", "Causeway Bay", "Tim Hau", "Fortress Hill", "North Point", "Quarry Bay",  "Tai Koo", "Sai Wan Ho", "Shau Kei Wan", "Heng Fa Chuen", "Chai Wan"],
        "run_times": [1.6, 1.8, 2.2, 1.7, 1.6, 2.0, 2.2, 1.7, 1.5, 1.9, 1.6, 2.4, 1.5, 1.7, 3.3, 2.5],
        "fare_per_segment": 1.4,
        "directions": {
            "forward": {
                "label": "Toward Chai Wan",
                "first_train": "06:00",
                "last_train": "24:50",
                "headway": [
                    ("06:00", "07:00", 6),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:50", 7)
                ],
                "crowding": [
                    ("06:00", "07:00", 1),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 3),
                    ("17:00", "19:00", 5),
                    ("19:00", "24:50", 2)
                ],
                "disruption_windows": []
            },
            "backward": {
                "label": "Toward Kennedy Town",
                "first_train": "06:05",
                "last_train": "24:35",
                "headway": [
                    ("06:05", "07:00", 6),
                    ("07:00", "09:00", 4),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 3),
                    ("19:00", "24:35", 7)
                ],
                "crowding": [
                    ("06:05", "07:00", 1),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 2),
                    ("17:00", "19:00", 5),
                    ("19:00", "24:35", 2)
                ],
                "disruption_windows": []
            }
        }
    },
    "Line 2": {
        "stations": ["Central", "Admiralty", "Tsim Sha Tsui", "Jordan", "Yau Ma Tei", "Mong Kok", "Prince Edward", "Sham Shui Po", "Cheung Sha Wan", "Lai Chi Kok", "Mei Foo", "Lai King", "Kwai Fong", "Kwai Hing", "Tai Wo Hau", "Tsuen Wan"],
        "run_times": [1.6, 2.2, 1.3, 1.3, 1.5, 1.1, 1.5, 1.3, 1.3, 1.7, 2.1, 1.5, 1.3, 1.5, 1.7],
        "fare_per_segment": 1.5,
        "directions": {
            "forward": {
                "label": "Toward Tsuen Wan",
                "first_train": "06:06",
                "last_train": "24:54",
                "headway": [
                    ("06:06", "07:00", 6),
                    ("07:00", "09:00", 4),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 3),
                    ("19:00", "24:54", 7)
                ],
                "crowding": [
                    ("06:06", "07:00", 1),
                    ("07:00", "09:00", 2),
                    ("09:00", "17:00", 2),
                    ("17:00", "19:00", 5),
                    ("19:00", "24:54", 3)
                ],
                "disruption_windows": []
            },
            "backward": {
                "label": "Toward Central",
                "first_train": "06:00",
                "last_train": "24:30",
                "headway": [
                    ("06:00", "07:00", 6),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:30", 7)
                ],
                "crowding": [
                    ("06:00", "07:00", 1),
                    ("07:00", "09:00", 5),
                    ("09:00", "17:00", 2),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:30", 2)
                ],
                "disruption_windows": []
            }
        }
    },
    "Line 3": {
        "stations": ["Whampoa", "Ho Man Tin", "Yau Ma Tei", "Mong Kok", "Prince Edward", "Shek Kip Mei", "Kowloon Tong", "Lok Fu", "Wong Tai Sin", "Diamond Hill", "Choi Hung", "Kowloon Bay", "Ngau Tau Kok", "Kwun Tong", "Lam Tin", "Yau Tong", "Tiu Keng Leng"],
        "run_times": [1.3, 1.5, 1.1, 1.0, 1.2, 1.5, 1.0, 1.0, 1.2, 1.3, 1.5, 1.2, 1.2, 1.5, 1.8, 2.1],
        "fare_per_segment": 1.6,
        "directions": {
            "forward": {
                "label": "Toward Tiu Keng Leng",
                "first_train": "06:10",
                "last_train": "24:40",
                "headway": [
                    ("06:10", "07:00", 6),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:40", 7)
                ],
                "crowding": [
                    ("06:10", "07:00", 2),
                    ("07:00", "09:00", 5),
                    ("09:00", "17:00", 2),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:40", 2)
                ],
                "disruption_windows": []
            },
            "backward": {
                "label": "Toward Whampoa",
                "first_train": "06:07",
                "last_train": "00:22",
                "headway": [
                    ("06:07", "07:00", 6),
                    ("07:00", "09:00", 4),
                    ("09:00", "17:00", 5),
                    ("17:00", "19:00", 3),
                    ("19:00", "24:22", 7)
                ],
                "crowding": [
                    ("06:07", "07:00", 2),
                    ("07:00", "09:00", 3),
                    ("09:00", "17:00", 2),
                    ("17:00", "19:00", 4),
                    ("19:00", "24:22", 2)
                ],
                "disruption_windows": []
            }
        }
    }
}

[TRANSFER_TIMES]
[
    ("Central", "Line 1", "Line 2", 4),
    ("Admiralty", "Line 1", "Line 2", 2),
    ("Central", "Line 2", "Line 1", 4),
    ("Admiralty", "Line 2", "Line 1", 2),
    ("Yau Ma Tei", "Line 2", "Line 3", 1.5),
    ("Yau Ma Tei", "Line 3", "Line 2", 1.5),
    ("Mong Kok", "Line 2", "Line 3", 1.5),
    ("Mong Kok", "Line 3", "Line 2", 1.5),
    ("Prince Edward", "Line 2", "Line 3", 1.5),
    ("Prince Edward", "Line 3", "Line 2", 1.5)
]

[STATION_INFO]
{
    "Kennedy Town" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Kennedy Town Swimming Pool", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Smithfield Municipal Services Building", "walk": 1, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Belcher's Bay Park", "walk": 3, "elevator": False, "stairs": 1},
                {"landmark": "The Belcher's", "walk": 4, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Forbes Street Tree Walls", "walk": 1, "elevator": True, "stairs": 0},
                {"landmark": "Kennedy Town Temporary Recreation Ground", "walk": 5, "elevator": True, "stairs": 1}
            ]
        }
    },
    "HKU" :
    {
        "entries": {
            "Gate A": {"walk": 5, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 4, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "The University of Hong Kong", "walk": 5, "elevator": True, "stairs": 0},
                {"landmark": "St. Paul's College", "walk": 7, "elevator": True, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Chong Yip Shopping Centre", "walk": 4, "elevator": False, "stairs": 1},
                {"landmark": "Shek Tong Tsui Municipal Services Building", "walk": 3, "elevator": True, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "St.Anthony's Church", "walk": 4, "elevator": True, "stairs": 0},
                {"landmark": "The Belcher's", "walk": 5, "elevator": True, "stairs": 1}
            ]
        }
    },
    "Sheung Wan" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 4, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Wing Lok Street", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "The Center", "walk": 5, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Sheung Wan Civic Centre", "walk": 3, "elevator": False, "stairs": 1},
                {"landmark": "Man Mo Temple", "walk": 8, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Western Market", "walk": 4, "elevator": False, "stairs": 0},
                {"landmark": "Shun Tak Centre", "walk": 6, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Central" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 4, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Exchange Square", "walk": 3, "elevator": False, "stairs": 0},
                {"landmark": "General Post Office", "walk": 5, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "World-Wide HOuse", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "Hang Seng Bank Headquarters", "walk": 4, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Dogulas Street", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Pedder Street", "walk": 3, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Admiralty" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 4, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Admiralty Centre", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Central Government Offices", "walk": 5, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Far East Finance Centre", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "Lippo Centre", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Pacific Place", "walk": 5, "elevator": False, "stairs": 0},
                {"landmark": "Hong Kong Park", "walk": 8, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Causeway Bay" :
    {
        "entries": {
            "Gate A": {"walk": 5, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Times Square", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Soundwill Plaza", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Causeway Bay Plaza I", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "Circle Tower", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Sino Plaza", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Elizabeth House", "walk": 4, "elevator": False, "stairs": 1}
            ]
        }
    },
    "North Point" :
    {
        "entries": {
            "Gate A": {"walk": 4, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Java Road Market", "walk": 4, "elevator": False, "stairs": 0},
                {"landmark": "Harbour North", "walk": 6, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Healthy Gardens", "walk": 5, "elevator": False, "stairs": 1},
                {"landmark": "Island Place", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "North Point Government Offices", "walk": 1, "elevator": True, "stairs": 0},
                {"landmark": "Model Housing Estate", "walk": 3, "elevator": True, "stairs": 1}
            ]
        }
    },
    "Tai Koo" :
    {
        "entries": {
            "Gate A": {"walk": 4, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Kornhill Plaza", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Kornhill", "walk": 4, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Cityplaza", "walk": 3, "elevator": False, "stairs": 1},
                {"landmark": "Kornhill Garden", "walk": 2, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Quarry Bay Park", "walk": 5, "elevator": False, "stairs": 0},
                {"landmark": "Taikoo Shing", "walk": 4, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Chai Wan" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "New Jade Shopping Arcade", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Chai Wan Municipal Services Building", "walk": 5, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Kut Shing Street", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "Chai Wan Industrial City", "walk": 8, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Youth Square", "walk": 4, "elevator": False, "stairs": 0},
                {"landmark": "Law Uk Folk Museum", "walk": 6, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Yau Ma Tei" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Sino Centre", "walk": 5, "elevator": False, "stairs": 0},
                {"landmark": "Pitt Street", "walk": 1, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "In's Point", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "Portland Street", "walk": 1, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Broadway Cinematheque", "walk": 8, "elevator": False, "stairs": 0},
                {"landmark": "Public Square Street", "walk": 2, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Mong Kok" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 4, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Mong Kok Road", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Portland Street", "walk": 1, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Argyle Centre", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "T.O.P This Is Our Place", "walk": 2, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Langham Place", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Cordis Hong Kong", "walk": 2, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Prince Edward" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Mong Kok Police Station", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Playing Field Road", "walk": 2, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Allied Plaza", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "Flower Market", "walk": 6, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Pioneer Centre", "walk": 3, "elevator": False, "stairs": 0},
                {"landmark": "Sai Yeung Choi Street South", "walk": 1, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Cheung Sha Wan" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Un Chau Estate", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "CSW Jockey Club Clinic", "walk": 4, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Fortune Estate", "walk": 5, "elevator": False, "stairs": 1},
                {"landmark": "CSW Playground", "walk": 2, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Lei Cheng Uk Han Tomb Museum", "walk": 12, "elevator": False, "stairs": 0},
                {"landmark": "Un Chau Street", "walk": 1, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Lai King" :
    {
        "entries": {
            "Gate A": {"walk": 4, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Cheung Sha Wan Plaza", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Hong Kong Centre", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Elite Industrial Centre", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "Hong Kong Industrial Centre", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "D2 Place", "walk": 3, "elevator": False, "stairs": 0},
                {"landmark": "Lai Chi Kok Reception Centre", "walk": 8, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Kwai Hing" :
    {
        "entries": {
            "Gate A": {"walk": 1, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 1, "line_bias": {"Line 1": 1, "Line 2": 0}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Kwai Hing Government Offices", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Kwai Hing Estate", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Kwai Chung Centre", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "KCC", "walk": 5, "elevator": False, "stairs": 0}
            ]
        }
    },
    "Tsuen Wan" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "D·PARK", "walk": 8, "elevator": False, "stairs": 0},
                {"landmark": "Tsuen Wan Government Offices", "walk": 5, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Nan Fung Centre", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "Tsuen Wan Multi-storey Carpark", "walk": 3, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Luk Yeung Galleria", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "Wai Tsuen Sports Centre", "walk": 6, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Whampoa" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Whampoa Garden", "walk": 2, "elevator": False, "stairs": 0},
                {"landmark": "Tak Ting Street", "walk": 1, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "The Whampoa-Boat", "walk": 3, "elevator": False, "stairs": 1},
                {"landmark": "Whampoa Gourmet Place", "walk": 2, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Whampoa Estate", "walk": 3, "elevator": True, "stairs": 0},
                {"landmark": "Shun King Street", "walk": 1, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Kowloon Tong" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Bapist Hospital", "walk": 8, "elevator": False, "stairs": 0},
                {"landmark": "Hong Kong Baptist University", "walk": 10, "elevator": False, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Edbrooke Road", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "St. Teresa's Church", "walk": 12, "elevator": False, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Festival Walk", "walk": 1, "elevator": False, "stairs": 0},
                {"landmark": "City University of Hong Kong", "walk": 5, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Wong Tai Sin" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Wong Tai Sin Temple", "walk": 2, "elevator": True, "stairs": 0},
                {"landmark": "Muk Lun Street", "walk": 3, "elevator": True, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Temple Mall", "walk": 1, "elevator": False, "stairs": 1},
                {"landmark": "Lion Rock", "walk": 8, "elevator": True, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Lower Wong Tai Sin Estate", "walk": 3, "elevator": True, "stairs": 0},
                {"landmark": "Ching Tak Street", "walk": 1, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Choi Hung" :
    {
        "entries": {
            "Gate A": {"walk": 3, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 3, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Ping Shek Estate", "walk": 2, "elevator": True, "stairs": 0},
                {"landmark": "NWG Municipal Services Building", "walk": 4, "elevator": True, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Ngau Chi Wan Village", "walk": 2, "elevator": False, "stairs": 1},
                {"landmark": "SJ Anglo-Chinese School", "walk": 5, "elevator": True, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Choi Hung Estate", "walk": 2, "elevator": True, "stairs": 0},
                {"landmark": "Tan Fung House", "walk": 3, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Kwun Tong" :
    {
        "entries": {
            "Gate A": {"walk": 2, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 0}},
            "Gate C": {"walk": 2, "line_bias": {"Line 1": 1, "Line 2": 1}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "apm Mall", "walk": 1, "elevator": True, "stairs": 0},
                {"landmark": "Yue Man Square", "walk": 3, "elevator": True, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Camel Paint Building", "walk": 5, "elevator": False, "stairs": 1},
                {"landmark": "Hoi Yuen Road", "walk": 1, "elevator": True, "stairs": 0}
            ],
            "Gate C": [
                {"landmark": "Kwun Tong Government Offices", "walk": 3, "elevator": True, "stairs": 0},
                {"landmark": "Kwun Tong Community Centre", "walk": 5, "elevator": False, "stairs": 1}
            ]
        }
    },
    "Tiu Keng Leng" :
    {
        "entries": {
            "Gate A": {"walk": 1, "line_bias": {"Line 1": 0, "Line 2": 1}},
            "Gate B": {"walk": 1, "line_bias": {"Line 1": 1, "Line 2": 0}}
        },
        "exits": {
            "Gate A": [
                {"landmark": "Metro Town", "walk": 1, "elevator": True, "stairs": 0},
                {"landmark": "HKDI", "walk": 2, "elevator": True, "stairs": 0}
            ],
            "Gate B": [
                {"landmark": "Kin Ming Estate", "walk": 3, "elevator": False, "stairs": 1},
                {"landmark": "Shin Ming Estate", "walk": 5, "elevator": True, "stairs": 0}
            ]
        }
    }
}  

'''

DEFAULT_TRANSFER_TIME = 5

CARBON_CONFIG = {
    "metro_kg_per_passenger_km": 0.06,
    "car_kg_per_passenger_km": 0.17,
    "metro_avg_kmh": 35,
}