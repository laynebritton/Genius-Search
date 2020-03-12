from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random 
from operator import itemgetter 


app = Flask(__name__)

albums = [
    {
        "id": 11,
        "title": "Late Registration",
        "artists": ["Kanye West"],
        "year": 2005,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/f/f4/Late_registration_cd_cover.jpg",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Devo Springsteen","Jon Brion"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "mark_as_deleted": False,
        "description": """ Late Registration is the second studio album by American rapper and producer Kanye West. It was released on August 30, 2005, through Def Jam Recordings and Roc-A-Fella Records. The album was recorded for over a year in sessions held across studios in New York City and Hollywood, with West collaborating with American record producer and composer Jon Brion. It features guest contributions from Adam Levine, Lupe Fiasco, Jamie Foxx, Common, Jay-Z, Brandy, and Nas, among others. The production of Late Registration was notably more lush and elaborate than West's 2004 debut studio album The College Dropout, as he utilized intricate sampling methods and string orchestration with Brion while drawing on stylistic influences from alternative acts such as Portishead, Coldplay, and Fiona Apple. The rapper's lyrics explore both personal and broader political themes, including poverty, drug trafficking, racism, healthcare, and the blood diamond trade.""",
    },
    {
        "id": 12,
        "title": "Graduation",
        "artists": ["Kanye West"],
        "year": 2007,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/7/70/Graduation_%28album%29.jpg",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Shawn Carter","Kyambo 'Hip Hop' Joshua","Gee Roberson"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Graduation is the third studio album by American rapper Kanye West, released on September 11, 2007, through Def Jam Recordings and Roc-A-Fella Records. Recording sessions took place during 2005 to 2007 at several studios in New York and Los Angeles. It was primarily produced by West himself, with contributions from various other producers. The album also features guest appearances from recording artists such as Dwele, T-Pain, Lil Wayne, DJ Premier, and Chris Martin of Coldplay. The cover art and its interior artwork were designed by Japanese contemporary artist Takashi Murakami, who would also design the cover art for West's collaborative album with Kid Cudi, eponymously titled Kids See Ghosts (2018). Inspired by stadium tours, house-music and indie rock, Graduation marked a departure from the ornate, soul-based sound of West's previous releases as he musically progressed to more anthemic compositions. West incorporated layered synthesizers and dabbled with electronics while sampling from various music genres and altering his approach to rapping. He conveys an ambivalent outlook on his newfound fame and media scrutiny alongside providing inspirational messages of triumph directed at listeners. Graduation concludes the education theme of West's first two albums The College Dropout (2004) and Late Registration (2005).""",
    },
    {
        "id": 12,
        "title": "808s & Heartbreak",
        "artists": ["Kanye West"],
        "year": 2008,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/f/f1/808s_%26_Heartbreak.png",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Kyambo 'Hip Hop' Joshua","Gee Roberson","Mr. Hudson"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ 808s & Heartbreak is the fourth studio album by American producer and vocalist Kanye West. It was released on November 24, 2008, through Def Jam Recordings and Roc-A-Fella Records. West recorded the album during September and October 2008 at Glenwood Studios in Burbank, California and Avex Recording Studio in Honolulu, Hawaii, with the help of producers No I.D., Jeff Bhasker and others. Guest appearances are featured from Kid Cudi, Young Jeezy, Mr Hudson, and Lil Wayne. Conceived in the wake of several distressing personal events, 808s & Heartbreak marked a major musical departure from West's previous rap records, instead featuring a sparse, electronic sound and West singing through an Auto-Tune vocal processor. His lyrics explore themes of loss, alienated fame, and heartache, while the album's production abandons conventional hip hop sounds in favor of a minimalist sonic palette, which includes prominent use of the titular Roland TR-808 drum machine.""",
    },
    {
        "id": 13,
        "title": "My Beautiful Dark Twisted Fantasy",
        "artists": ["Kanye West"],
        "year": 2010,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/b/be/MBDTF_ALT.jpg",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Bink","DJ Frank E"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ My Beautiful Dark Twisted Fantasy is the fifth studio album by American rapper and producer Kanye West. It was released on November 22, 2010, by Def Jam Recordings and Roc-A-Fella Records. It follows a period of public and legal controversy for the rapper, who retreated to a self-imposed exile in Hawaii in 2009 and recorded in a communal environment involving numerous contributing musicians and producers. Recorded mainly at Honolulu's Avex Recording Studio, additional sessions took place at Glenwood Place Studios in Burbank, California, and at Electric Lady Studios and Platinum Sound Recording Studios in New York City. The album was produced primarily by West, along with a variety of high-profile producers such as Mike Dean, No I.D., Jeff Bhasker, RZA, S1, Bink, and DJ Frank E. Music journalists have noted the album features a maximalist aesthetic and opulent production quality with elements of West's previous works, including soul, baroque, electro, and symphonic styles, as well as progressive rock influences. Thematically, My Beautiful Dark Twisted Fantasy explores West's status as a celebrity, consumer culture, race, and the idealism of the American Dream. Guest vocalists on the album include: Bon Iver, Jay-Z, Pusha T, Rick Ross, Kid Cudi, Nicki Minaj, John Legend, and Raekwon.""",
    },
    {
        "id": 14,
        "title": "Watch the Throne",
        "artists": ["Kanye West", "Jay-Z"],
        "year": 2011,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/e/ee/Watch_The_Throne.jpg",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Jay-Z","Gee Roberson","Kyambo Joshua","88-Keys"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """Watch the Throne is a collaborative studio album by American rappers Jay-Z and Kanye West, released on August 8, 2011 by Roc-A-Fella Records, Roc Nation, and Def Jam Recordings. Before the album, Jay-Z and Kanye had collaborated on various singles, and with the latter as a producer on the former's work. They originally sought out to record a five-song EP together, but the project eventually evolved into a full-length album. The project features guest appearances from Frank Ocean, The-Dream, Beyoncé and Mr Hudson, as well as posthumous vocals by Otis Redding and Curtis Mayfield. It also features vocal contributions from Kid Cudi, Seal, Justin Vernon, Elly Jackson, Connie Mitchell, Charlie Wilson and Pete Rock, among others. Recording sessions took place at various locations and began in November 2010, with production on led by West and a variety of high-profile producers, including Mike Dean, Swizz Beatz, Tyler Pase, Jeff Bhasker, The Neptunes, and Q-Tip. Expanding on the dense production style of West's 2010 album My Beautiful Dark Twisted Fantasy, Watch the Throne incorporates orchestral and progressive rock influences, unconventional samples, and dramatic melodies in its sound. Its braggadocio lyrics exhibit themes of opulence, fame, materialism, power, and the burdens of success, as well as political and socioeconomic context. The album also expresses other topics, such as Jay-Z's thoughts on fatherhood, West's reflection on being deemed a social villain, and their success as performers. Many writers interpreted the subject matter to concern the rappers' plight as African Americans struggling with financial success in America. """,
    },
    {
        "id": 15,
        "title": "Yeezus",
        "artists": ["Kanye West"],
        "year": 2013,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/0/03/Yeezus_album_cover.png",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West","Daft Punk","Hudson Mohawke","Lunice"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Yeezus is the sixth studio album by American rapper and producer Kanye West. It was released on June 18, 2013, through Def Jam Recordings and Roc-A-Fella Records. West gathered a number of artists and close collaborators for the production, including Mike Dean, Daft Punk, Noah Goldstein, Arca, Hudson Mohawke, and Travis Scott. The album also features guest vocals from Justin Vernon, Chief Keef, Kid Cudi, Assassin, King L, Charlie Wilson, and Frank Ocean. Fifteen days before its release date, West enlisted the help of producer Rick Rubin to strip down the sound of Yeezus in favor of a more minimalist approach. The album has been characterized as West's most experimental and sonically abrasive work. It draws from an array of genres, including industrial, acid house, electro, punk, and Chicago drill. West's unconventional use of samples is also contained, as on "Blood on the Leaves", which contains a sample from Nina Simone's 1965 rendition of "Strange Fruit".""",
    },
    {
        "id": 16,
        "title": "The Life of Pablo",
        "artists": ["Kanye West"],
        "year": 2016,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/4/4d/The_life_of_pablo_alternate.jpg",
        "labels": ["GOOD","Def Jam"],
        "producers": ["Kanye West","Boi-1da","Cashmere Cat","Chance the Rapper","Charlie Heat"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ The Life of Pablo is the seventh studio album by American rapper and producer Kanye West. It was released on February 14, 2016, through GOOD Music and distributed by Def Jam Recordings. Recording sessions took place from 2013 to 2016, in Italy, Mexico, Canada, and the United States. The production was handled by West and a variety of other producers, including co-executive producers Rick Rubin and Noah Goldstein. West also enlisted guest vocals for the album, including Ty Dolla Sign, Desiigner, Kid Cudi, Rihanna, and Post Malone.""",
    },
    {
        "id": 17,
        "title": "Ye",
        "artists": ["Kanye West"],
        "year": 2018,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/7/74/Ye_album_cover.jpg",
        "labels": ["GOOD","Def Jam"],
        "producers": ["Kanye West", "7 Aurelius"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Ye (/jeɪ/; stylized as ye) is the eighth studio album by American rapper and producer Kanye West. It was released on June 1, 2018, through GOOD Music and distributed by Def Jam Recordings. Following controversy surrounding an interview with TMZ, West re-recorded all the work on the album, completing it over the course of just two weeks at his ranch in Jackson Hole, Wyoming.""",
    },
    {
        "id": 18,
        "title": "Kids See Ghosts",
        "artists": ["Kids See Ghosts", "Kanye West", "Kid Cudi"],
        "year": 2018,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/1/18/Kids_See_Ghost_Cover.jpg",
        "labels": ["Def Jam","GOOD"],
        "producers": ["Kanye West","Kid Cudi","André 3000"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Kids See Ghosts is the eponymous debut studio album by American hip hop duo Kids See Ghosts, composed of Kanye West and Kid Cudi. It was released on June 8, 2018, through GOOD Music and distributed by Def Jam Recordings. Prior to the release, West and Cudi enjoyed a strong relationship as close friends and musical allies since meeting in 2008, and expressed a desire to record a collaborative album. However, an album never initially materialized, with the duo instead experiencing brief fallings-out in 2013 and 2016. They reunited a year later, when the first studio sessions for the album began.""",
    },
    {
        "id": 19,
        "title": "Section.80",
        "artists": ["Kendrick Lamar"],
        "year": 2011,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/4/48/Section.80-Cover.jpg",
        "labels": ["Top Dawg"],
        "producers": ["Dave Free", "J. Cole", "Sounwave"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Section.80 is the debut studio album by American rapper Kendrick Lamar. It was released on July 2, 2011, through Top Dawg Entertainment. The album features guest appearances from GLC, Colin Munroe, Ashtrobot, BJ the Chicago Kid, Schoolboy Q, Ab-Soul and vocals from late singer-songwriter Alori Joh. The production was mainly handled by Top Dawg in-house producers from production group Digi+Phonics, along with THC, Tommy Black, Wyldfyer, Terrace Martin and J. Cole. The concept album features lyrical themes delivered by Lamar such as the 1980s crack epidemic, racism and medication tolerance. The album's lead single, "HiiiPoWeR" was released on April 12, 2011.""",
    },
        {
        "id": 20,
        "title": "good kid, m.A.A.d city",
        "artists": ["Kendrick Lamar"],
        "year": 2012,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/9/93/KendrickGKMC.jpg",
        "labels": ["Top Dawg"],
        "producers": ["DJ Dahi","Hit-Boy","Just Blaze","Pharrell Williams"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Good Kid, M.A.A.D City (stylized as good kid, m.A.A.d city) is the second studio album by American rapper Kendrick Lamar. It was released on October 22, 2012, through Top Dawg Entertainment, distributed by Aftermath Entertainment and Interscope Records. The album is Lamar's major label debut, after his independently released first album Section.80 in 2011 and his signing to Aftermath and Interscope the following year. Good Kid, M.A.A.D City was recorded mostly at several studios in California, with producers such as Dr. Dre, Just Blaze, Pharrell Williams, Hit-Boy, Scoop DeVille, Jack Splash, and T-Minus, among others, contributing to the album. Billed as a "short film by Kendrick Lamar" on the album cover, the concept album follows the story of Lamar's teenage experiences in the drug-infested streets and gang lifestyle of his native Compton. The album received widespread acclaim from critics, who praised its thematic scope and Lamar's lyrics. It earned Lamar four Grammy Award nominations at the 2014 Grammy Awards, including Album of the Year.""",
    },
    {
        "id": 21,
        "title": "To Pimp a Butterfly",
        "artists": ["Kendrick Lamar"],
        "year": 2015,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/f/f6/Kendrick_Lamar_-_To_Pimp_a_Butterfly.png",
        "labels": ["Top Dawg","Aftermath"],
        "producers": ["Flying Lotus","Pharrell Williams","Thundercat"],
        "genres": ["Hip hop","Jazz rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ To Pimp a Butterfly is the third studio album by American rapper Kendrick Lamar. It was released on March 15, 2015, through Top Dawg Entertainment, distributed by Aftermath Entertainment and Interscope Records. The album was recorded in studios throughout the United States, with production from Sounwave, Terrace Martin, Taz "Tisa" Arnold, Thundercat, Rahki, LoveDragon, Flying Lotus, Pharrell Williams, Boi-1da, Knxwledge, and several other high-profile hip hop producers, as well as executive production from Dr. Dre and Anthony "Top Dawg" Tiffith. The album incorporates elements of jazz, funk, soul, spoken word, and avant-garde music and explores a variety of political and personal themes concerning African-American culture, racial inequality, depression, and institutional discrimination.""",
    },
    {
        "id": 22,
        "title": "Untitled Unmastered",
        "artists": ["Kendrick Lamar"],
        "year": 2016,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/b/be/Kendrick_Lamar_-_Untitled_Unmastered_%28Artwork%29.jpg",
        "labels": ["Top Dawg","Aftermath"],
        "producers": ["Thundercat","Swizz  Beats","Terrace Martin"],
        "genres": ["Hip hop", "Jazz Rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """Untitled Unmastered (stylized as untitled unmastered.) is a compilation album by American rapper Kendrick Lamar. It was released on March 4, 2016,[1] by Top Dawg Entertainment, Aftermath Entertainment and Interscope Records. It consists of previously unreleased demos that originated during the recording of Lamar's album To Pimp a Butterfly (2015),[2] continuing that work's exploration of politically-charged and philosophical themes, as well as its experimentation with free jazz, soul, avant-garde music, and funk styles. The compilation album received widespread acclaim from critics, and it debuted atop the US Billboard 200. """,
    },
    {
        "id": 23,
        "title": "DAMN",
        "artists": ["Kendrick Lamar"],
        "year": 2017,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/5/51/Kendrick_Lamar_-_Damn.png",
        "labels": ["Top Dawg","Aftermath"],
        "producers": ["9th Wonder","The Alchemist","Mike Will Made It","DJ Dahi"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Damn (stylized as DAMN.) is the fourth studio album by American rapper Kendrick Lamar. It was released on April 14, 2017, through Top Dawg Entertainment, distributed by Aftermath Entertainment and Interscope Records. Damn features production from a variety of record producers, including executive producer and Top Dawg Entertainment label-head Anthony "Top Dawg" Tiffith, Sounwave, DJ Dahi, Mike Will Made It, and Ricci Riera; as well as further production contributions from James Blake, Steve Lacy, BadBadNotGood, Greg Kurstin, The Alchemist, and 9th Wonder, among others. Damn features appearances from singers Rihanna and Top Dawg signee Zacari, along with Irish rock band U2.""",
    },
    {
        "id": 24,
        "title": "Illmatic",
        "artists": ["Nas"],
        "year": 1994,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/2/27/IllmaticNas.jpg",
        "labels": ["Columbia"],
        "producers": ["MC Serch","Faith N.","Q-Tip"],
        "genres": ["Hip hop","Jazz rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Illmatic is the debut studio album by American rapper Nas. It was released on April 19, 1994, by Columbia Records. After signing with the label with the help of MC Serch, Nas recorded the album in 1992 and 1993 at Chung King Studios, D&D Recording, Battery Studios, and Unique Recording Studios in New York City. The album's production was handled by DJ Premier, Large Professor, Pete Rock, Q-Tip, L.E.S. and Nas himself. Styled as a hardcore hip hop album, Illmatic features multi-syllabic internal rhymes and inner-city narratives based on Nas' experiences in Queensbridge, New York.""",
    },
    {
        "id": 25,
        "title": "Born Sinner",
        "artists": ["J. Cole"],
        "year": 2013,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/f/fa/J_Cole_Born_Sinner3.jpg",
        "labels": ["Columbia","Dreamville"],
        "producers": ["J. Cole","Jake One"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Born Sinner is the second studio album by American rapper J. Cole. It was released on June 18, 2013, by ByStorm Entertainment, Columbia Records, Dreamville Records and Roc Nation. The album serves as the follow-up to his debut album, Cole World: The Sideline Story (2011). The album features guest appearances from Miguel, Amber Coffman, Jhené Aiko, James Fauntleroy, Bas, TLC, Kendrick Lamar and 50 Cent. The album was also primarily produced by Cole himself, along with others such as Jake One, Syience, and Elite.""",
    },
    {
        "id": 26,
        "title": "2014 Forest Hills Drive",
        "artists": ["J. Cole"],
        "year": 2014,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/2/2a/2014ForestHillsDrive.jpg",
        "labels": ["Columbia","Dreamville"],
        "producers": ["J. Cole","Illmind"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ 2014 Forest Hills Drive is the third studio album by American rapper J. Cole. It was released on December 9, 2014, by ByStorm Entertainment, Columbia Records, Dreamville Records and Roc Nation. Recording sessions took place over the whole year, while the production on the album was primarily handled by Cole himself, along with several others such as Illmind, Vinylz, Phonix Beats and Willie B. It was announced three weeks before its release and had very little marketing, with no singles or promotion taking place prior to its release. The album was supported by four singles: "Apparently", "Wet Dreamz", "No Role Modelz" and "Love Yourz".""",
    },
    {
        "id": 27,
        "title": "4 Your Eyez Only",
        "artists": ["J. Cole"],
        "year": 2016,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/b/bb/J._Cole_%E2%80%94_4_Your_Eyez_Only_album_cover.jpg",
        "labels": ["Dreamville","Roc Nation"],
        "producers": ["J. Cole","Ibrahim Hamad","Elite"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ 4 Your Eyez Only is the fourth studio album by American rapper J. Cole. It was released on December 9, 2016, by Dreamville Records, Roc Nation and Interscope Records.[5] The album was Cole's first release with Interscope—his previous albums were released by Columbia Records.[6] 4 Your Eyez Only was released exactly two years after Cole's previous studio album, 2014 Forest Hills Drive.""",
    },
    {
        "id": 28,
        "title": "KOD",
        "artists": ["J. Cole"],
        "year": 2018,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/d/d3/JColeKOD.jpg",
        "labels": ["Dreamville","Roc Nation"],
        "producers": ["J. Cole","Ibrahim Hamad"],
        "genres": ["Hip hop","Jazz rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ KOD (an initialism for Kids on Drugs, Kings Overdosed and Kill Our Demons)[1] is the fifth studio album by American rapper J. Cole. It was released on April 20, 2018 through Dreamville Records, Roc Nation and Interscope Records.[2] The majority of the production on the album was handled by Cole himself, along with others such as T-Minus, Mark Pelli, BLVK and Ron Gilmore. The album incorporates elements of jazz rap and trap, Cole has stated that the production and rhyme schemes used throughout the album was inspired by SoundCloud rap. The album explores a variety of topics including drug abuse, addiction, depression, greed, African-American culture, and taxation in the United States.[3]""",
    },
    {
        "id": 29,
        "title": "Revenge of the Dreamers III",
        "artists": ["Dreamville","J. Cole"],
        "year": 2019,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/0/02/Dreamville_-_Revenge_of_the_Dreamers_III.png",
        "labels": ["Dreamville"],
        "producers": ["J. Cole","Ibrahim Hamad"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Revenge of the Dreamers III is the third compilation album by American record label Dreamville and J. Cole, released on July 5, 2019, by Dreamville and Interscope Records. Revenge of the Dreamers III includes contributions from Dreamville artists, J. Cole, Bas, Cozz, Omen, Lute, Ari Lennox, EarthGang, and JID. The album features appearances from several artists including DaBaby, T.I, Young Nudy, Buddy, Reason, Maxo Kream, Ski Mask the Slump God, Mez, 6lack, Mereba, Vince Staples, Ty Dolla Sign, Dreezy, Smino, Saba, and Guapdad 4000, among others. The album features production from a variety of record producers, including T-Minus, Christo, Elite, Bink!, Deputy, Henny Tha Bizness, Hollywood JB, ChaseTheMoney, Pyrex, Galimatias, Pluss, Kal Banx, and Cam O'bi, among others. Recording sessions for Revenge of the Dreamers III took place in Atlanta, Georgia at Tree Sound Studios over the course of 10 days in January 2019. A total of 343 artists and producers were invited, while 142 songs were recorded during the sessions. On the standard edition of the album, 35 artists and 27 producers contributed to the final product.[4] The album was accompanied by a thirty-minute documentary titled, Dreamville Presents: Revenge, documenting the recording sessions.[5]""",
    },
    {
        "id": 30,
        "title": "Acid Rap",
        "artists": ["Chance the Rapper"],
        "year": 2013,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/5/5b/Chance_the_rapper_acid_rap.jpg",
        "labels": ["Self-release (no label)"],
        "producers": ["Nate Fox","Peter Cottontale"],
        "genres": ["Hip hop","Jazz rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Acid Rap is the second mixtape by American rapper Chance the Rapper. It was released on April 30, 2013, as a free digital download. In July 2013, the album debuted at number 63 on the Billboard Top R&B/Hip-Hop Albums, due to bootleg downloads on iTunes and Amazon not affiliated with the artist.[2] The mixtape has been certified "diamond" on mixtape site Datpiff, for garnering over 10,000,000 downloads.[3] It was rereleased on streaming services on June 21, 2019, alongside his 2012 mixtape 10 Day.""",
    },
    {
        "id": 31,
        "title": "Coloring Book",
        "artists": ["Chance the Rapper"],
        "year": 2016,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/c/c4/Chance_the_Rapper_-_Coloring_Book.png",
        "labels": ["Self-release (no label)"],
        "producers": ["Kanye West","Brasstracks","Francis and the Lights"],
        "genres": ["Hip hop","Gospel rap"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Coloring Book is the third mixtape by American rapper Chance the Rapper. It was produced by his group The Social Experiment, Lido, and Kaytranada, among others. For the mixtape, Chance also collaborated with musicians such as Kanye West, Young Thug, Francis and the Lights, Justin Bieber, 2 Chainz, Kirk Franklin, and the Chicago Children's Choir. Coloring Book was released on May 13, 2016, exclusively on Apple Music, before being made available to other streaming services on May 27. It was the first album to chart on the US Billboard 200 solely on streams, peaking at number eight, while receiving widespread acclaim from critics who praised its fusion of hip hop and gospel sounds. It won Best Rap Album at the 2017 Grammy Awards. It was also the first streaming-only album ever to win a Grammy.[2]""",
    },
        {
        "id": 32,
        "title": "SATURATION",
        "artists": ["Brockhampton"],
        "year": 2017,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/b/b0/Brockhampton_-_Saturation.png",
        "labels": ["Brockhampton", "Empire"],
        "producers": ["Brockhampton"],
        "genres": ["Hip hop"],
        "user_reviews" : ["My favorite of the SATURATION Trilogy!","If you enjoyed this, check out SATURATION II and SATURATION III"],
        "mark_as_deleted": False,        
        "description": """ Saturation (stylized in all caps) is the debut studio album by American rap collective Brockhampton, released on June 9, 2017.[2][3] It's part of the Saturation trilogy, together with Saturation II and III. It primarily features Brockhampton members Kevin Abstract, Merlyn Wood, Dom McLennon, Matt Champion, Russell "Joba" Boring, and former member Ameer Vann. Group member Bearface also contributes to the album's closing track. Production was primarily handled by Romil Hemnani and Q3—a production duo consisting of Jabari Manwa and Kiko Merley, with additional production contributions by Joba, Bearface, and Rome Gomez.""",
    },
    {
        "id": 33,
        "title": "SATURATION II",
        "artists": ["Brockhampton"],
        "year": 2017,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/d/d1/Brockhampton_-_Saturation_II.png",
        "labels": ["Question Everything", "Empire"],
        "producers": ["Brockhampton"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """Saturation II (stylized in all caps) is the second studio album by American rap collective Brockhampton, released on August 25, 2017.[1] Production is primarily handled by Romil Hemnani, alongside production duo Q3 (composed of Jabari Manwa and Kiko Merley), Bearface, Kevin Abstract, and JOBA. """,
    },
    {
        "id": 34,
        "title": "SATURATION III",
        "artists": ["Brockhampton"],
        "year": 2017,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/9/93/Brockhampton_-_Saturation_III.png",
        "labels": ["Question Everything", "Empire"],
        "producers": ["Brockhampton"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """Saturation III (stylized in all caps) is the third studio album by American rap collective Brockhampton, released on December 15, 2017.[1][2] Production is predominantly handled by Romil Hemnani, alongside production duo Q3 (composed of Jabari Manwa and Kiko Merley), as with previous releases. It concludes the Saturation trilogy, commenced with Saturation and followed with Saturation II. Originally promoted as the group's "final studio album", the group announced their fourth album, Team Effort, a day before Saturation III was released.[3] Saturation III is the band's last album with founding member Ameer Vann, who left the band in May 2018 amid accusations of sexual misconduct.[4] """,
    },
    {
        "id": 35,
        "title": "iridescence",
        "artists": ["Brockhampton"],
        "year": 2018,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/5/5e/Brockhampton_-_Iridescence.png",
        "labels": ["Question Everything", "RCA"],
        "producers": ["Brockhampton"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Iridescence (stylized in all lowercase) is the fourth studio album by American rap collective Brockhampton, released on September 21, 2018 by Question Everything, Inc. RCA Records. It is their major-label debut and the first installment of their The Best Years of Our Lives trilogy. The self-produced album was recorded at Abbey Road Studios in London, as well as the group's own studio in Hawaii. It is their first album since founding member Ameer Vann's departure from the group following sexual misconduct allegations. It debuted at number one on the US Billboard 200 albums chart, becoming the group's first chart-topping album.""",
    },
    {
        "id": 36,
        "title": "GINGER",
        "artists": ["Brockhampton"],
        "year": 2019,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/a/a0/Brockhampton_-_Ginger.png",
        "labels": ["Question Everything", "Empire"],
        "producers": ["Brockhampton"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """Ginger (stylized in all caps) is the fifth studio album by American hip hop collective Brockhampton. It was released on August 23, 2019, through the band's label Question Everything and RCA.[2]""",
    },
    {
        "id": 37,
        "title": "Flower Boy",
        "artists": ["Tyler, the Creator"],
        "year": 2017,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/c/c3/Tyler%2C_the_Creator_-_Flower_Boy.png",
        "labels": ["Columbia"],
        "producers": ["Tyler, the Creator"],
        "genres": ["Hip hop", "Jazz rap", "Neo soul"],
        "user_reviews" : ["Very interesting jazz-influenced instrumentals!","First great project from Tyler."],
        "mark_as_deleted": False,
        "description": """ Flower Boy (alternatively titled Scum Fuck Flower Boy) is the fourth studio album by American rapper Tyler, the Creator. The album was released on July 21, 2017, by Columbia Records. Produced entirely by Tyler, the album features guest vocals from a range of artists; including Frank Ocean, ASAP Rocky, Anna of the North, Lil Wayne, Kali Uchis, Steve Lacy, Estelle, Jaden Smith and Rex Orange County. Flower Boy was supported by four singles: "Who Dat Boy" / "911", "Boredom", "I Ain't Got Time!" and "See You Again". The album received widespread acclaim from critics, and debuted at number two on the US Billboard 200. It was named among the best albums of 2017 by multiple publications and was nominated for Best Rap Album at the 2018 Grammy Awards.""",
    },
    {
        "id": 38,
        "title": "IGOR",
        "artists": ["Tyler, the Creator"],
        "year": 2019,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/5/51/Igor_-_Tyler%2C_the_Creator.jpg",
        "labels": ["Columbia","A Boy is a Gun"],
        "producers": ["Tyler, the Creator"],
        "genres": ["Hip hop", "R&B", "Neo soul"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Igor (stylized in all caps) is the fifth studio album[a] by American rapper Tyler, the Creator, released on May 17, 2019, through A Boy is a Gun and distributed by Columbia Records. Produced entirely by Tyler, the album follows the 2017 release of Flower Boy. It features guest appearances from Playboi Carti, Lil Uzi Vert, Solange, Kanye West, and Jerrod Carmichael, along with backing vocals from Santigold, Jessy Wilson, La Roux, CeeLo Green, Charlie Wilson, Slowthai, and Pharrell, among others. Igor received widespread acclaim from critics and debuted at number one on the US Billboard 200, becoming Tyler's first US number-one album. The album's lead single "Earfquake" became Tyler's highest-charting US Billboard Hot 100 single, peaking at number 13. It won Best Rap Album at the 2020 Grammy Awards.""",
    },
    {
        "id": 39,
        "title": "TA13OO",
        "artists": ["Denzel Curry"],
        "year": 2018,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/4/42/Ta13oo_by_Denzel_Curry.jpg",
        "labels": ["Loma Vista","PH"],
        "producers": ["Charlie Heat","DJ Dahi","FnZ","Hippie Sabotage"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Ta13oo (stylized TA13OO and pronounced Taboo) is the third studio album by American rapper Denzel Curry. It was released on July 27, 2018, through PH Recordings and distributed by Loma Vista Recordings. The album serves as the follow-up to Curry's second studio album, Imperial, released in 2016, and the 13 EP, released in 2017. Ta13oo features guest appearances from Twelve'len, GoldLink, Nyyjerya, JID, JPEGMafia, ZillaKami, and additional vocals by Billie Eilish. Production was handled by FnZ, DJ Dahi, Ronny J, Illmind, Charlie Heat, and Mickey de Grand IV, among others. Ta13oo was supported by five singles: "Sumo", "Percs", "Clout Cobain", "Vengeance", and "Black Balloons". The album received widespread acclaim from critics.""",
    },
    {
        "id": 40,
        "title": "ZUU",
        "artists": ["Denzel Curry"],
        "year": 2019,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/d/d6/Denzel_Curry_-_Zuu.png",
        "labels": ["Loma Vista","PH"],
        "producers": ["Charlie Heat","Fabio Aguilar","FnZ","Keanu Beats","Tay Keith"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ Zuu (stylized in all caps) is the fourth studio album by American rapper Denzel Curry, released through PH Recordings and distributed by Loma Vista Recordings on May 31, 2019. The title is a nickname for his home city, Carol City, Miami, Florida. Zuu is the follow-up to Curry's 2018 studio album Ta13oo. It was supported by two singles: "Ricky" and "Speedboat". The album received widespread acclaim from critics, with many praising Curry's tributes to other artists from Carol City.""",
    },
    {
        "id": 41,
        "title": "The College Droupout",
        "artists": ["Kanye West"],
        "year": 2004,
        "album_art": "https://upload.wikimedia.org/wikipedia/en/a/a3/Kanyewest_collegedropout.jpg",
        "labels": ["Def Jam","Roc-A-Fella"],
        "producers": ["Kanye West"],
        "genres": ["Hip hop"],
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": """ The College Dropout is the debut studio album by American rapper and producer Kanye West. It was released on February 10, 2004, by Def Jam Recordings and Roc-A-Fella Records. In the years leading up to release, West had received praise for his production work for rappers such as Jay-Z and Talib Kweli, but faced difficulty being accepted as an artist in his own right by figures in the music industry. Intent on pursuing a solo career, he signed a record deal with Roc-A-Fella and recorded the album over a period of four years, beginning in 1999. The production of The College Dropout was primarily handled by West and developed his "chipmunk soul" production style, which made use of sped-up, pitch shifted vocal samples from soul and R&B records, in addition to West's own drum programming, string accompaniments, and gospel choirs; the album also features contributions from Jay-Z, Mos Def, Jamie Foxx, Syleena Johnson, and Ludacris, among others. Diverging from the then-dominant gangster persona in hip hop, West's lyrics concern themes of family, self-consciousness, materialism, religion, racism, and higher education.""",
    },
]

@app.route('/')
def index():
    recent_albums = get_most_recent_non_deleted_albums(10)
    return render_template('home.html', results=recent_albums)

@app.route('/search/<term>')
def search(term=None):
    global albums
    if term=="*all":
        return render_template('search.html', results=albums)

    search_term = term.lower()    
    results= list(filter(lambda album: ( search_fields(album,search_term) ), albums))

    return render_template('search.html', results=results)

def get_most_recent_non_deleted_albums(count):
    global albums
    reverse_albums = albums.copy()
    reverse_albums.reverse()
    temp = []
    counter = 0
    for album in reverse_albums:
        if album["mark_as_deleted"] == False:
            temp.append(album)
            counter += 1
        if counter >= count:
            temp
            return temp
    return temp

def search_fields(album, search_term):
    if album["mark_as_deleted"] == True:
        return False
    
    if search_term in album["title"].lower():
        return True

    for artist in album["artists"]:
        if search_term in artist.lower():
            return True

    if search_term == str(album["year"]):
        return True

    for label in album["labels"]:
        if search_term in label.lower():
            return True

    return False

@app.route('/view/<id>')
def view(id=None):
    global albums
    return render_template('album-view.html', album = next((album for album in albums if album["id"] == int(id)),None))

@app.route('/create')
def create():
    return render_template('create-album.html')

@app.route('/create-album', methods=['POST'])
def create_album():
    global albums
    json_data = request.get_json()   

    new_id=albums[len(albums)-1].get("id") + 1

    new_album={
        "id": new_id,
        "title": json_data["title"],
        "artists": json_data["artists"].split(","),
        "year": json_data["year"],
        "album_art": json_data["album_art"],
        "labels": json_data["labels"].split(","),
        "producers": json_data["producers"].split(","),
        "genres": json_data["genres"].split(","),
        "user_reviews" : [],
        "mark_as_deleted": False,
        "description": json_data["description"],
    }

    albums.append(new_album)
    print(new_id,flush=True)

    return jsonify(new_album)

@app.route( '/edit/<id>')
def edit(id=None):
    return render_template('update-album.html', album = next((album for album in albums if album["id"] == int(id)),None))

@app.route('/add-review', methods=['POST'])
def add_review():
    global albums
    json_data = request.get_json()   

    id = json_data["id"]

    user_review = json_data["user_review"]
    print(user_review,flush=True)

    results= list(filter(lambda album: album["id"] == id, albums))
    
    print(results, flush=True)

    for result in results:
        result["user_reviews"].append(user_review)

    return jsonify(results)

@app.route('/delete-album',methods=['POST'])
def delete_album():
    global albums
    json_data = request.get_json()   

    id = json_data["id"]

    albums[:] = [album for album in albums if album.get("id") != int(id)]
    # results= list(filter(lambda album: album["id"] == id, albums))

    return jsonify(albums)
    
if __name__ == '__main__':
   app.run(debug = True)
