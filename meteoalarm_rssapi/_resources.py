# Produced by 'meteoalarm-tools' @'2021-01-19UTC15:25'

# TODO Build database of regions (for countries with many regions) 
#      and get the rss directly for the region

regions = {
    "AT": {},
    "BA": {},
    "BE": {},
    "BG": {},
    "CH": {},
    "CY": {},
    "CZ": {},
    "DE": {
"Alb-Donau-Kreis und Stadt Ulm":"074",
"Altmarkkreis Salzwedel":"216",
"B.gau-Hochschwarzwald / Freiburg":"035",
"Bodenseekreis":"271",
"Bundesstadt Bonn":"289",
"Burgenlandkreis":"145",
"Darmstadt-Dieburg / Darmstadt":"047",
"Donnersbergkreis":"197",
"Eifelkreis Bitburg-Prüm":"387",
"Elbe von Hamburg bis Cuxhaven":"804",
"Elbe Wesermündung":"805",
"Ennepe-Ruhr-Kreis":"134",
"Enzkreis und Stadt Pforzheim":"050",
"Erzgebirgskreis":"343",
"Flensburg bis Femarn":"808",
"Hansestadt Bremen":"369",
"Hansestadt Hamburg":"413",
"Hansestadt Lübeck":"265",
"Hansestadt Rostock":"234",
"Heidekreis":"317",
"Helgoland":"803",
"Hochsauerlandkreis":"411",
"Hochtaunuskreis":"201",
"Hohenlohekreis":"212",
"Ilm-Kreis":"254",
"Insel Borkum":"039",
"Insel Helgoland":"422",
"Kreis Ahrweiler":"232",
"Kreis Aichach-Friedberg":"375",
"Kreis Altenburger Land":"255",
"Kreis Altenkirchen":"199",
"Kreis Altötting":"116",
"Kreis Alzey-Worms":"397",
"Kreis Amberg-Sulzbach":"353",
"Kreis Ammerland":"221",
"Kreis Anhalt-Bitterfeld":"357",
"Kreis Aurich - Binnenland":"102",
"Kreis Aurich - Küste":"103",
"Kreis Bad Dürkheim":"390",
"Kreis Bad Kissingen":"409",
"Kreis Bad Kreuznach":"143",
"Kreis Bad Tölz-Wolfratshausen":"371",
"Kreis Barnim":"264",
"Kreis Bautzen - Bergland":"086",
"Kreis Bautzen - Tiefland":"054",
"Kreis Berchtesgadener Land":"183",
"Kreis Bergstraße":"361",
"Kreis Bernkastel-Wittlich":"190",
"Kreis Biberach":"163",
"Kreis Birkenfeld":"182",
"Kreis Böblingen":"223",
"Kreis Börde":"306",
"Kreis Borken":"355",
"Kreis Calw":"152",
"Kreis Celle":"138",
"Kreis Cham":"309",
"Kreis Cloppenburg":"200",
"Kreis Cochem-Zell":"214",
"Kreis Coesfeld":"125",
"Kreis Cuxhaven - Binnenland":"030",
"Kreis Cuxhaven - Küste":"045",
"Kreis Dachau":"414",
"Kreis Dahme-Spreewald":"172",
"Kreis Deggendorf":"117",
"Kreis Diepholz":"310",
"Kreis Dillingen a.d. Donau":"354",
"Kreis Dingolfing-Landau":"251",
"Kreis Dithmarschen - Binnenland":"081",
"Kreis Dithmarschen - Küste":"091",
"Kreis Donau-Ries":"147",
"Kreis Düren":"314",
"Kreis Ebersberg":"260",
"Kreis Eichsfeld":"406",
"Kreis Eichstätt":"303",
"Kreis Elbe-Elster":"261",
"Kreis Emmendingen":"227",
"Kreis Emsland":"376",
"Kreis Erding":"339",
"Kreis Erlangen-Höchstadt":"196",
"Kreis Esslingen":"302",
"Kreis Euskirchen":"127",
"Kreis Forchheim":"191",
"Kreis Freising":"374",
"Kreis Freudenstadt":"404",
"Kreis Freyung-Grafenau":"380",
"Kreis Friesland - Binnenland":"065",
"Kreis Friesland - Küste":"104",
"Kreis Fulda":"248",
"Kreis Fürstenfeldbruck":"379",
"Kreis Garmisch-Partenkirchen":"195",
"Kreis Germersheim":"153",
"Kreis Gießen":"185",
"Kreis Gifhorn":"244",
"Kreis Göppingen":"215",
"Kreis Görlitz - Bergland":"070",
"Kreis Görlitz - Tiefland":"075",
"Kreis Goslar":"328",
"Kreis Gotha":"193",
"Kreis Göttingen":"151",
"Kreis Grafschaft Bentheim":"237",
"Kreis Greiz":"352",
"Kreis Groß-Gerau":"166",
"Kreis Günzburg":"388",
"Kreis Gütersloh":"119",
"Kreis Hameln-Pyrmont":"111",
"Kreis Hamm":"159",
"Kreis Harburg":"170",
"Kreis Harz - Bergland":"093",
"Kreis Harz - Tiefland":"048",
"Kreis Haßberge":"335",
"Kreis Havelland":"382",
"Kreis Heidenheim":"311",
"Kreis Heinsberg":"157",
"Kreis Helmstedt":"415",
"Kreis Herford":"365",
"Kreis Hersfeld-Rotenburg":"217",
"Kreis Herzogtum Lauenburg":"236",
"Kreis Hildburghausen":"305",
"Kreis Hildesheim":"384",
"Kreis Holzminden":"176",
"Kreis Höxter":"327",
"Kreis Jerichower Land":"141",
"Kreis Kelheim":"165",
"Kreis Kitzingen":"399",
"Kreis Kleve":"283",
"Kreis Konstanz":"419",
"Kreis Kronach":"296",
"Kreis Kulmbach":"245",
"Kreis Kusel":"160",
"Kreis Landsberg am Lech":"130",
"Kreis Leer":"069",
"Kreis Leipzig":"179",
"Kreis Lichtenfels":"178",
"Kreis Limburg-Weilburg":"341",
"Kreis Lindau":"280",
"Kreis Lippe":"407",
"Kreis Lörrach":"312",
"Kreis Lüchow-Dannenberg":"122",
"Kreis Ludwigsburg":"241",
"Kreis Ludwigslust-Parchim - Ost":"076",
"Kreis Ludwigslust-Parchim - West":"107",
"Kreis Lüneburg":"383",
"Kreis Main-Spessart":"304",
"Kreis Mainz-Bingen / Mainz":"097",
"Kreis Mansfeld-Südharz":"180",
"Kreis Marburg-Biedenkopf":"362",
"Kreis Märkisch-Oderland":"233",
"Kreis Mayen-Koblenz":"351",
"Kreis Meißen":"416",
"Kreis Merzig-Wadern":"137",
"Kreis Mettmann":"250",
"Kreis Miesbach":"293",
"Kreis Miltenberg":"266",
"Kreis Minden-Lübbecke":"131",
"Kreis Mittelsachsen - Bergland":"099",
"Kreis Mittelsachsen - Tiefland":"094",
"Kreis Mühldorf a. Inn":"332",
"Kreis Neu-Ulm":"348",
"Kreis Neuburg-Schrobenhausen":"402",
"Kreis Neumarkt i.d. OPf.":"219",
"Kreis Neunkirchen":"274",
"Kreis Neustadt a.d. Waldnaab":"321",
"Kreis Neuwied":"270",
"Kreis Nienburg":"298",
"Kreis Nordfriesland - Binnenland":"106",
"Kreis Nordfriesland - Küste":"095",
"Kreis Nordhausen":"373",
"Kreis Nordsachsen - Nord":"028",
"Kreis Nordsachsen - Süd":"071",
"Kreis Northeim":"294",
"Kreis Nürnberger Land":"358",
"Kreis Oberallgäu":"330",
"Kreis Oberhavel":"322",
"Kreis Oberspreewald-Lausitz":"140",
"Kreis Oder-Spree":"242",
"Kreis Olpe":"229",
"Kreis Ostallgäu":"239",
"Kreis Osterholz":"209",
"Kreis Osterode am Harz":"326",
"Kreis Ostholstein - Binnenland":"073",
"Kreis Ostholstein - Küste":"061",
"Kreis Ostprignitz-Ruppin":"313",
"Kreis Paderborn":"324",
"Kreis Peine":"257",
"Kreis Pfaffenhofen a.d. Ilm":"420",
"Kreis Pinneberg":"058",
"Kreis Plön - Binnenland":"088",
"Kreis Plön - Küste":"037",
"Kreis Potsdam-Mittelmark":"187",
"Kreis Prignitz":"247",
"Kreis Rastatt":"146",
"Kreis Ravensburg":"344",
"Kreis Recklinghausen":"224",
"Kreis Regen":"391",
"Kreis Reutlingen":"276",
"Kreis Rhön-Grabfeld":"121",
"Kreis Rostock - Binnenland Nord":"036",
"Kreis Rostock - Binnenland Süd":"027",
"Kreis Rostock - Küste":"055",
"Kreis Rotenburg (Wümme)":"142",
"Kreis Roth":"338",
"Kreis Rottal-Inn":"421",
"Kreis Rottweil":"285",
"Kreis Saalfeld-Rudolstadt":"115",
"Kreis Saarlouis":"240",
"Kreis Schaumburg":"225",
"Kreis Schmalkalden-Meiningen":"203",
"Kreis Schwäbisch Hall":"340",
"Kreis Schwandorf":"112",
"Kreis Segeberg":"181",
"Kreis Siegen-Wittgenstein":"269",
"Kreis Sigmaringen":"320",
"Kreis Soest":"155",
"Kreis Sömmerda":"323",
"Kreis Sonneberg":"206",
"Kreis Spree-Neiße":"129",
"Kreis St. Wendel":"136",
"Kreis Stade":"222",
"Kreis Starnberg":"267",
"Kreis Steinburg":"158",
"Kreis Steinfurt":"273",
"Kreis Stendal":"325",
"Kreis Stormarn":"400",
"Kreis Südliche Weinstraße":"405",
"Kreis Südwestpfalz / Pirmasens":"098",
"Kreis Teltow-Fläming":"345",
"Kreis Tirschenreuth":"398",
"Kreis Traunstein":"288",
"Kreis Trier-Saarburg / Trier":"051",
"Kreis Tübingen":"301",
"Kreis Tuttlingen":"175",
"Kreis Uckermark":"144",
"Kreis Uelzen":"350",
"Kreis und Stadt Ansbach":"078",
"Kreis und Stadt Aschaffenburg":"057",
"Kreis und Stadt Augsburg":"096",
"Kreis und Stadt Bamberg":"046",
"Kreis und Stadt Bayreuth":"042",
"Kreis und Stadt Coburg":"087",
"Kreis und Stadt Fürth":"020",
"Kreis und Stadt Heilbronn":"080",
"Kreis und Stadt Hof":"089",
"Kreis und Stadt Kaiserslautern":"084",
"Kreis und Stadt Karlsruhe":"109",
"Kreis und Stadt Kassel":"026",
"Kreis und Stadt Landshut":"021",
"Kreis und Stadt München":"056",
"Kreis und Stadt Offenbach":"041",
"Kreis und Stadt Oldenburg":"079",
"Kreis und Stadt Osnabrück":"024",
"Kreis und Stadt Passau":"066",
"Kreis und Stadt Regensburg":"049",
"Kreis und Stadt Rosenheim":"029",
"Kreis und Stadt Schweinfurt":"105",
"Kreis und Stadt Würzburg":"077",
"Kreis Unna":"235",
"Kreis Unterallgäu":"249",
"Kreis Vechta":"188",
"Kreis Verden":"393",
"Kreis Viersen":"113",
"Kreis Vulkaneifel":"356",
"Kreis Waldeck-Frankenberg":"218",
"Kreis Waldshut":"281",
"Kreis Warendorf":"171",
"Kreis Weilheim-Schongau":"342",
"Kreis Weimarer Land":"194",
"Kreis Weißenburg-Gunzenhausen":"410",
"Kreis Wesel":"253",
"Kreis Wesermarsch - Binnenland":"064",
"Kreis Wesermarsch - Küste":"101",
"Kreis Wittenberg":"263",
"Kreis Wittmund - Binnenland":"053",
"Kreis Wittmund - Küste":"083",
"Kreis Wolfenbüttel":"220",
"Kreis Wunsiedel":"213",
"Kreis Zwickau - Bergland":"044",
"Kreis Zwickau - Tiefland":"040",
"Kyffhäuserkreis":"262",
"Lahn-Dill-Kreis":"395",
"Main-Kinzig-Kreis":"118",
"Main-Tauber-Kreis":"308",
"Main-Taunus-Kreis":"412",
"Märkischer Kreis":"389",
"Mecklenburg. Seenplatte - Mitte":"025",
"Mecklenburg. Seenplatte - Südost":"082",
"Mecklenburg. Seenplatte - West":"059",
"Neckar-Odenwald-Kreis":"290",
"Neustadt/Aisch - Bad Windsheim":"372",
"Nordfriesische Küste":"801",
"Nordwestmecklenburg - Binnenland":"085",
"Nordwestmecklenburg - Küste":"033",
"Oberbergischer Kreis":"243",
"Odenwaldkreis":"360",
"Ortenaukreis":"329",
"Ostalbkreis":"346",
"Ostfriesische Küste":"802",
"Östlich Fehmarn bis Rügen":"806",
"Östlich Rügen":"807",
"Region Hannover":"169",
"Regionalverband Saarbrücken":"189",
"Rems-Murr-Kreis":"284",
"Rendsburg-Eckernförde - Binnenl.":"031",
"Rendsburg-Eckernförde - Küste":"067",
"Rhein-Erft-Kreis":"367",
"Rhein-Hunsrück-Kreis":"292",
"Rhein-Kreis Neuss":"164",
"Rhein-Lahn-Kreis":"300",
"Rhein-Neckar-Kreis / Heidelberg":"110",
"Rhein-Pfalz-Kreis / Ludwigshafen":"068",
"Rhein-Sieg-Kreis":"198",
"Rheingau-Taunus-Kreis":"268",
"Rheinisch-Bergischer Kreis":"366",
"Saale-Holzland-Kreis":"386",
"Saale-Orla-Kreis":"318",
"Saalekreis":"204",
"Saarpfalz-Kreis":"238",
"Sächs. Schweiz-Osterzgeb.-ö. Bgl":"063",
"Sächs. Schweiz-Osterzgeb.-Tiefl.":"038",
"Sächs. Schweiz-Osterzgeb.-w. Bgl":"092",
"Salzlandkreis":"228",
"Schleswig-Flensburg - Binnenland":"062",
"Schleswig-Flensburg - Küste":"060",
"Schwalm-Eder-Kreis":"177",
"Schwarzwald-Baar-Kreis":"408",
"Stadt Amberg":"205",
"Stadt Baden-Baden":"347",
"Stadt Berlin":"202",
"Stadt Bielefeld":"378",
"Stadt Bochum":"396",
"Stadt Bottrop":"295",
"Stadt Brandenburg":"392",
"Stadt Braunschweig":"275",
"Stadt Bremerhaven":"173",
"Stadt Chemnitz":"297",
"Stadt Cottbus":"394",
"Stadt Delmenhorst":"337",
"Stadt Dessau-Roßlau":"259",
"Stadt Dortmund":"230",
"Stadt Dresden":"363",
"Stadt Duisburg":"336",
"Stadt Düsseldorf":"128",
"Stadt Eisenach":"286",
"Stadt Emden":"154",
"Stadt Erfurt":"359",
"Stadt Erlangen":"139",
"Stadt Essen":"364",
"Stadt Flensburg":"156",
"Stadt Frankenthal":"370",
"Stadt Frankfurt (Oder)":"272",
"Stadt Frankfurt am Main":"133",
"Stadt Gelsenkirchen":"161",
"Stadt Gera":"162",
"Stadt Hagen":"291",
"Stadt Halle (Saale)":"135",
"Stadt Herne":"211",
"Stadt Ingolstadt":"282",
"Stadt Jena":"417",
"Stadt Kaufbeuren":"120",
"Stadt Kempten (Allgäu)":"381",
"Stadt Kiel":"418",
"Stadt Koblenz":"277",
"Stadt Köln":"299",
"Stadt Krefeld":"377",
"Stadt Landau in der Pfalz":"368",
"Stadt Leipzig":"126",
"Stadt Leverkusen":"256",
"Stadt Magdeburg":"278",
"Stadt Mannheim":"184",
"Stadt Memmingen":"174",
"Stadt Mönchengladbach":"114",
"Stadt Mülheim an der Ruhr":"132",
"Stadt Münster":"167",
"Stadt Neumünster":"192",
"Stadt Neustadt an der Weinstraße":"210",
"Stadt Nürnberg":"150",
"Stadt Oberhausen":"401",
"Stadt Potsdam":"385",
"Stadt Remscheid":"252",
"Stadt Salzgitter":"334",
"Stadt Schwabach":"246",
"Stadt Schwerin":"331",
"Stadt Solingen":"186",
"Stadt Speyer":"287",
"Stadt Stuttgart":"226",
"Stadt Suhl":"208",
"Stadt Weiden in der Oberpfalz":"316",
"Stadt Weimar":"307",
"Stadt Wiesbaden":"403",
"Stadt Wilhelmshaven":"124",
"Stadt Wolfsburg":"319",
"Stadt Worms":"333",
"Stadt Wuppertal":"207",
"Stadt Zweibrücken":"349",
"StädteRegion Aachen":"258",
"Straubing-Bogen / Straubing":"043",
"Unstrut-Hainich-Kreis":"123",
"Vogelsbergkreis":"315",
"Vogtlandkreis - Bergland":"023",
"Vogtlandkreis - Tiefland":"108",
"Vorpommern-Greifsw. - Binnenl. N":"022",
"Vorpommern-Greifsw. - Binnenl. S":"034",
"Vorpommern-Greifsw. - Küste Nord":"072",
"Vorpommern-Greifsw. - Küste Süd":"100",
"Vorpommern-Rügen - Binnenland":"090",
"Vorpommern-Rügen - Insel Rügen":"052",
"Vorpommern-Rügen - Küste":"032",
"Wartburgkreis":"149",
"Werra-Meissner-Kreis":"279",
"Westerwaldkreis":"148",
"Wetteraukreis":"231",
"Zollernalbkreis":"168",
    },
    "DK": {},
    "EE": {},
    "ES": {
"A Mariña":"206",
"Albarracín y Jiloca":"102",
"Alcaraz y Segura":"162",
"Alcarria conquense":"168",
"Alcarria de Guadalajara":"173",
"Altiplano de Murcia":"221",
"Ampurdán":"184",
"Andévalo y Condado":"086",
"Antequera":"092",
"Aracena":"085",
"Área metropolitana de Tenerife":"131",
"Axarquía":"095",
"Bajo Aragón de Teruel":"104",
"Barros y Serena":"196",
"Bierzo de León":"146",
"Bizkaia interior":"236",
"Bizkaia litoral":"235",
"Campiña cordobesa":"079",
"Campiña gaditana":"075",
"Campiña sevillana":"097",
"Campo de Cartagena y Mazarrón":"225",
"Cantabria del Ebro":"136",
"Capital y Montes de Jaén":"091",
"Cazorla y Segura":"089",
"Central y Valles Mineros":"111",
"Centro de Huesca":"100",
"Centro de Lugo":"207",
"Centro de Navarra":"227",
"Centro y valle de Villaverde":"135",
"Ceuta":"250",
"Cinco Villas de Zaragoza":"105",
"Condado de Treviño":"142",
"Cordillera Cantábrica de Burgos":"140",
"Cordillera Cantábrica de León":"145",
"Cordillera Cantábrica de Palencia":"148",
"Cordillera y Picos de Europa":"112",
"Costa - A Mariña":"845",
"Costa - Ampurdán":"890",
"Costa - Área metropolitana de Tenerife":"884",
"Costa - Axarquía":"855",
"Costa - Bizkaia litoral":"841",
"Costa - Campo de Cartagena y Mazarrón":"860",
"Costa - Ceuta":"871",
"Costa - Costa granadina":"856",
"Costa - El Hierro":"879",
"Costa - Este de La Palma":"881",
"Costa - Este, sur y oeste de Gran Canaria":"886",
"Costa - Este, sur y oeste de Tenerife":"885",
"Costa - Estrecho":"853",
"Costa - Fuerteventura":"888",
"Costa - Gipuzkoa litoral":"840",
"Costa - Ibiza y Formentera":"873",
"Costa - La Gomera":"882",
"Costa - Lanzarote":"889",
"Costa - Levante almeriense":"858",
"Costa - Levante mallorquín":"877",
"Costa - Litoral cántabro":"842",
"Costa - Litoral de Barcelona":"869",
"Costa - Litoral de Huelva":"851",
"Costa - Litoral gaditano":"852",
"Costa - Litoral norte de Alicante":"862",
"Costa - Litoral norte de Castellón":"866",
"Costa - Litoral norte de Tarragona":"868",
"Costa - Litoral norte de Valencia":"864",
"Costa - Litoral occidental asturiano":"844",
"Costa - Litoral oriental asturiano":"843",
"Costa - Litoral sur de Alicante":"861",
"Costa - Litoral sur de Castellón":"865",
"Costa - Litoral sur de Girona":"870",
"Costa - Litoral sur de Tarragona":"867",
"Costa - Litoral sur de Valencia":"863",
"Costa - Melilla":"872",
"Costa - Menorca":"878",
"Costa - Miño de Pontevedra":"850",
"Costa - Noroeste de A Coruña":"846",
"Costa - Norte de Gran Canaria":"887",
"Costa - Norte de Tenerife":"883",
"Costa - Norte y nordeste de Mallorca":"876",
"Costa - Oeste de A Coruña":"847",
"Costa - Oeste de La Palma":"880",
"Costa - Poniente y Almería Capital":"857",
"Costa - Rias Baixas":"849",
"Costa - Sierra Tramontana":"875",
"Costa - Sol y Guadalhorce":"854",
"Costa - Sur de Mallorca":"874",
"Costa - Suroeste de A Coruña":"848",
"Costa granadina":"084",
"Costa Valle Guadalentín Lorca Águilas":"859",
"Cuenca del Genil":"081",
"Cuenca del Nervión":"230",
"Cumbres de Gran Canaria":"121",
"Cumbres de La Palma":"125",
"Depresión central de Barcelona":"179",
"Depresión central de Lleida":"188",
"Depresión central de Tarragona":"189",
"El Hierro":"129",
"Este de La Palma":"126",
"Este, sur y oeste de Gran Canaria":"122",
"Este, sur y oeste de Tenerife":"132",
"Estrecho":"077",
"Fuerteventura":"124",
"Gipuzkoa interior":"234",
"Gipuzkoa litoral":"233",
"Grazalema":"074",
"Guadix y Baza":"082",
"Gúdar y Maestrazgo":"103",
"Hellín y Almansa":"163",
"Ibérica de Burgos":"144",
"Ibérica de Soria":"155",
"Ibérica riojana":"238",
"Ibérica zaragozana":"106",
"Ibiza y Formentera":"113",
"Interior de A Coruña":"204",
"Interior de Alicante":"240",
"Interior de Mallorca":"116",
"Interior de Pontevedra":"216",
"Interior norte de Castellón":"242",
"Interior norte de Valencia":"246",
"Interior sur de Castellón":"244",
"Interior sur de Valencia":"248",
"La Gomera":"128",
"La Mancha albaceteña":"161",
"La Mancha conquense":"170",
"La Mancha de Ciudad Real":"165",
"La Mancha toledana":"177",
"La Siberia extremeña":"195",
"Lanzarote":"123",
"Levante almeriense":"073",
"Levante mallorquín":"118",
"Liébana":"134",
"Litoral cántabro":"133",
"Litoral de Barcelona":"181",
"Litoral de Huelva":"087",
"Litoral gaditano":"076",
"Litoral norte de Alicante":"239",
"Litoral norte de Castellón":"243",
"Litoral norte de Tarragona":"191",
"Litoral norte de Valencia":"247",
"Litoral occidental asturiano":"108",
"Litoral oriental asturiano":"109",
"Litoral sur de Alicante":"241",
"Litoral sur de Castellón":"245",
"Litoral sur de Girona":"185",
"Litoral sur de Tarragona":"192",
"Litoral sur de Valencia":"249",
"Llanada alavesa":"231",
"Melilla":"251",
"Menorca":"119",
"Meseta cacereña":"200",
"Meseta de Ávila":"137",
"Meseta de Burgos":"143",
"Meseta de León":"147",
"Meseta de Palencia":"149",
"Meseta de Salamanca":"150",
"Meseta de Segovia":"153",
"Meseta de Soria":"156",
"Meseta de Valladolid":"158",
"Meseta de Zamora":"160",
"Metropolitana y Henares":"219",
"Miño de Ourense":"211",
"Miño de Pontevedra":"217",
"Montaña de Lugo":"208",
"Montaña de Ourense":"213",
"Montes de Toledo":"176",
"Montes del norte y Anchuras":"164",
"Morena y Condado":"088",
"Nacimiento y Campo de Tabernas":"071",
"Nevada y Alpujarras":"083",
"Noroeste de A Coruña":"202",
"Noroeste de Murcia":"222",
"Noroeste de Ourense":"210",
"Norte de Burgos":"141",
"Norte de Cáceres":"198",
"Norte de Gran Canaria":"120",
"Norte de Tenerife":"130",
"Norte y nordeste de Mallorca":"115",
"Oeste de A Coruña":"203",
"Oeste de La Palma":"127",
"Parameras de Molina":"172",
"Pirineo de Girona":"182",
"Pirineo de Lleida":"187",
"Pirineo navarro":"228",
"Pirineo oscense":"099",
"Poniente y Almería Capital":"072",
"Prelitoral de Barcelona":"180",
"Prelitoral de Girona":"183",
"Prelitoral norte de Tarragona":"190",
"Prelitoral sur de Tarragona":"193",
"Prepirineo de Barcelona":"178",
"Rias Baixas":"215",
"Ribera del Ebro de La Rioja":"237",
"Ribera del Ebro de Navarra":"229",
"Ribera del Ebro de Zaragoza":"107",
"Rioja alavesa":"232",
"Ronda":"093",
"Sanabria":"159",
"Serranía de Cuenca":"169",
"Serranía de Guadalajara":"171",
"Sierra de Madrid":"218",
"Sierra de San Vicente":"174",
"Sierra norte de Sevilla":"096",
"Sierra sur de Sevilla":"098",
"Sierra Tramontana":"114",
"Sierra y Pedroches":"078",
"Sierras de Alcudia y Madrona":"167",
"Sistema Central de Ávila":"138",
"Sistema Central de Salamanca":"151",
"Sistema Central de Segovia":"154",
"Sistema Central de Soria":"157",
"Sol y Guadalhorce":"094",
"Subbética cordobesa":"080",
"Sur de Ávila":"139",
"Sur de Badajoz":"197",
"Sur de Huesca":"101",
"Sur de Lugo":"209",
"Sur de Mallorca":"117",
"Sur de Ourense":"212",
"Sur de Salamanca":"152",
"Sur, Vegas y Oeste":"220",
"Suroccidental asturiana":"110",
"Suroeste de A Coruña":"205",
"Tajo y Alagón":"199",
"Valdeorras":"214",
"Valle de Arán":"186",
"Valle del Almanzora y Los Vélez":"070",
"Valle del Guadalentín, Lorca y Águilas":"224",
"Valle del Guadalquivir de Jaén":"090",
"Valle del Guadiana":"166",
"Valle del Tajo":"175",
"Vega del Segura":"223",
"Vegas del Guadiana":"194",
"Vertiente cantábrica de Navarra":"226",
"Villuercas y Montánchez":"201",
},
    "FI": {},
    "FR": {
"Ain":"039",
"Aisne":"073",
"Allier":"043",
"Alpes de Haute Provence":"032",
"Alpes Maritimes":"029",
"Andorre":"001",
"Ardèche":"026",
"Ardennes":"074",
"Ariège":"008",
"Aube":"075",
"Aude":"007",
"Aveyron":"021",
"Bas Rhin":"086",
"Bouches du Rhône":"027",
"Calvados":"052",
"Cantal":"024",
"Charente":"016",
"Charente Maritime":"015",
"Cher":"059",
"Corrèze":"018",
"Corse du Sud":"090",
"Côte d'Or":"078",
"Côtes d'Armor":"047",
"Creuse":"041",
"Deux Sèvres":"094",
"Dordogne":"017",
"Doubs":"080",
"Drôme":"031",
"Essonne":"066",
"Eure":"056",
"Eure et Loir":"063",
"Finistère":"046",
"Gard":"022",
"Gers":"005",
"Gironde":"014",
"Haut Rhin":"083",
"Haute Corse":"089",
"Haute Garonne":"009",
"Haute Loire":"025",
"Haute Marne":"085",
"Haute Saône":"082",
"Haute Savoie":"035",
"Haute Vienne":"019",
"Hautes Alpes":"033",
"Hautes Pyrénées":"003",
"Hérault":"020",
"Ille et Vilaine":"050",
"Indre":"042",
"Indre et Loire":"093",
"Isère":"034",
"Jura":"079",
"Landes":"004",
"Loir et Cher":"058",
"Loire":"037",
"Loire Atlantique":"049",
"Loiret":"061",
"Lot":"013",
"Lot et Garonne":"012",
"Lozère":"023",
"Maine et Loire":"092",
"Manche":"051",
"Marne":"076",
"Mayenne":"053",
"Meurthe et Moselle":"088",
"Meuse":"002",
"Morbihan":"048",
"Moselle":"087",
"Nièvre":"060",
"Nord":"070",
"Oise":"072",
"Orne":"054",
"Paris et Petite Couronne":"067",
"Pas de Calais":"069",
"Puy de Dôme":"040",
"Pyrénées Atlantiques":"091",
"Pyrénées Orientales":"006",
"Rhône":"038",
"Saône et Loire":"077",
"Sarthe":"057",
"Savoie":"036",
"Seine et Marne":"068",
"Seine Maritime":"055",
"Somme":"071",
"Tarn":"011",
"Tarn et Garonne":"010",
"Territoire de Belfort":"081",
"Val d'Oise":"065",
"Var":"028",
"Vaucluse":"030",
"Vendée":"044",
"Vienne":"045",
"Vosges":"084",
"Yonne":"062",
"Yvelines":"064",
},
    "GR": {},
    "HR": {},
    "HU": {},
    "IE": {},
    "IL": {},
    "IS": {},
    "IT": {
"Abruzzo":"013",
"Basilicata":"017",
"Calabria":"001",
"Campania":"016",
"Emilia e Romagna":"008",
"Friuli VeneziaGiulia":"020",
"Lazio":"012",
"Liguria":"007",
"Lombardia":"003",
"Marche":"011",
"Molise":"014",
"Piemonte":"005",
"Puglia":"015",
"Sardegna":"019",
"Sicilia":"018",
"Toscana":"009",
"Trentino Alto Adige":"002",
"Umbria":"010",
"Valle d'Aosta":"004",
"Veneto":"006",
},
    "LT": {},
    "LU": {},
    "LV": {},
    "MD": {},
    "ME": {},
    "MK": {},
    "MT": {},
    "NL": {},
    "NO": {},
    "PL": {
"Aleksandrowski":"0401",
"Augustowski":"2001",
"Bartoszycki":"2801",
"Będziński":"2401",
"Bełchatowski":"1001",
"Bialski":"0601",
"Biała Podlaska":"0661",
"Białobrzeski":"1401",
"Białogardzki":"3201",
"Białostocki":"2002",
"Białystok":"2061",
"Bielski":"2003",
"Bielski":"2402",
"Bielsko-Biała":"2461",
"Bieruńsko-Lędziński":"2414",
"Bieszczadzki":"1801",
"Biłgorajski":"0602",
"Bocheński":"1201",
"Bolesławiecki":"0201",
"Braniewski":"2802",
"Brodnicki":"0402",
"Brzeski":"1202",
"Brzeski":"1601",
"Brzeziński":"1021",
"Brzozowski":"1802",
"Buski":"2601",
"Bydgoski":"0403",
"Bydgoszcz":"0461",
"Bytom":"2462",
"Bytowski":"2201",
"Central coastal zone":"804",
"Chełm":"0662",
"Chełmiński":"0404",
"Chełmski":"0603",
"Chodzieski":"3001",
"Chojnicki":"2202",
"Chorzów":"2463",
"Choszczeński":"3202",
"Chrzanowski":"1203",
"Ciechanowski":"1402",
"Cieszyński":"2403",
"Czarnkowsko-Trzcianecki":"3002",
"Częstochowa":"2464",
"Częstochowski":"2404",
"Człuchowski":"2203",
"Dąbrowa Górnicza":"2465",
"Dąbrowski":"1204",
"Dębicki":"1803",
"Drawski":"3203",
"Działdowski":"2803",
"Dzierżoniowski":"0202",
"Eastern coastal zone":"805",
"Elbląg":"2861",
"Elbląski":"2804",
"Ełcki":"2805",
"Garwoliński":"1403",
"Gdańsk":"2261",
"Gdański":"2204",
"Gdynia":"2262",
"Giżycki":"2806",
"Gliwice":"2466",
"Gliwicki":"2405",
"Gnieźnieński":"3003",
"Goleniowski":"3204",
"Golubsko-Dobrzyński":"0405",
"Gorlicki":"1205",
"Górowski":"0204",
"Gorzów Wielkopolski":"0861",
"Gorzowski":"0801",
"Gostyniński":"1404",
"Gostyński":"3004",
"Gołdapski":"2818",
"Grajewski":"2004",
"Grodziski":"3005",
"Grodziski":"1405",
"Grójecki":"1406",
"Grudziądz":"0462",
"Grudziądzki":"0406",
"Gryficki":"3205",
"Gryfiński":"3206",
"Głogowski":"0203",
"Głubczycki":"1602",
"Hajnowski":"2005",
"Hrubieszowski":"0604",
"Inowrocławski":"0407",
"Iławski":"2807",
"Janowski":"0605",
"Jarociński":"3006",
"Jarosławski":"1804",
"Jasielski":"1805",
"Jastrzębie-Zdrój":"2467",
"Jaworski":"0205",
"Jaworzno":"2468",
"Jędrzejowski":"2602",
"Jelenia Góra":"0261",
"Jeleniogórski":"0206",
"Kaliski":"3007",
"Kalisz":"3061",
"Kamiennogórski":"0207",
"Kamieński":"3207",
"Kartuski":"2205",
"Katowice":"2469",
"Kazimierski":"2603",
"Kędzierzyńsko-Kozielski":"1603",
"Kępiński":"3008",
"Kętrzyński":"2808",
"Kielce":"2661",
"Kielecki":"2604",
"Kluczborski":"1604",
"Kolbuszowski":"1806",
"Kolneński":"2006",
"Kolski":"3009",
"Konecki":"2605",
"Konin":"3062",
"Koniński":"3010",
"Kościański":"3011",
"Kościerski":"2206",
"Koszalin":"3261",
"Koszaliński":"3209",
"Kozienicki":"1407",
"Kołobrzeski":"3208",
"Kraków":"1261",
"Krakowski":"1206",
"Krapkowicki":"1605",
"Kraśnicki":"0607",
"Krasnostawski":"0606",
"Krośnieński":"0802",
"Krośnieński":"1807",
"Krosno":"1861",
"Krotoszyński":"3012",
"Kutnowski":"1002",
"Kwidzyński":"2207",
"Kłobucki":"2406",
"Kłodzki":"0208",
"Lęborski":"2208",
"Legionowski":"1408",
"Legnica":"0262",
"Legnicki":"0209",
"Leski":"1821",
"Leszczyński":"3013",
"Leszno":"3063",
"Leżajski":"1808",
"Lidzbarski":"2809",
"Limanowski":"1207",
"Lipnowski":"0408",
"Lipski":"1409",
"Lubaczowski":"1809",
"Lubański":"0210",
"Lubartowski":"0608",
"Lubelski":"0609",
"Lubiński":"0211",
"Lublin":"0663",
"Lubliniecki":"2407",
"Lwówecki":"0212",
"Makowski":"1411",
"Malborski":"2209",
"Miechowski":"1208",
"Międzychodzki":"3014",
"Międzyrzecki":"0803",
"Mielecki":"1811",
"Mikołowski":"2408",
"Milicki":"0213",
"Miński":"1412",
"Mogileński":"0409",
"Moniecki":"2008",
"Mrągowski":"2810",
"Myślenicki":"1209",
"Myśliborski":"3210",
"Myszkowski":"2409",
"Mysłowice":"2470",
"Mławski":"1413",
"Nakielski":"0410",
"Namysłowski":"1606",
"Nidzicki":"2811",
"Niżański":"1812",
"Nowodworski":"1414",
"Nowodworski":"2210",
"Nowomiejski":"2812",
"Nowosądecki":"1210",
"Nowosolski":"0804",
"Nowotarski":"1211",
"Nowotomyski":"3015",
"Nowy Sącz":"1262",
"Nyski":"1607",
"Obornicki":"3016",
"Olecki":"2813",
"Oleski":"1608",
"Oleśnicki":"0214",
"Olkuski":"1212",
"Olsztyn":"2862",
"Olsztyński":"2814",
"Opatowski":"2606",
"Opoczyński":"1007",
"Opole":"1661",
"Opolski":"0612",
"Opolski":"1609",
"Ostródzki":"2815",
"Ostrowiecki":"2607",
"Ostrowski":"3017",
"Ostrowski":"1416",
"Ostrołęcki":"1415",
"Ostrołęka":"1461",
"Ostrzeszowski":"3018",
"Oświęcimski":"1213",
"Otwocki":"1417",
"Oławski":"0215",
"Pabianicki":"1008",
"Pajęczański":"1009",
"Parczewski":"0613",
"Piaseczyński":"1418",
"Piekary Śląskie":"2471",
"Pilski":"3019",
"Pińczowski":"2608",
"Piotrków Trybunalski":"1062",
"Piotrkowski":"1010",
"Piski":"2816",
"Pleszewski":"3020",
"Poddębicki":"1011",
"Policki":"3211",
"Polkowicki":"0216",
"Poznań":"3064",
"Poznański":"3021",
"Proszowicki":"1214",
"Prudnicki":"1610",
"Pruszkowski":"1421",
"Przasnyski":"1422",
"Przemyski":"1813",
"Przemyśl":"1862",
"Przeworski":"1814",
"Przysuski":"1423",
"Pszczyński":"2410",
"Pucki":"2211",
"Puławski":"0614",
"Pułtuski":"1424",
"Pyrzycki":"3212",
"Płock":"1462",
"Płocki":"1419",
"Płoński":"1420",
"Raciborski":"2411",
"Radom":"1463",
"Radomski":"1425",
"Radomszczański":"1012",
"Radziejowski":"0411",
"Radzyński":"0615",
"Rawicki":"3022",
"Rawski":"1013",
"Ropczycko-Sędziszowski":"1815",
"Ruda Śląska":"2472",
"Rybnicki":"2412",
"Rybnik":"2473",
"Rycki":"0616",
"Rypiński":"0412",
"Rzeszów":"1863",
"Rzeszowski":"1816",
"Sandomierski":"2609",
"Sanocki":"1817",
"Sejneński":"2009",
"Sępoleński":"0413",
"Siedlce":"1464",
"Siedlecki":"1426",
"Siemianowice Śląskie":"2474",
"Siemiatycki":"2010",
"Sieradzki":"1014",
"Sierpecki":"1427",
"Skarżyski":"2610",
"Skierniewice":"1063",
"Skierniewicki":"1015",
"Sochaczewski":"1428",
"Sokólski":"2011",
"Sokołowski":"1429",
"Sopot":"2264",
"Sosnowiec":"2475",
"Średzki":"3025",
"Średzki":"0218",
"Śremski":"3026",
"Stalowowolski":"1818",
"Starachowicki":"2611",
"Stargardzki":"3214",
"Starogardzki":"2213",
"Staszowski":"2612",
"Strefa Brzegowa Wschodnia":"801",
"Strefa Brzegowa Zachodnia":"802",
"Strzelecki":"1611",
"Strzelecko-Drezdenecki":"0806",
"Strzeliński":"0217",
"Strzyżowski":"1819",
"Sulęciński":"0807",
"Suski":"1215",
"Suwalski":"2012",
"Suwałki":"2063",
"Świdnicki":"0617",
"Świdnicki":"0219",
"Świdwiński":"3216",
"Świebodziński":"0808",
"Świecki":"0414",
"Świętochłowice":"2476",
"Świnoujście":"3263",
"Szamotulski":"3024",
"Szczecin":"3262",
"Szczecinecki":"3215",
"Szczycieński":"2817",
"Sztumski":"2216",
"Szydłowiecki":"1430",
"Sławieński":"3213",
"Słubicki":"0805",
"Słupecki":"3023",
"Słupsk":"2263",
"Słupski":"2212",
"Tarnobrzeg":"1864",
"Tarnobrzeski":"1820",
"Tarnogórski":"2413",
"Tarnów":"1263",
"Tarnowski":"1216",
"Tatrzański":"1217",
"Tczewski":"2214",
"Tomaszowski":"1016",
"Tomaszowski":"0618",
"Toruń":"0463",
"Toruński":"0415",
"Trzebnicki":"0220",
"Tucholski":"0416",
"Turecki":"3027",
"Tychy":"2477",
"Wąbrzeski":"0417",
"Wadowicki":"1218",
"Wągrowiecki":"3028",
"Warszawa":"1465",
"Warszawski Zachodni":"1432",
"Wałbrzych":"0265",
"Wałbrzyski":"0221",
"Wałecki":"3217",
"Węgorzewski":"2819",
"Węgrowski":"1433",
"Wejherowski":"2215",
"Western coastal zone":"803",
"Wielicki":"1219",
"Wieluński":"1017",
"Wieruszowski":"1018",
"Wodzisławski":"2415",
"Wolsztyński":"3029",
"Wołomiński":"1434",
"Wołowski":"0222",
"Wrocław":"0264",
"Wrocławski":"0223",
"Wrzesiński":"3030",
"Wschowski":"0812",
"Wysokomazowiecki":"2013",
"Wyszkowski":"1435",
"Włocławek":"0464",
"Włocławski":"0418",
"Włodawski":"0619",
"Włoszczowski":"2613",
"Ząbkowicki":"0224",
"Zabrze":"2478",
"Żagański":"0810",
"Zambrowski":"2014",
"Zamojski":"0620",
"Zamość":"0664",
"Żarski":"0811",
"Zawierciański":"2416",
"Zduńskowolski":"1019",
"Zgierski":"1020",
"Zgorzelecki":"0225",
"Zielona Góra":"0862",
"Zielonogórski":"0809",
"Żniński":"0419",
"Żory":"2479",
"Żuromiński":"1437",
"Zwoleński":"1436",
"Żyrardowski":"1438",
"Żywiecki":"2417",
"Złotoryjski":"0226",
"Złotowski":"3031",
"Łańcucki":"1810",
"Łaski":"1003",
"Łęczycki":"1004",
"Łęczyński":"0610",
"Łobeski":"3218",
"Łódź":"1061",
"Łódzki Wschodni":"1006",
"Łomża":"2062",
"Łomżyński":"2007",
"Łosicki":"1410",
"Łowicki":"1005",
"Łukowski":"0611",
},
    "PT": {},
    "RO": {},
    "RS": {},
    "SE": {},
    "SI": {},
    "SK": {},
    "UK": {},
}


awt = {
    "1": "Wind",
    "2": "Snow/Ice",
    "3": "Thunderstorms",
    "4": "Fog",
    "5": "Extreme high temperature",
    "6": "Extreme low temperature",
    "7": "Coastal Event",
    "8": "Forestfire",
    "9": "Avalanches",
    "10": "Rain",
    "12": "Flood",
    "13": "Rain-Flood",
}

awl = {
    "0": ("White", "Missing, insufficient, outdated or suspicious data."),
    "1": ("Green", "No particular awareness of the weather is required."),
    "2": (
        "Yellow",
        "The weather is potentially dangerous. The weather phenomena that have been forecast are not unusual, but be attentive if you intend to practice activities exposed to meteorological risks. Keep informed about the expected meteorological conditions and do not take any avoidable risk.",
    ),
    "3": (
        "Orange",
        "The weather is dangerous. Unusual meteorological phenomena have been forecast. Damage and casualties are likely to happen. Be very vigilant and keep regularly informed about the detailed expected meteorological conditions. Be aware of the risks that might be unavoidable. Follow any advice given by your authorities.",
    ),
    "4": (
        "Red",
        "The weather is very dangerous. Exceptionally intense meteorological phenomena have been forecast. Major damage and accidents are likely, in many cases with threat to life and limb, over a wide area. Keep frequently informed about detailed expected meteorological conditions and risks. Follow orders and any advice given by your authorities under all circumstances, be prepared for extraordinary measures.",
    ),
}


countries = {
    "AT": ("AT-Austria", "deutsch"),
    "BA": ("BA-Bosnia-Herzegovina", "/"),
    "BE": ("BE-Belgium", ""),
    "BG": ("BG-Bulgaria", ""),
    "CH": ("CH-Switzerland", "english"),
    "CY": ("CY-Cyprus", ""),
    "CZ": ("CZ-Czechia", "čeština"),
    "DE": ("DE-Germany", "deutsch"),
    "DK": ("DK-Denmark", ""),
    "EE": ("EE-Estonia", ""),
    "ES": ("ES-Spain", "español"),
    "FI": ("FI-Finland", "suomi"),
    "FR": ("FR-France", "français"),
    "GR": ("GR-Greece", "Ελληνικά"),
    "HR": ("HR-Croatia", "hrvatski"),
    "HU": ("HU-Hungary", ""),
    "IE": ("IE-Ireland", ""),
    "IL": ("IL-Israel", "עברית"),
    "IS": ("IS-Iceland", ""),
    "IT": ("IT-Italy", "italiano"),
    "LT": ("LT-Lithuania", "lietuviu"),
    "LU": ("LU-Luxembourg", ""),
    "LV": ("LV-Latvia", "latviešu"),
    "MD": ("MD-Moldova", ""),
    "ME": ("ME-Montenegro", "Црногорски"),
    "MK": ("MK-Republic%20of%20North%20Macedonia", ""),
    "MT": ("MT-Malta", "Malti"),
    "NL": ("NL-Netherlands", "nederlands"),
    "NO": ("NO-Norway", "norsk"),
    "PL": ("PL-Poland", "polski"),
    "PT": ("PT-Portugal", "português"),
    "RO": ("RO-Romania", ""),
    "RS": ("RS-Serbia", "српски"),
    "SE": ("SE-Sweden", ""),
    "SI": ("SI-Slovenia", "slovenščina"),
    "SK": ("SK-Slovakia", "slovenčina"),
    "UK": ("UK-United%20Kingdom", ""),
}
