# mcq_data.py

mcq_bank = {
    "1": {
        "Mathematics": {
            "Easy": [
                {"question": "What is 1 + 1?", "options": ["1", "2", "3", "4"], "answer": "2"},
                {"question": "What comes after 2?", "options": ["1", "3", "4", "5"], "answer": "3"},
                {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
                {"question": "What is 3 - 1?", "options": ["1", "2", "3", "4"], "answer": "2"},
                {"question": "What number comes before 5?", "options": ["4", "6", "3", "2"], "answer": "4"},
                {"question": "What is 0 + 1?", "options": ["1", "0", "2", "3"], "answer": "1"},
                {"question": "Which is the smallest number?", "options": ["1", "2", "3", "0"], "answer": "0"},
                {"question": "What is 1 more than 4?", "options": ["3", "4", "5", "6"], "answer": "5"},
                {"question": "What is 5 - 4?", "options": ["1", "2", "0", "3"], "answer": "1"},
                {"question": "What is 3 + 1?", "options": ["3", "4", "5", "6"], "answer": "4"}
            ],
            "Medium": [
                {"question": "What is 5 - 2?", "options": ["1", "2", "3", "4"], "answer": "3"},
                {"question": "What comes after 9?", "options": ["10", "11", "8", "12"], "answer": "10"},
                {"question": "What is 6 + 2?", "options": ["7", "8", "9", "6"], "answer": "8"},
                {"question": "What is 10 - 4?", "options": ["6", "5", "7", "8"], "answer": "6"},
                {"question": "Which is greater: 7 or 3?", "options": ["7", "3", "Both", "None"], "answer": "7"},
                {"question": "What is 3 + 3?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "What is 2 less than 6?", "options": ["4", "3", "2", "5"], "answer": "4"},
                {"question": "What is 1 more than 6?", "options": ["7", "6", "5", "8"], "answer": "7"},
                {"question": "What is 8 - 2?", "options": ["5", "6", "7", "4"], "answer": "6"},
                {"question": "What is 2 + 5?", "options": ["6", "7", "8", "9"], "answer": "7"}
            ],
            "Hard": [
                {"question": "What is 10 - 7 + 2?", "options": ["3", "4", "5", "6"], "answer": "5"},
                {"question": "What is 9 - 3 + 1?", "options": ["6", "7", "5", "8"], "answer": "7"},
                {"question": "What is 4 + 4 - 2?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "What is the result of 2 + 2 + 2?", "options": ["4", "6", "8", "2"], "answer": "6"},
                {"question": "What is 6 - 1 - 2?", "options": ["2", "3", "4", "5"], "answer": "3"},
                {"question": "What is 5 + 5 - 5?", "options": ["5", "0", "10", "1"], "answer": "5"},
                {"question": "What is 7 - 2 + 3?", "options": ["7", "8", "9", "10"], "answer": "8"},
                {"question": "What is 8 - 4 + 1?", "options": ["4", "5", "6", "3"], "answer": "5"},
                {"question": "What is 2 + 3 + 4?", "options": ["8", "9", "7", "6"], "answer": "9"},
                {"question": "What is 10 - 2 - 3?", "options": ["4", "5", "6", "3"], "answer": "5"}
            ]
        },
        "English": {
            "Easy": [
                {"question": "Alphabet after A?", "options": ["B", "C", "D", "E"], "answer": "B"},
                {"question": "Alphabet before C?", "options": ["A", "B", "D", "E"], "answer": "B"},
                {"question": "What is the first letter of the alphabet?", "options": ["Z", "Y", "A", "B"], "answer": "A"},
                {"question": "Alphabet after D?", "options": ["E", "F", "C", "G"], "answer": "E"},
                {"question": "Which letter comes before B?", "options": ["A", "C", "D", "Z"], "answer": "A"},
                {"question": "Which of these is a vowel?", "options": ["A", "B", "C", "D"], "answer": "A"},
                {"question": "Which is a capital letter?", "options": ["a", "B", "c", "d"], "answer": "B"},
                {"question": "Which is a small letter?", "options": ["A", "B", "c", "D"], "answer": "c"},
                {"question": "Which letter is between A and C?", "options": ["B", "D", "E", "F"], "answer": "B"},
                {"question": "Which letter is after Y?", "options": ["Z", "X", "W", "A"], "answer": "Z"}
            ],
            "Medium": [
                {"question": "Which of these is a noun?", "options": ["Run", "Blue", "Cat", "Jump"], "answer": "Cat"},
                {"question": "Select the correct pronoun: She ___ a book.", "options": ["have", "has", "is", "are"], "answer": "has"},
                {"question": "Which is a verb?", "options": ["Dog", "Eat", "Fast", "Book"], "answer": "Eat"},
                {"question": "Choose the adjective: The ___ cat is black.", "options": ["Fast", "Jump", "Sing", "Run"], "answer": "Fast"},
                {"question": "What is the opposite of 'big'?", "options": ["Small", "Tall", "Fast", "Short"], "answer": "Small"},
                {"question": "Which word is a color?", "options": ["Run", "Blue", "Cat", "Jump"], "answer": "Blue"},
                {"question": "Complete the sentence: I ___ happy.", "options": ["am", "is", "are", "was"], "answer": "am"},
                {"question": "What is the plural of 'dog'?", "options": ["dogs", "dog", "doges", "dags"], "answer": "dogs"},
                {"question": "Choose the correct article: ___ apple.", "options": ["An", "A", "The", "No article"], "answer": "An"},
                {"question": "What is the past tense of 'run'?", "options": ["run", "ran", "running", "runs"], "answer": "ran"}
            ],
            "Hard": [
                {"question": "Identify the adjective: The tall boy is running.", "options": ["Tall", "Boy", "Running", "Is"], "answer": "Tall"},
                {"question": "Which sentence is correct?", "options": ["She don't like apples.", "She doesn't like apples.", "She no like apples.", "She not like apples."], "answer": "She doesn't like apples."},
                {"question": "Choose the correct conjunction: I like tea ___ coffee.", "options": ["and", "but", "or", "so"], "answer": "and"},
                {"question": "What is the plural form of 'child'?", "options": ["Childs", "Children", "Childes", "Child"], "answer": "Children"},
                {"question": "Find the verb: The dog barks loudly.", "options": ["Dog", "Barks", "Loudly", "The"], "answer": "Barks"},
                {"question": "What is the correct past tense of 'go'?", "options": ["Goed", "Went", "Going", "Go"], "answer": "Went"},
                {"question": "Choose the sentence in passive voice.", "options": ["The dog chased the cat.", "The cat was chased by the dog.", "The dog is chasing the cat.", "The cat chases the dog."], "answer": "The cat was chased by the dog."},
                {"question": "Select the adverb: She runs quickly.", "options": ["She", "Runs", "Quickly", "The"], "answer": "Quickly"},
                {"question": "Identify the pronoun: He is my friend.", "options": ["He", "Is", "My", "Friend"], "answer": "He"},
                {"question": "Which is a proper noun?", "options": ["city", "Delhi", "dog", "car"], "answer": "Delhi"}
            ]
        },
        "EVS": {
            "Easy": [
                {"question": "What do plants need to grow?", "options": ["Water", "Chocolate", "Cars", "Toys"], "answer": "Water"},
                {"question": "Which one is an animal?", "options": ["Car", "Dog", "Tree", "Flower"], "answer": "Dog"},
                {"question": "What do we breathe?", "options": ["Water", "Air", "Food", "Soil"], "answer": "Air"},
                {"question": "Which is a fruit?", "options": ["Apple", "Car", "Chair", "Pen"], "answer": "Apple"},
                {"question": "What do birds use to fly?", "options": ["Wings", "Legs", "Hands", "Eyes"], "answer": "Wings"},
                {"question": "Which is the biggest planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Jupiter"},
                {"question": "What do we wear on feet?", "options": ["Gloves", "Shoes", "Hats", "Socks"], "answer": "Shoes"},
                {"question": "Which one gives us milk?", "options": ["Cow", "Dog", "Cat", "Fish"], "answer": "Cow"},
                {"question": "Where do fish live?", "options": ["Water", "Land", "Sky", "Trees"], "answer": "Water"},
                {"question": "What do bees make?", "options": ["Honey", "Milk", "Water", "Sugar"], "answer": "Honey"}
            ],
            "Medium": [
                {"question": "Which part of plant absorbs water?", "options": ["Root", "Leaf", "Flower", "Stem"], "answer": "Root"},
                {"question": "What do we call a baby dog?", "options": ["Puppy", "Kitten", "Cub", "Calf"], "answer": "Puppy"},
                {"question": "Which planet is called the Red Planet?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "answer": "Mars"},
                {"question": "Which is a source of light?", "options": ["Sun", "Moon", "Earth", "Water"], "answer": "Sun"},
                {"question": "Where does the sun rise from?", "options": ["East", "West", "North", "South"], "answer": "East"},
                {"question": "Which animals live in water?", "options": ["Fish", "Tiger", "Elephant", "Lion"], "answer": "Fish"},
                {"question": "What do plants make during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Water", "Nitrogen"], "answer": "Oxygen"},
                {"question": "Which is the largest mammal?", "options": ["Elephant", "Whale", "Tiger", "Lion"], "answer": "Whale"},
                {"question": "What gas do we breathe in?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
                {"question": "Which animal is known as the king of the jungle?", "options": ["Lion", "Tiger", "Elephant", "Bear"], "answer": "Lion"}
            ],
            "Hard": [
                {"question": "What is photosynthesis?", "options": ["Process by which plants make food", "Animal breathing", "Water cycle", "Earth rotation"], "answer": "Process by which plants make food"},
                {"question": "Which gas is essential for burning?", "options": ["Oxygen", "Nitrogen", "Hydrogen", "Carbon Dioxide"], "answer": "Oxygen"},
                {"question": "What is the main source of energy for Earth?", "options": ["Sun", "Moon", "Stars", "Wind"], "answer": "Sun"},
                {"question": "Which organ pumps blood in our body?", "options": ["Heart", "Lungs", "Brain", "Stomach"], "answer": "Heart"},
                {"question": "What do you call animals that eat only plants?", "options": ["Herbivores", "Carnivores", "Omnivores", "Insectivores"], "answer": "Herbivores"},
                {"question": "Which layer protects Earth from harmful rays?", "options": ["Ozone layer", "Water layer", "Soil layer", "Air layer"], "answer": "Ozone layer"},
                {"question": "What is the boiling point of water?", "options": ["100°C", "0°C", "50°C", "90°C"], "answer": "100°C"},
                {"question": "What do decomposers do?", "options": ["Break down dead plants and animals", "Make food", "Give oxygen", "Store water"], "answer": "Break down dead plants and animals"},
                {"question": "Which organ helps in breathing?", "options": ["Lungs", "Heart", "Stomach", "Kidney"], "answer": "Lungs"},
                {"question": "Which planet is nearest to the sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"}
            ]
        },
                "Hindi": {
            "Easy": [
                {"question": "निम्नलिखित में से कौन सा वर्ण है?", "options": ["क", "ग", "अ", "ह"], "answer": "अ"},
                {"question": "अक्षर 'क' के बाद कौन सा अक्षर आता है?", "options": ["ख", "ग", "च", "ज"], "answer": "ख"},
                {"question": "कौन सा शब्द फूल है?", "options": ["कमल", "कुत्ता", "घर", "किताब"], "answer": "कमल"},
                {"question": "निम्नलिखित में से कौन सा रंग है?", "options": ["नीला", "कुर्सी", "कपड़ा", "खाना"], "answer": "नीला"},
                {"question": "सूरज किस दिशा से निकलता है?", "options": ["पूरब", "पश्चिम", "उत्तर", "दक्षिण"], "answer": "पूरब"},
                {"question": "निम्नलिखित में से कौन सा जानवर है?", "options": ["गाय", "पेड", "पानी", "घर"], "answer": "गाय"},
                {"question": "निम्नलिखित में से कौन सा फल है?", "options": ["सेब", "कुर्सी", "किताब", "खाना"], "answer": "सेब"},
                {"question": "कौन सा शब्द पानी है?", "options": ["जल", "पानी", "नदी", "तालाब"], "answer": "पानी"},
                {"question": "निम्नलिखित में से कौन सा वस्त्र है?", "options": ["कमीज", "किताब", "खाना", "कमल"], "answer": "कमीज"},
                {"question": "नीचे दिए गए शब्दों में से कौन सा जानवर नहीं है?", "options": ["गाय", "कुत्ता", "पक्षी", "किताब"], "answer": "किताब"}
            ],
            "Medium": [
                {"question": "निम्नलिखित में से कौन सा वाक्य सही है?", "options": ["मैं स्कूल जाता हूँ।", "मैं स्कूल जाता हैं।", "मैं स्कूल जाती हूँ।", "मैं स्कूल जाती हैं।"], "answer": "मैं स्कूल जाता हूँ।"},
                {"question": "शब्द 'घर' का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "संबंधवाचक", "क्रिया"], "answer": "एकवचन"},
                {"question": "निम्नलिखित में से कौन सा वाक्य प्रश्नवाचक है?", "options": ["तुम कैसे हो?", "मैं ठीक हूँ।", "यह मेरा घर है।", "वह बाजार गया।"], "answer": "तुम कैसे हो?"},
                {"question": "कौन सा शब्द संज्ञा है?", "options": ["खेलना", "बच्चा", "जल्दी", "सुंदर"], "answer": "बच्चा"},
                {"question": "निम्नलिखित में से कौन सा विशेषण है?", "options": ["लाल", "खेलना", "घर", "तुम"], "answer": "लाल"},
                {"question": "शब्द 'खेलना' किस प्रकार का शब्द है?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "क्रिया"},
                {"question": "निम्नलिखित में से सर्वनाम कौन सा है?", "options": ["वह", "किताब", "लड़का", "खाना"], "answer": "वह"},
                {"question": "शब्द 'अच्छा' किस प्रकार का शब्द है?", "options": ["विशेषण", "क्रिया", "संज्ञा", "सर्वनाम"], "answer": "विशेषण"},
                {"question": "निम्नलिखित में से सही वाक्य चुनिए:", "options": ["वह स्कूल जाती है।", "वह स्कूल जाता है।", "वह स्कूल जाना है।", "वह स्कूल जाते हैं।"], "answer": "वह स्कूल जाती है।"},
                {"question": "कौन सा शब्द क्रिया है?", "options": ["खाना", "लाल", "किताब", "सुंदर"], "answer": "खाना"}
            ],
            "Hard": [
                {"question": "निम्नलिखित वाक्यों में से सही वाक्य कौन सा है?", "options": ["मैंने खाना खाया।", "मैं खाना खाया।", "मैंने खाना खाए।", "मैं खाना खाए।"], "answer": "मैंने खाना खाया।"},
                {"question": "शब्द 'विद्यार्थी' का पर्यायवाची शब्द कौन सा है?", "options": ["छात्र", "गुरु", "मित्र", "अध्यापक"], "answer": "छात्र"},
                {"question": "कौन सा वाक्य भविष्य काल में है?", "options": ["मैं कल स्कूल जाऊँगा।", "मैं स्कूल गया था।", "मैं स्कूल जा रहा हूँ।", "मैं स्कूल जाता हूँ।"], "answer": "मैं कल स्कूल जाऊँगा।"},
                {"question": "निम्नलिखित में से कौन सा वचन सही है?", "options": ["हम खेलेंगे।", "हम खेलोगे।", "हम खेलूँगा।", "हम खेलती हैं।"], "answer": "हम खेलेंगे।"},
                {"question": "शब्द 'सुंदरता' किस प्रकार का शब्द है?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "संज्ञा"},
                {"question": "निम्नलिखित में से सही वाक्य चुनिए:", "options": ["तुम अच्छा गाते हो।", "तुम अच्छा गाती हो।", "तुम अच्छा गाता हो।", "तुम अच्छा गाती हैं।"], "answer": "तुम अच्छा गाते हो।"},
                {"question": "शब्द 'सहायक' का विलोम शब्द क्या है?", "options": ["विरोधी", "साथी", "दोस्त", "मित्र"], "answer": "विरोधी"},
                {"question": "निम्नलिखित में से क्रिया कौन सी है?", "options": ["खेलना", "सफेद", "खुशी", "सुंदर"], "answer": "खेलना"},
                {"question": "वाक्य 'राम ने खाना खाया।' में कर्ता कौन है?", "options": ["राम", "खाना", "ने", "खाया"], "answer": "राम"},
                {"question": "निम्नलिखित में से सही वाक्य कौन सा है?", "options": ["वह मेरे साथ आए।", "वह मेरे साथ आई।", "वह मेरे साथ आया।", "वह मेरे साथ आओ।"], "answer": "वह मेरे साथ आए।"}
            ]
        }

    },
     
    "2": {
        "Mathematics": {
            "Easy": [
                {"question": "What is 5 + 3?", "options": ["7", "8", "6", "9"], "answer": "8"},
                {"question": "What comes after 29?", "options": ["28", "30", "31", "32"], "answer": "30"},
                {"question": "Which is the smallest number?", "options": ["9", "6", "3", "1"], "answer": "1"},
                {"question": "What is 10 - 2?", "options": ["6", "9", "8", "7"], "answer": "8"},
                {"question": "How many sides does a square have?", "options": ["3", "4", "5", "6"], "answer": "4"},
                {"question": "Which number is even?", "options": ["1", "3", "5", "4"], "answer": "4"},
                {"question": "What is double of 4?", "options": ["6", "8", "10", "12"], "answer": "8"},
                {"question": "Which number comes between 45 and 47?", "options": ["44", "46", "48", "43"], "answer": "46"},
                {"question": "What is 7 - 3?", "options": ["3", "4", "5", "6"], "answer": "4"},
                {"question": "Count by twos: What comes after 2, 4, 6?", "options": ["7", "8", "9", "10"], "answer": "8"}
            ],
            "Medium": [
                {"question": "What is 9 + 8?", "options": ["17", "18", "16", "19"], "answer": "17"},
                {"question": "What is 15 - 7?", "options": ["8", "6", "7", "9"], "answer": "8"},
                {"question": "Which shape has 3 sides?", "options": ["Square", "Circle", "Triangle", "Rectangle"], "answer": "Triangle"},
                {"question": "How many tens are there in 40?", "options": ["2", "3", "4", "5"], "answer": "4"},
                {"question": "What is half of 20?", "options": ["5", "10", "15", "8"], "answer": "10"},
                {"question": "Which number is greater: 58 or 85?", "options": ["58", "85", "Both are equal", "None"], "answer": "85"},
                {"question": "Which coin is of highest value?", "options": ["1 rupee", "2 rupees", "5 rupees", "10 rupees"], "answer": "10 rupees"},
                {"question": "Add: 24 + 17 = ?", "options": ["41", "40", "42", "39"], "answer": "41"},
                {"question": "What is the time in half past 2?", "options": ["2:00", "2:30", "3:00", "1:30"], "answer": "2:30"},
                {"question": "How many days are there in a week?", "options": ["6", "7", "8", "9"], "answer": "7"}
            ],
            "Hard": [
                {"question": "Subtract: 65 - 29 = ?", "options": ["34", "36", "35", "37"], "answer": "36"},
                {"question": "Multiply: 4 × 5 = ?", "options": ["20", "25", "15", "30"], "answer": "20"},
                {"question": "How many hours in a day?", "options": ["12", "24", "18", "30"], "answer": "24"},
                {"question": "What is one-fourth of 20?", "options": ["4", "5", "6", "8"], "answer": "5"},
                {"question": "What comes next in the pattern: 10, 20, 30, ...?", "options": ["35", "40", "45", "50"], "answer": "40"},
                {"question": "What is the place value of 6 in 67?", "options": ["60", "6", "600", "7"], "answer": "60"},
                {"question": "If 3 pencils cost ₹15, what is the cost of 1 pencil?", "options": ["3", "4", "5", "6"], "answer": "5"},
                {"question": "What is the sum of the first 5 even numbers?", "options": ["20", "30", "40", "50"], "answer": "30"},
                {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "What is the missing number: 50, 45, ___, 35?", "options": ["40", "42", "44", "38"], "answer": "40"}
            ]
        },
    
    "English": {
        "Easy": [
            {"question": "What is the plural of 'cat'?", "options": ["cats", "cat", "cates", "cot"], "answer": "cats"},
            {"question": "Choose the correct word: 'I ___ a book.'", "options": ["has", "have", "had", "is"], "answer": "have"},
            {"question": "What is the opposite of 'big'?", "options": ["small", "tall", "long", "fast"], "answer": "small"},
            {"question": "Which one is a fruit?", "options": ["apple", "car", "table", "chair"], "answer": "apple"},
            {"question": "How many days are there in a week?", "options": ["5", "6", "7", "8"], "answer": "7"},
            {"question": "Fill in the blank: The sun is ___", "options": ["hot", "cold", "wet", "dry"], "answer": "hot"},
            {"question": "Which one is a color?", "options": ["blue", "cat", "run", "big"], "answer": "blue"},
            {"question": "Choose the correct pronoun: She is my ___", "options": ["brother", "sister", "father", "uncle"], "answer": "sister"},
            {"question": "What comes after letter 'B'?", "options": ["A", "C", "D", "E"], "answer": "C"},
            {"question": "Choose the correct verb: Birds ___", "options": ["fly", "run", "sit", "jump"], "answer": "fly"}
        ],
        "Medium": [
            {"question": "Choose the correct past tense: 'I ___ a cake yesterday.'", "options": ["eat", "eats", "ate", "eating"], "answer": "ate"},
            {"question": "Find the adjective: The sky is ___", "options": ["blue", "run", "tree", "sing"], "answer": "blue"},
            {"question": "Select the correct sentence:", "options": ["He are happy", "He is happy", "He am happy", "He be happy"], "answer": "He is happy"},
            {"question": "What is the plural form of 'child'?", "options": ["childs", "childes", "children", "child"], "answer": "children"},
            {"question": "Fill in the blank: She ___ to school every day.", "options": ["go", "goes", "gone", "going"], "answer": "goes"},
            {"question": "Which word is a noun?", "options": ["run", "happy", "book", "quick"], "answer": "book"},
            {"question": "What is the opposite of 'day'?", "options": ["night", "sun", "light", "moon"], "answer": "night"},
            {"question": "Choose the correct article: ___ apple a day keeps the doctor away.", "options": ["An", "A", "The", "No article"], "answer": "An"},
            {"question": "Select the correct spelling:", "options": ["beautifull", "beautifull", "beautiful", "beutiful"], "answer": "beautiful"},
            {"question": "What is the plural of 'fox'?", "options": ["foxs", "foxes", "foxx", "fox"], "answer": "foxes"}
        ],
        "Hard": [
            {"question": "Identify the verb in the sentence: 'She sings beautifully.'", "options": ["She", "sings", "beautifully", "sentence"], "answer": "sings"},
            {"question": "Choose the correct form: 'They ___ playing in the garden.'", "options": ["is", "are", "am", "was"], "answer": "are"},
            {"question": "Fill in the blank: 'I have ___ my homework.'", "options": ["do", "did", "done", "doing"], "answer": "done"},
            {"question": "What is a synonym of 'happy'?", "options": ["sad", "glad", "angry", "tired"], "answer": "glad"},
            {"question": "Select the correct sentence:", "options": ["He don't like ice cream.", "He doesn't likes ice cream.", "He doesn't like ice cream.", "He don't likes ice cream."], "answer": "He doesn't like ice cream."},
            {"question": "Choose the correct preposition: 'The book is ___ the table.'", "options": ["in", "on", "under", "between"], "answer": "on"},
            {"question": "What is the past tense of 'run'?", "options": ["runned", "ran", "run", "running"], "answer": "ran"},
            {"question": "Find the adjective: 'The quick brown fox jumps over the lazy dog.'", "options": ["quick", "fox", "jumps", "dog"], "answer": "quick"},
            {"question": "Choose the correct sentence:", "options": ["Is he coming?", "Are he coming?", "Is he comes?", "Are he come?"], "answer": "Is he coming?"},
            {"question": "Fill in the blank: 'She has been ___ for two hours.'", "options": ["sleep", "sleeping", "slept", "sleeps"], "answer": "sleeping"}
        ]
    },

    "Science": {
        "Easy": [
            {"question": "Which part of the plant makes food?", "options": ["Root", "Leaf", "Stem", "Flower"], "answer": "Leaf"},
            {"question": "What do we need to breathe?", "options": ["Water", "Oxygen", "Food", "Sunlight"], "answer": "Oxygen"},
            {"question": "Which animal gives us milk?", "options": ["Cat", "Cow", "Dog", "Lion"], "answer": "Cow"},
            {"question": "What do bees collect from flowers?", "options": ["Nectar", "Water", "Leaves", "Soil"], "answer": "Nectar"},
            {"question": "The Sun gives us ___", "options": ["Light", "Water", "Food", "Air"], "answer": "Light"},
            {"question": "Which body part helps us to see?", "options": ["Ear", "Nose", "Eye", "Hand"], "answer": "Eye"},
            {"question": "What do plants need to grow?", "options": ["Sunlight", "Food", "Clothes", "Toys"], "answer": "Sunlight"},
            {"question": "Which planet do we live on?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Earth"},
            {"question": "Water turns into ___ when it freezes.", "options": ["Ice", "Steam", "Rain", "Cloud"], "answer": "Ice"},
            {"question": "What do we use to smell things?", "options": ["Nose", "Tongue", "Eyes", "Ear"], "answer": "Nose"}
        ],
        "Medium": [
            {"question": "Which part of the body pumps blood?", "options": ["Heart", "Lungs", "Brain", "Stomach"], "answer": "Heart"},
            {"question": "What do plants absorb from the soil?", "options": ["Water", "Sunlight", "Air", "Food"], "answer": "Water"},
            {"question": "Which sense helps us hear?", "options": ["Nose", "Ear", "Mouth", "Skin"], "answer": "Ear"},
            {"question": "The process by which plants make food is called?", "options": ["Photosynthesis", "Digestion", "Respiration", "Excretion"], "answer": "Photosynthesis"},
            {"question": "Which animal is known as the 'King of the Jungle'?", "options": ["Tiger", "Elephant", "Lion", "Bear"], "answer": "Lion"},
            {"question": "What gas do plants take in?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon dioxide"},
            {"question": "Which of these is a source of water?", "options": ["River", "Mountain", "Tree", "Sun"], "answer": "River"},
            {"question": "What do we call animals that eat only plants?", "options": ["Carnivores", "Herbivores", "Omnivores", "Insectivores"], "answer": "Herbivores"},
            {"question": "Which organ helps us breathe?", "options": ["Lungs", "Kidneys", "Heart", "Brain"], "answer": "Lungs"},
            {"question": "What do you call a baby frog?", "options": ["Calf", "Caterpillar", "Tadpole", "Puppy"], "answer": "Tadpole"}
        ],
        "Hard": [
            {"question": "Which part of the plant holds it firmly in the soil?", "options": ["Stem", "Root", "Leaf", "Flower"], "answer": "Root"},
            {"question": "What is the main source of energy for Earth?", "options": ["Moon", "Sun", "Stars", "Wind"], "answer": "Sun"},
            {"question": "Which gas do humans breathe out?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"], "answer": "Carbon dioxide"},
            {"question": "What do you call animals that eat both plants and meat?", "options": ["Herbivores", "Carnivores", "Omnivores", "Insectivores"], "answer": "Omnivores"},
            {"question": "What is the process by which water changes into vapor called?", "options": ["Evaporation", "Condensation", "Precipitation", "Freezing"], "answer": "Evaporation"},
            {"question": "Which sense organ detects taste?", "options": ["Eye", "Ear", "Tongue", "Nose"], "answer": "Tongue"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "Which part of the body controls thinking?", "options": ["Heart", "Lungs", "Brain", "Stomach"], "answer": "Brain"},
            {"question": "What is the name of the process where plants release oxygen?", "options": ["Respiration", "Photosynthesis", "Transpiration", "Digestion"], "answer": "Photosynthesis"},
            {"question": "Which animals live both on land and in water?", "options": ["Mammals", "Reptiles", "Amphibians", "Birds"], "answer": "Amphibians"}
        ]
    },
    
    "Hindi": {
        "Easy": [
            {"question": "निम्नलिखित में से कौन सा अक्षर है?", "options": ["क", "123", "!", "@"], "answer": "क"},
            {"question": "अंगूठा किसका हिस्सा है?", "options": ["हाथ", "पैर", "सिर", "कंधा"], "answer": "हाथ"},
            {"question": "सूरज किस रंग का होता है?", "options": ["पीला", "नीला", "हरा", "लाल"], "answer": "पीला"},
            {"question": "पानी ठंडा होता है या गर्म?", "options": ["ठंडा", "गर्म", "दोनों", "नहीं पता"], "answer": "ठंडा"},
            {"question": "नमस्ते किसे कहते हैं?", "options": ["अलविदा", "नमस्कार", "खेल", "खाना"], "answer": "नमस्कार"},
            {"question": "तुम्हारा नाम क्या है?", "options": ["राम", "गीता", "राज", "सभी सही"], "answer": "सभी सही"},
            {"question": "सूरज कहां से निकलता है?", "options": ["पूरब", "पश्चिम", "उत्तर", "दक्षिण"], "answer": "पूरब"},
            {"question": "यह कौन सी वस्तु है?", "options": ["किताब", "फल", "पानी", "पेड़"], "answer": "किताब"},
            {"question": "स्कूल क्या होता है?", "options": ["खेल का मैदान", "पढ़ाई की जगह", "खाना खाने की जगह", "सोने की जगह"], "answer": "पढ़ाई की जगह"},
            {"question": "बारिश कब होती है?", "options": ["जब बादल होते हैं", "जब सूरज चमकता है", "जब हवा चलती है", "जब बिजली चमकती है"], "answer": "जब बादल होते हैं"}
        ],
        "Medium": [
            {"question": "निम्नलिखित में से वचन बदलो: बच्चे", "options": ["बच्चा", "बच्चों", "बच्चियों", "बच्चे"], "answer": "बच्चा"},
            {"question": "सही शब्द चुनें: सूरज ___ निकलता है।", "options": ["सभी", "सुबह", "रात", "शाम"], "answer": "सुबह"},
            {"question": "पंचतंत्र की कहानी किस लिए प्रसिद्ध है?", "options": ["जानवरों के लिए", "सिखाने के लिए", "खेलने के लिए", "खाने के लिए"], "answer": "सिखाने के लिए"},
            {"question": "नीचे दिए गए में से कौन सा शब्द क्रिया है?", "options": ["खेल", "सुंदर", "गुलाब", "लाल"], "answer": "खेल"},
            {"question": "‘लड़की’ का पुल्लिंग रूप क्या है?", "options": ["लड़का", "लड़की", "लड़के", "लड़क"], "answer": "लड़का"},
            {"question": "‘खाना’ का पर्यायवाची शब्द क्या है?", "options": ["भोजन", "नींद", "पढ़ाई", "खेल"], "answer": "भोजन"},
            {"question": "सही वाक्य चुनें:", "options": ["मैं स्कूल जाता हूँ।", "मैं स्कूल जाती हूँ।", "मैं स्कूल जाते हैं।", "मैं स्कूल जाती हैं।"], "answer": "मैं स्कूल जाता हूँ।"},
            {"question": "‘बड़ा’ का विलोम शब्द क्या है?", "options": ["छोटा", "लंबा", "मोटा", "तगड़ा"], "answer": "छोटा"},
            {"question": "किसका वचन है: ‘पक्षी उड़ रहे हैं’?", "options": ["बहुवचन", "एकवचन", "द्विवचन", "नहीं पता"], "answer": "बहुवचन"},
            {"question": "नीचे दिए गए में से कौन सा संज्ञा है?", "options": ["खेलना", "लड़का", "सुंदर", "तेज"], "answer": "लड़का"}
        ],
        "Hard": [
            {"question": "‘सूरज’ शब्द में कितने वर्ण हैं?", "options": ["3", "4", "2", "1"], "answer": "3"},
            {"question": "‘मैंने किताब पढ़ी’ वाक्य में किस प्रकार की क्रिया है?", "options": ["साधारण", "पूर्ण", "अपूर्ण", "सम्पूर्ण"], "answer": "पूर्ण"},
            {"question": "निम्नलिखित में से पर्यायवाची शब्द चुनें: 'सुंदर'", "options": ["खूबसूरत", "बदसूरत", "बड़ा", "छोटा"], "answer": "खूबसूरत"},
            {"question": "‘तुम्हारा’ का वचन और लिंग क्या है?", "options": ["एकवचन पुल्लिंग", "बहुवचन पुल्लिंग", "एकवचन स्त्रीलिंग", "बहुवचन स्त्रीलिंग"], "answer": "एकवचन पुल्लिंग"},
            {"question": "‘रोजाना’ का विलोम शब्द क्या है?", "options": ["कभी-कभी", "हमेशा", "अक्सर", "मोहब्बत"], "answer": "कभी-कभी"},
            {"question": "‘मिट्टी’ से बने घर को क्या कहते हैं?", "options": ["पक्का घर", "कच्चा घर", "टीन शेड", "मकान"], "answer": "कच्चा घर"},
            {"question": "‘धूप’ और ‘छाया’ में क्या संबंध है?", "options": ["विलोम", "समानार्थी", "कारक", "क्रिया"], "answer": "विलोम"},
            {"question": "निम्नलिखित में से कौन सा वचन है: 'पेड़'", "options": ["एकवचन", "बहुवचन", "दोवचन", "त्रिवचन"], "answer": "एकवचन"},
            {"question": "‘राम ने खाना खाया’ वाक्य में संज्ञा कौन सी है?", "options": ["राम", "खाना", "खाया", "ने"], "answer": "राम"},
            {"question": "सही वाक्य चुनें:", "options": ["वह स्कूल जाता है।", "वह स्कूल जाती है।", "वह स्कूल जाते हैं।", "वह स्कूल जाती हैं।"], "answer": "वह स्कूल जाता है।"}
        ]
    }
},

 "3": {
        "Mathematics": {
            "Easy": [
                {"question": "What is 10 + 5?", "options": ["12", "13", "14", "15"], "answer": "15"},
                {"question": "What comes after 39?", "options": ["38", "40", "41", "42"], "answer": "40"},
                {"question": "How many sides does a triangle have?", "options": ["3", "4", "5", "6"], "answer": "3"},
                {"question": "What is 7 - 3?", "options": ["3", "4", "5", "6"], "answer": "4"},
                {"question": "Which number is the smallest?", "options": ["45", "21", "18", "56"], "answer": "18"},
                {"question": "What is the place value of 4 in 342?", "options": ["40", "4", "400", "0"], "answer": "40"},
                {"question": "Which shape has 4 equal sides?", "options": ["Rectangle", "Triangle", "Square", "Circle"], "answer": "Square"},
                {"question": "What is 6 + 8?", "options": ["13", "14", "15", "16"], "answer": "14"},
                {"question": "How many days are there in a week?", "options": ["5", "6", "7", "8"], "answer": "7"},
                {"question": "What is 20 - 10?", "options": ["5", "10", "15", "20"], "answer": "10"}
            ],
            "Medium": [
                {"question": "What is 4 × 6?", "options": ["24", "26", "28", "30"], "answer": "24"},
                {"question": "Divide 20 by 4.", "options": ["4", "5", "6", "7"], "answer": "5"},
                {"question": "Which is the odd number?", "options": ["14", "18", "21", "28"], "answer": "21"},
                {"question": "Which number is greater: 278 or 287?", "options": ["278", "287", "Both same", "None"], "answer": "287"},
                {"question": "Raju has 12 pencils. He gives 3 to his friend. How many left?", "options": ["8", "9", "10", "11"], "answer": "9"},
                {"question": "Which shape is round in shape?", "options": ["Square", "Triangle", "Rectangle", "Circle"], "answer": "Circle"},
                {"question": "What is 100 - 45?", "options": ["50", "55", "60", "65"], "answer": "55"},
                {"question": "What is the time shown by the clock if the hour hand is at 3 and minute hand at 12?", "options": ["3:00", "12:00", "6:00", "9:00"], "answer": "3:00"},
                {"question": "How many 10s are there in 90?", "options": ["8", "9", "10", "11"], "answer": "9"},
                {"question": "If 1 pencil costs ₹5, what is the cost of 4 pencils?", "options": ["15", "20", "25", "30"], "answer": "20"}
            ],
            "Hard": [
                {"question": "What is the product of 12 × 5?", "options": ["60", "50", "70", "55"], "answer": "60"},
                {"question": "Find the difference: 142 - 67", "options": ["75", "77", "79", "80"], "answer": "75"},
                {"question": "What is 81 ÷ 9?", "options": ["8", "9", "10", "7"], "answer": "9"},
                {"question": "What is 7 × 8?", "options": ["54", "56", "58", "60"], "answer": "56"},
                {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
                {"question": "Which number is divisible by 3?", "options": ["27", "28", "29", "31"], "answer": "27"},
                {"question": "How many centimeters make a meter?", "options": ["10", "100", "1000", "10000"], "answer": "100"},
                {"question": "Which is greater: 3 hundreds + 5 tens or 4 hundreds?", "options": ["3 hundreds + 5 tens", "4 hundreds", "Both equal", "None"], "answer": "4 hundreds"},
                {"question": "Which unit is used to measure weight?", "options": ["Litres", "Grams", "Metres", "Seconds"], "answer": "Grams"},
                {"question": "Find the value of: (25 + 15) ÷ 5", "options": ["6", "7", "8", "9"], "answer": "8"}
            ]
        },
        "English": {
    "Easy": [
        {"question": "What is the opposite of 'big'?", "options": ["small", "tall", "fat", "wide"], "answer": "small"},
        {"question": "What do we call a baby dog?", "options": ["Kitten", "Puppy", "Cub", "Calf"], "answer": "Puppy"},
        {"question": "Which letter comes after 'C'?", "options": ["D", "E", "B", "F"], "answer": "D"},
        {"question": "Which of these is a noun?", "options": ["Run", "Apple", "Quickly", "Blue"], "answer": "Apple"},
        {"question": "What is the plural of 'book'?", "options": ["Bookes", "Books", "Bookies", "Booka"], "answer": "Books"},
        {"question": "Choose the correct article: ___ apple", "options": ["A", "An", "The", "No article"], "answer": "An"},
        {"question": "Which word rhymes with 'cat'?", "options": ["Dog", "Bat", "Cow", "Hen"], "answer": "Bat"},
        {"question": "Who is the writer of 'The Magic Garden'?", "options": ["Unknown", "Anita Desai", "Ruskin Bond", "R.K. Narayan"], "answer": "Unknown"},
        {"question": "What do birds do?", "options": ["Sing", "Cook", "Swim", "Dig"], "answer": "Sing"},
        {"question": "What is the opposite of 'happy'?", "options": ["Glad", "Joyful", "Sad", "Excited"], "answer": "Sad"}
    ],
    "Medium": [
        {"question": "Choose the correct verb: He ___ a book.", "options": ["read", "reads", "reading", "is"], "answer": "reads"},
        {"question": "What did Nina not want?", "options": ["To go to school", "To go to a wedding", "To eat food", "To sing"], "answer": "To go to a wedding"},
        {"question": "Which word is an adjective?", "options": ["Green", "Slowly", "Tiger", "Dance"], "answer": "Green"},
        {"question": "What do you do with your ears?", "options": ["See", "Smell", "Hear", "Touch"], "answer": "Hear"},
        {"question": "Pick the correct sentence:", "options": ["She going to school.", "She go school.", "She is going to school.", "She is go to school."], "answer": "She is going to school."},
        {"question": "What is the opposite of 'cold'?", "options": ["Soft", "Hot", "Short", "Dry"], "answer": "Hot"},
        {"question": "Which is a punctuation mark?", "options": ["Comma", "Letter", "Word", "Phrase"], "answer": "Comma"},
        {"question": "What is the describing word in 'a tall tree'?", "options": ["Tree", "A", "Tall", "The"], "answer": "Tall"},
        {"question": "Pick the correct question word: ___ is your name?", "options": ["Where", "When", "What", "Who"], "answer": "What"},
        {"question": "Fill in the blank: The ___ shines in the sky.", "options": ["Moon", "Star", "Sun", "Cloud"], "answer": "Sun"}
    ],
    "Hard": [
        {"question": "In the poem 'Little by Little', what grew into a tree?", "options": ["Seed", "Stone", "Leaf", "Flower"], "answer": "Seed"},
        {"question": "What is a group of lions called?", "options": ["Pack", "Flock", "Pride", "Herd"], "answer": "Pride"},
        {"question": "Choose the correct form: They ___ playing.", "options": ["was", "are", "is", "be"], "answer": "are"},
        {"question": "Which is a proper noun?", "options": ["boy", "city", "Delhi", "fruit"], "answer": "Delhi"},
        {"question": "Which word is a synonym of 'begin'?", "options": ["End", "Stop", "Start", "Go"], "answer": "Start"},
        {"question": "What is the opposite of 'clean'?", "options": ["Bright", "Neat", "Dirty", "Clear"], "answer": "Dirty"},
        {"question": "Identify the adverb: She sings sweetly.", "options": ["She", "Sings", "Sweetly", "Sings sweetly"], "answer": "Sweetly"},
        {"question": "What is the moral of 'He is My Brother'?", "options": ["Love pets", "Help your brother", "Be selfish", "Win the race"], "answer": "Help your brother"},
        {"question": "Fill in the blank: The bird is sitting ___ the tree.", "options": ["in", "on", "under", "behind"], "answer": "on"},
        {"question": "Choose the correct sentence:", "options": ["The sun rises at east.", "The sun rise in east.", "The sun rises in the east.", "Sun rise east."], "answer": "The sun rises in the east."}
    ]
},

    
    "EVS": {
    "Easy": [
        {"question": "Which part of a plant is green and makes food?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Leaf"},
        {"question": "Which animal gives us milk?", "options": ["Cow", "Dog", "Tiger", "Cat"], "answer": "Cow"},
        {"question": "What do we use to clean our hands?", "options": ["Water", "Dust", "Soil", "Paint"], "answer": "Water"},
        {"question": "Which one is a source of water?", "options": ["River", "Road", "Tree", "House"], "answer": "River"},
        {"question": "Who lives in a nest?", "options": ["Fish", "Bird", "Tiger", "Frog"], "answer": "Bird"},
        {"question": "What do we throw in a dustbin?", "options": ["Food", "Toys", "Garbage", "Water"], "answer": "Garbage"},
        {"question": "We breathe through our ___", "options": ["Mouth", "Nose", "Ears", "Eyes"], "answer": "Nose"},
        {"question": "The sun rises in the ___", "options": ["North", "West", "East", "South"], "answer": "East"},
        {"question": "Which of these is not a fruit?", "options": ["Apple", "Banana", "Potato", "Mango"], "answer": "Potato"},
        {"question": "Which of these animals can fly?", "options": ["Elephant", "Horse", "Bird", "Lion"], "answer": "Bird"}
    ],
    "Medium": [
        {"question": "Which part of the plant is under the soil?", "options": ["Leaf", "Flower", "Root", "Stem"], "answer": "Root"},
        {"question": "What is a joint family?", "options": ["Only parents", "Only children", "Big family with grandparents", "None of these"], "answer": "Big family with grandparents"},
        {"question": "What do plants need to grow?", "options": ["Soil, Water, Air, Sunlight", "Books", "Toys", "Food"], "answer": "Soil, Water, Air, Sunlight"},
        {"question": "Why do we need to drink clean water?", "options": ["To get sick", "To stay healthy", "To play", "To color"], "answer": "To stay healthy"},
        {"question": "What is the use of clothes?", "options": ["To play", "To decorate", "To cover and protect the body", "To sleep"], "answer": "To cover and protect the body"},
        {"question": "Where do fish live?", "options": ["Land", "Water", "Sky", "Nest"], "answer": "Water"},
        {"question": "Who helps us learn at school?", "options": ["Driver", "Doctor", "Teacher", "Chef"], "answer": "Teacher"},
        {"question": "Which of these is a source of drinking water?", "options": ["River", "Sea", "Pond", "Drain"], "answer": "River"},
        {"question": "What do we call people living near us?", "options": ["Enemies", "Neighbors", "Friends", "Guests"], "answer": "Neighbors"},
        {"question": "What is 'Our First School'?", "options": ["School", "Playground", "Home", "Bus"], "answer": "Home"}
    ],
    "Hard": [
        {"question": "Why do birds fly in the sky?", "options": ["They have fins", "They have wings", "They swim", "They bark"], "answer": "They have wings"},
        {"question": "What is vermicomposting?", "options": ["Growing worms", "Throwing waste", "Making compost using worms", "Killing worms"], "answer": "Making compost using worms"},
        {"question": "Which plant has no stem?", "options": ["Grass", "Banana", "Lotus", "Cactus"], "answer": "Grass"},
        {"question": "What is the function of roots?", "options": ["To make food", "To absorb water", "To grow leaves", "To fly"], "answer": "To absorb water"},
        {"question": "In which season do we wear woolen clothes?", "options": ["Summer", "Winter", "Rainy", "Spring"], "answer": "Winter"},
        {"question": "What are sense organs?", "options": ["Parts of plants", "Body parts for sensing", "Toys", "Fruits"], "answer": "Body parts for sensing"},
        {"question": "Which one is not a sense organ?", "options": ["Eyes", "Nose", "Tongue", "Leg"], "answer": "Leg"},
        {"question": "Which utensil is used to cook food?", "options": ["Pen", "Plate", "Pan", "Box"], "answer": "Pan"},
        {"question": "Why is air important for us?", "options": ["To see", "To eat", "To breathe", "To walk"], "answer": "To breathe"},
        {"question": "Which of these travels the farthest to school in the chapter 'He is My Brother'?", "options": ["The girl", "The boy", "Mother", "Teacher"], "answer": "The girl"}
    ]
},
"Hindi": {
    "Easy": [
        {"question": "हिंदी वर्णमाला में पहला अक्षर कौन सा है?", "options": ["अ", "आ", "इ", "उ"], "answer": "अ"},
        {"question": "निम्नलिखित में से कौन सा शब्द फल है?", "options": ["सेब", "कुत्ता", "पानी", "गाड़ी"], "answer": "सेब"},
        {"question": "‘मैं’ किस प्रकार का शब्द है?", "options": ["सर्वनाम", "संज्ञा", "क्रिया", "विशेषण"], "answer": "सर्वनाम"},
        {"question": "‘खेलना’ शब्द किसका उदाहरण है?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "क्रिया"},
        {"question": "निम्नलिखित में से कौन सा रंग है?", "options": ["नीला", "कुर्सी", "पानी", "गाना"], "answer": "नीला"},
        {"question": "‘बड़ा’ शब्द का पर्यायवाची क्या है?", "options": ["छोटा", "विशाल", "लंबा", "मोटा"], "answer": "विशाल"},
        {"question": "‘गाना’ शब्द का विलोम क्या है?", "options": ["रोकना", "चलना", "सोना", "नाचना"], "answer": "रोकना"},
        {"question": "निम्नलिखित में से कौन सा जानवर है?", "options": ["सांप", "किताब", "पेन", "कुर्सी"], "answer": "सांप"},
        {"question": "‘सुंदर’ शब्द किस प्रकार का है?", "options": ["संज्ञा", "विशेषण", "सर्वनाम", "क्रिया"], "answer": "विशेषण"},
        {"question": "‘तुम’ किसका उदाहरण है?", "options": ["संज्ञा", "सर्वनाम", "क्रिया", "विशेषण"], "answer": "सर्वनाम"}
    ],
    "Medium": [
        {"question": "‘राम और श्याम’ में कौन सा शब्द है?", "options": ["संज्ञा", "सर्वनाम", "विशेषण", "क्रिया"], "answer": "संज्ञा"},
        {"question": "निम्नलिखित वाक्य में क्रिया कौन सी है? ‘मेरा भाई पढ़ रहा है।’", "options": ["मेरा", "भाई", "पढ़ रहा है", "है"], "answer": "पढ़ रहा है"},
        {"question": "संधि किसे कहते हैं?", "options": ["दो शब्दों का मेल", "अक्षरों का मेल", "वाक्यों का मेल", "पंक्तियों का मेल"], "answer": "दो शब्दों का मेल"},
        {"question": "‘सफेद और लाल’ शब्द किस प्रकार के हैं?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "विशेषण"},
        {"question": "‘पढ़ाई’ शब्द किसका उदाहरण है?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "संज्ञा"},
        {"question": "निम्नलिखित में से कौन सा वाक्य है?", "options": ["लड़का", "खेलता है", "लड़का खेलता है", "खेल"], "answer": "लड़का खेलता है"},
        {"question": "‘मैं बाजार जा रहा हूँ’ में सर्वनाम कौन सा है?", "options": ["मैं", "बाजार", "जा रहा", "हूँ"], "answer": "मैं"},
        {"question": "‘सूरज’ किस प्रकार का शब्द है?", "options": ["संज्ञा", "सर्वनाम", "विशेषण", "क्रिया"], "answer": "संज्ञा"},
        {"question": "‘माँ ने खाना बनाया’ में क्रिया कौन सी है?", "options": ["माँ", "खाना", "बनाया", "ने"], "answer": "बनाया"},
        {"question": "‘लाल रंग’ में ‘लाल’ क्या है?", "options": ["संज्ञा", "विशेषण", "सर्वनाम", "क्रिया"], "answer": "विशेषण"}
    ],
    "Hard": [
        {"question": "‘रामफल’ शब्द किस प्रकार का शब्द है?", "options": ["समास", "संधि", "एकवचन", "बहुवचन"], "answer": "समास"},
        {"question": "‘विद्यार्थी’ शब्द में कितने वर्ण हैं?", "options": ["5", "6", "7", "8"], "answer": "6"},
        {"question": "संधि विच्छेद करें: ‘रामायण’", "options": ["राम + अयन", "राम + अयण", "रा + मायण", "र + आमायण"], "answer": "राम + अयन"},
        {"question": "‘सीता ने कविता पढ़ी’ में किस प्रकार का क्रिया प्रयोग हुआ है?", "options": ["साधारण", "समयवाचक", "भाववाचक", "विषयवाचक"], "answer": "साधारण"},
        {"question": "निम्नलिखित में से कौन सा बहुवचन शब्द है?", "options": ["किताब", "लड़के", "लड़की", "फल"], "answer": "लड़के"},
        {"question": "‘मित्र’ शब्द का विलोम क्या है?", "options": ["शत्रु", "सखा", "दोस्त", "अलग"], "answer": "शत्रु"},
        {"question": "‘तुम्हारा’ किस प्रकार का शब्द है?", "options": ["सर्वनाम", "संज्ञा", "विशेषण", "क्रिया"], "answer": "सर्वनाम"},
        {"question": "‘खेल रहे हैं’ किस प्रकार की क्रिया है?", "options": ["साधारण", "समयवाचक", "भाववाचक", "विषयवाचक"], "answer": "समयवाचक"},
        {"question": "‘अच्छा’ शब्द किस प्रकार का शब्द है?", "options": ["विशेषण", "संज्ञा", "सर्वनाम", "क्रिया"], "answer": "विशेषण"},
        {"question": "‘राम और श्याम स्कूल गए’ में कौन सा शब्द कारक है?", "options": ["राम", "श्याम", "स्कूल", "गए"], "answer": "स्कूल"}
    ]
}
},

"4": {
        "Math": {
            "Easy": [
                {"question": "What is the place value of 5 in 3,562?", "options": ["5", "50", "500", "5,000"], "answer": "50"},
                {"question": "Which is the smallest 4-digit number?", "options": ["1000", "999", "100", "10000"], "answer": "1000"},
                {"question": "What is 235 + 564?", "options": ["799", "789", "809", "899"], "answer": "799"},
                {"question": "How many sides does a triangle have?", "options": ["3", "4", "5", "6"], "answer": "3"},
                {"question": "Which fraction is equivalent to 1/2?", "options": ["2/4", "3/5", "1/3", "3/4"], "answer": "2/4"},
                {"question": "How many hours are there in a day?", "options": ["12", "24", "48", "36"], "answer": "24"},
                {"question": "Which number comes after 4999?", "options": ["4998", "5000", "4999", "6000"], "answer": "5000"},
                {"question": "What is the sum of 10 and 15?", "options": ["20", "25", "30", "15"], "answer": "25"},
                {"question": "How many sides does a square have?", "options": ["3", "4", "5", "6"], "answer": "4"},
                {"question": "What is the weight unit?", "options": ["Meter", "Kilogram", "Litre", "Second"], "answer": "Kilogram"}
            ],
            "Medium": [
                {"question": "What is 456 - 278?", "options": ["178", "188", "178", "198"], "answer": "178"},
                {"question": "Which of the following is a prime number?", "options": ["4", "6", "7", "9"], "answer": "7"},
                {"question": "What is the product of 25 and 4?", "options": ["100", "90", "110", "120"], "answer": "100"},
                {"question": "Which of these is the largest?", "options": ["0.4", "0.44", "0.444", "0.4"], "answer": "0.444"},
                {"question": "What is 3/4 + 1/4?", "options": ["1", "1/2", "3/4", "2"], "answer": "1"},
                {"question": "How many days are there in a leap year?", "options": ["365", "364", "366", "367"], "answer": "366"},
                {"question": "Find the missing number: 7 x __ = 56", "options": ["7", "8", "9", "6"], "answer": "8"},
                {"question": "What is the perimeter of a rectangle with length 8cm and width 5cm?", "options": ["26cm", "40cm", "13cm", "30cm"], "answer": "26cm"},
                {"question": "Which is a factor of 36?", "options": ["4", "9", "12", "All of these"], "answer": "All of these"},
                {"question": "Convert 5000 grams into kilograms.", "options": ["0.5 kg", "5 kg", "50 kg", "500 kg"], "answer": "5 kg"}
            ],
            "Hard": [
                {"question": "What is the LCM of 6 and 8?", "options": ["12", "24", "18", "16"], "answer": "24"},
                {"question": "Simplify: (3/5) ÷ (1/10)", "options": ["6", "5", "3", "10"], "answer": "6"},
                {"question": "If the length of a rectangle is doubled and width is halved, what happens to the area?", "options": ["Remains same", "Doubles", "Halves", "Quadruples"], "answer": "Remains same"},
                {"question": "A triangle has angles 35° and 65°. What is the third angle?", "options": ["90°", "80°", "75°", "100°"], "answer": "80°"},
                {"question": "Convert 3 hours 45 minutes into minutes.", "options": ["225", "180", "210", "230"], "answer": "225"},
                {"question": "The product of two numbers is 144 and one of the numbers is 12. Find the other number.", "options": ["10", "11", "12", "15"], "answer": "12"},
                {"question": "Find the value of x: 5x - 10 = 20", "options": ["2", "4", "6", "8"], "answer": "6"},
                {"question": "Which is the smallest fraction?", "options": ["2/3", "3/4", "1/2", "4/5"], "answer": "1/2"},
                {"question": "What is the volume of a cube with side 4 cm?", "options": ["64 cm³", "16 cm³", "32 cm³", "48 cm³"], "answer": "64 cm³"},
                {"question": "If the time is 3:15 PM now, what will be the time after 2 hours and 45 minutes?", "options": ["6:00 PM", "6:15 PM", "5:30 PM", "6:45 PM"], "answer": "6:00 PM"}
            ]
        },
        "English": {
            "Easy": [
                {"question": "What is the plural of 'book'?", "options": ["books", "bookes", "bookies", "book"], "answer": "books"},
                {"question": "Choose the correct article: ___ apple a day keeps the doctor away.", "options": ["A", "An", "The", "No article"], "answer": "An"},
                {"question": "Which word is a noun?", "options": ["run", "happy", "dog", "blue"], "answer": "dog"},
                {"question": "What is the opposite of 'hot'?", "options": ["cold", "warm", "cool", "heat"], "answer": "cold"},
                {"question": "Fill in the blank: She ___ playing in the park.", "options": ["is", "are", "am", "be"], "answer": "is"},
                {"question": "Choose the correct pronoun: This is ___ book.", "options": ["my", "mine", "me", "I"], "answer": "my"},
                {"question": "What is the past tense of 'play'?", "options": ["played", "play", "plays", "playing"], "answer": "played"},
                {"question": "Identify the adjective: The red ball is mine.", "options": ["red", "ball", "mine", "is"], "answer": "red"},
                {"question": "How many vowels are there in the word 'school'?", "options": ["2", "3", "4", "5"], "answer": "2"},
                {"question": "Complete the sentence: The cat is ___ the table.", "options": ["on", "in", "at", "under"], "answer": "on"}
            ],
            "Medium": [
                {"question": "Choose the correct verb: They ___ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "go"},
                {"question": "Select the correct sentence.", "options": ["She are reading.", "She is reading.", "She am reading.", "She be reading."], "answer": "She is reading."},
                {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childes", "child"], "answer": "children"},
                {"question": "Find the synonym of 'happy'.", "options": ["sad", "joyful", "angry", "tired"], "answer": "joyful"},
                {"question": "Identify the adverb in the sentence: He runs quickly.", "options": ["He", "runs", "quickly", "none"], "answer": "quickly"},
                {"question": "Choose the correct tense: She ___ her homework yesterday.", "options": ["did", "do", "does", "doing"], "answer": "did"},
                {"question": "Select the correct preposition: The bird is ___ the tree.", "options": ["on", "in", "under", "beside"], "answer": "on"},
                {"question": "Choose the correct conjunction: I like tea ___ coffee.", "options": ["and", "but", "or", "so"], "answer": "and"},
                {"question": "Identify the subject in the sentence: The dog barks loudly.", "options": ["dog", "barks", "loudly", "The"], "answer": "dog"},
                {"question": "Fill in the blank with correct pronoun: This is ___ pen.", "options": ["her", "his", "my", "mine"], "answer": "my"}
            ],
            "Hard": [
                {"question": "Choose the correct sentence.", "options": ["He don't like apples.", "He doesn't like apples.", "He doesn't likes apples.", "He not like apples."], "answer": "He doesn't like apples."},
                {"question": "Identify the indirect object: She gave him a gift.", "options": ["She", "him", "a gift", "gave"], "answer": "him"},
                {"question": "Find the antonym of 'ancient'.", "options": ["old", "modern", "ancient", "historic"], "answer": "modern"},
                {"question": "Choose the correct form: Neither of the boys ___ coming.", "options": ["are", "is", "were", "be"], "answer": "is"},
                {"question": "Identify the type of sentence: 'Close the door!'", "options": ["Imperative", "Interrogative", "Declarative", "Exclamatory"], "answer": "Imperative"},
                {"question": "Choose the correct passive voice: 'She wrote a letter.'", "options": ["A letter is written by her.", "A letter was written by her.", "A letter wrote by her.", "A letter is write by her."], "answer": "A letter was written by her."},
                {"question": "Fill in the blank with correct tense: By next year, I ___ finished my studies.", "options": ["will have", "will", "have", "had"], "answer": "will have"},
                {"question": "What is the meaning of the idiom 'Break the ice'?", "options": ["To start a conversation", "To break something", "To feel cold", "To get angry"], "answer": "To start a conversation"},
                {"question": "Choose the correct reported speech: He said, 'I am tired.'", "options": ["He said he was tired.", "He said he is tired.", "He says he was tired.", "He said he will be tired."], "answer": "He said he was tired."},
                {"question": "Identify the correct spelling.", "options": ["Recieve", "Receive", "Recive", "Receeve"], "answer": "Receive"}
            ]
        },
        "EVS": {
            "Easy": [
                {
                    "question": "Which part of the plant absorbs water from the soil?",
                    "options": ["Roots", "Stem", "Leaves", "Flowers"],
                    "answer": "Roots"
                },
                {
                    "question": "What do we call animals that eat only plants?",
                    "options": ["Herbivores", "Carnivores", "Omnivores", "Insects"],
                    "answer": "Herbivores"
                },
                {
                    "question": "Which of these is a source of water?",
                    "options": ["River", "Mountain", "Rock", "Sun"],
                    "answer": "River"
                },
                {
                    "question": "What do bees make?",
                    "options": ["Honey", "Milk", "Eggs", "Silk"],
                    "answer": "Honey"
                },
                {
                    "question": "The Sun provides us with?",
                    "options": ["Light", "Electricity", "Water", "Food"],
                    "answer": "Light"
                },
                {
                    "question": "Which is a useful product of trees?",
                    "options": ["Wood", "Stone", "Water", "Coal"],
                    "answer": "Wood"
                },
                {
                    "question": "Which one is a living thing?",
                    "options": ["Rock", "Water", "Cat", "Air"],
                    "answer": "Cat"
                },
                {
                    "question": "Where do fish live?",
                    "options": ["Water", "Land", "Air", "Tree"],
                    "answer": "Water"
                },
                {
                    "question": "Which gas do plants need for photosynthesis?",
                    "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"],
                    "answer": "Carbon dioxide"
                },
                {
                    "question": "Which is used for cooking food?",
                    "options": ["Fire", "Water", "Soil", "Air"],
                    "answer": "Fire"
                }
            ],
            "Medium": [
                {
                    "question": "Which part of the plant carries food from leaves to other parts?",
                    "options": ["Stem", "Roots", "Flowers", "Fruits"],
                    "answer": "Stem"
                },
                {
                    "question": "Which animals give us wool?",
                    "options": ["Sheep", "Cow", "Goat", "Horse"],
                    "answer": "Sheep"
                },
                {
                    "question": "What do we call animals that eat both plants and animals?",
                    "options": ["Omnivores", "Herbivores", "Carnivores", "Insects"],
                    "answer": "Omnivores"
                },
                {
                    "question": "Why should we save water?",
                    "options": ["Because it is limited", "Because it is dirty", "Because it is cheap", "Because it is colorless"],
                    "answer": "Because it is limited"
                },
                {
                    "question": "Which of these is a non-living thing?",
                    "options": ["Bird", "Water", "Tree", "Cat"],
                    "answer": "Water"
                },
                {
                    "question": "Which gas do humans breathe in?",
                    "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
                    "answer": "Oxygen"
                },
                {
                    "question": "What is soil made up of?",
                    "options": ["Rocks and minerals", "Water only", "Air only", "Plants"],
                    "answer": "Rocks and minerals"
                },
                {
                    "question": "Which energy do we get from the Sun?",
                    "options": ["Solar energy", "Wind energy", "Hydro energy", "Electric energy"],
                    "answer": "Solar energy"
                },
                {
                    "question": "How do plants help us?",
                    "options": ["By giving oxygen", "By giving water", "By giving soil", "By giving fire"],
                    "answer": "By giving oxygen"
                },
                {
                    "question": "Which of these is a natural resource?",
                    "options": ["Air", "Plastic", "Paper", "Glass"],
                    "answer": "Air"
                }
            ],
            "Hard": [
                {
                    "question": "What is photosynthesis?",
                    "options": [
                        "Process by which plants make food",
                        "Process by which animals eat plants",
                        "Process by which plants absorb water",
                        "Process by which animals breathe"
                    ],
                    "answer": "Process by which plants make food"
                },
                {
                    "question": "Which layer of the Earth do we live on?",
                    "options": ["Crust", "Mantle", "Core", "Atmosphere"],
                    "answer": "Crust"
                },
                {
                    "question": "Which gas causes air pollution and harms living beings?",
                    "options": ["Carbon monoxide", "Oxygen", "Nitrogen", "Hydrogen"],
                    "answer": "Carbon monoxide"
                },
                {
                    "question": "What is a habitat?",
                    "options": [
                        "The natural home of an animal or plant",
                        "A type of plant",
                        "A tool used by humans",
                        "A type of rock"
                    ],
                    "answer": "The natural home of an animal or plant"
                },
                {
                    "question": "How can we reduce pollution?",
                    "options": [
                        "By planting trees",
                        "By cutting trees",
                        "By burning plastic",
                        "By wasting water"
                    ],
                    "answer": "By planting trees"
                },
                {
                    "question": "What is an endangered species?",
                    "options": [
                        "A species at risk of extinction",
                        "A species that lives in water",
                        "A species that is very common",
                        "A species that only eats plants"
                    ],
                    "answer": "A species at risk of extinction"
                },
                {
                    "question": "Which of the following is a renewable resource?",
                    "options": ["Solar energy", "Coal", "Petroleum", "Natural gas"],
                    "answer": "Solar energy"
                },
                {
                    "question": "Why should we not waste food?",
                    "options": [
                        "Because many people are hungry",
                        "Because food is cheap",
                        "Because food is easy to make",
                        "Because it smells good"
                    ],
                    "answer": "Because many people are hungry"
                },
                {
                    "question": "Which part of the plant carries water from roots to leaves?",
                    "options": ["Xylem", "Phloem", "Stem", "Leaf"],
                    "answer": "Xylem"
                },
                {
                    "question": "What is composting?",
                    "options": [
                        "Turning organic waste into manure",
                        "Burning waste in fire",
                        "Throwing garbage in river",
                        "Making plastic from waste"
                    ],
                    "answer": "Turning organic waste into manure"
                }
            ]
        },
        "Hindi": {
            "Easy": [
                {
                    "question": "‘लड़का’ शब्द का वचन क्या है?",
                    "options": ["एकवचन", "बहुवचन", "विभक्ति", "कारक"],
                    "answer": "एकवचन"
                },
                {
                    "question": "नीचे दिए गए में से कौन सा विशेषण है?",
                    "options": ["सुंदर", "खेलना", "खुशी", "खाना"],
                    "answer": "सुंदर"
                },
                {
                    "question": "‘मैं’ किस प्रकार का सर्वनाम है?",
                    "options": ["पुरुषवाचक", "निजवाचक", "संबंधवाचक", "अनिर्दिष्ट"],
                    "answer": "निजवाचक"
                },
                {
                    "question": "‘घर’ शब्द का विलोम शब्द क्या है?",
                    "options": ["मंदिर", "स्कूल", "बाहर", "सड़क"],
                    "answer": "बाहर"
                },
                {
                    "question": "किस वाक्य में क्रिया है?",
                    "options": ["वह खेल रहा है।", "यह एक सुंदर फूल है।", "आम मीठा होता है।", "गुलाब लाल रंग का है।"],
                    "answer": "वह खेल रहा है।"
                },
                {
                    "question": "‘रानी’ शब्द का लिंग क्या है?",
                    "options": ["स्त्रीलिंग", "पुल्लिंग", "नपुंसकलिंग", "बहुवचन"],
                    "answer": "स्त्रीलिंग"
                },
                {
                    "question": "नीचे दिए गए शब्द में कौन-सा समास है?",
                    "options": ["जलपान", "फल", "घर", "खेल"],
                    "answer": "जलपान"
                },
                {
                    "question": "‘आम’ किस प्रकार का शब्द है?",
                    "options": ["संज्ञा", "सर्वनाम", "विशेषण", "क्रिया"],
                    "answer": "संज्ञा"
                },
                {
                    "question": "‘राम’ किस वचन में है?",
                    "options": ["एकवचन", "बहुवचन", "विभक्ति", "संज्ञा"],
                    "answer": "एकवचन"
                },
                {
                    "question": "वाक्य पूरा करो: वह ____ पढ़ रहा है।",
                    "options": ["खेल", "खेलता", "खेल रही", "खेलता है"],
                    "answer": "खेलता है"
                }
            ],
            "Medium": [
                {
                    "question": "नीचे दिए गए में से कौन-सा पर्यायवाची शब्द है ‘सुंदर’ का?",
                    "options": ["खूबसूरत", "बुरा", "मोटा", "लाल"],
                    "answer": "खूबसूरत"
                },
                {
                    "question": "सही वाक्य चुनिए:",
                    "options": [
                        "मैं स्कूल जाता हूँ।",
                        "मैं स्कूल जाती हूँ।",
                        "मैं स्कूल जाना।",
                        "मैं स्कूल जाते हैं।"
                    ],
                    "answer": "मैं स्कूल जाता हूँ।"
                },
                {
                    "question": "‘खेल’ शब्द का क्या रूप है?",
                    "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"],
                    "answer": "संज्ञा"
                },
                {
                    "question": "वाक्य में ‘तेज़’ किस प्रकार का शब्द है?",
                    "options": ["विशेषण", "क्रिया", "संज्ञा", "सर्वनाम"],
                    "answer": "विशेषण"
                },
                {
                    "question": "नीचे दिए गए शब्द में ‘अधिकार’ किसका पर्यायवाची है?",
                    "options": ["हक", "अपराध", "धन", "शक्ति"],
                    "answer": "हक"
                },
                {
                    "question": "‘लड़कियाँ’ शब्द का बहुवचन क्या है?",
                    "options": ["लड़की", "लड़कियाँ", "लड़कों", "लड़का"],
                    "answer": "लड़कियाँ"
                },
                {
                    "question": "‘वहां’ किस प्रकार का शब्द है?",
                    "options": ["सर्वनाम", "क्रिया", "विशेषण", "संबंधबोधक"],
                    "answer": "संबंधबोधक"
                },
                {
                    "question": "सही वाक्य चुनिए:",
                    "options": [
                        "तुम घर जा रहे हो।",
                        "तुम घर जाता हो।",
                        "तुम घर जाता है।",
                        "तुम घर जाना है।"
                    ],
                    "answer": "तुम घर जा रहे हो।"
                },
                {
                    "question": "नीचे दिए गए में से कौन-सा वचन है?",
                    "options": ["पाठशाला", "पाठशालाएँ", "पाठशाला में", "पाठशाला से"],
                    "answer": "पाठशालाएँ"
                },
                {
                    "question": "‘जल्दी’ शब्द किसका उदाहरण है?",
                    "options": ["क्रिया", "विशेषण", "क्रिया विशेषण", "संज्ञा"],
                    "answer": "क्रिया विशेषण"
                }
            ],
            "Hard": [
                {
                    "question": "‘राम ने सीता को फल दिया।’ इस वाक्य में ‘सीता’ किस कारक में है?",
                    "options": ["कर्म कारक", "कर्तृ कारक", "सम्प्रदान कारक", "अपादान कारक"],
                    "answer": "सम्प्रदान कारक"
                },
                {
                    "question": "‘नीलम’ किस प्रकार का वचन है?",
                    "options": ["संज्ञा", "सर्वनाम", "विशेषण", "क्रिया"],
                    "answer": "संज्ञा"
                },
                {
                    "question": "‘मैंने किताब पढ़ी।’ वाक्य में ‘मैंने’ किस कारक में है?",
                    "options": ["कर्तृ कारक", "कर्म कारक", "अपादान कारक", "सम्प्रदान कारक"],
                    "answer": "कर्तृ कारक"
                },
                {
                    "question": "‘शब्दों’ का कारक रूप क्या है?",
                    "options": ["बहुवचन", "एकवचन", "संबोधन", "विभक्ति"],
                    "answer": "विभक्ति"
                },
                {
                    "question": "नीचे दिए गए में से कौन-सा समास है?",
                    "options": ["राजपुत्र", "पुत्र", "राजा", "राज्य"],
                    "answer": "राजपुत्र"
                },
                {
                    "question": "‘वहां’ और ‘यहां’ में क्या भेद है?",
                    "options": [
                        "दूरी का भेद",
                        "समय का भेद",
                        "संख्या का भेद",
                        "लिंग का भेद"
                    ],
                    "answer": "दूरी का भेद"
                },
                {
                    "question": "‘कवि’ और ‘कविता’ में कौन-सा लिंग है?",
                    "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "बहुवचन"],
                    "answer": "पुल्लिंग"
                },
                {
                    "question": "‘दौड़ना’ किस प्रकार का क्रिया है?",
                    "options": ["सक्रिय क्रिया", "निष्क्रिय क्रिया", "सहायक क्रिया", "भाववाचक क्रिया"],
                    "answer": "सक्रिय क्रिया"
                },
                {
                    "question": "‘सूरज निकला है।’ वाक्य का प्रकार क्या है?",
                    "options": ["वर्णनात्मक", "विस्मयादिबोधक", "आज्ञार्थक", "प्रश्नवाचक"],
                    "answer": "वर्णनात्मक"
                },
                {
                    "question": "नीचे दिए गए में से कौन-सा विशेषण नहीं है?",
                    "options": ["सुंदर", "लाल", "चलना", "मीठा"],
                    "answer": "चलना"
                }
            ]
        }
    },
    "5": {
    "Mathematics": {
        "Easy": [
            {"question": "What is 345 + 567?", "options": ["912", "900", "802", "1000"], "answer": "912"},
            {"question": "What is the place value of 7 in 7,345?", "options": ["700", "7", "70", "7000"], "answer": "7000"},
            {"question": "What is 1000 - 567?", "options": ["433", "4330", "533", "530"], "answer": "433"},
            {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
            {"question": "What is the value of 9 × 8?", "options": ["72", "81", "64", "78"], "answer": "72"},
            {"question": "What is half of 50?", "options": ["20", "25", "30", "15"], "answer": "25"},
            {"question": "Which number comes after 4999?", "options": ["5000", "4998", "4900", "6000"], "answer": "5000"},
            {"question": "What is 15 ÷ 3?", "options": ["4", "5", "6", "3"], "answer": "5"},
            {"question": "What is the sum of the angles in a triangle?", "options": ["180°", "90°", "360°", "270°"], "answer": "180°"},
            {"question": "Which number is a multiple of 5?", "options": ["21", "25", "28", "33"], "answer": "25"}
        ],
        "Medium": [
            {"question": "What is the LCM of 6 and 8?", "options": ["14", "24", "48", "12"], "answer": "24"},
            {"question": "What is 3/4 as a decimal?", "options": ["0.25", "0.5", "0.75", "1.25"], "answer": "0.75"},
            {"question": "Find the perimeter of a rectangle with length 8 cm and width 5 cm.", "options": ["26 cm", "40 cm", "13 cm", "20 cm"], "answer": "26 cm"},
            {"question": "What is 15% of 200?", "options": ["20", "25", "30", "35"], "answer": "30"},
            {"question": "Which fraction is equivalent to 2/3?", "options": ["4/6", "3/4", "2/5", "5/6"], "answer": "4/6"},
            {"question": "What is the volume of a cube with side 3 cm?", "options": ["9 cm³", "27 cm³", "18 cm³", "12 cm³"], "answer": "27 cm³"},
            {"question": "What is the product of 0.5 and 0.2?", "options": ["0.1", "0.7", "0.05", "0.2"], "answer": "0.1"},
            {"question": "Which is a prime number?", "options": ["21", "23", "25", "27"], "answer": "23"},
            {"question": "What is the area of a square with side 7 cm?", "options": ["49 cm²", "14 cm²", "28 cm²", "21 cm²"], "answer": "49 cm²"},
            {"question": "What is the difference between 1000 and 765?", "options": ["245", "235", "225", "255"], "answer": "235"}
        ],
        "Hard": [
            {"question": "Simplify: (5 × 4) + (12 ÷ 3) - 7", "options": ["15", "17", "18", "20"], "answer": "15"},
            {"question": "If the radius of a circle is 7 cm, what is its circumference? (Use π = 22/7)", "options": ["44 cm", "42 cm", "49 cm", "14 cm"], "answer": "44 cm"},
            {"question": "Find the HCF of 18 and 24.", "options": ["6", "12", "18", "24"], "answer": "6"},
            {"question": "What is the decimal form of 7/8?", "options": ["0.75", "0.875", "0.85", "0.8"], "answer": "0.875"},
            {"question": "Convert 3 hours 45 minutes into minutes.", "options": ["215", "230", "225", "240"], "answer": "225"},
            {"question": "Solve for x: 2x + 7 = 19", "options": ["6", "7", "5", "4"], "answer": "6"},
            {"question": "If a triangle has sides 5 cm, 12 cm and 13 cm, what type of triangle is it?", "options": ["Equilateral", "Isosceles", "Right-angled", "Scalene"], "answer": "Right-angled"},
            {"question": "What is the mean of these numbers: 5, 10, 15, 20, 25?", "options": ["15", "12", "10", "20"], "answer": "15"},
            {"question": "What is the median of the set: 3, 9, 7, 5, 11?", "options": ["7", "9", "5", "11"], "answer": "7"},
            {"question": "If a car travels 60 km in 1 hour 15 minutes, what is its average speed in km/h?", "options": ["48", "45", "50", "60"], "answer": "48"}
        ]
    },
    "English": {
        "Easy": [
            {"question": "Choose the correct plural form: 'fox'", "options": ["foxes", "foxs", "foxies", "foxe"], "answer": "foxes"},
            {"question": "Fill in the blank: She ___ playing in the garden.", "options": ["is", "are", "am", "be"], "answer": "is"},
            {"question": "What is the past tense of 'go'?", "options": ["goed", "went", "goes", "going"], "answer": "went"},
            {"question": "Choose the correct article: ___ orange is sweet.", "options": ["A", "An", "The", "No article"], "answer": "An"},
            {"question": "Select the noun: 'The cat is sleeping.'", "options": ["cat", "is", "sleeping", "the"], "answer": "cat"},
            {"question": "Identify the pronoun: 'He is my friend.'", "options": ["He", "my", "friend", "is"], "answer": "He"},
            {"question": "What is the opposite of 'happy'?", "options": ["sad", "angry", "tired", "fast"], "answer": "sad"},
            {"question": "Fill in the blank: I ___ a book.", "options": ["have", "has", "had", "having"], "answer": "have"},
            {"question": "Choose the correct spelling:", "options": ["friend", "freind", "frend", "friand"], "answer": "friend"},
            {"question": "What is the correct sentence?", "options": ["She are running.", "She is running.", "She am running.", "She be running."], "answer": "She is running."}
        ],
        "Medium": [
            {"question": "Choose the correct verb: They ___ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "go"},
            {"question": "Select the correct sentence.", "options": ["He don't like apples.", "He doesn't like apples.", "He doesn't likes apples.", "He not like apples."], "answer": "He doesn't like apples."},
            {"question": "Find the synonym of 'happy'.", "options": ["sad", "joyful", "angry", "tired"], "answer": "joyful"},
            {"question": "Identify the adverb in the sentence: She sings beautifully.", "options": ["She", "sings", "beautifully", "none"], "answer": "beautifully"},
            {"question": "Choose the correct tense: She ___ her homework yesterday.", "options": ["did", "do", "does", "doing"], "answer": "did"},
            {"question": "Select the correct preposition: The book is ___ the table.", "options": ["on", "in", "under", "beside"], "answer": "on"},
            {"question": "Choose the correct conjunction: I like tea ___ coffee.", "options": ["and", "but", "or", "so"], "answer": "and"},
            {"question": "Identify the subject in the sentence: The dog barks loudly.", "options": ["dog", "barks", "loudly", "The"], "answer": "dog"},
            {"question": "Fill in the blank with correct pronoun: This is ___ pen.", "options": ["her", "his", "my", "mine"], "answer": "my"},
            {"question": "What is the plural of 'child'?", "options": ["childs", "children", "childes", "child"], "answer": "children"}
        ],
        "Hard": [
            {"question": "Identify the indirect object: She gave him a gift.", "options": ["She", "him", "a gift", "gave"], "answer": "him"},
            {"question": "Find the antonym of 'ancient'.", "options": ["old", "modern", "ancient", "historic"], "answer": "modern"},
            {"question": "Choose the correct form: Neither of the boys ___ coming.", "options": ["are", "is", "were", "be"], "answer": "is"},
            {"question": "Identify the type of sentence: 'Close the door!'", "options": ["Imperative", "Interrogative", "Declarative", "Exclamatory"], "answer": "Imperative"},
            {"question": "Choose the correct passive voice: 'She wrote a letter.'", "options": ["A letter is written by her.", "A letter was written by her.", "A letter wrote by her.", "A letter is write by her."], "answer": "A letter was written by her."},
            {"question": "Fill in the blank with correct tense: By next year, I ___ finished my studies.", "options": ["will have", "will", "have", "had"], "answer": "will have"},
            {"question": "What is the meaning of the idiom 'Break the ice'?", "options": ["To start a conversation", "To break something", "To feel cold", "To get angry"], "answer": "To start a conversation"},
            {"question": "Choose the correct reported speech: He said, 'I am tired.'", "options": ["He said he was tired.", "He said he is tired.", "He says he was tired.", "He said he will be tired."], "answer": "He said he was tired."},
            {"question": "Identify the correct spelling.", "options": ["Recieve", "Receive", "Recive", "Receeve"], "answer": "Receive"},
            {"question": "What is the meaning of the phrase 'Once in a blue moon'?", "options": ["Very rarely", "Very often", "Every day", "Never"], "answer": "Very rarely"}
        ]
    },
    "Science": {
        "Easy": [
            {"question": "What do plants need to make their food?", "options": ["Water", "Sunlight", "Air", "All of these"], "answer": "All of these"},
            {"question": "Which part of the plant absorbs water?", "options": ["Leaves", "Stem", "Roots", "Flowers"], "answer": "Roots"},
            {"question": "What is the boiling point of water?", "options": ["50°C", "100°C", "150°C", "200°C"], "answer": "100°C"},
            {"question": "Which sense organ helps us to see?", "options": ["Ear", "Nose", "Eye", "Tongue"], "answer": "Eye"},
            {"question": "What do we call animals that eat only plants?", "options": ["Herbivores", "Carnivores", "Omnivores", "Insectivores"], "answer": "Herbivores"},
            {"question": "Which gas do we breathe in to live?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "The Sun is a ___?", "options": ["Planet", "Star", "Moon", "Comet"], "answer": "Star"},
            {"question": "Which part of the body pumps blood?", "options": ["Brain", "Heart", "Lungs", "Kidneys"], "answer": "Heart"},
            {"question": "Water changes into vapor by the process of?", "options": ["Condensation", "Evaporation", "Precipitation", "Freezing"], "answer": "Evaporation"},
            {"question": "What do bees collect from flowers?", "options": ["Pollen", "Water", "Soil", "Leaves"], "answer": "Pollen"}
        ],
        "Medium": [
            {"question": "What do we call animals that eat both plants and animals?", "options": ["Herbivores", "Carnivores", "Omnivores", "Insectivores"], "answer": "Omnivores"},
            {"question": "Which organ helps us to breathe?", "options": ["Heart", "Lungs", "Brain", "Stomach"], "answer": "Lungs"},
            {"question": "What is the main source of energy for the Earth?", "options": ["Moon", "Sun", "Stars", "Water"], "answer": "Sun"},
            {"question": "Which process helps plants to make food?", "options": ["Photosynthesis", "Respiration", "Digestion", "Evaporation"], "answer": "Photosynthesis"},
            {"question": "Which of these is a non-renewable source of energy?", "options": ["Solar", "Wind", "Coal", "Hydro"], "answer": "Coal"},
            {"question": "Which blood cells help fight infections?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "White blood cells"},
            {"question": "Which part of the eye controls the amount of light entering?", "options": ["Cornea", "Iris", "Pupil", "Retina"], "answer": "Iris"},
            {"question": "What type of animals are frogs?", "options": ["Reptiles", "Mammals", "Amphibians", "Birds"], "answer": "Amphibians"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What do we call the movement of water from plants to the atmosphere?", "options": ["Transpiration", "Evaporation", "Condensation", "Precipitation"], "answer": "Transpiration"}
        ],
        "Hard": [
            {"question": "What is the process by which water vapor changes back to liquid?", "options": ["Evaporation", "Condensation", "Precipitation", "Sublimation"], "answer": "Condensation"},
            {"question": "Which gas is produced by plants during photosynthesis?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "What is the function of the respiratory system?", "options": ["To digest food", "To pump blood", "To help in breathing", "To remove waste"], "answer": "To help in breathing"},
            {"question": "Which part of the brain controls balance and coordination?", "options": ["Cerebrum", "Cerebellum", "Medulla", "Spinal cord"], "answer": "Cerebellum"},
            {"question": "What is the unit of force?", "options": ["Newton", "Joule", "Watt", "Pascal"], "answer": "Newton"},
            {"question": "Which type of teeth are used for tearing food?", "options": ["Incisors", "Canines", "Molars", "Premolars"], "answer": "Canines"},
            {"question": "What is the main function of roots in plants?", "options": ["Absorb water and minerals", "Make food", "Reproduce", "Produce flowers"], "answer": "Absorb water and minerals"},
            {"question": "Which gas is responsible for global warming?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"], "answer": "Carbon dioxide"},
            {"question": "What is the term for animals that are active during the night?", "options": ["Diurnal", "Nocturnal", "Crepuscular", "Carnivores"], "answer": "Nocturnal"},
            {"question": "What part of the plant conducts photosynthesis?", "options": ["Roots", "Stem", "Leaves", "Flowers"], "answer": "Leaves"}
        ]
    },
    "Social Science": {
        "Easy": [
            {"question": "What is the name of our country?", "options": ["India", "USA", "China", "Australia"], "answer": "India"},
            {"question": "Which is the capital city of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
            {"question": "What do we call the people who live in a country?", "options": ["Citizens", "Visitors", "Tourists", "Foreigners"], "answer": "Citizens"},
            {"question": "Which is the national bird of India?", "options": ["Peacock", "Eagle", "Sparrow", "Parrot"], "answer": "Peacock"},
            {"question": "Which tool do farmers use to plough fields?", "options": ["Tractor", "Plough", "Harvester", "Sprayer"], "answer": "Plough"},
            {"question": "What is a map?", "options": ["A picture of animals", "A drawing of roads", "A representation of places", "A book"], "answer": "A representation of places"},
            {"question": "Who is the head of a village?", "options": ["Mayor", "Sarpanch", "Governor", "President"], "answer": "Sarpanch"},
            {"question": "Which is the largest continent?", "options": ["Asia", "Africa", "Europe", "Australia"], "answer": "Asia"},
            {"question": "Which river is the longest in India?", "options": ["Ganga", "Yamuna", "Brahmaputra", "Indus"], "answer": "Ganga"},
            {"question": "What do we call the season when crops are harvested?", "options": ["Winter", "Summer", "Harvest season", "Monsoon"], "answer": "Harvest season"}
        ],
        "Medium": [
            {"question": "Who was the first Prime Minister of India?", "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Indira Gandhi", "Dr. Ambedkar"], "answer": "Jawaharlal Nehru"},
            {"question": "Which mountain range is called the 'Abode of Snow'?", "options": ["Aravalli", "Himalayas", "Vindhyas", "Satpuras"], "answer": "Himalayas"},
            {"question": "What is the main source of livelihood in rural India?", "options": ["Farming", "Business", "Teaching", "Fishing"], "answer": "Farming"},
            {"question": "Which festival is known as the Festival of Lights?", "options": ["Holi", "Diwali", "Eid", "Christmas"], "answer": "Diwali"},
            {"question": "Which is the largest desert in India?", "options": ["Thar Desert", "Sahara Desert", "Gobi Desert", "Kalahari Desert"], "answer": "Thar Desert"},
            {"question": "What do we call the law-making body of India?", "options": ["Supreme Court", "Parliament", "President", "Prime Minister"], "answer": "Parliament"},
            {"question": "Which type of government does India have?", "options": ["Monarchy", "Democracy", "Dictatorship", "Republic"], "answer": "Democracy"},
            {"question": "Which is the main river flowing through Delhi?", "options": ["Yamuna", "Ganga", "Brahmaputra", "Godavari"], "answer": "Yamuna"},
            {"question": "What is a democracy?", "options": ["Rule by one person", "Rule by the people", "Rule by army", "Rule by king"], "answer": "Rule by the people"},
            {"question": "Who was the freedom fighter known as the 'Iron Man of India'?", "options": ["Mahatma Gandhi", "Sardar Patel", "Jawaharlal Nehru", "Bhagat Singh"], "answer": "Sardar Patel"}
        ],
        "Hard": [
            {"question": "Which ancient civilization developed along the Indus River?", "options": ["Egyptian", "Mesopotamian", "Harappan", "Greek"], "answer": "Harappan"},
            {"question": "What is the significance of the 'Green Revolution'?", "options": ["Increase in agricultural production", "Industrial development", "Urbanization", "Deforestation"], "answer": "Increase in agricultural production"},
            {"question": "Who wrote the Indian Constitution?", "options": ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel"], "answer": "Dr. B.R. Ambedkar"},
            {"question": "What is the primary function of the Parliament?", "options": ["Make laws", "Enforce laws", "Interpret laws", "Execute laws"], "answer": "Make laws"},
            {"question": "Which Indian state is famous for its backwaters?", "options": ["Kerala", "Tamil Nadu", "Goa", "Karnataka"], "answer": "Kerala"},
            {"question": "Who was the first woman Prime Minister of India?", "options": ["Indira Gandhi", "Pratibha Patil", "Sonia Gandhi", "Mamata Banerjee"], "answer": "Indira Gandhi"},
            {"question": "What is the role of the Supreme Court of India?", "options": ["Legislative body", "Judicial authority", "Executive body", "Financial authority"], "answer": "Judicial authority"},
            {"question": "Which geographical feature separates India from China?", "options": ["Aravalli Hills", "Himalayas", "Vindhya Range", "Western Ghats"], "answer": "Himalayas"},
            {"question": "What is the primary occupation of people living in coastal areas?", "options": ["Fishing", "Farming", "Mining", "Trading"], "answer": "Fishing"},
            {"question": "Which Indian leader gave the slogan 'Jai Jawan Jai Kisan'?", "options": ["Lal Bahadur Shastri", "Jawaharlal Nehru", "Indira Gandhi", "Sardar Patel"], "answer": "Lal Bahadur Shastri"}
        ]
    },
    "Hindi": {
        "Easy": [
            {"question": "निम्नलिखित में से कौन सा शब्द संज्ञा है?", "options": ["खेलना", "लाल", "स्कूल", "जल्दी"], "answer": "स्कूल"},
            {"question": "‘घर’ शब्द का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "वचनहीन", "अज्ञात"], "answer": "एकवचन"},
            {"question": "‘पढ़ना’ शब्द किस प्रकार का क्रिया है?", "options": ["सकर्मक क्रिया", "अकर्मक क्रिया", "द्विकर्मक क्रिया", "सहायक क्रिया"], "answer": "सकर्मक क्रिया"},
            {"question": "निम्नलिखित में से कौन सा सर्वनाम है?", "options": ["मैं", "घर", "खेल", "लाल"], "answer": "मैं"},
            {"question": "‘सुंदर’ शब्द किस प्रकार का शब्द है?", "options": ["विशेषण", "क्रिया", "संज्ञा", "सर्वनाम"], "answer": "विशेषण"},
            {"question": "‘खेल’ शब्द का वचन बताइए।", "options": ["एकवचन", "बहुवचन", "दोवचन", "अज्ञात"], "answer": "एकवचन"},
            {"question": "‘सूरज’ शब्द क्या दर्शाता है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "संज्ञा"},
            {"question": "‘मैं’ शब्द किस प्रकार का शब्द है?", "options": ["संज्ञा", "सर्वनाम", "क्रिया", "विशेषण"], "answer": "सर्वनाम"},
            {"question": "‘दौड़ना’ शब्द किस प्रकार की क्रिया है?", "options": ["सकर्मक", "अकर्मक", "द्विकर्मक", "सहायक"], "answer": "अकर्मक"},
            {"question": "‘किताबें’ शब्द का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "दोवचन", "वचनहीन"], "answer": "बहुवचन"}
        ],
        "Medium": [
            {"question": "‘लिखना’ क्रिया किस प्रकार की है?", "options": ["सकर्मक", "अकर्मक", "द्विकर्मक", "सहायक"], "answer": "सकर्मक"},
            {"question": "निम्नलिखित में से कौन सा विशेषण है?", "options": ["सुंदर", "खेल", "चलना", "मैं"], "answer": "सुंदर"},
            {"question": "‘वह’ शब्द किस प्रकार का सर्वनाम है?", "options": ["सर्वनाम", "संज्ञा", "विशेषण", "क्रिया"], "answer": "सर्वनाम"},
            {"question": "‘हम’ शब्द किस वचन में है?", "options": ["एकवचन", "बहुवचन", "दोवचन", "अज्ञात"], "answer": "बहुवचन"},
            {"question": "‘खेलते’ शब्द किस काल का है?", "options": ["वर्तमान काल", "भूतकाल", "भविष्यत काल", "अज्ञात"], "answer": "वर्तमान काल"},
            {"question": "‘घर’ शब्द किस लिंग का है?", "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "अज्ञात"], "answer": "पुल्लिंग"},
            {"question": "‘बड़ा’ शब्द किस प्रकार का शब्द है?", "options": ["विशेषण", "संज्ञा", "सर्वनाम", "क्रिया"], "answer": "विशेषण"},
            {"question": "‘उन्होंने’ शब्द किस प्रकार का सर्वनाम है?", "options": ["संबंधवाचक", "व्यक्तिवाचक", "अन्वयवाचक", "अन्य"], "answer": "व्यक्तिवाचक"},
            {"question": "‘कूदना’ क्रिया किस काल की है?", "options": ["वर्तमान काल", "भूतकाल", "भविष्यत काल", "अज्ञात"], "answer": "वर्तमान काल"},
            {"question": "‘लड़की’ शब्द किस लिंग का है?", "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "अज्ञात"], "answer": "स्त्रीलिंग"}
        ],
        "Hard": [
            {"question": "‘मैंने खाना खा लिया है।’ वाक्य में कौन सा कारक है?", "options": ["कर्ता", "कर्म", "करण", "सम्प्रदान"], "answer": "कर्ता"},
            {"question": "‘तुम्हारा’ शब्द किस प्रकार का सर्वनाम है?", "options": ["संबंधवाचक", "व्यक्तिवाचक", "अन्वयवाचक", "अन्य"], "answer": "संबंधवाचक"},
            {"question": "‘घर में बच्चे खेल रहे हैं।’ वाक्य में कितने कारक हैं?", "options": ["एक", "दो", "तीन", "चार"], "answer": "दो"},
            {"question": "‘सच्चाई’ शब्द किस प्रकार का शब्द है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "संज्ञा"},
            {"question": "‘धूप’ शब्द किस लिंग का है?", "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "अज्ञात"], "answer": "स्त्रीलिंग"},
            {"question": "‘नदी के किनारे हम बैठे थे।’ वाक्य में ‘किनारे’ शब्द का कारक क्या है?", "options": ["अधिकार", "सम्प्रदान", "अधिकरण", "करण"], "answer": "अधिकरण"},
            {"question": "‘आदर्श’ शब्द किस प्रकार का शब्द है?", "options": ["विशेषण", "संज्ञा", "सर्वनाम", "क्रिया"], "answer": "विशेषण"},
            {"question": "‘वे लोग स्कूल गए थे।’ वाक्य में कौन सा कारक है?", "options": ["कर्ता", "कर्म", "करण", "सम्प्रदान"], "answer": "कर्ता"},
            {"question": "‘लिखना’ और ‘पढ़ना’ किस प्रकार की क्रिया हैं?", "options": ["सकर्मक", "अकर्मक", "द्विकर्मक", "सहायक"], "answer": "सकर्मक"},
            {"question": "‘हमारा’ शब्द किस प्रकार का सर्वनाम है?", "options": ["संबंधवाचक", "व्यक्तिवाचक", "अन्वयवाचक", "अन्य"], "answer": "संबंधवाचक"}
        ]
    }
},
"6": {
    "Mathematics": {
        "Easy": [
            {"question": "What is 123 + 456?", "options": ["579", "569", "577", "587"], "answer": "579"},
            {"question": "What is the place value of 5 in 5,432?", "options": ["5000", "500", "50", "5"], "answer": "5000"},
            {"question": "What is 600 - 278?", "options": ["322", "332", "318", "328"], "answer": "322"},
            {"question": "How many sides does a pentagon have?", "options": ["4", "5", "6", "7"], "answer": "5"},
            {"question": "What is 6 × 7?", "options": ["42", "36", "48", "52"], "answer": "42"},
            {"question": "What is half of 80?", "options": ["30", "40", "50", "60"], "answer": "40"},
            {"question": "Which number comes after 1,999?", "options": ["2000", "1900", "1998", "2100"], "answer": "2000"},
            {"question": "What is 18 ÷ 3?", "options": ["5", "6", "7", "8"], "answer": "6"},
            {"question": "What is the sum of angles in a triangle?", "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
            {"question": "Which is a multiple of 9?", "options": ["28", "36", "45", "54"], "answer": "36"}
        ],
        "Medium": [
            {"question": "What is the LCM of 8 and 12?", "options": ["24", "20", "16", "36"], "answer": "24"},
            {"question": "What is 7/8 as a decimal?", "options": ["0.875", "0.78", "0.8750", "0.87"], "answer": "0.875"},
            {"question": "Find the perimeter of a rectangle of length 12 cm and width 7 cm.", "options": ["38 cm", "42 cm", "19 cm", "48 cm"], "answer": "38 cm"},
            {"question": "What is 20% of 150?", "options": ["30", "25", "35", "40"], "answer": "30"},
            {"question": "Which fraction is equivalent to 3/5?", "options": ["6/10", "2/5", "3/10", "4/5"], "answer": "6/10"},
            {"question": "What is the volume of a cube with side 4 cm?", "options": ["64 cm³", "16 cm³", "48 cm³", "32 cm³"], "answer": "64 cm³"},
            {"question": "What is the product of 0.4 and 0.6?", "options": ["0.24", "0.40", "0.06", "0.10"], "answer": "0.24"},
            {"question": "Which number is prime?", "options": ["27", "29", "33", "35"], "answer": "29"},
            {"question": "What is the area of a square with side 9 cm?", "options": ["81 cm²", "18 cm²", "27 cm²", "72 cm²"], "answer": "81 cm²"},
            {"question": "What is the difference between 2000 and 987?", "options": ["1013", "1033", "1003", "1023"], "answer": "1013"}
        ],
        "Hard": [
            {"question": "Simplify: (8 × 5) + (24 ÷ 6) - 9", "options": ["31", "25", "29", "27"], "answer": "31"},
            {"question": "If radius of a circle is 14 cm, what is its circumference? (π = 22/7)", "options": ["88 cm", "44 cm", "76 cm", "99 cm"], "answer": "88 cm"},
            {"question": "Find the HCF of 28 and 42.", "options": ["14", "7", "28", "42"], "answer": "14"},
            {"question": "What is decimal form of 5/16?", "options": ["0.3125", "0.325", "0.315", "0.321"], "answer": "0.3125"},
            {"question": "Convert 2 hours 30 minutes into minutes.", "options": ["150", "130", "140", "160"], "answer": "150"},
            {"question": "Solve for x: 3x + 5 = 20", "options": ["5", "6", "7", "8"], "answer": "5"},
            {"question": "If triangle sides are 9 cm, 12 cm, 15 cm, what type is it?", "options": ["Right-angled", "Isosceles", "Equilateral", "Scalene"], "answer": "Right-angled"},
            {"question": "What is mean of: 10, 15, 20, 25, 30?", "options": ["20", "22", "25", "18"], "answer": "20"},
            {"question": "What is median of: 2, 14, 7, 10, 5?", "options": ["7", "10", "5", "14"], "answer": "7"},
            {"question": "A bus travels 90 km in 1 hour 30 minutes. What is average speed?", "options": ["60 km/h", "80 km/h", "90 km/h", "75 km/h"], "answer": "60 km/h"}
        ]
    },
    "English": {
        "Easy": [
            {"question": "Choose the plural of 'child'", "options": ["childs", "children", "childes", "child"], "answer": "children"},
            {"question": "Fill in the blank: She ___ reading a book.", "options": ["is", "are", "am", "be"], "answer": "is"},
            {"question": "What is the past tense of 'run'?", "options": ["runned", "ran", "runs", "running"], "answer": "ran"},
            {"question": "Choose the correct article: ___ apple a day keeps the doctor away.", "options": ["A", "An", "The", "No article"], "answer": "An"},
            {"question": "Select the noun: 'The bird is flying.'", "options": ["bird", "is", "flying", "the"], "answer": "bird"},
            {"question": "Identify the pronoun: 'They are playing cricket.'", "options": ["They", "playing", "cricket", "are"], "answer": "They"},
            {"question": "What is the opposite of 'big'?", "options": ["large", "small", "fast", "tall"], "answer": "small"},
            {"question": "Fill in the blank: I ___ two sisters.", "options": ["have", "has", "had", "having"], "answer": "have"},
            {"question": "Choose the correct spelling:", "options": ["accomodate", "accommodate", "acommodate", "accomadate"], "answer": "accommodate"},
            {"question": "What is the correct sentence?", "options": ["He are playing.", "He is playing.", "He am playing.", "He be playing."], "answer": "He is playing."}
        ],
        "Medium": [
            {"question": "Choose the correct verb: They ___ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "go"},
            {"question": "Select the correct sentence.", "options": ["She don't eat rice.", "She doesn't eat rice.", "She don't eats rice.", "She doesn't eats rice."], "answer": "She doesn't eat rice."},
            {"question": "Find the synonym of 'happy'.", "options": ["sad", "joyful", "angry", "tired"], "answer": "joyful"},
            {"question": "Identify the adverb: 'He speaks softly.'", "options": ["He", "speaks", "softly", "none"], "answer": "softly"},
            {"question": "Choose the correct tense: She ___ her homework yesterday.", "options": ["did", "do", "does", "doing"], "answer": "did"},
            {"question": "Pick the correct preposition: The cat is ___ the table.", "options": ["on", "in", "under", "beside"], "answer": "on"},
            {"question": "Choose the conjunction: I like tea ___ coffee.", "options": ["and", "but", "or", "so"], "answer": "and"},
            {"question": "Identify the subject: 'The dogs bark loudly.'", "options": ["dogs", "bark", "loudly", "The"], "answer": "dogs"},
            {"question": "Fill in: This is ___ book.", "options": ["his", "him", "he", "hers"], "answer": "his"},
            {"question": "Which is a proper noun?", "options": ["city", "india", "India", "country"], "answer": "India"}
        ],
        "Hard": [
            {"question": "Identify the indirect object: He gave me a gift.", "options": ["He", "me", "a gift", "gave"], "answer": "me"},
            {"question": "Find the antonym of 'ancient'.", "options": ["old", "modern", "ancient", "historic"], "answer": "modern"},
            {"question": "Choose: Neither of them ___ coming.", "options": ["are", "is", "were", "be"], "answer": "is"},
            {"question": "What type of sentence is: 'Don't touch that!'?", "options": ["Imperative", "Interrogative", "Declarative", "Exclamatory"], "answer": "Imperative"},
            {"question": "Passive form: 'They painted the house.'", "options": ["The house was painted by them.", "The house is painted by them.", "The house painted by them.", "They was painted the house."], "answer": "The house was painted by them."},
            {"question": "Choose the correct form: By next year, I ___ finished.", "options": ["will have", "will", "have", "had"], "answer": "will have"},
            {"question": "What does the idiom 'break the ice' mean?", "options": ["start conversation", "break something", "freeze water", "get angry"], "answer": "start conversation"},
            {"question": "Reported speech: He said, 'I am tired.'", "options": ["He said he was tired.", "He said he is tired.", "He says he was tired.", "He said he will be tired."], "answer": "He said he was tired."},
            {"question": "Identify correct spelling:", "options": ["Receive", "Recieve", "Receeve", "Recive"], "answer": "Receive"},
            {"question": "What is a phrasal verb?", "options": ["two-word verb", "noun + verb", "adjective phrase", "single verb"], "answer": "two-word verb"}
        ]
    },
    "Science": {
        "Easy": [
            {"question": "Which sense organ helps us to see?", "options": ["Eyes", "Ears", "Nose", "Skin"], "answer": "Eyes"},
            {"question": "What is the main source of energy for Earth?", "options": ["Sun", "Moon", "Stars", "Wind"], "answer": "Sun"},
            {"question": "Which part of the plant makes food?", "options": ["Root", "Stem", "Flower", "Leaf"], "answer": "Leaf"},
            {"question": "Which of the following is a liquid?", "options": ["Air", "Stone", "Water", "Salt"], "answer": "Water"},
            {"question": "What do we breathe in for respiration?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "What is the boiling point of water?", "options": ["100°C", "0°C", "50°C", "25°C"], "answer": "100°C"},
            {"question": "Which of these is a natural fibre?", "options": ["Nylon", "Polyester", "Cotton", "Plastic"], "answer": "Cotton"},
            {"question": "Which gas do plants release during photosynthesis?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "Which part of the body helps in circulation of blood?", "options": ["Lungs", "Heart", "Stomach", "Liver"], "answer": "Heart"},
            {"question": "Which object will sink in water?", "options": ["Stone", "Plastic ball", "Feather", "Wood"], "answer": "Stone"}
        ],
        "Medium": [
            {"question": "Which planet is known as the 'Red Planet'?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
            {"question": "Which nutrient builds our body?", "options": ["Proteins", "Fats", "Carbohydrates", "Vitamins"], "answer": "Proteins"},
            {"question": "Which part of the plant absorbs water?", "options": ["Leaves", "Roots", "Stem", "Flower"], "answer": "Roots"},
            {"question": "What is the process of water changing to vapor called?", "options": ["Condensation", "Melting", "Evaporation", "Freezing"], "answer": "Evaporation"},
            {"question": "How many bones are in the human body?", "options": ["206", "201", "208", "210"], "answer": "206"},
            {"question": "Which one is a magnetic material?", "options": ["Wood", "Plastic", "Iron", "Glass"], "answer": "Iron"},
            {"question": "What do we call animals that eat only plants?", "options": ["Herbivores", "Carnivores", "Omnivores", "Insectivores"], "answer": "Herbivores"},
            {"question": "Which of the following is not a habitat?", "options": ["Desert", "Ocean", "Mountain", "Water"], "answer": "Water"},
            {"question": "Which vitamin do we get from sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
            {"question": "What is the main function of the lungs?", "options": ["Digestion", "Breathing", "Circulation", "Reproduction"], "answer": "Breathing"}
        ],
        "Hard": [
            {"question": "Which metal is liquid at room temperature?", "options": ["Iron", "Gold", "Mercury", "Copper"], "answer": "Mercury"},
            {"question": "Which gas turns lime water milky?", "options": ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], "answer": "Carbon dioxide"},
            {"question": "The process of separating grains from chaff is called?", "options": ["Threshing", "Winnowing", "Sieving", "Filtering"], "answer": "Winnowing"},
            {"question": "Which of these is a reversible change?", "options": ["Burning paper", "Melting ice", "Cooking food", "Rusting iron"], "answer": "Melting ice"},
            {"question": "How many layers does the Earth have?", "options": ["2", "3", "4", "5"], "answer": "3"},
            {"question": "What is the function of stomata?", "options": ["Absorb sunlight", "Help in breathing", "Exchange gases", "Produce chlorophyll"], "answer": "Exchange gases"},
            {"question": "Which is a good conductor of electricity?", "options": ["Plastic", "Glass", "Copper", "Rubber"], "answer": "Copper"},
            {"question": "Which disease is caused by mosquito bite?", "options": ["Malaria", "Diabetes", "Cancer", "Asthma"], "answer": "Malaria"},
            {"question": "Which force pulls everything towards the Earth?", "options": ["Magnetic", "Friction", "Gravity", "Electric"], "answer": "Gravity"},
            {"question": "Which of these is an adaptation in camel?", "options": ["Webbed feet", "Hump", "Sharp claws", "Sticky tongue"], "answer": "Hump"}
        ]
    },
    "Social Science": {
        "Easy": [
            {"question": "Who was the first Prime Minister of India?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Indira Gandhi", "Dr. Rajendra Prasad"], "answer": "Jawaharlal Nehru"},
            {"question": "Which direction does the sun rise from?", "options": ["North", "South", "East", "West"], "answer": "East"},
            {"question": "Which is the longest river in India?", "options": ["Yamuna", "Ganga", "Brahmaputra", "Godavari"], "answer": "Ganga"},
            {"question": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi"},
            {"question": "Which planet do we live on?", "options": ["Mars", "Venus", "Earth", "Jupiter"], "answer": "Earth"},
            {"question": "Who is the head of a state government?", "options": ["President", "Governor", "Prime Minister", "Chief Minister"], "answer": "Chief Minister"},
            {"question": "What does a compass show?", "options": ["Time", "Speed", "Direction", "Temperature"], "answer": "Direction"},
            {"question": "What is a globe?", "options": ["Flat map", "Model of the Earth", "Ball", "Book"], "answer": "Model of the Earth"},
            {"question": "What do we call the people who study history?", "options": ["Geologists", "Historians", "Scientists", "Writers"], "answer": "Historians"},
            {"question": "In which direction does the compass needle always point?", "options": ["East", "West", "North", "South"], "answer": "North"}
        ],
        "Medium": [
            {"question": "Which mountain range separates India from Tibet?", "options": ["Aravalli", "Himalayas", "Western Ghats", "Nilgiris"], "answer": "Himalayas"},
            {"question": "What is the basic unit of society?", "options": ["Village", "Family", "Community", "Government"], "answer": "Family"},
            {"question": "What is the meaning of 'prehistory'?", "options": ["History with writing", "History before writing", "Future history", "Fictional history"], "answer": "History before writing"},
            {"question": "Which landform is higher than a hill?", "options": ["Plateau", "Mountain", "Plain", "Valley"], "answer": "Mountain"},
            {"question": "Who elects the Members of Parliament?", "options": ["President", "Citizens", "Prime Minister", "Supreme Court"], "answer": "Citizens"},
            {"question": "What is a tributary?", "options": ["Main river", "Small river that joins a larger river", "Sea", "Waterfall"], "answer": "Small river that joins a larger river"},
            {"question": "What is the southernmost point of India?", "options": ["Indira Point", "Kanyakumari", "Kolkata", "Lakshadweep"], "answer": "Indira Point"},
            {"question": "Which of the following is not a natural resource?", "options": ["Air", "Water", "Minerals", "Plastic"], "answer": "Plastic"},
            {"question": "What is the name of our national emblem?", "options": ["Ashoka Chakra", "Lion Capital", "Tricolour", "Satyamev Jayate"], "answer": "Lion Capital"},
            {"question": "Which is the largest continent?", "options": ["Africa", "Asia", "Europe", "Australia"], "answer": "Asia"}
        ],
        "Hard": [
            {"question": "What is the significance of the Tropic of Cancer?", "options": ["Longest river", "Divides Earth into zones", "Passes through India", "Imaginary line for longitude"], "answer": "Passes through India"},
            {"question": "What is archaeology?", "options": ["Study of planets", "Study of old buildings and tools", "Study of economy", "Study of climate"], "answer": "Study of old buildings and tools"},
            {"question": "Who wrote the book 'Arthashastra'?", "options": ["Ashoka", "Chanakya", "Harsha", "Kalidasa"], "answer": "Chanakya"},
            {"question": "Which gas is responsible for global warming?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon dioxide"},
            {"question": "What do we call a person who represents people in the Parliament?", "options": ["MLA", "Governor", "MP", "Judge"], "answer": "MP"},
            {"question": "In which direction does the Earth rotate?", "options": ["East to West", "West to East", "North to South", "South to North"], "answer": "West to East"},
            {"question": "Where is the Thar Desert located?", "options": ["Rajasthan", "Maharashtra", "Gujarat", "Punjab"], "answer": "Rajasthan"},
            {"question": "Which ancient site is located in Haryana?", "options": ["Lothal", "Mohenjo-Daro", "Kalibangan", "Rakhigarhi"], "answer": "Rakhigarhi"},
            {"question": "What is meant by 'urban area'?", "options": ["Forest region", "Village", "Town or city", "Agricultural land"], "answer": "Town or city"},
            {"question": "The Panchayati Raj system operates at which level?", "options": ["State", "District", "Village", "Country"], "answer": "Village"}
        ]
    },
    "Hindi": {
        "Easy": [
            {"question": "'पानी की कहानी' पाठ में किसकी कहानी है?", "options": ["दूध की", "तेल की", "पानी की", "रस की"], "answer": "पानी की"},
            {"question": "‘बचपन’ कविता के लेखक कौन हैं?", "options": ["रवींद्रनाथ ठाकुर", "सुभद्राकुमारी चौहान", "हरिवंश राय बच्चन", "निराला"], "answer": "हरिवंश राय बच्चन"},
            {"question": "‘वचन’ कितने प्रकार के होते हैं?", "options": ["एक", "दो", "तीन", "चार"], "answer": "दो"},
            {"question": "‘राम ने गाना गाया।’ वाक्य में क्रिया क्या है?", "options": ["राम", "ने", "गाना", "गाया"], "answer": "गाया"},
            {"question": "‘नील’ शब्द में कौन-सा विशेषण है?", "options": ["गुणवाचक", "संबंधवाचक", "संख्यावाचक", "परिमाणवाचक"], "answer": "गुणवाचक"},
            {"question": "‘पेड़’ शब्द का वचन बदलो।", "options": ["पेड़ें", "पेड़ों", "पेड़", "पेड़िया"], "answer": "पेड़"},
            {"question": "‘खुश’ शब्द का विपरीत शब्द क्या होगा?", "options": ["रोता", "दुखी", "सुखी", "परेशान"], "answer": "दुखी"},
            {"question": "‘मैं स्कूल जाता हूँ।’ वाक्य किस काल का है?", "options": ["भूतकाल", "वर्तमानकाल", "भविष्यकाल", "अनिश्चित काल"], "answer": "वर्तमानकाल"},
            {"question": "‘पढ़ाई’ शब्द संज्ञा है या क्रिया?", "options": ["क्रिया", "संज्ञा", "विशेषण", "सर्वनाम"], "answer": "संज्ञा"},
            {"question": "‘जो काम करता है’ उसे क्या कहते हैं?", "options": ["कर्ता", "कर्म", "विशेषण", "क्रिया"], "answer": "कर्ता"}
        ],
        "Medium": [
            {"question": "‘रामायण’ किसके द्वारा रचित है?", "options": ["तुलसीदास", "महर्षि वाल्मीकि", "कबीर", "रहीम"], "answer": "महर्षि वाल्मीकि"},
            {"question": "‘मित्र’ शब्द में कौन-सा संधि है?", "options": ["विसर्ग संधि", "स्वर संधि", "व्यंजन संधि", "यण संधि"], "answer": "व्यंजन संधि"},
            {"question": "‘अनार’ शब्द में उपसर्ग क्या है?", "options": ["अ", "अन", "ना", "आर"], "answer": "अन"},
            {"question": "‘कहानी’ शब्द का सही पर्यायवाची क्या है?", "options": ["कथा", "लेख", "निबंध", "वार्ता"], "answer": "कथा"},
            {"question": "‘शब्द’ किसका उदाहरण है?", "options": ["संज्ञा", "क्रिया", "अव्यय", "सर्वनाम"], "answer": "संज्ञा"},
            {"question": "‘वह दौड़ रहा है।’ में क्रिया का प्रकार क्या है?", "options": ["सकर्मक", "अकर्मक", "निजवाचक", "प्रेरणार्थक"], "answer": "अकर्मक"},
            {"question": "‘पढ़ाई’ शब्द किस धातु से बना है?", "options": ["पढ़", "पढ़ा", "पढ़ाइ", "पढ़ी"], "answer": "पढ़"},
            {"question": "‘जल्दी आना’ में 'जल्दी' कौन-सा शब्द है?", "options": ["क्रिया", "क्रियाविशेषण", "विशेषण", "संज्ञा"], "answer": "क्रियाविशेषण"},
            {"question": "‘जंगल’ शब्द का विलोम शब्द क्या है?", "options": ["शहर", "गांव", "पर्वत", "जंगलहीन"], "answer": "शहर"},
            {"question": "‘बालक स्कूल गया।’ वाक्य में ‘गया’ कौन-सा शब्द है?", "options": ["क्रिया", "विशेषण", "संज्ञा", "सर्वनाम"], "answer": "क्रिया"}
        ],
        "Hard": [
            {"question": "‘वह नहीं आएगा’ — यह वाक्य किस प्रकार का है?", "options": ["नकारात्मक", "प्रश्नवाचक", "आदेशात्मक", "विधिवाचक"], "answer": "नकारात्मक"},
            {"question": "‘समानार्थी शब्द’ किसे कहते हैं?", "options": ["उल्टा अर्थ", "मिलता-जुलता अर्थ", "एक ही अर्थ", "कोई नहीं"], "answer": "एक ही अर्थ"},
            {"question": "‘भारत एक महान देश है।’ वाक्य में विशेषण शब्द कौन-सा है?", "options": ["भारत", "एक", "महान", "देश"], "answer": "महान"},
            {"question": "‘सूर्य’ शब्द में कौन-सा लिंग है?", "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "कोई नहीं"], "answer": "पुल्लिंग"},
            {"question": "‘जो दूसरों का भला चाहता है’ — उसके लिए एक शब्द?", "options": ["दानी", "हितैषी", "क्रोधी", "शत्रु"], "answer": "हितैषी"},
            {"question": "‘धैर्य’ शब्द कौन-सी संज्ञा है?", "options": ["भाववाचक", "व्यक्तिवाचक", "जातिवाचक", "स्थानवाचक"], "answer": "भाववाचक"},
            {"question": "‘रामायण’ किस प्रकार की रचना है?", "options": ["उपन्यास", "कविता", "महाकाव्य", "नाटक"], "answer": "महाकाव्य"},
            {"question": "‘सच्चा’ शब्द का विलोम क्या होगा?", "options": ["झूठा", "मिथ्या", "गलत", "दोषी"], "answer": "झूठा"},
            {"question": "‘कवि’ शब्द का स्त्रीलिंग रूप क्या है?", "options": ["कविता", "कवियत्री", "कविया", "कविन"], "answer": "कवियत्री"},
            {"question": "‘भूख लगना’ मुहावरे का सही अर्थ क्या है?", "options": ["खाना खाना", "भोजन पचाना", "भोजन का समय होना", "खाने की इच्छा होना"], "answer": "खाने की इच्छा होना"}
        ]
    },
    "Sanskrit": {
        "Easy": [
            {"question": "रामः कः अस्ति?", "options": ["बालकः", "गुरुः", "अश्वः", "फलम्"], "answer": "बालकः"},
            {"question": "‘फलम्’ शब्दस्य अर्थः कः?", "options": ["फल", "पुस्तक", "फलम्", "पानी"], "answer": "फल"},
            {"question": "‘धावति’ क्रियापदम् कः कालः अस्ति?", "options": ["वर्तमान कालः", "भूत कालः", "भविष्यत् कालः", "सर्वे कालाः"], "answer": "वर्तमान कालः"},
            {"question": "‘गच्छति’ शब्दस्य रूपं किम्?", "options": ["धातु", "संज्ञा", "विशेषणम्", "सर्वनाम"], "answer": "धातु"},
            {"question": "रामः वृक्षस्य समीपे कुत्र अस्ति?", "options": ["पादः", "नीचे", "ऊपर", "वृक्षस्य समीपे"], "answer": "वृक्षस्य समीपे"},
            {"question": "‘पठति’ क्रिया का अर्थ है?", "options": ["चलना", "पढ़ना", "खेलना", "खाना"], "answer": "पढ़ना"},
            {"question": "‘सूर्यः कः अस्ति?’", "options": ["तारा", "प्रकाश", "नदी", "पहाड़"], "answer": "प्रकाश"},
            {"question": "‘मित्रं’ शब्द का अर्थ क्या है?", "options": ["दोस्त", "शत्रु", "घर", "फल"], "answer": "दोस्त"},
            {"question": "‘धैर्यं’ शब्द का अर्थ है?", "options": ["साहस", "डर", "उदास", "खुशी"], "answer": "साहस"},
            {"question": "‘जलम्’ शब्द का अर्थ है?", "options": ["पानी", "अग्नि", "वायु", "भूमि"], "answer": "पानी"}
        ],
        "Medium": [
            {"question": "रामः फलानि खादति। वाक्य में कर्ता कौन है?", "options": ["फलानि", "रामः", "खादति", "वृक्षः"], "answer": "रामः"},
            {"question": "‘सीता पाठशालां गच्छति।’ वाक्य का प्रकार क्या है?", "options": ["विधेय वाक्य", "विनय वाक्य", "आज्ञा वाक्य", "प्रश्नवाचक वाक्य"], "answer": "विधेय वाक्य"},
            {"question": "‘लिखति’ शब्द का लकार क्या है?", "options": ["लट्", "लिट्", "लुङ्", "लृट्"], "answer": "लट्"},
            {"question": "‘सुन्दरम्’ शब्द किस प्रकार का है?", "options": ["संज्ञा", "विशेषण", "क्रियापद", "सर्वनाम"], "answer": "विशेषण"},
            {"question": "‘अहम् पाठशालां गच्छामि।’ क्रिया का लकार क्या है?", "options": ["लट्", "लिट्", "लुङ्", "लृट्"], "answer": "लट्"},
            {"question": "‘पुस्तकं’ शब्द का कारक कौन सा है?", "options": ["कर्तृ", "कर्म", "सम्प्रदान", "अपादान"], "answer": "कर्म"},
            {"question": "‘रामस्य’ शब्द किस कारक का प्रयोग है?", "options": ["कर्तृ", "सम्प्रदान", "भाव", "संबंध"], "answer": "संबंध"},
            {"question": "‘अत्र’ शब्द का अर्थ क्या है?", "options": ["यहाँ", "वहाँ", "कहाँ", "कभी"], "answer": "यहाँ"},
            {"question": "‘किम्’ शब्द किस प्रकार का शब्द है?", "options": ["सर्वनाम", "संज्ञा", "प्रश्नवाचक", "क्रिया"], "answer": "प्रश्नवाचक"},
            {"question": "‘पठ’ धातु का क्या अर्थ है?", "options": ["पढ़ना", "लिखना", "चलना", "खेलना"], "answer": "पढ़ना"}
        ],
        "Hard": [
            {"question": "‘रामः पुस्तकम् पठति।’ में कर्ता कौन है?", "options": ["रामः", "पुस्तकम्", "पठति", "सीता"], "answer": "रामः"},
            {"question": "‘किम् रामः खादति?’ वाक्य का प्रकार क्या है?", "options": ["विधेय", "विनय", "प्रश्नवाचक", "आज्ञा"], "answer": "प्रश्नवाचक"},
            {"question": "‘भवान् कुत्र गच्छति?’ प्रश्नवाचक पद कौन सा है?", "options": ["कुत्र", "भवान्", "गच्छति", "कस्मिन्"], "answer": "कुत्र"},
            {"question": "‘सीता फलं खादति।’ में ‘फलम्’ किस कारक में है?", "options": ["कर्तृ", "कर्म", "सम्प्रदान", "अपादान"], "answer": "कर्म"},
            {"question": "‘रामस्य गृहः सुन्दरः अस्ति।’ में लकार कौन सा है?", "options": ["लट्", "लिट्", "लुङ्", "लृट्"], "answer": "लट्"},
            {"question": "‘न नदी तिष्ठति।’ में ‘न’ का प्रयोग क्या है?", "options": ["नकारक", "अव्यय", "सर्वनाम", "क्रिया"], "answer": "अव्यय"},
            {"question": "‘शब्दः’ शब्द का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "द्विवचन", "अनेकवचन"], "answer": "एकवचन"},
            {"question": "‘रामेण’ शब्द का कारक क्या है?", "options": ["करण कारक", "अपादान कारक", "सम्प्रदान कारक", "अधिकरण कारक"], "answer": "करण कारक"},
            {"question": "‘गच्छतु’ शब्द का लकार क्या है?", "options": ["लोट्", "लुट्", "लृट्", "लिट्"], "answer": "लोट्"},
            {"question": "‘सत्यमेव जयते’ में ‘सत्यम्’ शब्द क्या है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "संज्ञा"}
        ]
    }
},
"7": {
    "Mathematics": {
        "Easy": [
            {"question": "What is the place value of 7 in 47,853?", "options": ["7", "700", "7,000", "70,000"], "answer": "7,000"},
            {"question": "Simplify: 8 + 6 × 2", "options": ["28", "20", "16", "24"], "answer": "20"},
            {"question": "What is the sum of interior angles of a triangle?", "options": ["90°", "180°", "360°", "270°"], "answer": "180°"},
            {"question": "What is the next prime number after 7?", "options": ["9", "11", "13", "17"], "answer": "11"},
            {"question": "How many sides does a pentagon have?", "options": ["4", "5", "6", "8"], "answer": "5"},
            {"question": "Convert 1/2 into decimal.", "options": ["0.25", "0.5", "0.75", "1"], "answer": "0.5"},
            {"question": "What is 15% of 200?", "options": ["20", "25", "30", "35"], "answer": "30"},
            {"question": "Which of these is an acute angle?", "options": ["45°", "90°", "120°", "180°"], "answer": "45°"},
            {"question": "What is 7 × 9?", "options": ["54", "56", "63", "72"], "answer": "63"},
            {"question": "What is the LCM of 4 and 6?", "options": ["12", "24", "18", "10"], "answer": "12"}
        ],
        "Medium": [
            {"question": "Solve: 3(x + 5) = 21. Find x.", "options": ["2", "3", "4", "5"], "answer": "2"},
            {"question": "What is the area of a rectangle with length 7 cm and breadth 4 cm?", "options": ["28 cm²", "22 cm²", "24 cm²", "30 cm²"], "answer": "28 cm²"},
            {"question": "The sum of angles on a straight line is?", "options": ["90°", "180°", "360°", "270°"], "answer": "180°"},
            {"question": "Find the value of 2³ + 3².", "options": ["17", "18", "12", "14"], "answer": "17"},
            {"question": "If a triangle has sides 3 cm, 4 cm, and 5 cm, what type of triangle is it?", "options": ["Equilateral", "Isosceles", "Right-angled", "Scalene"], "answer": "Right-angled"},
            {"question": "What is the volume of a cube with side 5 cm?", "options": ["125 cm³", "100 cm³", "25 cm³", "50 cm³"], "answer": "125 cm³"},
            {"question": "Express 0.375 as a fraction.", "options": ["3/8", "7/20", "5/8", "1/4"], "answer": "3/8"},
            {"question": "What is the difference between the greatest and smallest 3-digit number?", "options": ["899", "900", "999", "1000"], "answer": "899"},
            {"question": "If the perimeter of a square is 20 cm, what is the length of one side?", "options": ["4 cm", "5 cm", "6 cm", "7 cm"], "answer": "5 cm"},
            {"question": "What is the HCF of 18 and 24?", "options": ["6", "8", "9", "12"], "answer": "6"}
        ],
        "Hard": [
            {"question": "If 5x - 3 = 2x + 9, find x.", "options": ["2", "3", "4", "5"], "answer": "4"},
            {"question": "The sum of three consecutive numbers is 72. Find the numbers.", "options": ["23, 24, 25", "24, 25, 26", "22, 23, 24", "21, 22, 23"], "answer": "23, 24, 25"},
            {"question": "A cylinder has radius 7 cm and height 10 cm. Find its volume. (Use π = 22/7)", "options": ["1540 cm³", "1430 cm³", "1500 cm³", "1600 cm³"], "answer": "1540 cm³"},
            {"question": "If the ratio of two numbers is 3:4 and their LCM is 36, find the numbers.", "options": ["9 and 12", "6 and 8", "12 and 16", "15 and 20"], "answer": "9 and 12"},
            {"question": "What is the sum of interior angles of a hexagon?", "options": ["540°", "720°", "600°", "360°"], "answer": "720°"},
            {"question": "Simplify: (2/3) ÷ (4/9)", "options": ["3/2", "1/2", "9/8", "2/3"], "answer": "3/2"},
            {"question": "Find the median of the data set: 12, 15, 20, 22, 25, 30, 35.", "options": ["20", "22", "23.5", "25"], "answer": "22"},
            {"question": "If a triangle has sides 7 cm, 24 cm and 25 cm, is it a right triangle?", "options": ["Yes", "No"], "answer": "Yes"},
            {"question": "Factorize: x² + 5x + 6.", "options": ["(x + 2)(x + 3)", "(x - 2)(x - 3)", "(x + 1)(x + 6)", "(x - 1)(x - 6)"], "answer": "(x + 2)(x + 3)"},
            {"question": "What is the probability of getting an even number when a die is rolled?", "options": ["1/2", "1/3", "1/4", "1/6"], "answer": "1/2"}
        ]
    },
    "English": {
        "Easy": [
            {"question": "Choose the correct plural form of 'knife'.", "options": ["knifes", "knives", "knifes", "knive"], "answer": "knives"},
            {"question": "Fill in the blank: She ___ going to school.", "options": ["is", "are", "am", "be"], "answer": "is"},
            {"question": "What is the synonym of 'happy'?", "options": ["sad", "joyful", "angry", "tired"], "answer": "joyful"},
            {"question": "Choose the correct article: ___ elephant is big.", "options": ["A", "An", "The", "No article"], "answer": "An"},
            {"question": "Identify the adjective: The sky is blue.", "options": ["sky", "is", "blue", "The"], "answer": "blue"},
            {"question": "What is the opposite of 'cold'?", "options": ["hot", "warm", "cool", "freezing"], "answer": "hot"},
            {"question": "Fill in the blank: They ___ playing football.", "options": ["is", "are", "am", "be"], "answer": "are"},
            {"question": "Choose the correct spelling:", "options": ["becaus", "because", "becauss", "becauz"], "answer": "because"},
            {"question": "What is the past tense of 'write'?", "options": ["writed", "wrote", "writing", "writes"], "answer": "wrote"},
            {"question": "Identify the pronoun: She is my friend.", "options": ["She", "my", "friend", "is"], "answer": "She"}
        ],
        "Medium": [
            {"question": "Choose the correct verb: He ___ finished his homework.", "options": ["has", "have", "had", "having"], "answer": "has"},
            {"question": "Select the correct sentence.", "options": ["I goes to school.", "I go to school.", "I going to school.", "I gone to school."], "answer": "I go to school."},
            {"question": "Find the antonym of 'beautiful'.", "options": ["ugly", "pretty", "handsome", "nice"], "answer": "ugly"},
            {"question": "Identify the adverb: She sings beautifully.", "options": ["sings", "beautifully", "she", "none"], "answer": "beautifully"},
            {"question": "Choose the correct tense: They ___ playing cricket now.", "options": ["is", "are", "am", "be"], "answer": "are"},
            {"question": "Pick the correct preposition: The book is ___ the table.", "options": ["on", "in", "under", "beside"], "answer": "on"},
            {"question": "Choose the conjunction: I want tea ___ coffee.", "options": ["and", "but", "or", "so"], "answer": "or"},
            {"question": "Identify the subject: The birds are singing.", "options": ["birds", "are", "singing", "The"], "answer": "birds"},
            {"question": "Fill in: This is ___ pen.", "options": ["his", "him", "he", "hers"], "answer": "his"},
            {"question": "Which is a proper noun?", "options": ["city", "india", "India", "country"], "answer": "India"}
        ],
        "Hard": [
            {"question": "Identify the indirect object: He gave her a gift.", "options": ["He", "her", "a gift", "gave"], "answer": "her"},
            {"question": "Find the synonym of 'ancient'.", "options": ["old", "modern", "ancient", "historic"], "answer": "old"},
            {"question": "Choose: Neither of the options ___ correct.", "options": ["are", "is", "were", "be"], "answer": "is"},
            {"question": "What type of sentence is: 'Please close the door.'?", "options": ["Imperative", "Interrogative", "Declarative", "Exclamatory"], "answer": "Imperative"},
            {"question": "Passive form: 'They built the house.'", "options": ["The house was built by them.", "The house is built by them.", "The house built by them.", "They was built the house."], "answer": "The house was built by them."},
            {"question": "Choose the correct form: By next year, I ___ graduated.", "options": ["will have", "will", "have", "had"], "answer": "will have"},
            {"question": "What does the idiom 'break the ice' mean?", "options": ["start conversation", "break something", "freeze water", "get angry"], "answer": "start conversation"},
            {"question": "Reported speech: He said, 'I am happy.'", "options": ["He said he was happy.", "He said he is happy.", "He says he was happy.", "He said he will be happy."], "answer": "He said he was happy."},
            {"question": "Identify the correct spelling:", "options": ["Receive", "Recieve", "Receeve", "Recive"], "answer": "Receive"},
            {"question": "What is a phrasal verb?", "options": ["two-word verb", "noun + verb", "adjective phrase", "single verb"], "answer": "two-word verb"}
        ]
    },
    "Science": {
        "Easy": [
            {"question": "What is the boiling point of water?", "options": ["100°C", "0°C", "50°C", "25°C"], "answer": "100°C"},
            {"question": "Which gas do plants absorb for photosynthesis?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon dioxide"},
            {"question": "What is the process by which plants make their food?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Digestion"], "answer": "Photosynthesis"},
            {"question": "Which part of the plant conducts water?", "options": ["Xylem", "Phloem", "Leaf", "Root"], "answer": "Xylem"},
            {"question": "What do bees collect from flowers?", "options": ["Nectar", "Water", "Pollen", "Sap"], "answer": "Nectar"},
            {"question": "Which organ pumps blood in the human body?", "options": ["Lungs", "Kidneys", "Heart", "Liver"], "answer": "Heart"},
            {"question": "What is the natural source of light?", "options": ["Lamp", "Sun", "Bulb", "Fire"], "answer": "Sun"},
            {"question": "Which gas do humans breathe in?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Helium"], "answer": "Oxygen"},
            {"question": "What are animals that eat only plants called?", "options": ["Carnivores", "Herbivores", "Omnivores", "Insectivores"], "answer": "Herbivores"},
            {"question": "What do roots absorb from the soil?", "options": ["Water and minerals", "Air", "Sunlight", "Carbon dioxide"], "answer": "Water and minerals"}
        ],
        "Medium": [
            {"question": "Which part of the plant carries food from leaves to other parts?", "options": ["Xylem", "Phloem", "Stem", "Root"], "answer": "Phloem"},
            {"question": "What is the main function of the respiratory system?", "options": ["Digest food", "Pump blood", "Exchange gases", "Filter waste"], "answer": "Exchange gases"},
            {"question": "Which vitamin is produced in our skin when exposed to sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
            {"question": "Which of the following is a non-renewable source of energy?", "options": ["Solar energy", "Wind energy", "Coal", "Hydro energy"], "answer": "Coal"},
            {"question": "What is the unit of force?", "options": ["Newton", "Watt", "Pascal", "Joule"], "answer": "Newton"},
            {"question": "Which blood cells help in fighting infections?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "White blood cells"},
            {"question": "What is the basic unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "answer": "Cell"},
            {"question": "Which process releases energy in cells?", "options": ["Photosynthesis", "Respiration", "Digestion", "Excretion"], "answer": "Respiration"},
            {"question": "What is the function of the skeleton?", "options": ["Protection", "Movement", "Support", "All of these"], "answer": "All of these"},
            {"question": "Which organ helps in removing waste from the blood?", "options": ["Liver", "Kidneys", "Lungs", "Heart"], "answer": "Kidneys"}
        ],
        "Hard": [
            {"question": "What is osmosis?", "options": ["Movement of water from high to low concentration", "Movement of solutes from low to high concentration", "Movement of water from low to high concentration", "Movement of solutes from high to low concentration"], "answer": "Movement of water from high to low concentration"},
            {"question": "Which part of the brain controls balance?", "options": ["Cerebrum", "Cerebellum", "Medulla", "Spinal cord"], "answer": "Cerebellum"},
            {"question": "Which blood group is known as the universal donor?", "options": ["A", "B", "AB", "O"], "answer": "O"},
            {"question": "What is the chemical formula of water?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
            {"question": "Which vitamin is essential for blood clotting?", "options": ["Vitamin A", "Vitamin K", "Vitamin C", "Vitamin D"], "answer": "Vitamin K"},
            {"question": "What is the function of mitochondria in a cell?", "options": ["Protein synthesis", "Energy production", "Digestion", "Waste removal"], "answer": "Energy production"},
            {"question": "What is the role of chlorophyll in plants?", "options": ["Absorbs sunlight", "Produces oxygen", "Stores food", "Absorbs water"], "answer": "Absorbs sunlight"},
            {"question": "What is the difference between conductors and insulators?", "options": ["Conductors allow electricity to flow, insulators do not", "Insulators allow electricity to flow, conductors do not", "Both conduct electricity", "Neither conduct electricity"], "answer": "Conductors allow electricity to flow, insulators do not"},
            {"question": "Which part of the eye controls the amount of light entering?", "options": ["Cornea", "Iris", "Lens", "Retina"], "answer": "Iris"},
            {"question": "What is the term for animals that can live both on land and water?", "options": ["Mammals", "Reptiles", "Amphibians", "Birds"], "answer": "Amphibians"}
        ]
    },
    "Social Science": {
        "Easy": [
            {"question": "Who was the founder of the Mughal Empire in India?", "options": ["Akbar", "Babur", "Aurangzeb", "Shah Jahan"], "answer": "Babur"},
            {"question": "Which river is known as the 'Sorrow of Bihar'?", "options": ["Ganga", "Kosi", "Yamuna", "Brahmaputra"], "answer": "Kosi"},
            {"question": "What is the main purpose of a constitution?", "options": ["To declare war", "To outline laws and rights", "To elect the Prime Minister", "To collect taxes"], "answer": "To outline laws and rights"},
            {"question": "What type of government is present in India?", "options": ["Monarchy", "Democracy", "Dictatorship", "Oligarchy"], "answer": "Democracy"},
            {"question": "Which mountain range separates India from China?", "options": ["Himalayas", "Western Ghats", "Vindhyas", "Aravallis"], "answer": "Himalayas"},
            {"question": "What is the capital city of Rajasthan?", "options": ["Jaipur", "Udaipur", "Jodhpur", "Bikaner"], "answer": "Jaipur"},
            {"question": "Which leader is known as the 'Father of the Indian Constitution'?", "options": ["Jawaharlal Nehru", "B.R. Ambedkar", "Mahatma Gandhi", "Sardar Patel"], "answer": "B.R. Ambedkar"},
            {"question": "Which is the largest state in India by area?", "options": ["Maharashtra", "Rajasthan", "Madhya Pradesh", "Uttar Pradesh"], "answer": "Rajasthan"},
            {"question": "What is the main crop grown in the Gangetic plains?", "options": ["Wheat", "Rice", "Maize", "Barley"], "answer": "Rice"},
            {"question": "Which is the lower house of the Indian Parliament?", "options": ["Rajya Sabha", "Lok Sabha", "Vidhan Sabha", "Gram Sabha"], "answer": "Lok Sabha"}
        ],
        "Medium": [
            {"question": "What was the main reason for the decline of the Mughal Empire?", "options": ["Invasions by foreign powers", "Internal conflicts and weak rulers", "Natural disasters", "Lack of trade"], "answer": "Internal conflicts and weak rulers"},
            {"question": "The Chipko Movement was related to:", "options": ["Wildlife protection", "Forest conservation", "Water pollution", "Urban development"], "answer": "Forest conservation"},
            {"question": "What is the function of the Election Commission of India?", "options": ["Conduct elections", "Make laws", "Collect taxes", "Maintain law and order"], "answer": "Conduct elections"},
            {"question": "Which soil type is most suitable for growing cotton?", "options": ["Red soil", "Black soil", "Alluvial soil", "Laterite soil"], "answer": "Black soil"},
            {"question": "The Satyagraha movement was started by:", "options": ["Jawaharlal Nehru", "Subhash Chandra Bose", "Mahatma Gandhi", "Bhagat Singh"], "answer": "Mahatma Gandhi"},
            {"question": "What is the main source of energy for photosynthesis?", "options": ["Water", "Oxygen", "Sunlight", "Soil"], "answer": "Sunlight"},
            {"question": "Which of these is a fundamental right in India?", "options": ["Right to property", "Right to vote", "Right to education", "Right to carry arms"], "answer": "Right to education"},
            {"question": "What is the term for a group of people living together in a village and managing local affairs?", "options": ["Panchayat", "Municipality", "Corporation", "Parliament"], "answer": "Panchayat"},
            {"question": "Which river is called the 'Dakshina Ganga'?", "options": ["Godavari", "Krishna", "Cauvery", "Narmada"], "answer": "Godavari"},
            {"question": "What is a referendum?", "options": ["A public vote on a particular issue", "A parliamentary session", "A court judgment", "An election campaign"], "answer": "A public vote on a particular issue"}
        ],
        "Hard": [
            {"question": "Who was the last Governor-General of independent India?", "options": ["Lord Mountbatten", "C. Rajagopalachari", "Jawaharlal Nehru", "Sardar Patel"], "answer": "C. Rajagopalachari"},
            {"question": "What was the main purpose of the Rowlatt Act?", "options": ["To promote education", "To restrict civil liberties", "To improve agriculture", "To grant independence"], "answer": "To restrict civil liberties"},
            {"question": "Which amendment gave the right to property the status of a legal right instead of a fundamental right?", "options": ["42nd Amendment", "44th Amendment", "25th Amendment", "61st Amendment"], "answer": "44th Amendment"},
            {"question": "The Indian National Congress session of 1929 is famous for:", "options": ["Passing the Purna Swaraj resolution", "Electing Gandhi as president", "Demanding separate electorates", "Opposing British rule peacefully"], "answer": "Passing the Purna Swaraj resolution"},
            {"question": "What is the primary function of the Lok Sabha Speaker?", "options": ["Conducting parliamentary debates", "Making laws", "Enforcing laws", "Overseeing elections"], "answer": "Conducting parliamentary debates"},
            {"question": "Which state in India was formerly known as Mysore?", "options": ["Karnataka", "Kerala", "Tamil Nadu", "Andhra Pradesh"], "answer": "Karnataka"},
            {"question": "The Thar Desert is located in which state?", "options": ["Rajasthan", "Gujarat", "Haryana", "Punjab"], "answer": "Rajasthan"},
            {"question": "What was the main cause of the Revolt of 1857?", "options": ["Economic exploitation", "Religious interference", "Use of greased cartridges", "All of the above"], "answer": "All of the above"},
            {"question": "Who wrote the famous book 'Annihilation of Caste'?", "options": ["B.R. Ambedkar", "Jawaharlal Nehru", "Mahatma Gandhi", "Rabindranath Tagore"], "answer": "B.R. Ambedkar"},
            {"question": "Which constitutional body protects the fundamental rights of citizens?", "options": ["Supreme Court", "Election Commission", "Comptroller and Auditor General", "Finance Commission"], "answer": "Supreme Court"}
        ]
    },
  "Hindi": {
    "Easy": [
      {"question": "किसका अर्थ है 'कहानी'?", "options": ["नाटक", "कहानी", "गीत", "निबंध"], "answer": "कहानी"},
      {"question": "निम्नलिखित में से कौन सा एक शब्द है?", "options": ["खेलना", "खेल", "खेलता", "खेलने"], "answer": "खेल"},
      {"question": "‘सुंदर’ का पर्यायवाची शब्द कौन सा है?", "options": ["अस सुंदर", "खूबसूरत", "भद्दा", "साधारण"], "answer": "खूबसूरत"},
      {"question": "‘रवि’ का अर्थ क्या होता है?", "options": ["चंद्रमा", "सूरज", "तारा", "आकाश"], "answer": "सूरज"},
      {"question": "किसमें ‘संज्ञा’ होती है?", "options": ["व्यक्ति", "क्रिया", "विशेषण", "वाच्य"], "answer": "व्यक्ति"},
      {"question": "‘मैं खेलता हूँ’ में क्रिया कौन सी है?", "options": ["मैं", "खेलता", "हूँ", "नहीं"], "answer": "खेलता"},
      {"question": "निम्नलिखित में से कौन सा वचन है?", "options": ["वचन", "एकवचन", "बहुवचन", "सर्वनाम"], "answer": "एकवचन"},
      {"question": "‘लाल’ शब्द किस प्रकार का शब्द है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "विशेषण"},
      {"question": "किसमें ‘सर्वनाम’ होता है?", "options": ["मैं", "घर", "खेल", "सड़क"], "answer": "मैं"},
      {"question": "‘पढ़ना’ शब्द किस प्रकार का है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "क्रिया"}
    ],
    "Medium": [
      {"question": "‘सूरज निकल रहा है’ में कौन-सी क्रिया है?", "options": ["निकल", "सूरज", "रहा", "है"], "answer": "निकल"},
      {"question": "‘वह छात्र पुस्तक पढ़ रहा है’ में ‘वह’ किस प्रकार का शब्द है?", "options": ["संज्ञा", "सर्वनाम", "विशेषण", "क्रिया"], "answer": "सर्वनाम"},
      {"question": "‘कृपया दरवाजा बंद करो’ में क्रिया कौन-सी है?", "options": ["दरवाजा", "कृपया", "बंद करो", "को"], "answer": "बंद करो"},
      {"question": "निम्नलिखित में से कौन-सा वाक्य सही है?", "options": ["मैं बाज़ार जाऊंगा", "मैं बाज़ार जाएगी", "मैं बाज़ार जाएंगे", "मैं बाज़ार जाना"], "answer": "मैं बाज़ार जाऊंगा"},
      {"question": "‘धैर्य’ शब्द का सही अर्थ क्या है?", "options": ["सहनशीलता", "क्रोध", "निराशा", "जल्दबाजी"], "answer": "सहनशीलता"},
      {"question": "‘यहाँ बहुत सारे पेड़ हैं’ में ‘बहुत सारे’ किस प्रकार के शब्द हैं?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "विशेषण"},
      {"question": "‘राम ने खेला’ वाक्य में ‘ने’ क्या है?", "options": ["संज्ञा", "कारक चिन्ह", "सर्वनाम", "क्रिया"], "answer": "कारक चिन्ह"},
      {"question": "निम्नलिखित में से कौन-सा वाक्य कर्ता विहीन है?", "options": ["वह खेल रहा है", "बारिश हो रही है", "मैं घर जा रहा हूँ", "वे पढ़ रहे हैं"], "answer": "बारिश हो रही है"},
      {"question": "‘बहुत’ शब्द का पर्यायवाची क्या है?", "options": ["कम", "अधिक", "थोड़ा", "मध्यम"], "answer": "अधिक"},
      {"question": "‘खेल’ शब्द का विलोम शब्द क्या है?", "options": ["अखेल", "रोक", "काम", "विश्राम"], "answer": "काम"}
    ],
    "Hard": [
      {"question": "‘रचना’ शब्द किस भाषा से लिया गया है?", "options": ["संस्कृत", "अंग्रेज़ी", "फारसी", "अरबी"], "answer": "संस्कृत"},
      {"question": "‘संधि’ किसे कहते हैं?", "options": ["शब्दों का मिलन", "वाक्य", "अलंकार", "काव्य"], "answer": "शब्दों का मिलन"},
      {"question": "‘समास’ किसे कहते हैं?", "options": ["दो या अधिक शब्दों का युग्म", "एक शब्द", "वाक्य", "पद्य"], "answer": "दो या अधिक शब्दों का युग्म"},
      {"question": "‘अलंकार’ का अर्थ क्या है?", "options": ["सजावट", "काव्य का शिल्प", "छंद", "रचना"], "answer": "काव्य का शिल्प"},
      {"question": "‘उपसर्ग’ किसे कहते हैं?", "options": ["शब्द के पहले लगने वाले अक्षर", "शब्द के बाद लगने वाले अक्षर", "वाक्य के हिस्से", "अलंकार"], "answer": "शब्द के पहले लगने वाले अक्षर"},
      {"question": "‘धातु’ किसे कहते हैं?", "options": ["क्रिया के मूल रूप", "संज्ञा", "विशेषण", "सर्वनाम"], "answer": "क्रिया के मूल रूप"},
      {"question": "निम्नलिखित में से कौन सा वाक्य ‘संधि-विच्छेद’ है?", "options": ["रामायण", "गृहस्थ", "विद्या", "सर्वत्र"], "answer": "गृहस्थ"},
      {"question": "‘वाक्य’ में कितने भेद होते हैं?", "options": ["2", "3", "4", "5"], "answer": "4"},
      {"question": "‘काव्य’ का प्रमुख उद्देश्य क्या है?", "options": ["सौंदर्य प्रस्तुत करना", "सूचना देना", "आदेश देना", "तथ्य बताना"], "answer": "सौंदर्य प्रस्तुत करना"},
      {"question": "‘चित्रकाव्य’ किस प्रकार की कविता है?", "options": ["चित्रात्मक कविता", "गीत", "नाटक", "गद्य"], "answer": "चित्रात्मक कविता"}
    ]
  },
  "Sanskrit": {
    "Easy": [
      {"question": "‘रामः’ शब्दस्य अर्थः किम्?", "options": ["राम", "सीता", "हनुमान्", "लक्ष्मणः"], "answer": "राम"},
      {"question": "‘अस्ति’ क्रिया शब्दः का अर्थः?", "options": ["है", "होगा", "था", "चलता है"], "answer": "है"},
      {"question": "‘फलम्’ शब्दस्य जातिः किम्?", "options": ["पुंल्लिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग", "बहुवचन"], "answer": "नपुंसकलिङ्ग"},
      {"question": "‘बालिका’ शब्दस्य अर्थः किम्?", "options": ["लड़की", "लड़का", "गाय", "कुत्ता"], "answer": "लड़की"},
      {"question": "‘गच्छति’ क्रिया का अर्थ क्या है?", "options": ["चलना", "सोचना", "खाना", "पीना"], "answer": "चलना"},
      {"question": "‘अहं’ सर्वनाम का अर्थ है?", "options": ["मैं", "तुम", "वह", "हम"], "answer": "मैं"},
      {"question": "‘सूर्यः’ शब्द का अर्थ है?", "options": ["चंद्रमा", "सूरज", "तारा", "पृथ्वी"], "answer": "सूरज"},
      {"question": "‘शिक्षकः’ शब्द का अर्थ है?", "options": ["छात्र", "शिक्षक", "पुस्तक", "विद्यालय"], "answer": "शिक्षक"},
      {"question": "‘पुस्तकम्’ शब्द का लिंग क्या है?", "options": ["पुंल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "बहुवचन"], "answer": "नपुंसकलिंग"},
      {"question": "‘वनम्’ शब्द का अर्थ क्या है?", "options": ["नगर", "वन", "नदी", "पहाड़"], "answer": "वन"}
    ],
    "Medium": [
      {"question": "‘रामः वनं गच्छति’ वाक्यं कथम् अस्ति?", "options": ["सरल वाक्य", "योजनावाक्य", "समासवाक्य", "वाक्यं नास्ति"], "answer": "सरल वाक्य"},
      {"question": "‘शुभ्रं’ शब्दस्य अर्थः किम्?", "options": ["सफेद", "काला", "लाल", "नीला"], "answer": "सफेद"},
      {"question": "‘बालिका विद्यालयं गच्छति’ इति वाक्ये कः कर्ता?", "options": ["विद्यालयं", "बालिका", "गच्छति", "किंचिदपि न"], "answer": "बालिका"},
      {"question": "‘मधुरं गीतं गायति’ इति वाक्यस्य क्रिया किम्?", "options": ["मधुरं", "गीतं", "गायति", "न"], "answer": "गायति"},
      {"question": "‘सः फलानि खादति’ इत्यत्र ‘फलानि’ शब्दस्य वचनं किम्?", "options": ["एकवचनम्", "बहुवचनम्", "द्विवचनम्", "नपुंसकलिङ्ग"], "answer": "बहुवचनम्"},
      {"question": "‘रामः पुस्तकम् पठति’ इति वाक्ये ‘पुस्तकम्’ शब्दस्य कारकः किम्?", "options": ["कर्तृकारकः", "कर्मकारकः", "सम्प्रदानकारकः", "अधिकारकारकः"], "answer": "कर्मकारकः"},
      {"question": "‘भवान्’ शब्दः कः सर्वनामः?", "options": ["पुरुष", "व्यक्ति", "प्रथम पुरुष", "तृतीय पुरुष"], "answer": "व्यक्ति"},
      {"question": "‘अहं गच्छामि’ वाक्ये क्रियापदानाम् रूपं किम्?", "options": ["गच्छति", "गच्छामि", "गच्छसि", "गच्छन्ति"], "answer": "गच्छामि"},
      {"question": "‘रामस्य पुस्तकं’ इति वाक्ये ‘रामस्य’ पदस्य कारकः कः?", "options": ["कर्तृकारकः", "सम्प्रदानकारकः", "सम्बन्धकारकः", "अधिकारकारकः"], "answer": "सम्बन्धकारकः"},
      {"question": "‘सुन्दरः पुष्पः’ इति पदयोः सम्बन्धः कः?", "options": ["विशेषण-संज्ञा सम्बन्धः", "संज्ञा-सर्वनाम सम्बन्धः", "क्रिया-संज्ञा सम्बन्धः", "विशेषण-क्रिया सम्बन्धः"], "answer": "विशेषण-संज्ञा सम्बन्धः"}
    ],
    "Hard": [
      {"question": "‘समासः’ इति किमर्थं प्रयुज्यते?", "options": ["द्वौ वा अधिकौ पदौ एकस्मिन्पद्मध्ये सम्यक् योज्यन्ते", "शब्दस्य लिङ्गपरिवर्तनाय", "क्रियापदस्य रूपनिर्माणाय", "सर्वनामस्य रूपनिर्माणाय"], "answer": "द्वौ वा अधिकौ पदौ एकस्मिन्पद्मध्ये सम्यक् योज्यन्ते"},
      {"question": "‘कर्मणि’ कारकः कः अस्ति?", "options": ["कर्तृकारकः", "कर्मकारकः", "सम्प्रदानकारकः", "अपादानकारकः"], "answer": "कर्मकारकः"},
      {"question": "‘अव्यय’ शब्दस्य अर्थः किम्?", "options": ["परिवर्तनीय शब्दः", "अपरिवर्तनीय शब्दः", "संज्ञा", "विशेषण"], "answer": "अपरिवर्तनीय शब्दः"},
      {"question": "‘कर्तृवाच्यः’ वाक्यः कः?", "options": ["यः कर्ता स्पष्टः भवति", "यः कर्म स्पष्टः भवति", "यः क्रिया न स्पष्टा भवति", "यः सर्वनामः भवति"], "answer": "यः कर्ता स्पष्टः भवति"},
      {"question": "‘द्वन्द्वसमासः’ कः?", "options": ["द्वौ पदौ समासे सम्यक् योजितौ", "एकः पदः द्विगुणो भवति", "एकस्मिन्नेव पद्मध्ये क्रिया योज्यते", "अव्ययस्य उपयोगः"], "answer": "द्वौ पदौ समासे सम्यक् योजितौ"},
      {"question": "‘संस्कृतस्य लिपिः कया लिख्यते?’", "options": ["देवनागरी", "रोमन", "अरबी", "बंगाली"], "answer": "देवनागरी"},
      {"question": "‘धातु’ शब्दस्य प्रयोगः कः?", "options": ["क्रियापदस्य मूलः", "संज्ञा", "विशेषण", "सर्वनाम"], "answer": "क्रियापदस्य मूलः"},
      {"question": "‘प्रत्ययः’ कः?", "options": ["शब्दस्य अंते योज्यते", "शब्दस्य आरम्भे योज्यते", "वाक्यस्य आरम्भे योज्यते", "क्रियापदस्य अंते न योज्यते"], "answer": "शब्दस्य अंते योज्यते"},
      {"question": "‘कर्णधारः’ पदस्य अर्थः?", "options": ["हेयरबैंड", "मुख्य व्यक्ति", "सरकार", "भूमि"], "answer": "मुख्य व्यक्ति"},
      {"question": "‘पदपरिवर्तन’ इति किमर्थं भवति?", "options": ["शब्दस्य रूपान्तरम्", "वाक्यस्य संरचना", "वाक्यस्य विस्तारः", "पद्यस्य छन्दः"], "answer": "शब्दस्य रूपान्तरम्"}
    ]
  }
},
"8": {
    "Mathematics": {
        "Easy": [
            {"question": "What is the value of 5²?", "options": ["10", "25", "15", "20"], "answer": "25"},
            {"question": "Which number is a rational number?", "options": ["√2", "π", "3/4", "0.333..."], "answer": "3/4"},
            {"question": "Which of the following is an equation?", "options": ["2x + 3", "x – 4 = 6", "x + 5", "5x"], "answer": "x – 4 = 6"},
            {"question": "Which is a perfect square?", "options": ["18", "36", "45", "50"], "answer": "36"},
            {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "answer": "6"},
            {"question": "Which of these is an even number?", "options": ["15", "21", "42", "33"], "answer": "42"},
            {"question": "What is the value of x in: x + 4 = 9?", "options": ["3", "5", "7", "9"], "answer": "5"},
            {"question": "The additive identity of integers is:", "options": ["1", "0", "-1", "None"], "answer": "0"},
            {"question": "What is the value of √64?", "options": ["6", "7", "8", "9"], "answer": "8"},
            {"question": "In a triangle, the sum of angles is:", "options": ["360°", "90°", "180°", "100°"], "answer": "180°"}
        ],
        "Medium": [
            {"question": "Which of these is a solution of the equation 2x = 10?", "options": ["2", "5", "10", "12"], "answer": "5"},
            {"question": "What is the square root of 121?", "options": ["10", "11", "12", "13"], "answer": "11"},
            {"question": "What is the cube of 3?", "options": ["6", "9", "27", "18"], "answer": "27"},
            {"question": "Which of the following is not a rational number?", "options": ["2/3", "4/5", "√5", "7/8"], "answer": "√5"},
            {"question": "What is the perimeter of a square of side 6 cm?", "options": ["12 cm", "18 cm", "24 cm", "36 cm"], "answer": "24 cm"},
            {"question": "Which of the following is a prime number?", "options": ["15", "21", "29", "35"], "answer": "29"},
            {"question": "A triangle with all sides equal is called:", "options": ["Isosceles", "Scalene", "Right-angled", "Equilateral"], "answer": "Equilateral"},
            {"question": "Value of (-3)² is:", "options": ["-6", "6", "9", "-9"], "answer": "9"},
            {"question": "What is the area of a rectangle with length 8 cm and breadth 5 cm?", "options": ["13 cm²", "40 cm²", "30 cm²", "25 cm²"], "answer": "40 cm²"},
            {"question": "Which of the following is a linear equation?", "options": ["x² + 3 = 9", "2x – 3 = 5", "x³ = 27", "x⁴ = 16"], "answer": "2x – 3 = 5"}
        ],
        "Hard": [
            {"question": "What is the cube root of 512?", "options": ["8", "9", "6", "7"], "answer": "8"},
            {"question": "Which of the following is a Pythagorean triplet?", "options": ["3, 4, 6", "5, 12, 13", "6, 8, 10", "7, 24, 26"], "answer": "5, 12, 13"},
            {"question": "If x/2 = 3/4, then x =", "options": ["3/2", "1.5", "6/4", "3/2"], "answer": "3/2"},
            {"question": "Area of a triangle with base 10 cm and height 6 cm is:", "options": ["60 cm²", "30 cm²", "20 cm²", "40 cm²"], "answer": "30 cm²"},
            {"question": "The volume of a cube of side 5 cm is:", "options": ["125 cm³", "100 cm³", "25 cm³", "150 cm³"], "answer": "125 cm³"},
            {"question": "In statistics, the median of the data: 2, 5, 8, 11, 14 is:", "options": ["5", "8", "11", "14"], "answer": "8"},
            {"question": "Which is a perfect cube?", "options": ["64", "125", "100", "90"], "answer": "125"},
            {"question": "The angle sum of a quadrilateral is:", "options": ["180°", "360°", "270°", "90°"], "answer": "360°"},
            {"question": "Which of the following represents a rational number?", "options": ["√7", "π", "3/7", "√2"], "answer": "3/7"},
            {"question": "If 5x – 3 = 2x + 6, then x =", "options": ["2", "3", "4", "5"], "answer": "3"}
        ]
    },
    "Science": {
        "Easy": [
            {"question": "What is the function of roots in a plant?", "options": ["Photosynthesis", "Anchoring and absorbing water", "Reproduction", "Transpiration"], "answer": "Anchoring and absorbing water"},
            {"question": "Which gas is essential for respiration?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "Which part of the human body helps in breathing?", "options": ["Heart", "Lungs", "Kidneys", "Liver"], "answer": "Lungs"},
            {"question": "How many planets are there in the solar system?", "options": ["7", "8", "9", "10"], "answer": "8"},
            {"question": "Which of these is a synthetic fibre?", "options": ["Cotton", "Wool", "Silk", "Nylon"], "answer": "Nylon"},
            {"question": "Which organ pumps blood in our body?", "options": ["Lungs", "Brain", "Heart", "Liver"], "answer": "Heart"},
            {"question": "What is the process of changing water into vapour called?", "options": ["Condensation", "Precipitation", "Evaporation", "Sublimation"], "answer": "Evaporation"},
            {"question": "Which of the following is a liquid at room temperature?", "options": ["Oxygen", "Water", "Iron", "Carbon dioxide"], "answer": "Water"},
            {"question": "Which force pulls objects towards the Earth?", "options": ["Friction", "Magnetic force", "Gravitational force", "Electrostatic force"], "answer": "Gravitational force"},
            {"question": "What is the unit of current?", "options": ["Ohm", "Volt", "Watt", "Ampere"], "answer": "Ampere"}
        ],
        "Medium": [
            {"question": "Which of the following is a non-metal that is liquid at room temperature?", "options": ["Bromine", "Mercury", "Chlorine", "Carbon"], "answer": "Bromine"},
            {"question": "Which hormone is responsible for growth in humans?", "options": ["Insulin", "Thyroxine", "Growth hormone", "Adrenaline"], "answer": "Growth hormone"},
            {"question": "Which acid is present in lemon?", "options": ["Acetic acid", "Citric acid", "Sulphuric acid", "Hydrochloric acid"], "answer": "Citric acid"},
            {"question": "Which part of the cell contains the genetic material?", "options": ["Cytoplasm", "Nucleus", "Cell membrane", "Mitochondria"], "answer": "Nucleus"},
            {"question": "Which of these is a renewable source of energy?", "options": ["Coal", "Petrol", "Wind", "Diesel"], "answer": "Wind"},
            {"question": "What is friction?", "options": ["A force that pushes objects", "A force that pulls objects", "A force that opposes motion", "A magnetic force"], "answer": "A force that opposes motion"},
            {"question": "Which blood cells help in fighting infection?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "White blood cells"},
            {"question": "Which metal is used in making thermometers?", "options": ["Gold", "Copper", "Mercury", "Aluminium"], "answer": "Mercury"},
            {"question": "Which of the following helps in digestion of food?", "options": ["Lungs", "Heart", "Stomach", "Kidneys"], "answer": "Stomach"},
            {"question": "What is the function of chlorophyll in plants?", "options": ["Absorbs nutrients", "Stores energy", "Gives green color and helps in photosynthesis", "Protects leaves"], "answer": "Gives green color and helps in photosynthesis"}
        ],
        "Hard": [
            {"question": "Which process is responsible for the formation of clouds?", "options": ["Evaporation", "Condensation", "Precipitation", "Transpiration"], "answer": "Condensation"},
            {"question": "What type of joint is found in the shoulder?", "options": ["Hinge joint", "Pivot joint", "Ball and socket joint", "Fixed joint"], "answer": "Ball and socket joint"},
            {"question": "Which organ filters blood in the human body?", "options": ["Liver", "Heart", "Kidney", "Lungs"], "answer": "Kidney"},
            {"question": "Which instrument is used to measure atmospheric pressure?", "options": ["Thermometer", "Barometer", "Anemometer", "Hygrometer"], "answer": "Barometer"},
            {"question": "Which of these is a sexually transmitted disease?", "options": ["Typhoid", "HIV/AIDS", "Malaria", "Dengue"], "answer": "HIV/AIDS"},
            {"question": "Which planet has the largest number of moons?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Saturn"},
            {"question": "Which layer of the Earth is made of molten rock?", "options": ["Crust", "Mantle", "Core", "Lithosphere"], "answer": "Mantle"},
            {"question": "Which vitamin is synthesized in our skin in the presence of sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
            {"question": "Which method is best for removing salt from seawater?", "options": ["Filtration", "Sedimentation", "Evaporation", "Decantation"], "answer": "Evaporation"},
            {"question": "What is the main cause of acid rain?", "options": ["Carbon monoxide", "Nitrogen and sulphur oxides", "Ozone", "Helium"], "answer": "Nitrogen and sulphur oxides"}
        ]
    },
    "English": {
        "Easy": [
            {"question": "Who is the author of the story 'The Best Christmas Present in the World'?", "options": ["Charles Dickens", "Michael Morpurgo", "Ruskin Bond", "R.K. Narayan"], "answer": "Michael Morpurgo"},
            {"question": "What kind of animal is 'Macavity' in the poem 'Macavity – The Mystery Cat'?", "options": ["Dog", "Tiger", "Cat", "Lion"], "answer": "Cat"},
            {"question": "In the poem 'The Ant and the Cricket', who was lazy?", "options": ["The Ant", "The Cricket", "The Bee", "The Spider"], "answer": "The Cricket"},
            {"question": "What does the 'glorious sun' refer to in 'The Last Bargain'?", "options": ["Pride", "Freedom", "Money", "Power"], "answer": "Freedom"},
            {"question": "Who was the visitor in 'The Tsunami'?", "options": ["An animal", "A teacher", "A giant wave", "A farmer"], "answer": "A giant wave"},
            {"question": "What is the central theme of 'Geography Lesson'?", "options": ["Political issues", "Human greed", "Earth from a plane", "Historical monuments"], "answer": "Earth from a plane"},
            {"question": "What is the meaning of 'bargain' in 'The Last Bargain'?", "options": ["Agreement", "Argument", "Discussion", "Order"], "answer": "Agreement"},
            {"question": "Where was Tilly Smith during the Tsunami?", "options": ["Thailand", "Indonesia", "India", "Japan"], "answer": "Thailand"},
            {"question": "Who is the poet of 'When I Set Out for Lyonnesse'?", "options": ["W.B. Yeats", "Robert Frost", "Thomas Hardy", "Rabindranath Tagore"], "answer": "Thomas Hardy"},
            {"question": "What gift did Jim buy for Della in 'The Gift of the Magi'?", "options": ["A comb", "A watch chain", "A dress", "A mirror"], "answer": "A watch chain"}
        ],
        "Medium": [
            {"question": "In 'Children at Work', where did Velu run away to?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "Chennai"},
            {"question": "What is the profession of Taro in 'Taro’s Reward'?", "options": ["Farmer", "Woodcutter", "Fisherman", "Blacksmith"], "answer": "Woodcutter"},
            {"question": "Why did the narrator visit Mrs. Macpherson in 'The Best Christmas Present in the World'?", "options": ["To return her letter", "To sell books", "To take care of her", "To read poems"], "answer": "To return her letter"},
            {"question": "What did the earthquake do in the poem 'The Tsunami'?", "options": ["Destroyed buildings", "Triggered the tsunami", "Shook only trees", "Flooded fields"], "answer": "Triggered the tsunami"},
            {"question": "What lesson does 'The Ant and the Cricket' teach?", "options": ["Share food", "Plan for future", "Sing often", "Work less"], "answer": "Plan for future"},
            {"question": "In 'The Summit Within', who is the first Indian woman to climb Mt. Everest?", "options": ["Tenzing Norgay", "Santosh Yadav", "Bachendri Pal", "Premlata Agarwal"], "answer": "Bachendri Pal"},
            {"question": "Who helped Velu in the city in 'Children at Work'?", "options": ["A constable", "Jaya", "An old man", "Ramu"], "answer": "Jaya"},
            {"question": "What is the main idea in the poem 'On the Grasshopper and Cricket'?", "options": ["Birds chirping", "Nature’s constant music", "Animals in forest", "Rainy season"], "answer": "Nature’s constant music"},
            {"question": "In 'The Open Window', what was Vera’s talent?", "options": ["Singing", "Storytelling", "Drawing", "Cooking"], "answer": "Storytelling"},
            {"question": "In the poem 'The School Boy', why does the boy not enjoy school?", "options": ["He dislikes books", "He wants to play", "He feels caged and unhappy", "He likes the forest"], "answer": "He feels caged and unhappy"}
        ],
        "Hard": [
            {"question": "In 'A Short Monsoon Diary', who is the author?", "options": ["Ruskin Bond", "R.K. Narayan", "Michael Morpurgo", "Sudha Murty"], "answer": "Ruskin Bond"},
            {"question": "In 'This is Jody’s Fawn', why does Jody want to bring the fawn home?", "options": ["To save it", "To feed it", "He feels responsible as its mother died to save his father", "To gift it to Mill-wheel"], "answer": "He feels responsible as its mother died to save his father"},
            {"question": "What does the poem 'Macavity – The Mystery Cat' compare Macavity to?", "options": ["A policeman", "Napoleon of crime", "Sherlock Holmes", "A ghost"], "answer": "Napoleon of crime"},
            {"question": "In 'The Comet – I', what is the profession of Duttada?", "options": ["Mathematician", "Politician", "Amateur scientist", "Writer"], "answer": "Amateur scientist"},
            {"question": "In 'The Comet – II', who is Sir John Macpherson?", "options": ["British scientist", "Defence Minister", "Astronomer Royal", "UN leader"], "answer": "Defence Minister"},
            {"question": "In 'The Great Stone Face – I', what did Ernest’s mother tell him?", "options": ["To play", "To study", "To watch the stone face and wait", "To travel"], "answer": "To watch the stone face and wait"},
            {"question": "In 'The Great Stone Face – II', who was General Blood-and-Thunder?", "options": ["A school teacher", "A war hero", "A businessman", "A poet"], "answer": "A war hero"},
            {"question": "What is the figure of speech used in 'The Last Bargain'?", "options": ["Simile", "Alliteration", "Metaphor", "Personification"], "answer": "Metaphor"},
            {"question": "In 'The Summit Within', what is the ‘internal summit’?", "options": ["Another mountain", "A physical climb", "Conquering one’s fears", "A world record"], "answer": "Conquering one’s fears"},
            {"question": "Which poem describes summer and winter through insects?", "options": ["The School Boy", "The Ant and the Cricket", "On the Grasshopper and Cricket", "Geography Lesson"], "answer": "On the Grasshopper and Cricket"}
        ]
    },
    "Social Science": {
        "Easy": [
            {"question": "Who introduced the Doctrine of Lapse?", "options": ["Lord Mountbatten", "Lord Wellesley", "Lord Dalhousie", "Lord Curzon"], "answer": "Lord Dalhousie"},
            {"question": "What is the meaning of 'Swaraj'?", "options": ["British rule", "Self-rule", "Military rule", "Emergency rule"], "answer": "Self-rule"},
            {"question": "Which revolution is known as the first war of Indian Independence?", "options": ["1942 Quit India Movement", "1857 Revolt", "Non-Cooperation Movement", "Civil Disobedience Movement"], "answer": "1857 Revolt"},
            {"question": "What is the basic unit of resource classification?", "options": ["Utility", "Origin", "Ownership", "Distribution"], "answer": "Utility"},
            {"question": "Which type of resource is solar energy?", "options": ["Non-renewable", "Biotic", "Renewable", "Non-biotic"], "answer": "Renewable"},
            {"question": "Which one of these is a human-made resource?", "options": ["Water", "Minerals", "Buildings", "Forests"], "answer": "Buildings"},
            {"question": "What is a constitution?", "options": ["A story book", "A holy book", "A set of rules", "A type of law"], "answer": "A set of rules"},
            {"question": "Which level of government is responsible for local governance?", "options": ["State Government", "Central Government", "Local Government", "Judiciary"], "answer": "Local Government"},
            {"question": "Who led the tribal revolt in Chhotanagpur region?", "options": ["Birsa Munda", "Mangal Pandey", "Tantia Tope", "Bhagat Singh"], "answer": "Birsa Munda"},
            {"question": "What is the capital of Jharkhand?", "options": ["Patna", "Ranchi", "Jamshedpur", "Dhanbad"], "answer": "Ranchi"}
        ],
        "Medium": [
            {"question": "Which law passed in 2005 provides transparency in government work?", "options": ["PIL Act", "RTI Act", "Lokpal Act", "Income Tax Act"], "answer": "RTI Act"},
            {"question": "The Permanent Settlement was introduced in Bengal by:", "options": ["Lord Cornwallis", "Lord Canning", "Warren Hastings", "Lord Ripon"], "answer": "Lord Cornwallis"},
            {"question": "Which revolt took place in 1855 before the Revolt of 1857?", "options": ["Santhal Rebellion", "Sepoy Mutiny", "Chauri Chaura", "Salt Satyagraha"], "answer": "Santhal Rebellion"},
            {"question": "Which mineral is called 'liquid gold'?", "options": ["Water", "Crude Oil", "Petrol", "Diesel"], "answer": "Crude Oil"},
            {"question": "What is the importance of judiciary?", "options": ["Making laws", "Punishing politicians", "Resolving disputes", "Controlling media"], "answer": "Resolving disputes"},
            {"question": "What is meant by 'Equal Representation'?", "options": ["All get the same job", "All have equal rights", "All cast same vote", "All vote counts equally"], "answer": "All vote counts equally"},
            {"question": "Which Indian tribal group revolted against the British in 1831?", "options": ["Munda", "Santhal", "Khasi", "Kol"], "answer": "Kol"},
            {"question": "What are abiotic resources?", "options": ["Living resources", "Man-made resources", "Non-living resources", "Energy resources"], "answer": "Non-living resources"},
            {"question": "Which type of farming is practiced in small patches by tribal people?", "options": ["Commercial farming", "Shifting cultivation", "Plantation", "Subsistence farming"], "answer": "Shifting cultivation"},
            {"question": "What does ‘rule of law’ mean?", "options": ["Rules are optional", "Kings make laws", "Everyone is equal before the law", "Law changes daily"], "answer": "Everyone is equal before the law"}
        ],
        "Hard": [
            {"question": "Who wrote the book *Poverty and Un-British Rule in India*?", "options": ["Dadabhai Naoroji", "Bal Gangadhar Tilak", "Gopal Krishna Gokhale", "Surendranath Banerjee"], "answer": "Dadabhai Naoroji"},
            {"question": "What was the aim of the Ilbert Bill?", "options": ["To suppress Indian press", "To remove racial discrimination in judiciary", "To promote Indian education", "To increase land revenue"], "answer": "To remove racial discrimination in judiciary"},
            {"question": "Who was the founder of the Arya Samaj?", "options": ["Raja Ram Mohan Roy", "Swami Dayanand Saraswati", "Ishwar Chandra Vidyasagar", "Rabindranath Tagore"], "answer": "Swami Dayanand Saraswati"},
            {"question": "Which Act transferred power from the East India Company to the Crown?", "options": ["Charter Act of 1813", "Regulating Act", "Government of India Act 1858", "Pitt's India Act"], "answer": "Government of India Act 1858"},
            {"question": "What is the meaning of secularism in Indian Constitution?", "options": ["Favoring majority religion", "Ban on religious practices", "Equal respect for all religions", "No religion allowed"], "answer": "Equal respect for all religions"},
            {"question": "Which country inspired Indian Constitution’s parliamentary system?", "options": ["USA", "UK", "France", "Russia"], "answer": "UK"},
            {"question": "Which resource is both renewable and non-renewable depending on usage?", "options": ["Soil", "Water", "Forest", "Air"], "answer": "Water"},
            {"question": "Which movement aimed at improving lives of Indian farmers post-independence?", "options": ["Swadeshi Movement", "Green Revolution", "Quit India Movement", "Non-Cooperation Movement"], "answer": "Green Revolution"},
            {"question": "Which Indian leader gave the slogan 'Swaraj is my birthright'?", "options": ["Mahatma Gandhi", "Bal Gangadhar Tilak", "Subhash Chandra Bose", "Lala Lajpat Rai"], "answer": "Bal Gangadhar Tilak"},
            {"question": "Which fundamental right protects against untouchability?", "options": ["Right to Equality", "Right to Freedom", "Right to Education", "Right to Constitutional Remedies"], "answer": "Right to Equality"}
        ]
    },
    "Hindi": {
        "Easy": [
            {"question": "‘बस की यात्रा’ पाठ के लेखक कौन हैं?", "options": ["रामवृक्ष बेनीपुरी", "सुभद्राकुमारी चौहान", "सचिन तेंडुलकर", "महादेवी वर्मा"], "answer": "रामवृक्ष बेनीपुरी"},
            {"question": "‘लैपटॉप’ कविता में लैपटॉप को क्या कहा गया है?", "options": ["खिलौना", "दोस्त", "ज्ञान का भंडार", "बोझ"], "answer": "ज्ञान का भंडार"},
            {"question": "‘गठबंधन’ शब्द में कौन-सी संधि है?", "options": ["वर्ण संधि", "यण संधि", "दीर्घ संधि", "वृद्धि संधि"], "answer": "वृद्धि संधि"},
            {"question": "‘विकलांग’ शब्द का सही विलोम क्या है?", "options": ["दुर्बल", "समर्थ", "अशक्त", "कमजोर"], "answer": "समर्थ"},
            {"question": "‘न्यूटन की कहानी’ पाठ में न्यूटन किस वस्तु को गिरते देखकर सोच में पड़ जाते हैं?", "options": ["सेब", "पत्थर", "गेंद", "पत्ता"], "answer": "सेब"},
            {"question": "‘वृक्ष हमारे मित्र’ पाठ में किसका विशेष महत्व बताया गया है?", "options": ["पक्षियों का", "वृक्षों का", "पानी का", "पर्वतों का"], "answer": "वृक्षों का"},
            {"question": "‘हम पंछी उन्मुक्त गगन के’ कविता के कवि कौन हैं?", "options": ["हरिवंश राय बच्चन", "रामधारी सिंह दिनकर", "सुभद्राकुमारी चौहान", "मैथिलीशरण गुप्त"], "answer": "रामधारी सिंह दिनकर"},
            {"question": "‘विदेशी सामान का बहिष्कार करो’ किस आंदोलन का नारा था?", "options": ["स्वदेशी आंदोलन", "नमक सत्याग्रह", "असहयोग आंदोलन", "भारत छोड़ो आंदोलन"], "answer": "स्वदेशी आंदोलन"},
            {"question": "‘पढ़ाई का महत्व’ पाठ में किसके जीवन की चर्चा की गई है?", "options": ["बाल मजदूर", "अशिक्षित ग्रामीण", "विद्यार्थी", "किसान"], "answer": "बाल मजदूर"},
            {"question": "‘बिल्ली का बच्चा’ पाठ में बच्चा किसे अपनाता है?", "options": ["कुत्ते को", "बिल्ली को", "गिलहरी को", "चिड़िया को"], "answer": "बिल्ली को"}
        ],
        "Medium": [
            {"question": "‘धूल’ शब्द में कौन-सा समास है?", "options": ["तत्पुरुष", "बहुव्रीहि", "द्वंद्व", "अव्ययीभाव"], "answer": "तत्पुरुष"},
            {"question": "‘प्रकृति का अनुपम उपहार’ पाठ का मुख्य संदेश क्या है?", "options": ["पक्षी बचाओ", "जल बचाओ", "वृक्षों का संरक्षण", "प्रदूषण कम करो"], "answer": "वृक्षों का संरक्षण"},
            {"question": "‘हर की पौड़ी’ पाठ में लेखक किस नगर की यात्रा करते हैं?", "options": ["काशी", "हरिद्वार", "बद्रीनाथ", "ऋषिकेश"], "answer": "हरिद्वार"},
            {"question": "‘खाली स्थान भरो’: वह बहुत ____ लड़का है।", "options": ["तेजी", "तेज़", "तेज़ी", "तेज़ी से"], "answer": "तेज़"},
            {"question": "‘विद्युत’ शब्द का समानार्थी शब्द क्या है?", "options": ["चमक", "बिजली", "आग", "तेज"], "answer": "बिजली"},
            {"question": "‘कर्मवीर’ पाठ में किसके साहसिक कार्य का वर्णन है?", "options": ["एक डॉक्टर", "एक सैनिक", "एक पत्रकार", "एक शिक्षक"], "answer": "एक सैनिक"},
            {"question": "‘दृढ़ संकल्प’ का अर्थ क्या है?", "options": ["मजबूत सोच", "निर्णय में मजबूती", "नरमी", "दया"], "answer": "निर्णय में मजबूती"},
            {"question": "‘भोजन’ शब्द में कौन-सा प्रत्यय है?", "options": ["ण", "अन", "जन", "शन"], "answer": "अन"},
            {"question": "‘प्रदूषण’ से संबंधित कौन-सा वाक्य सही है?", "options": ["प्रदूषण से स्वास्थ्य लाभ होता है", "प्रदूषण से रोग फैलते हैं", "प्रदूषण जरूरी है", "प्रदूषण आनंददायक है"], "answer": "प्रदूषण से रोग फैलते हैं"},
            {"question": "‘उसने झटपट काम किया’ में ‘झटपट’ किस भेद का क्रिया विशेषण है?", "options": ["कारणवाचक", "रूपवाचक", "सामान्य", "रीति वाचक"], "answer": "रीति वाचक"}
        ],
        "Hard": [
            {"question": "‘सुख-दुख’ शब्द में कौन-सा समास है?", "options": ["द्वंद्व", "तत्पुरुष", "बहुव्रीहि", "द्विगु"], "answer": "द्वंद्व"},
            {"question": "‘कर्तृवाच्य वाक्य’ का उदाहरण क्या है?", "options": ["मैं पढ़ रहा हूँ।", "मुझसे पढ़ा गया।", "मुझसे किताब पढ़ी गई।", "किताब पढ़ी गई।"], "answer": "मैं पढ़ रहा हूँ।"},
            {"question": "‘रवि’ का तद्भव शब्द क्या है?", "options": ["रऊ", "रव", "रौ", "रवा"], "answer": "रऊ"},
            {"question": "‘प्रेरक’ का संधि विच्छेद क्या है?", "options": ["प्रे+रक", "प्र+रक", "प्रे+अरक", "प्र+इरक"], "answer": "प्रे+रक"},
            {"question": "‘सौंदर्य’ किस प्रकार का शब्द है?", "options": ["तत्सम", "तद्भव", "देशज", "विदेशज"], "answer": "तत्सम"},
            {"question": "‘रामायण’ शब्द में कौन-सी संधि है?", "options": ["दीर्घ संधि", "यण संधि", "वर्ण संधि", "गुण संधि"], "answer": "यण संधि"},
            {"question": "‘कवि’ शब्द में कौन-सा उपसर्ग है?", "options": ["वि", "क", "कवि", "None"], "answer": "None"},
            {"question": "‘असत्य’ में कौन-सा उपसर्ग है?", "options": ["अ", "सु", "सत्", "त्य"], "answer": "अ"},
            {"question": "‘निर्मल’ का सही संधि विच्छेद क्या है?", "options": ["नि + र्मल", "निर + मल", "नि + मल", "निर्म + अल"], "answer": "नि + मल"},
            {"question": "‘विनाश’ शब्द में कौन-सा प्रत्यय है?", "options": ["ना", "नाश", "इन", "आश"], "answer": "आश"}
        ]
    },
    "Sanskrit": {
        "Easy": [
            {"question": "‘सुभाषितानि’ पाठ में मुख्य विषय क्या है?", "options": ["नीति शिक्षण", "प्रकृति चित्रण", "युद्ध", "क्रीड़ा"], "answer": "नीति शिक्षण"},
            {"question": "‘शिष्टाचारः’ पाठ में क्या सिखाया गया है?", "options": ["क्रोध", "आलस्य", "विनम्रता", "दुर्व्यवहार"], "answer": "विनम्रता"},
            {"question": "‘परोपकाराय’ शब्द का अर्थ क्या है?", "options": ["अपने लिए", "दूसरों का अहित", "दूसरों की भलाई के लिए", "दंड देने के लिए"], "answer": "दूसरों की भलाई के लिए"},
            {"question": "‘मम नाम रामः अस्ति’ का अर्थ है?", "options": ["उसका नाम राम है", "मेरा नाम राम है", "मैं राम को बुलाता हूँ", "राम सो रहा है"], "answer": "मेरा नाम राम है"},
            {"question": "‘गच्छति’ किस लकार में है?", "options": ["लोट्", "लङ्", "लट्", "लृट्"], "answer": "लट्"},
            {"question": "‘विद्यालेयः’ का अर्थ है?", "options": ["घर", "बाजार", "विद्यालय", "कार्यालय"], "answer": "विद्यालय"},
            {"question": "‘पठति’ क्रिया का अर्थ है?", "options": ["खाता है", "सोता है", "पढ़ता है", "गाता है"], "answer": "पढ़ता है"},
            {"question": "‘रामः विद्यालयं गच्छति।’ वाक्य में कर्ता कौन है?", "options": ["विद्यालयं", "गच्छति", "रामः", "None"], "answer": "रामः"},
            {"question": "‘सुखं’ शब्द का सही अर्थ क्या है?", "options": ["दुख", "क्रोध", "आनंद", "अंधकार"], "answer": "आनंद"},
            {"question": "‘कविः’ शब्द किस लिंग में है?", "options": ["स्त्रीलिंग", "पुल्लिंग", "नपुंसकलिंग", "कोई नहीं"], "answer": "पुल्लिंग"}
        ],
        "Medium": [
            {"question": "‘फलानि’ शब्द किस वचन में है?", "options": ["एकवचन", "द्विवचन", "बहुवचन", "None"], "answer": "बहुवचन"},
            {"question": "‘रामेण’ का सही कारक है?", "options": ["कर्ता", "कर्म", "करण", "अपादान"], "answer": "करण"},
            {"question": "‘बालकाः पठन्ति।’ का काल क्या है?", "options": ["भविष्यत्", "वर्तमान", "भूतकाल", "आज्ञा"], "answer": "वर्तमान"},
            {"question": "‘माता गृहे अस्ति।’ वाक्य में 'गृहे' कौन-सा विभक्ति है?", "options": ["प्रथमा", "सप्तमी", "चतुर्थी", "षष्ठी"], "answer": "सप्तमी"},
            {"question": "‘गृह’ शब्द का बहुवचन क्या होगा?", "options": ["गृहे", "गृहाणि", "गृहाः", "गृहयोः"], "answer": "गृहाणि"},
            {"question": "‘क्रीडाम्’ शब्द में कौन-सा संधि है?", "options": ["यण संधि", "वर्ण संधि", "गुण संधि", "दीर्घ संधि"], "answer": "दीर्घ संधि"},
            {"question": "‘जननी’ शब्द का विलोम क्या है?", "options": ["पिता", "माता", "शत्रु", "None"], "answer": "पिता"},
            {"question": "‘सा पुस्तकं पठति’ वाक्य का सही अनुवाद क्या है?", "options": ["She writes a book", "She reads a book", "He reads a book", "She buys a book"], "answer": "She reads a book"},
            {"question": "‘गम्’ धातु का लट् लकार प्रथम पुरुष एकवचन रूप क्या है?", "options": ["गच्छति", "गच्छसि", "गच्छामि", "गच्छतः"], "answer": "गच्छति"},
            {"question": "‘त्वं कुत्र गच्छसि?’ वाक्य का अर्थ है?", "options": ["आप कौन हैं?", "तुम क्यों रोते हो?", "तुम कहाँ जा रहे हो?", "तुम क्या खा रहे हो?"], "answer": "तुम कहाँ जा रहे हो?"}
        ],
        "Hard": [
            {"question": "‘अहं विद्यालयं प्रति गच्छामि।’ में ‘प्रति’ क्या है?", "options": ["संज्ञा", "सर्वनाम", "क्रिया", "उपसर्ग/उपपद"], "answer": "उपसर्ग/उपपद"},
            {"question": "‘लट्’ लकार किस काल का द्योतक है?", "options": ["भविष्यत्", "वर्तमान", "भूतकाल", "आज्ञार्थ"], "answer": "वर्तमान"},
            {"question": "‘धावति’ किस धातु से बना है?", "options": ["स्था", "पठ", "धाव", "लिख"], "answer": "धाव"},
            {"question": "‘मम’ शब्द कौन-सी विभक्ति में है?", "options": ["प्रथमा", "षष्ठी", "तृतीया", "सप्तमी"], "answer": "षष्ठी"},
            {"question": "‘गजः वनं गच्छति।’ वाक्य में कर्म पद क्या है?", "options": ["गजः", "गच्छति", "वनं", "None"], "answer": "वनं"},
            {"question": "‘विद्यां ददाति विनयम्’ का क्या तात्पर्य है?", "options": ["विद्या केवल पुस्तक है", "विद्या से विनम्रता प्राप्त होती है", "विद्या युद्ध सिखाती है", "विद्या से सुख मिलता है"], "answer": "विद्या से विनम्रता प्राप्त होती है"},
            {"question": "‘सुपठति’ का सही विभक्ति और वचन क्या है?", "options": ["प्रथम पुरुष बहुवचन", "प्रथम पुरुष एकवचन", "मध्यम पुरुष बहुवचन", "उत्तम पुरुष एकवचन"], "answer": "प्रथम पुरुष एकवचन"},
            {"question": "‘नरः’ शब्द का षष्ठी विभक्ति एकवचन रूप क्या है?", "options": ["नरस्य", "नरेण", "नरम्", "नरे"], "answer": "नरस्य"},
            {"question": "‘ग्रामे’ किस विभक्ति का रूप है?", "options": ["षष्ठी", "सप्तमी", "पंचमी", "तृतीया"], "answer": "सप्तमी"},
            {"question": "‘सः किम् करोति?’ वाक्य का सही अनुवाद क्या है?", "options": ["What does he do?", "Where does he go?", "Who is he?", "What is your name?"], "answer": "What does he do?"}
        ]
    }
},
"9": {
    "Mathematics": {
        "Easy": [
            {"question": "What is the value of (−3) + 7?", "options": ["-10", "4", "10", "-4"], "answer": "4"},
            {"question": "What is the square of 5?", "options": ["10", "25", "15", "5"], "answer": "25"},
            {"question": "Which is the smallest prime number?", "options": ["1", "2", "3", "0"], "answer": "2"},
            {"question": "How many degrees are there in a right angle?", "options": ["45", "90", "180", "360"], "answer": "90"},
            {"question": "What is the cube of 2?", "options": ["4", "6", "8", "10"], "answer": "8"},
            {"question": "What is the HCF of 8 and 12?", "options": ["2", "4", "6", "8"], "answer": "4"},
            {"question": "What is the value of π (approximately)?", "options": ["2.14", "3.14", "4.14", "5.14"], "answer": "3.14"},
            {"question": "Which of the following is a rational number?", "options": ["√2", "π", "3/4", "√3"], "answer": "3/4"},
            {"question": "How many sides does a triangle have?", "options": ["2", "3", "4", "5"], "answer": "3"},
            {"question": "What is 10% of 200?", "options": ["10", "20", "30", "40"], "answer": "20"}
        ],
        "Medium": [
            {"question": "Which number is not a solution of the equation x² = 25?", "options": ["5", "-5", "0", "None"], "answer": "0"},
            {"question": "Which point lies on the y-axis?", "options": ["(0, 3)", "(3, 0)", "(3, 3)", "(1, 2)"], "answer": "(0, 3)"},
            {"question": "What is the factorization of x² - 9?", "options": ["(x - 3)(x + 3)", "(x - 9)(x + 1)", "(x + 9)(x - 1)", "None"], "answer": "(x - 3)(x + 3)"},
            {"question": "What is the sum of the angles of a quadrilateral?", "options": ["180°", "360°", "90°", "270°"], "answer": "360°"},
            {"question": "Which number is an irrational number?", "options": ["√2", "3/4", "1", "0"], "answer": "√2"},
            {"question": "If x + y = 10 and x - y = 2, what is x?", "options": ["4", "5", "6", "8"], "answer": "6"},
            {"question": "What is the area of a circle with radius 7 cm?", "options": ["154 cm²", "44 cm²", "49 cm²", "100 cm²"], "answer": "154 cm²"},
            {"question": "The coordinates of origin are:", "options": ["(1, 1)", "(1, 0)", "(0, 1)", "(0, 0)"], "answer": "(0, 0)"},
            {"question": "What is the surface area of a cube with side 4 cm?", "options": ["64 cm²", "96 cm²", "48 cm²", "32 cm²"], "answer": "96 cm²"},
            {"question": "Which polynomial has degree 2?", "options": ["x² + 3x + 2", "x³ + 1", "x + 1", "5"], "answer": "x² + 3x + 2"}
        ],
        "Hard": [
            {"question": "What is the value of x if 2x + 3 = 9?", "options": ["2", "3", "1", "6"], "answer": "3"},
            {"question": "Which of the following is a linear equation in two variables?", "options": ["x + y = 5", "x² + y = 5", "x³ = 8", "xy = 10"], "answer": "x + y = 5"},
            {"question": "If a/b = 2/3 and b/c = 4/5, then a:c = ?", "options": ["8:15", "2:5", "4:9", "6:5"], "answer": "8:15"},
            {"question": "The volume of a cube is 216 cm³. What is its side?", "options": ["5 cm", "6 cm", "7 cm", "8 cm"], "answer": "6 cm"},
            {"question": "What is the LCM of 12, 15 and 20?", "options": ["60", "120", "180", "240"], "answer": "60"},
            {"question": "What is the solution of 3x – 2 = 4?", "options": ["2", "3", "1", "0"], "answer": "2"},
            {"question": "In coordinate geometry, what is the distance between (0,0) and (3,4)?", "options": ["5", "6", "7", "4"], "answer": "5"},
            {"question": "Which of the following is a perfect square?", "options": ["49", "50", "51", "52"], "answer": "49"},
            {"question": "If the perimeter of a square is 36 cm, what is its area?", "options": ["81 cm²", "36 cm²", "100 cm²", "64 cm²"], "answer": "81 cm²"},
            {"question": "Which term is used for a polynomial with 3 terms?", "options": ["Monomial", "Binomial", "Trinomial", "Quadrinomial"], "answer": "Trinomial"}
        ]
    },
    "Science": {
        "Easy": [
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "NaCl"], "answer": "H2O"},
            {"question": "Which organ pumps blood in the human body?", "options": ["Lungs", "Brain", "Heart", "Liver"], "answer": "Heart"},
            {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Carbon dioxide"},
            {"question": "What is the boiling point of water?", "options": ["100°C", "0°C", "50°C", "212°C"], "answer": "100°C"},
            {"question": "What is the process by which plants make their food?", "options": ["Respiration", "Photosynthesis", "Digestion", "Transpiration"], "answer": "Photosynthesis"},
            {"question": "Which part of the plant conducts photosynthesis?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Leaf"},
            {"question": "What type of energy is stored in food?", "options": ["Kinetic energy", "Chemical energy", "Thermal energy", "Electrical energy"], "answer": "Chemical energy"},
            {"question": "What is the center of an atom called?", "options": ["Electron", "Proton", "Nucleus", "Neutron"], "answer": "Nucleus"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What type of simple machine is a seesaw?", "options": ["Lever", "Pulley", "Inclined plane", "Wheel and axle"], "answer": "Lever"}
        ],
        "Medium": [
            {"question": "Which gas is released during photosynthesis?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
            {"question": "What is the main function of the human respiratory system?", "options": ["Digestion", "Circulation", "Exchange of gases", "Excretion"], "answer": "Exchange of gases"},
            {"question": "Which of these is a non-renewable source of energy?", "options": ["Solar energy", "Wind energy", "Coal", "Hydro energy"], "answer": "Coal"},
            {"question": "What is the chemical formula of common salt?", "options": ["NaCl", "KCl", "NaOH", "HCl"], "answer": "NaCl"},
            {"question": "Which blood cells help in fighting infections?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "White blood cells"},
            {"question": "What is the unit of electric current?", "options": ["Volt", "Ohm", "Ampere", "Watt"], "answer": "Ampere"},
            {"question": "Which organ is responsible for filtering blood in humans?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": "Kidney"},
            {"question": "What type of reproduction involves a single parent?", "options": ["Sexual reproduction", "Asexual reproduction", "Fertilization", "Pollination"], "answer": "Asexual reproduction"},
            {"question": "Which instrument is used to measure atmospheric pressure?", "options": ["Thermometer", "Barometer", "Hygrometer", "Anemometer"], "answer": "Barometer"},
            {"question": "What is the SI unit of force?", "options": ["Newton", "Joule", "Watt", "Pascal"], "answer": "Newton"}
        ],
        "Hard": [
            {"question": "Which of these elements is a halogen?", "options": ["Oxygen", "Chlorine", "Nitrogen", "Hydrogen"], "answer": "Chlorine"},
            {"question": "What type of bond is formed by sharing electrons?", "options": ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"], "answer": "Covalent bond"},
            {"question": "What is the function of the xylem in plants?", "options": ["Transport water", "Transport food", "Photosynthesis", "Reproduction"], "answer": "Transport water"},
            {"question": "Which process converts sugar into alcohol?", "options": ["Fermentation", "Respiration", "Photosynthesis", "Combustion"], "answer": "Fermentation"},
            {"question": "What is the atomic number of Carbon?", "options": ["6", "12", "14", "8"], "answer": "6"},
            {"question": "Which part of the brain controls voluntary actions?", "options": ["Cerebrum", "Cerebellum", "Medulla", "Spinal cord"], "answer": "Cerebrum"},
            {"question": "What is the chemical formula of methane?", "options": ["CH4", "C2H6", "CO2", "C2H4"], "answer": "CH4"},
            {"question": "Which blood group is known as the universal donor?", "options": ["A", "B", "AB", "O"], "answer": "O"},
            {"question": "What is the role of enzymes in the body?", "options": ["Provide energy", "Speed up reactions", "Store information", "Build muscles"], "answer": "Speed up reactions"},
            {"question": "What is the pH of pure water?", "options": ["7", "0", "14", "1"], "answer": "7"}
        ]
    },
    "English": {
        "Easy": [
            {"question": "What is the synonym of 'happy'?", "options": ["Sad", "Joyful", "Angry", "Tired"], "answer": "Joyful"},
            {"question": "Choose the correct plural form of 'child'.", "options": ["Childs", "Children", "Childes", "Child"], "answer": "Children"},
            {"question": "Which of the following is a noun?", "options": ["Run", "Beautiful", "Happiness", "Quick"], "answer": "Happiness"},
            {"question": "Identify the verb in the sentence: 'She runs fast.'", "options": ["She", "Runs", "Fast", "None"], "answer": "Runs"},
            {"question": "Which is the correct sentence?", "options": ["He go to school.", "He goes to school.", "He going to school.", "He gone to school."], "answer": "He goes to school."},
            {"question": "What is the opposite of 'always'?", "options": ["Never", "Sometimes", "Often", "Usually"], "answer": "Never"},
            {"question": "Pick the correct article: ___ apple a day keeps the doctor away.", "options": ["A", "An", "The", "No article"], "answer": "An"},
            {"question": "Choose the correct preposition: She is sitting ___ the chair.", "options": ["on", "in", "at", "by"], "answer": "on"},
            {"question": "What is the past tense of 'go'?", "options": ["Goed", "Went", "Gone", "Going"], "answer": "Went"},
            {"question": "Identify the adjective in the sentence: 'The sky is blue.'", "options": ["Sky", "Is", "Blue", "The"], "answer": "Blue"}
        ],
        "Medium": [
            {"question": "Choose the correct form of the verb: 'They ___ playing football.'", "options": ["is", "are", "was", "be"], "answer": "are"},
            {"question": "What is the meaning of the idiom 'Break the ice'?", "options": ["To shatter ice", "To start a conversation", "To break something", "To feel cold"], "answer": "To start a conversation"},
            {"question": "Which sentence uses the passive voice?", "options": ["She wrote a letter.", "A letter was written by her.", "She writes letters.", "She is writing a letter."], "answer": "A letter was written by her."},
            {"question": "Choose the correct synonym for 'difficult'.", "options": ["Easy", "Hard", "Simple", "Soft"], "answer": "Hard"},
            {"question": "What is a metaphor?", "options": ["A comparison without using 'like' or 'as'", "A comparison using 'like' or 'as'", "A type of poem", "A kind of story"], "answer": "A comparison without using 'like' or 'as'"},
            {"question": "Identify the correct sentence:", "options": ["She don't like ice cream.", "She doesn't likes ice cream.", "She doesn't like ice cream.", "She don't likes ice cream."], "answer": "She doesn't like ice cream."},
            {"question": "Which is a compound sentence?", "options": ["I went home.", "I went home and cooked dinner.", "I went home but I was tired.", "I went home because I was tired."], "answer": "I went home but I was tired."},
            {"question": "Pick the correct indirect speech: She said, 'I am tired.'", "options": ["She said she was tired.", "She said she is tired.", "She said she tired.", "She said she am tired."], "answer": "She said she was tired."},
            {"question": "Choose the correct homophone: 'Their' means ___", "options": ["There", "Belonging to them", "They're", "Here"], "answer": "Belonging to them"},
            {"question": "What is the antonym of 'generous'?", "options": ["Kind", "Selfish", "Brave", "Honest"], "answer": "Selfish"}
        ],
        "Hard": [
            {"question": "Identify the figure of speech: 'The wind whispered through the trees.'", "options": ["Simile", "Personification", "Metaphor", "Alliteration"], "answer": "Personification"},
            {"question": "Choose the correct sentence with subjunctive mood:", "options": ["If I was you, I would study.", "If I were you, I would study.", "If I am you, I would study.", "If I be you, I would study."], "answer": "If I were you, I would study."},
            {"question": "What is the function of an adverb in a sentence?", "options": ["Describes a noun", "Describes a verb", "Connects clauses", "Shows possession"], "answer": "Describes a verb"},
            {"question": "Which is the correct passive form: 'They will complete the project tomorrow.'", "options": ["The project will complete by them.", "The project will be completed by them.", "The project is completed by them.", "The project was completed by them."], "answer": "The project will be completed by them."},
            {"question": "What is the mood used to express a command?", "options": ["Indicative", "Imperative", "Subjunctive", "Interrogative"], "answer": "Imperative"},
            {"question": "Identify the correct use of punctuation:", "options": ["She said 'Hello.'", "She said, 'Hello.'", "She said, Hello.", "She said 'Hello'."], "answer": "She said, 'Hello.'"},
            {"question": "What is the meaning of 'onomatopoeia'?", "options": ["A word that imitates sound", "A type of poem", "A metaphor", "A simile"], "answer": "A word that imitates sound"},
            {"question": "Choose the sentence with a complex sentence structure:", "options": ["I like coffee, but I prefer tea.", "Although it was raining, we went out.", "She runs fast and wins races.", "They went home early."], "answer": "Although it was raining, we went out."},
            {"question": "Identify the correct form of the verb in reported speech: He said, 'I have finished my homework.'", "options": ["He said he has finished his homework.", "He said he had finished his homework.", "He said he finished his homework.", "He said he will finish his homework."], "answer": "He said he had finished his homework."},
            {"question": "What is an oxymoron?", "options": ["Two contradictory words together", "An exaggeration", "A type of rhyme", "A short story"], "answer": "Two contradictory words together"}
        ]
    },
    "Social Science": {
        "Easy": [
            {"question": "Who was the first Governor-General of independent India?", "options": ["Lord Mountbatten", "C. Rajagopalachari", "Lord Wellesley", "Warren Hastings"], "answer": "Lord Mountbatten"},
            {"question": "Which river is called the 'Ganga of the South'?", "options": ["Godavari", "Krishna", "Cauvery", "Narmada"], "answer": "Godavari"},
            {"question": "What is the capital of Madhya Pradesh?", "options": ["Bhopal", "Indore", "Gwalior", "Jabalpur"], "answer": "Bhopal"},
            {"question": "Which is the lower house of the Indian Parliament?", "options": ["Lok Sabha", "Rajya Sabha", "Vidhan Sabha", "Gram Sabha"], "answer": "Lok Sabha"},
            {"question": "Who wrote the 'Discovery of India'?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhash Chandra Bose", "B.R. Ambedkar"], "answer": "Jawaharlal Nehru"},
            {"question": "Which type of soil is found in the Indo-Gangetic plains?", "options": ["Alluvial soil", "Black soil", "Red soil", "Laterite soil"], "answer": "Alluvial soil"},
            {"question": "What is the primary function of the Election Commission of India?", "options": ["Conduct elections", "Make laws", "Collect taxes", "Maintain law and order"], "answer": "Conduct elections"},
            {"question": "Which movement was started by Mahatma Gandhi in 1930?", "options": ["Quit India Movement", "Non-Cooperation Movement", "Salt Satyagraha", "Civil Disobedience Movement"], "answer": "Salt Satyagraha"},
            {"question": "Which mountain range is known as the 'Young Fold Mountains' in India?", "options": ["Himalayas", "Vindhyas", "Aravallis", "Satpuras"], "answer": "Himalayas"},
            {"question": "Who was the founder of the Indian National Congress?", "options": ["A.O. Hume", "Bal Gangadhar Tilak", "Bipin Chandra Pal", "Lala Lajpat Rai"], "answer": "A.O. Hume"}
        ],
        "Medium": [
            {"question": "The Revolt of 1857 started in which city?", "options": ["Meerut", "Delhi", "Lucknow", "Kanpur"], "answer": "Meerut"},
            {"question": "Which constitutional body is responsible for protecting Fundamental Rights?", "options": ["Supreme Court", "Election Commission", "Finance Commission", "Planning Commission"], "answer": "Supreme Court"},
            {"question": "Who was the first Prime Minister of independent India?", "options": ["Jawaharlal Nehru", "Sardar Patel", "Lal Bahadur Shastri", "Rajendra Prasad"], "answer": "Jawaharlal Nehru"},
            {"question": "What does 'Swaraj' mean?", "options": ["Self-rule", "Freedom from poverty", "Universal education", "Religious harmony"], "answer": "Self-rule"},
            {"question": "Which act introduced separate electorates for Muslims?", "options": ["Government of India Act 1909", "Government of India Act 1919", "Government of India Act 1935", "Indian Councils Act 1909"], "answer": "Government of India Act 1909"},
            {"question": "Which is the largest state in India by area?", "options": ["Rajasthan", "Madhya Pradesh", "Maharashtra", "Uttar Pradesh"], "answer": "Rajasthan"},
            {"question": "Who was the Viceroy of India during the Quit India Movement?", "options": ["Lord Linlithgow", "Lord Curzon", "Lord Mountbatten", "Lord Wavell"], "answer": "Lord Linlithgow"},
            {"question": "Which soil type is suitable for growing cotton?", "options": ["Black soil", "Alluvial soil", "Red soil", "Laterite soil"], "answer": "Black soil"},
            {"question": "What is the role of the Panchayat in rural India?", "options": ["Local self-government", "State government", "Central government", "Judicial system"], "answer": "Local self-government"},
            {"question": "Who was the leader of the Indian National Army (INA)?", "options": ["Subhash Chandra Bose", "Bhagat Singh", "Mahatma Gandhi", "Bal Gangadhar Tilak"], "answer": "Subhash Chandra Bose"}
        ],
        "Hard": [
            {"question": "Which session of the Indian National Congress declared 'Purna Swaraj'?", "options": ["Lahore Session 1929", "Calcutta Session 1905", "Bombay Session 1916", "Lucknow Session 1916"], "answer": "Lahore Session 1929"},
            {"question": "What was the main objective of the Rowlatt Act of 1919?", "options": ["To curb revolutionary activities", "To promote education", "To grant self-government", "To abolish salt tax"], "answer": "To curb revolutionary activities"},
            {"question": "Which amendment of the Indian Constitution added the Fundamental Duties?", "options": ["42nd Amendment", "44th Amendment", "52nd Amendment", "61st Amendment"], "answer": "42nd Amendment"},
            {"question": "Who was the President of the Constituent Assembly of India?", "options": ["Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel"], "answer": "Dr. Rajendra Prasad"},
            {"question": "The Champaran Satyagraha was related to which issue?", "options": ["Indigo plantation", "Salt tax", "Partition of Bengal", "Railway strike"], "answer": "Indigo plantation"},
            {"question": "Which river forms the traditional boundary between North and South India?", "options": ["Godavari", "Narmada", "Krishna", "Cauvery"], "answer": "Narmada"},
            {"question": "What was the Simon Commission?", "options": ["A British commission to study constitutional reforms", "An Indian political party", "A revolutionary group", "A British trade organization"], "answer": "A British commission to study constitutional reforms"},
            {"question": "Which constitutional body is responsible for the delimitation of constituencies?", "options": ["Delimitation Commission", "Election Commission", "Finance Commission", "Planning Commission"], "answer": "Delimitation Commission"},
            {"question": "Who authored the famous book 'India's Struggle for Independence'?", "options": ["Bipan Chandra", "Ramachandra Guha", "Jawaharlal Nehru", "M.K. Gandhi"], "answer": "Bipan Chandra"},
            {"question": "What is the significance of the Poona Pact of 1932?", "options": ["Agreement between Gandhi and Ambedkar on reserved seats", "Formation of the Indian National Army", "Launch of Quit India Movement", "Partition of Bengal"], "answer": "Agreement between Gandhi and Ambedkar on reserved seats"}
        ]
    },
    "Hindi": {
        "Easy": [
            {"question": "निम्नलिखित में से कौन सा शब्द संज्ञा है?", "options": ["चलना", "खेलना", "विद्यालय", "सुंदर"], "answer": "विद्यालय"},
            {"question": "‘राम ने कहा’ में ‘ने’ किस प्रकार का कारक है?", "options": ["कर्म कारक", "कर्तृ कारक", "सम्प्रदान कारक", "अपादान कारक"], "answer": "कर्तृ कारक"},
            {"question": "‘मैं बाजार जाता हूँ’ में क्रिया कौन सी है?", "options": ["मैं", "बाजार", "जाता", "हूँ"], "answer": "जाता"},
            {"question": "‘सुंदर’ शब्द किस वर्ग का है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "विशेषण"},
            {"question": "‘तुम क्या कर रहे हो?’ यह वाक्य किस प्रकार का है?", "options": ["विनयात्मक", "आज्ञात्मक", "प्रश्नवाचक", "विनम्र"], "answer": "प्रश्नवाचक"},
            {"question": "‘लड़का’ शब्द का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "दोवचन", "त्रिवचन"], "answer": "एकवचन"},
            {"question": "‘यह मेरा घर है’ में ‘मेरा’ किस प्रकार का शब्द है?", "options": ["सर्वनाम", "विशेषण", "क्रिया", "संज्ञा"], "answer": "सर्वनाम"},
            {"question": "‘चलो पढ़ाई करें’ में ‘चलो’ किस प्रकार का वचन है?", "options": ["वाच्य", "काल", "विधि", "उपदेशात्मक"], "answer": "उपदेशात्मक"},
            {"question": "‘गर्मी’ शब्द का पर्यायवाची क्या है?", "options": ["ताप", "शीतलता", "ठंड", "बरसात"], "answer": "ताप"},
            {"question": "‘सूरज’ शब्द किस वर्ग का है?", "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"], "answer": "संज्ञा"}
        ],
        "Medium": [
            {"question": "‘कर्म’ शब्द का वाक्य में क्या कार्य होता है?", "options": ["जो क्रिया करता है", "जिस पर क्रिया होती है", "क्रिया को दर्शाता है", "क्रिया के समय को दर्शाता है"], "answer": "जिस पर क्रिया होती है"},
            {"question": "निम्नलिखित में से कौन सा वचन बहुवचन नहीं है?", "options": ["लड़के", "लड़कियाँ", "लड़का", "बच्चे"], "answer": "लड़का"},
            {"question": "‘मैंने किताब पढ़ी’ में ‘मैंने’ किस कारक में है?", "options": ["कर्म कारक", "कर्तृ कारक", "सम्प्रदान कारक", "करण कारक"], "answer": "कर्तृ कारक"},
            {"question": "सही वाक्य चुनिए:", "options": ["मैंने खाना खाया", "मैं खाना खाया", "मुझे खाना खाया", "मैं खाना खाती हूँ"], "answer": "मैंने खाना खाया"},
            {"question": "निम्नलिखित में से कौन सा वाक्य संयोजन का उदाहरण है?", "options": ["राम गया और श्याम भी गया", "राम गया लेकिन श्याम नहीं गया", "राम गया", "शर्मा जी अच्छे हैं"], "answer": "राम गया और श्याम भी गया"},
            {"question": "‘सूर्य पूर्व से उगता है’ में ‘पूर्व’ किस प्रकार का शब्द है?", "options": ["संज्ञा", "विशेषण", "अव्यय", "सर्वनाम"], "answer": "अव्यय"},
            {"question": "‘हम खेल रहे हैं’ में ‘खेल’ कौन सा शब्द है?", "options": ["संज्ञा", "क्रिया", "विशेषण", "सर्वनाम"], "answer": "क्रिया"},
            {"question": "‘राजा’ शब्द का वचन क्या है?", "options": ["एकवचन", "बहुवचन", "दोवचन", "त्रिवचन"], "answer": "एकवचन"},
            {"question": "‘उसने मुझे उपहार दिया’ में ‘मुझे’ किस कारक में है?", "options": ["कर्म कारक", "कर्तृ कारक", "सम्प्रदान कारक", "करण कारक"], "answer": "सम्प्रदान कारक"},
            {"question": "‘तुम्हारा नाम क्या है?’ यह वाक्य किस प्रकार का है?", "options": ["विनयात्मक", "आज्ञात्मक", "प्रश्नवाचक", "विनम्र"], "answer": "प्रश्नवाचक"}
        ],
        "Hard": [
            {"question": "सही युग्म चुनिए: ‘ख़ुशी’ का विपरीत है?", "options": ["दुख", "शांति", "संतोष", "प्रसन्नता"], "answer": "दुख"},
            {"question": "‘संधि’ किसे कहते हैं?", "options": ["दो शब्दों का मेल", "वाक्य में क्रिया", "वर्णों का मिलन", "विशेषण का प्रयोग"], "answer": "वर्णों का मिलन"},
            {"question": "‘सर्वनाम’ के कितने प्रकार होते हैं?", "options": ["पाँच", "चार", "तीन", "दो"], "answer": "पाँच"},
            {"question": "‘क्रिया’ के काल कौन-कौन से होते हैं?", "options": ["वर्तमान, भूत, भविष्य", "वर्तमान, भूत", "भूत, भविष्य", "वर्तमान, भविष्य"], "answer": "वर्तमान, भूत, भविष्य"},
            {"question": "‘कर्मकारक’ क्या दर्शाता है?", "options": ["जिस पर क्रिया होती है", "जो क्रिया करता है", "जिसके द्वारा क्रिया होती है", "क्रिया का समय"], "answer": "जिस पर क्रिया होती है"},
            {"question": "‘अव्यय’ का क्या अर्थ है?", "options": ["जो न बदलता हो", "जो बदलता रहता हो", "क्रिया करने वाला", "विशेषण"], "answer": "जो न बदलता हो"},
            {"question": "‘तत्पुरुष’ संधि किस प्रकार की संधि है?", "options": ["समास", "संधि", "विसर्ग", "विभक्ति"], "answer": "समास"},
            {"question": "‘मुक्तक’ क्या है?", "options": ["एकल पद्यांश", "लंबा पद्य", "दोहे का दूसरा भाग", "काव्य"], "answer": "एकल पद्यांश"},
            {"question": "‘अलंकार’ के कितने प्रकार होते हैं?", "options": ["दो", "चार", "तीन", "एक"], "answer": "दो"},
            {"question": "‘भावार्थ’ का क्या अर्थ है?", "options": ["कविता का अर्थ", "कविता का शीर्षक", "कविता का लेखक", "कविता की भाषा"], "answer": "कविता का अर्थ"}
        ]
    },
  "Sanskrit": {
    "Easy": [
      {
        "question": "सप्तमि विभक्तिः का प्रयोग किस लिए होता है?",
        "options": ["कर्तृ", "कर्म", "संबोधन", "सम्बन्ध"],
        "answer": "सम्बन्ध"
      },
      {
        "question": "शब्द 'गच्छति' का सही अर्थ क्या है?",
        "options": ["खाता है", "चलता है", "सोता है", "देखता है"],
        "answer": "चलता है"
      },
      {
        "question": "‘रामः’ किस लिंग का शब्द है?",
        "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "बहुवचन"],
        "answer": "पुल्लिंग"
      },
      {
        "question": "वचन का अर्थ क्या है?",
        "options": ["काल", "संख्या", "विभक्ति", "लिंग"],
        "answer": "संख्या"
      },
      {
        "question": "सर्वनाम किसे कहते हैं?",
        "options": ["संज्ञा", "विशेषण", "सर्वनाम", "क्रिया"],
        "answer": "सर्वनाम"
      },
      {
        "question": "शब्द 'सुंदरः' किस प्रकार का शब्द है?",
        "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"],
        "answer": "विशेषण"
      },
      {
        "question": "कर्म विभक्ति किसे कहते हैं?",
        "options": ["कर्तृ", "कर्म", "सम्बन्ध", "अपादान"],
        "answer": "कर्म"
      },
      {
        "question": "‘अहं’ कौन सा सर्वनाम है?",
        "options": ["पुरुषवाचक", "संबंधवाचक", "प्रश्नवाचक", "निषेधवाचक"],
        "answer": "पुरुषवाचक"
      },
      {
        "question": "शब्द 'फलम्' किस प्रकार का शब्द है?",
        "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"],
        "answer": "संज्ञा"
      },
      {
        "question": "क्रिया किसे कहते हैं?",
        "options": ["कार्य", "कर्त्ता", "संज्ञा", "वचन"],
        "answer": "कार्य"
      }
    ],
    "Medium": [
      {
        "question": "अनेक शब्दों का बहुवचन रूप क्या है?",
        "options": ["एकवचन", "द्विवचन", "बहुवचन", "समस्तवचन"],
        "answer": "बहुवचन"
      },
      {
        "question": "‘रामस्य’ में कौन सी विभक्ति है?",
        "options": ["प्रथमा", "द्वितीया", "षष्ठी", "सप्तमी"],
        "answer": "षष्ठी"
      },
      {
        "question": "‘तस्मै’ कौन सी विभक्ति है?",
        "options": ["प्रथमा", "द्वितीया", "तृतीया", "षष्ठी"],
        "answer": "तृतीया"
      },
      {
        "question": "शब्द ‘गृहं’ का समास क्या होगा?",
        "options": ["द्वन्द्व", "तत्पुरुष", "कर्मधारय", "बहुव्रीहि"],
        "answer": "तत्पुरुष"
      },
      {
        "question": "‘कृष्णः’ किस लिंग का शब्द है?",
        "options": ["पुल्लिंग", "स्त्रीलिंग", "नपुंसकलिंग", "बहुवचन"],
        "answer": "पुल्लिंग"
      },
      {
        "question": "शब्द 'सुनः' का अर्थ क्या है?",
        "options": ["पुत्र", "पिता", "भाई", "मित्र"],
        "answer": "पुत्र"
      },
      {
        "question": "संख्या के तीन रूप क्या हैं?",
        "options": ["एकवचन, द्विवचन, बहुवचन", "पुरुष, लिंग, वचन", "कर्त्ता, कर्म, अपादान", "काल, लिंग, वचन"],
        "answer": "एकवचन, द्विवचन, बहुवचन"
      },
      {
        "question": "‘शुभं कार्यं करोति’ में ‘शुभं’ क्या है?",
        "options": ["संज्ञा", "विशेषण", "क्रिया", "सर्वनाम"],
        "answer": "विशेषण"
      },
      {
        "question": "‘रामेण’ कौन सी विभक्ति है?",
        "options": ["तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी"],
        "answer": "तृतीया"
      },
      {
        "question": "‘गजः’ का बहुवचन रूप क्या होगा?",
        "options": ["गजाः", "गजसः", "गजनः", "गजाः"],
        "answer": "गजाः"
      }
    ],
    "Hard": [
      {
        "question": "‘कर्मधारय समास’ का अर्थ क्या होता है?",
        "options": ["एक जैसा कार्य करने वाले शब्द", "दो शब्दों का यौगिक जो एक-दूसरे के अर्थ को स्पष्ट करता है", "एक शब्द जो संपूर्ण वाक्य का अर्थ देता है", "दो शब्द जो विलोम अर्थ रखते हैं"],
        "answer": "दो शब्दों का यौगिक जो एक-दूसरे के अर्थ को स्पष्ट करता है"
      },
      {
        "question": "‘भवत्’ किस पुरुष का सर्वनाम है?",
        "options": ["प्रथम पुरुष", "मध्यम पुरुष", "उत्तम पुरुष", "तृतीय पुरुष"],
        "answer": "उत्तम पुरुष"
      },
      {
        "question": "‘शब्दरूप’ का क्या अर्थ है?",
        "options": ["शब्द का भेद", "शब्द का रूप", "शब्द की संख्या", "शब्द की क्रिया"],
        "answer": "शब्द का रूप"
      },
      {
        "question": "‘वचन’ के अंतर्गत कौन-कौन से रूप आते हैं?",
        "options": ["एकवचन, द्विवचन, बहुवचन", "पुरुष, लिंग, वचन", "कर्त्ता, कर्म, अपादान", "काल, लिंग, वचन"],
        "answer": "एकवचन, द्विवचन, बहुवचन"
      },
      {
        "question": "‘तत्पुरुष समास’ किस प्रकार का समास है?",
        "options": ["अव्ययीभाव", "बहुव्रीहि", "कर्मधारय", "अनेकार्थी"],
        "answer": "कर्मधारय"
      },
      {
        "question": "‘संधि’ का क्या अर्थ है?",
        "options": ["शब्दों का मेल", "शब्दों का भेद", "वचन का रूप", "लिंग का रूप"],
        "answer": "शब्दों का मेल"
      },
      {
        "question": "‘शुद्धि’ किस प्रक्रिया को कहते हैं?",
        "options": ["शब्द सुधारना", "वाक्य निर्माण", "अक्षर जोड़ना", "वचन बदलना"],
        "answer": "शब्द सुधारना"
      },
      {
        "question": "‘विभक्ति’ किसे कहते हैं?",
        "options": ["शब्द के रूप", "शब्द के भेद", "शब्द की संख्या", "शब्द की क्रिया"],
        "answer": "शब्द के रूप"
      },
      {
        "question": "‘काल’ किसे कहते हैं?",
        "options": ["शब्द के समय", "शब्द के भेद", "शब्द की संख्या", "शब्द की क्रिया"],
        "answer": "शब्द के समय"
      },
      {
        "question": "‘अव्यय’ किसे कहते हैं?",
        "options": ["जिसका रूप नहीं बदलता", "जो लिंग में बदलता है", "जो वचन में बदलता है", "जो विभक्ति में बदलता है"],
        "answer": "जिसका रूप नहीं बदलता"
      }
    ]
  }
},
  "10": {
    "Mathematics": {
      "Easy": [
        {
          "question": "What is the value of 7 + 8?",
          "options": ["14", "15", "16", "17"],
          "answer": "15"
        },
        {
          "question": "What is the square of 6?",
          "options": ["36", "42", "12", "18"],
          "answer": "36"
        },
        {
          "question": "If the length of a rectangle is 8 cm and breadth is 3 cm, what is its area?",
          "options": ["11 cm²", "24 cm²", "18 cm²", "30 cm²"],
          "answer": "24 cm²"
        },
        {
          "question": "The perimeter of a square with side 5 cm is?",
          "options": ["10 cm", "20 cm", "15 cm", "25 cm"],
          "answer": "20 cm"
        },
        {
          "question": "Solve for x: x + 4 = 9",
          "options": ["5", "6", "4", "3"],
          "answer": "5"
        },
        {
          "question": "What is the value of 12 × 12?",
          "options": ["144", "124", "134", "154"],
          "answer": "144"
        },
        {
          "question": "How many sides does a pentagon have?",
          "options": ["5", "6", "4", "3"],
          "answer": "5"
        },
        {
          "question": "What is the value of 10% of 50?",
          "options": ["5", "10", "15", "20"],
          "answer": "5"
        },
        {
          "question": "Which number is a prime number?",
          "options": ["9", "11", "15", "21"],
          "answer": "11"
        },
        {
          "question": "What is the cube of 3?",
          "options": ["6", "9", "27", "18"],
          "answer": "27"
        }
      ],
      "Medium": [
        {
          "question": "If the roots of the equation x² - 5x + 6 = 0 are α and β, what is α + β?",
          "options": ["5", "6", "1", "11"],
          "answer": "5"
        },
        {
          "question": "Find the length of the diagonal of a square whose side is 7 cm.",
          "options": ["7√2 cm", "14 cm", "7 cm", "49 cm"],
          "answer": "7√2 cm"
        },
        {
          "question": "If the HCF of 36 and 60 is 12, what is their LCM?",
          "options": ["180", "240", "360", "720"],
          "answer": "180"
        },
        {
          "question": "The sum of two numbers is 30 and their difference is 4. What are the numbers?",
          "options": ["17 and 13", "18 and 12", "16 and 14", "20 and 10"],
          "answer": "17 and 13"
        },
        {
          "question": "What is the distance between points (3, 4) and (7, 1)?",
          "options": ["5", "6", "7", "8"],
          "answer": "5"
        },
        {
          "question": "The surface area of a sphere is 154 cm². Find its radius. (Use π = 3.14)",
          "options": ["7 cm", "14 cm", "11 cm", "10 cm"],
          "answer": "7 cm"
        },
        {
          "question": "If the circumference of a circle is 44 cm, what is its radius? (Use π = 22/7)",
          "options": ["7 cm", "14 cm", "11 cm", "22 cm"],
          "answer": "7 cm"
        },
        {
          "question": "What is the sum of the interior angles of a hexagon?",
          "options": ["720°", "540°", "360°", "900°"],
          "answer": "720°"
        },
        {
          "question": "Find the quadratic equation whose roots are 3 and -4.",
          "options": ["x² + x - 12 = 0", "x² - x + 12 = 0", "x² - 7x + 12 = 0", "x² + 7x - 12 = 0"],
          "answer": "x² + x - 12 = 0"
        },
        {
          "question": "The ratio of the areas of two squares is 16:25. What is the ratio of their sides?",
          "options": ["4:5", "16:25", "8:10", "2:3"],
          "answer": "4:5"
        }
      ],
      "Hard": [
        {
          "question": "Find the roots of the quadratic equation 2x² - 7x + 3 = 0.",
          "options": ["3/2 and 1", "1/2 and 3", "3 and 2", "2 and 3"],
          "answer": "3/2 and 1"
        },
        {
          "question": "The volume of a cylinder is 462 cm³. If its height is 7 cm and π = 3.14, find the radius of its base.",
          "options": ["6 cm", "7 cm", "5 cm", "8 cm"],
          "answer": "6 cm"
        },
        {
          "question": "The sum of the first 10 natural numbers is:",
          "options": ["55", "45", "60", "50"],
          "answer": "55"
        },
        {
          "question": "Find the coordinates of the midpoint of the line segment joining points (2, 3) and (4, 7).",
          "options": ["(3, 5)", "(2, 7)", "(4, 3)", "(3, 7)"],
          "answer": "(3, 5)"
        },
        {
          "question": "If sin A = 3/5, find cos A.",
          "options": ["4/5", "5/3", "3/4", "1/2"],
          "answer": "4/5"
        },
        {
          "question": "What is the area of an equilateral triangle with side 6 cm?",
          "options": ["9√3 cm²", "12√3 cm²", "18√3 cm²", "6√3 cm²"],
          "answer": "9√3 cm²"
        },
        {
          "question": "If a and b are positive numbers such that a² + b² = 25 and ab = 12, find (a + b)².",
          "options": ["49", "37", "25", "61"],
          "answer": "49"
        },
        {
          "question": "The sum of the cubes of two numbers is 35 and the sum of the numbers is 4. Find the product of the numbers.",
          "options": ["5", "6", "7", "8"],
          "answer": "5"
        },
        {
          "question": "The length of the diagonal of a rectangle is 10 cm and one side is 6 cm. Find the other side.",
          "options": ["8 cm", "7 cm", "6 cm", "5 cm"],
          "answer": "8 cm"
        },
        {
          "question": "A tangent is drawn at point P to the circle with center O. The angle between the radius OP and tangent at P is:",
          "options": ["90°", "45°", "60°", "30°"],
          "answer": "90°"
        }
      ]
    },
  "English": {
    "Easy": [
      {
        "question": "Who is the author of the story 'A Letter to God'?",
        "options": ["G.L. Fuentes", "Leo Tolstoy", "R.K. Narayan", "Ruskin Bond"],
        "answer": "G.L. Fuentes"
      },
      {
        "question": "What was Lencho’s profession in 'A Letter to God'?",
        "options": ["Teacher", "Postmaster", "Farmer", "Tailor"],
        "answer": "Farmer"
      },
      {
        "question": "Who wrote the poem 'Dust of Snow'?",
        "options": ["Robert Frost", "William Wordsworth", "Emily Dickinson", "John Keats"],
        "answer": "Robert Frost"
      },
      {
        "question": "What did the crow do in 'Dust of Snow'?",
        "options": ["Cawed loudly", "Flew away", "Shook down snow", "Pecked a branch"],
        "answer": "Shook down snow"
      },
      {
        "question": "Who was the little boy in 'The Midnight Visitor'?",
        "options": ["Fowler", "Ausable", "Max", "Horace Danby"],
        "answer": "Fowler"
      },
      {
        "question": "What kind of poem is 'Fire and Ice'?",
        "options": ["Narrative", "Descriptive", "Lyric", "Dramatic"],
        "answer": "Lyric"
      },
      {
        "question": "What does 'fire' symbolise in the poem 'Fire and Ice'?",
        "options": ["Love", "Hate", "Desire", "Coldness"],
        "answer": "Desire"
      },
      {
        "question": "Where did the thief hide in 'A Triumph of Surgery'?",
        "options": ["Under a bed", "In a box", "In a cupboard", "Behind a curtain"],
        "answer": "In a cupboard"
      },
      {
        "question": "What is the name of the dog in 'A Triumph of Surgery'?",
        "options": ["Tricky", "Ricky", "Tommy", "Johnny"],
        "answer": "Tricky"
      },
      {
        "question": "Who is the speaker in the poem 'Amanda!'?",
        "options": ["Amanda", "Mother", "Father", "Teacher"],
        "answer": "Mother"
      }
    ],
    "Medium": [
      {
        "question": "In 'The Ball Poem', what does the ball symbolize?",
        "options": ["Wealth", "Childhood", "Loss", "Love"],
        "answer": "Loss"
      },
      {
        "question": "What was the actual identity of the thief in 'Footprints without Feet'?",
        "options": ["Teacher", "Scientist", "Doctor", "Artist"],
        "answer": "Scientist"
      },
      {
        "question": "What is the main theme of 'Nelson Mandela: Long Walk to Freedom'?",
        "options": ["Revenge", "Slavery", "Freedom and Equality", "Colonialism"],
        "answer": "Freedom and Equality"
      },
      {
        "question": "Why was the thief boy caught in 'The Thief’s Story'?",
        "options": ["He was careless", "Hari Singh returned the money", "Police caught him", "He confessed"],
        "answer": "Hari Singh returned the money"
      },
      {
        "question": "What kind of poem is 'Animals' by Walt Whitman?",
        "options": ["Didactic", "Romantic", "Patriotic", "Autobiographical"],
        "answer": "Didactic"
      },
      {
        "question": "In 'From the Diary of Anne Frank', why did Anne start writing a diary?",
        "options": ["She loved writing", "She was forced", "She had no friend to share with", "Her father asked her"],
        "answer": "She had no friend to share with"
      },
      {
        "question": "What is the poetic device used in 'Dust of Snow'?",
        "options": ["Simile", "Metaphor", "Alliteration", "Hyperbole"],
        "answer": "Alliteration"
      },
      {
        "question": "In 'The Hundred Dresses-I', why did Wanda leave school?",
        "options": ["She was bullied", "She moved to another city", "She was sick", "She failed"],
        "answer": "She was bullied"
      },
      {
        "question": "What does Amanda wish to be in the poem?",
        "options": ["Fairy", "Mermaid", "Princess", "Bird"],
        "answer": "Mermaid"
      },
      {
        "question": "What does the tiger do in the poem 'A Tiger in the Zoo'?",
        "options": ["Roams freely", "Sits in his cage", "Chases deer", "Sleeps peacefully"],
        "answer": "Sits in his cage"
      }
    ],
    "Hard": [
      {
        "question": "What is the significance of the title 'The Necklace'?",
        "options": ["About a real necklace", "About borrowed necklace", "Symbol of pride and loss", "Gifted necklace"],
        "answer": "Symbol of pride and loss"
      },
      {
        "question": "What did Bholi suffer from in her childhood?",
        "options": ["Polio", "Measles", "Speech defect", "Blindness"],
        "answer": "Speech defect"
      },
      {
        "question": "Why did the doctor lie to Tricki’s owner in 'A Triumph of Surgery'?",
        "options": ["To save Tricki", "To make her happy", "To charge money", "To teach her a lesson"],
        "answer": "To teach her a lesson"
      },
      {
        "question": "What is the poetic device used in the line: ‘He stalks in his vivid stripes’?",
        "options": ["Metaphor", "Alliteration", "Personification", "Simile"],
        "answer": "Alliteration"
      },
      {
        "question": "In 'The Hack Driver', who was the hack driver actually?",
        "options": ["A lawyer", "A real hack driver", "Oliver Lutkins", "A policeman"],
        "answer": "Oliver Lutkins"
      },
      {
        "question": "What lesson does 'The Proposal' teach us?",
        "options": ["Marriage is important", "Dowry is bad", "Quarrels are silly", "Respect elders"],
        "answer": "Quarrels are silly"
      },
      {
        "question": "What did Anne Frank want to become?",
        "options": ["Doctor", "Artist", "Journalist", "Singer"],
        "answer": "Journalist"
      },
      {
        "question": "Why does the poet admire animals in 'Animals'?",
        "options": ["They are rich", "They don’t complain", "They have leaders", "They are clever"],
        "answer": "They don’t complain"
      },
      {
        "question": "What is the meaning of ‘desolate’ in ‘The Ball Poem’?",
        "options": ["Lonely", "Happy", "Shiny", "Excited"],
        "answer": "Lonely"
      },
      {
        "question": "Why was Matilda unhappy with her life in 'The Necklace'?",
        "options": ["She was poor", "She was ill", "She had no jewellery", "She wanted a better status"],
        "answer": "She wanted a better status"
      }
    ]
  },
  "Science": {
    "Easy": [
      {"question": "Which metal is liquid at room temperature?", "options": ["Iron", "Mercury", "Zinc", "Copper"], "answer": "Mercury"},
      {"question": "Which gas do plants use for photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Carbon dioxide"},
      {"question": "What is the color of a neutral litmus paper in acid?", "options": ["Blue", "Red", "Green", "Colorless"], "answer": "Red"},
      {"question": "Which organ pumps blood in the human body?", "options": ["Lungs", "Kidney", "Heart", "Liver"], "answer": "Heart"},
      {"question": "Which of the following is an acid?", "options": ["NaOH", "KOH", "HCl", "Ca(OH)₂"], "answer": "HCl"},
      {"question": "Which part of the eye controls the size of the pupil?", "options": ["Cornea", "Iris", "Retina", "Lens"], "answer": "Iris"},
      {"question": "What is the main function of roots in plants?", "options": ["Photosynthesis", "Absorption of water", "Respiration", "Reproduction"], "answer": "Absorption of water"},
      {"question": "Which gas is evolved during photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Methane"], "answer": "Oxygen"},
      {"question": "Which of the following is a conductor of electricity?", "options": ["Rubber", "Glass", "Plastic", "Copper"], "answer": "Copper"},
      {"question": "Which acid is present in lemon?", "options": ["Acetic acid", "Citric acid", "Hydrochloric acid", "Formic acid"], "answer": "Citric acid"}
    ],
    "Medium": [
      {"question": "Which of the following is a non-metal and remains liquid at room temperature?", "options": ["Sulphur", "Bromine", "Iodine", "Chlorine"], "answer": "Bromine"},
      {"question": "Which of the following has both acidic and basic properties?", "options": ["NaOH", "HCl", "H₂O", "ZnO"], "answer": "ZnO"},
      {"question": "Which component of blood helps in clotting?", "options": ["RBC", "WBC", "Platelets", "Plasma"], "answer": "Platelets"},
      {"question": "Which hormone regulates sugar in the blood?", "options": ["Insulin", "Thyroxine", "Adrenaline", "Estrogen"], "answer": "Insulin"},
      {"question": "Which part of the nephron is responsible for filtration?", "options": ["Tubule", "Bowman's capsule", "Collecting duct", "Ureter"], "answer": "Bowman's capsule"},
      {"question": "Which law states that energy is neither created nor destroyed?", "options": ["Ohm's Law", "Law of Inertia", "Law of Conservation of Energy", "Newton's Third Law"], "answer": "Law of Conservation of Energy"},
      {"question": "Which of the following has the highest refractive index?", "options": ["Air", "Water", "Glass", "Diamond"], "answer": "Diamond"},
      {"question": "Which reaction is used in the extraction of metals from their ores?", "options": ["Displacement", "Decomposition", "Redox", "Combustion"], "answer": "Redox"},
      {"question": "What is the SI unit of electric current?", "options": ["Volt", "Ohm", "Ampere", "Watt"], "answer": "Ampere"},
      {"question": "Which blood vessels carry blood away from the heart?", "options": ["Veins", "Arteries", "Capillaries", "Lymph vessels"], "answer": "Arteries"}
    ],
    "Hard": [
      {"question": "Which gas is evolved when zinc reacts with hydrochloric acid?", "options": ["Oxygen", "Nitrogen", "Hydrogen", "Chlorine"], "answer": "Hydrogen"},
      {"question": "Which part of the brain controls voluntary actions?", "options": ["Medulla", "Cerebellum", "Cerebrum", "Spinal Cord"], "answer": "Cerebrum"},
      {"question": "Which equation represents the process of photosynthesis?", "options": ["CO₂ + O₂ → C₆H₁₂O₆", "CO₂ + H₂O → C₆H₁₂O₆ + O₂", "H₂O + O₂ → CO₂", "C₆H₁₂O₆ + O₂ → CO₂ + H₂O"], "answer": "CO₂ + H₂O → C₆H₁₂O₆ + O₂"},
      {"question": "Which lens is used to correct myopia?", "options": ["Convex", "Concave", "Cylindrical", "Bifocal"], "answer": "Concave"},
      {"question": "Which physical quantity is the rate of change of velocity?", "options": ["Speed", "Displacement", "Acceleration", "Momentum"], "answer": "Acceleration"},
      {"question": "Which part of a plant is modified into a tuber in potato?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Stem"},
      {"question": "Which of the following shows both acidic and basic behavior (amphoteric)?", "options": ["CO₂", "NaCl", "Al₂O₃", "HCl"], "answer": "Al₂O₃"},
      {"question": "Which vitamin is produced in the human body in presence of sunlight?", "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
      {"question": "Which of the following is an example of a double displacement reaction?", "options": ["AgNO₃ + NaCl → AgCl + NaNO₃", "Zn + HCl → ZnCl₂ + H₂", "C + O₂ → CO₂", "CH₄ + O₂ → CO₂ + H₂O"], "answer": "AgNO₃ + NaCl → AgCl + NaNO₃"},
      {"question": "Which process is responsible for the formation of clouds?", "options": ["Condensation", "Evaporation", "Sublimation", "Precipitation"], "answer": "Condensation"}
    ]
  },
  "Social Science": {
    "Easy": [
      {"question": "Who was the founder of the 'Young Italy' movement?", "options": ["Giuseppe Garibaldi", "Giuseppe Mazzini", "Otto von Bismarck", "Victor Emmanuel"], "answer": "Giuseppe Mazzini"},
      {"question": "Which crop is a kharif crop?", "options": ["Wheat", "Barley", "Rice", "Mustard"], "answer": "Rice"},
      {"question": "In which year did the Jallianwala Bagh massacre take place?", "options": ["1915", "1919", "1921", "1930"], "answer": "1919"},
      {"question": "What is the capital of Sri Lanka?", "options": ["Colombo", "Dhaka", "Kathmandu", "Thimphu"], "answer": "Colombo"},
      {"question": "Which body conducts elections in India?", "options": ["Supreme Court", "Parliament", "Election Commission", "President"], "answer": "Election Commission"},
      {"question": "Which mineral is called 'liquid gold'?", "options": ["Petroleum", "Coal", "Iron", "Bauxite"], "answer": "Petroleum"},
      {"question": "Which river is the longest in India?", "options": ["Yamuna", "Ganga", "Godavari", "Brahmaputra"], "answer": "Ganga"},
      {"question": "Who wrote 'Hind Swaraj'?", "options": ["Jawaharlal Nehru", "B.R. Ambedkar", "Subhas Chandra Bose", "Mahatma Gandhi"], "answer": "Mahatma Gandhi"},
      {"question": "What is the full form of GDP?", "options": ["Gross Domestic Product", "General Development Plan", "Global Demand Policy", "Gross Development Project"], "answer": "Gross Domestic Product"},
      {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"}
    ],
    "Medium": [
      {"question": "Which Act allowed the British to imprison any person without trial?", "options": ["Rowlatt Act", "Salt Act", "Pitt’s India Act", "Ilbert Bill"], "answer": "Rowlatt Act"},
      {"question": "Which of these is a feature of federalism?", "options": ["Single government", "Power-sharing between central and state", "Only central power", "One-party rule"], "answer": "Power-sharing between central and state"},
      {"question": "Black soil is ideal for growing which crop?", "options": ["Rice", "Wheat", "Cotton", "Pulses"], "answer": "Cotton"},
      {"question": "Which country is known for the policy of 'Apartheid'?", "options": ["South Africa", "USA", "Russia", "France"], "answer": "South Africa"},
      {"question": "What is the meaning of 'Satyagraha'?", "options": ["Armed protest", "Peaceful resistance", "Economic reform", "Violent strike"], "answer": "Peaceful resistance"},
      {"question": "Which power station uses falling water to generate electricity?", "options": ["Thermal", "Hydroelectric", "Nuclear", "Solar"], "answer": "Hydroelectric"},
      {"question": "Which level of government in India makes laws on subjects like defense?", "options": ["State", "District", "Central", "Local"], "answer": "Central"},
      {"question": "Which organisation publishes the Human Development Index?", "options": ["UNESCO", "IMF", "World Bank", "UNDP"], "answer": "UNDP"},
      {"question": "What is the basic unit of a democratic setup?", "options": ["Village", "Ward", "Gram Panchayat", "Citizen"], "answer": "Citizen"},
      {"question": "Which soil is formed by the deposition of silt by rivers?", "options": ["Black soil", "Red soil", "Laterite soil", "Alluvial soil"], "answer": "Alluvial soil"}
    ],
    "Hard": [
      {"question": "When was the Civil Disobedience Movement launched?", "options": ["1920", "1929", "1930", "1942"], "answer": "1930"},
      {"question": "Which Indian leader gave the slogan 'Do or Die'?", "options": ["Subhas Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel"], "answer": "Mahatma Gandhi"},
      {"question": "Which revolution is called the ‘Bloody Sunday’?", "options": ["Russian Revolution", "American Revolution", "French Revolution", "Industrial Revolution"], "answer": "Russian Revolution"},
      {"question": "Which state has the largest coal reserves in India?", "options": ["Jharkhand", "Odisha", "Chhattisgarh", "Madhya Pradesh"], "answer": "Jharkhand"},
      {"question": "What is meant by ‘collateral’ in terms of loans?", "options": ["Interest amount", "Security for repayment", "Loan amount", "Loan period"], "answer": "Security for repayment"},
      {"question": "Which pressure group fights for the rights of farmers in India?", "options": ["SEWA", "AIKS", "FICCI", "ASSOCHAM"], "answer": "AIKS"},
      {"question": "Which fundamental right ensures equality before the law?", "options": ["Right to Equality", "Right to Freedom", "Right to Religion", "Right to Education"], "answer": "Right to Equality"},
      {"question": "Which two factors determine the sex ratio of a country?", "options": ["Birth rate and death rate", "Number of males and females", "Migration and education", "GDP and literacy"], "answer": "Number of males and females"},
      {"question": "Which Indian state is the largest producer of manganese?", "options": ["Odisha", "Maharashtra", "Karnataka", "Rajasthan"], "answer": "Odisha"},
      {"question": "Which body is responsible for resolving disputes between different levels of government in India?", "options": ["President", "High Court", "Supreme Court", "Governor"], "answer": "Supreme Court"}
    ]
  },
  "Hindi": {
    "Easy": [
      {"question": "‘अतीत में दबे पाँव’ पाठ के लेखक कौन हैं?", "options": ["निर्मल वर्मा", "हज़ारी प्रसाद द्विवेदी", "कमलेश्वर", "भीष्म साहनी"], "answer": "निर्मल वर्मा"},
      {"question": "‘साखियाँ’ किस कवि द्वारा रचित हैं?", "options": ["कबीर", "मीरा", "रहीम", "सूरदास"], "answer": "कबीर"},
      {"question": "‘साना–साना हाथ जोड़ि’ किस रचनाकार की आत्मकथात्मक रचना है?", "options": ["मन्नू भंडारी", "चित्रा मुद्गल", "मृदुला गर्ग", "मालती जोशी"], "answer": "मृदुला गर्ग"},
      {"question": "‘मैं क्यों लिखता हूँ’ पाठ किस लेखक की रचना है?", "options": ["मोहन राकेश", "रामविलास शर्मा", "सच्चिदानंद वात्स्यायन", "हरिशंकर परसाई"], "answer": "सच्चिदानंद वात्स्यायन"},
      {"question": "‘तत्सम’ शब्द कौन सा है?", "options": ["गृह", "घर", "घरे", "घरवा"], "answer": "गृह"},
      {"question": "‘कन्हैया’ किसका पर्यायवाची है?", "options": ["शिव", "राम", "कृष्ण", "हनुमान"], "answer": "कृष्ण"},
      {"question": "‘बड़े भाई साहब’ में छोटे भाई को क्या अधिक पसंद था?", "options": ["पढ़ाई", "खेलना", "घूमना", "सोना"], "answer": "खेलना"},
      {"question": "‘डायरी का एक पन्ना’ किस विषय पर आधारित है?", "options": ["विज्ञान", "आत्मकथा", "युद्ध अनुभव", "पर्यावरण"], "answer": "युद्ध अनुभव"},
      {"question": "‘तीसरी कसम के शिल्पकार शैलेन्द्र’ पाठ किस कलाकार पर आधारित है?", "options": ["शैलेन्द्र", "राज कपूर", "गुरुदत्त", "प्रेमचंद"], "answer": "शैलेन्द्र"},
      {"question": "‘कहानी एक बोझिल शाम की’ किस लेखक की रचना है?", "options": ["लीलाधर मंडलोई", "मोहन राकेश", "कृष्णा सोबती", "कमलेश्वर"], "answer": "लीलाधर मंडलोई"}
    ],
    "Medium": [
      {"question": "‘सपनों के-से दिन’ में लेखक कौन है?", "options": ["गजानन माधव मुक्तिबोध", "हरिशंकर परसाई", "मन्नू भंडारी", "चित्रा मुद्गल"], "answer": "गजानन माधव मुक्तिबोध"},
      {"question": "‘बोलनेवाली तोता’ किस प्रकार की रचना है?", "options": ["आत्मकथा", "रूपक", "काल्पनिक कथा", "निबंध"], "answer": "काल्पनिक कथा"},
      {"question": "‘सपनों के से दिन’ में लेखक को सबसे ज्यादा क्या अच्छा लगता था?", "options": ["कविता लिखना", "खेलना", "घूमना", "पढ़ना"], "answer": "कविता लिखना"},
      {"question": "‘पत्र लेखन’ में किस प्रकार की भाषा उपयोगी होती है?", "options": ["कठिन और साहित्यिक", "सरल और स्पष्ट", "आदेशात्मक", "काव्यात्मक"], "answer": "सरल और स्पष्ट"},
      {"question": "‘नौबतखाने में इबादत’ किस रचनाकार की कविता है?", "options": ["नज़ीर अकबराबादी", "धर्मवीर भारती", "रामधारी सिंह दिनकर", "सुभद्राकुमारी चौहान"], "answer": "नज़ीर अकबराबादी"},
      {"question": "‘राम-लक्ष्मण-परशुराम संवाद’ किस ग्रंथ से लिया गया है?", "options": ["रामचरितमानस", "महाभारत", "भागवत", "अकबरनामा"], "answer": "रामचरितमानस"},
      {"question": "‘तीसरी कसम’ फिल्म किस लेखक की कहानी पर आधारित है?", "options": ["फणीश्वर नाथ 'रेणु'", "प्रेमचंद", "शिवानी", "कमलेश्वर"], "answer": "फणीश्वर नाथ 'रेणु'"},
      {"question": "‘रस’ का शाब्दिक अर्थ क्या होता है?", "options": ["भावना", "स्वाद", "शक्ति", "कविता"], "answer": "स्वाद"},
      {"question": "‘दुर्योधन का अंतिम पाठ’ किस प्रकार की रचना है?", "options": ["कहानी", "नाटक", "कविता", "डायरी"], "answer": "नाटक"},
      {"question": "‘संयोग’ रस का स्थायी भाव क्या होता है?", "options": ["रति", "क्रोध", "हास", "घृणा"], "answer": "रति"}
    ],
    "Hard": [
      {"question": "‘उत्साह’ कविता में कवि ने किस युद्ध की पृष्ठभूमि को प्रस्तुत किया है?", "options": ["भारत-चीन युद्ध", "भारत-पाक युद्ध", "प्रथम विश्व युद्ध", "अमेरिका-जापान युद्ध"], "answer": "भारत-चीन युद्ध"},
      {"question": "‘शक्ति और कर्तव्य’ निबंध किस लेखक द्वारा रचित है?", "options": ["रामविलास शर्मा", "जवाहरलाल नेहरू", "सुभाष चंद्र बोस", "हरिवंश राय बच्चन"], "answer": "जवाहरलाल नेहरू"},
      {"question": "‘मनुष्यता’ कविता में किस गुण को सर्वोपरि बताया गया है?", "options": ["धर्म", "ज्ञान", "शक्ति", "करुणा"], "answer": "करुणा"},
      {"question": "‘पुस्तक समीक्षा’ में लेखक को किस पुस्तक की समीक्षा करनी होती है?", "options": ["अज्ञात", "समीक्षक की पसंदीदा", "दी गई पुस्तक", "कोई भी पत्रिका"], "answer": "दी गई पुस्तक"},
      {"question": "‘हरिहर काका’ कहानी में मुख्य समस्या क्या है?", "options": ["धार्मिक संघर्ष", "भूमि विवाद", "भ्रष्टाचार", "यात्रा समस्या"], "answer": "भूमि विवाद"},
      {"question": "‘सपनों के से दिन’ पाठ में लेखक ने अपने जीवन के किस समय को याद किया?", "options": ["बचपन", "प्रौढ़ावस्था", "विद्यालय जीवन", "सेवानिवृत्ति"], "answer": "विद्यालय जीवन"},
      {"question": "‘संधि’ के कितने भेद होते हैं?", "options": ["3", "4", "5", "2"], "answer": "3"},
      {"question": "‘नर’ और ‘नारी’ में कौन-सा समास है?", "options": ["द्वंद्व", "द्विगु", "तत्पुरुष", "बहुव्रीहि"], "answer": "द्वंद्व"},
      {"question": "‘गद्यांश’ से संबंधित प्रश्नों में मुख्य रूप से क्या पूछा जाता है?", "options": ["व्याकरण", "कहानी लेखन", "संदर्भ", "समझ-बूझ और निष्कर्ष"], "answer": "समझ-बूझ और निष्कर्ष"},
      {"question": "‘नमक का दरोगा’ में ड्यूटी और नैतिकता के बीच कौन संघर्ष दिखाया गया है?", "options": ["कर्तव्य और रिश्वत", "अहंकार और प्रेम", "धन और धर्म", "परिवार और समाज"], "answer": "कर्तव्य और रिश्वत"}
    ]
  },
  "Information Technology": {
    "Easy": [
      {"question": "Which shortcut key is used to copy text in a document?", "options": ["Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + Z"], "answer": "Ctrl + C"},
      {"question": "What is the extension of an OpenDocument Text file?", "options": [".doc", ".txt", ".odt", ".pdf"], "answer": ".odt"},
      {"question": "Which key combination is used to paste copied content?", "options": ["Ctrl + C", "Ctrl + X", "Ctrl + P", "Ctrl + V"], "answer": "Ctrl + V"},
      {"question": "Which feature is used to find and correct spelling errors?", "options": ["Grammar Check", "Spell Check", "Find & Replace", "Track Changes"], "answer": "Spell Check"},
      {"question": "What is the default alignment of text in a Writer document?", "options": ["Right", "Left", "Center", "Justify"], "answer": "Left"},
      {"question": "Which key is used to insert a new slide in presentation software?", "options": ["Ctrl + N", "Ctrl + M", "Ctrl + P", "Ctrl + S"], "answer": "Ctrl + M"},
      {"question": "Which software is used to create spreadsheets?", "options": ["Writer", "Calc", "Impress", "Draw"], "answer": "Calc"},
      {"question": "Which function is used to add a range of numbers in a spreadsheet?", "options": ["=ADD", "=TOTAL", "=SUM", "=PLUS"], "answer": "=SUM"},
      {"question": "Which symbol is used before a formula in Calc?", "options": ["@", "=", "#", "$"], "answer": "="},
      {"question": "Which tab is used to apply borders in Calc?", "options": ["Insert", "View", "Format", "Tools"], "answer": "Format"}
    ],
    "Medium": [
      {"question": "Which shortcut is used to undo an action?", "options": ["Ctrl + U", "Ctrl + Z", "Ctrl + R", "Ctrl + Y"], "answer": "Ctrl + Z"},
      {"question": "What is the shortcut key for 'Find and Replace'?", "options": ["Ctrl + F", "Ctrl + R", "Ctrl + H", "Ctrl + T"], "answer": "Ctrl + H"},
      {"question": "Which menu is used to insert header and footer in a document?", "options": ["Insert", "Format", "Tools", "Edit"], "answer": "Insert"},
      {"question": "Which function gives the highest number from a range?", "options": ["=MAX", "=HIGH", "=TOP", "=UP"], "answer": "=MAX"},
      {"question": "Which database object is used to store data?", "options": ["Query", "Form", "Table", "Report"], "answer": "Table"},
      {"question": "Which type of chart is used to show trends over time?", "options": ["Bar", "Pie", "Line", "Column"], "answer": "Line"},
      {"question": "Which function is used to count numeric values only?", "options": ["=COUNTA", "=COUNT", "=NUMCOUNT", "=VALUECOUNT"], "answer": "=COUNT"},
      {"question": "What is the shortcut to insert a hyperlink?", "options": ["Ctrl + H", "Ctrl + K", "Ctrl + L", "Ctrl + Shift + H"], "answer": "Ctrl + K"},
      {"question": "Which software is used for database management?", "options": ["Writer", "Calc", "Base", "Draw"], "answer": "Base"},
      {"question": "Which function returns the average of a range?", "options": ["=AVERAGE", "=MEAN", "=TOTAL/COUNT", "=AVG"], "answer": "=AVERAGE"}
    ],
    "Hard": [
      {"question": "What is the purpose of 'Track Changes' in a document?", "options": ["To add comments", "To see editing history", "To print document", "To format headings"], "answer": "To see editing history"},
      {"question": "What is the use of 'Data Validation' in Calc?", "options": ["To highlight duplicates", "To format data", "To restrict user input", "To change cell size"], "answer": "To restrict user input"},
      {"question": "Which tool helps create a summary of data in Calc?", "options": ["Filter", "Chart", "Pivot Table", "Data Sort"], "answer": "Pivot Table"},
      {"question": "What is the purpose of a 'Form' in Base?", "options": ["To format documents", "To generate reports", "To input data easily", "To print tables"], "answer": "To input data easily"},
      {"question": "Which chart type is best for showing percentages?", "options": ["Line", "Bar", "Pie", "Column"], "answer": "Pie"},
      {"question": "Which clause is used to filter records in SQL?", "options": ["ORDER BY", "SELECT", "FROM", "WHERE"], "answer": "WHERE"},
      {"question": "Which function returns the number of characters in a string?", "options": ["=LEN", "=CHAR", "=COUNT", "=NUM"], "answer": "=LEN"},
      {"question": "What does 'Ctrl + Shift + P' do in Writer?", "options": ["Print Preview", "Change Font Size", "Open Paragraph Dialog", "Insert Page Number"], "answer": "Change Font Size"},
      {"question": "Which tag is used for hyperlinks in HTML?", "options": ["<link>", "<a>", "<href>", "<hyper>"], "answer": "<a>"},
      {"question": "What is phishing?", "options": ["A method of hacking passwords", "A fake website to steal data", "Spam email", "Antivirus software"], "answer": "A fake website to steal data"}
    ]
  }
},
"11": {
  "English": {
    "Easy": [
      {
        "question": "Who is the author of the poem 'A Photograph'?",
        "options": ["Shirley Toulson", "Robert Frost", "John Keats", "William Wordsworth"],
        "answer": "Shirley Toulson"
      },
      {
        "question": "What is the main theme of 'The Portrait of a Lady'?",
        "options": ["Technology", "Grandmother-grandson relationship", "Adventure", "War"],
        "answer": "Grandmother-grandson relationship"
      },
      {
        "question": "What did the grandmother always carry with her?",
        "options": ["A stick", "A rosary", "A bag", "A book"],
        "answer": "A rosary"
      },
      {
        "question": "Where is Khushwant Singh’s grandmother’s village located?",
        "options": ["Delhi", "Punjab", "Mumbai", "Kolkata"],
        "answer": "Punjab"
      },
      {
        "question": "Who is the narrator of 'We're Not Afraid to Die... if We Can All Be Together'?",
        "options": ["Jonathan", "Suzanne", "The father", "The mother"],
        "answer": "The father"
      },
      {
        "question": "In the poem 'The Voice of the Rain', who is the speaker?",
        "options": ["The poet", "The cloud", "The rain", "The tree"],
        "answer": "The rain"
      },
      {
        "question": "What does rain compare itself to in 'The Voice of the Rain'?",
        "options": ["Music", "Poetry", "A song", "The earth"],
        "answer": "Poetry"
      },
      {
        "question": "In 'Childhood', what did the poet lose?",
        "options": ["His childhood", "His toy", "His diary", "His friend"],
        "answer": "His childhood"
      },
      {
        "question": "Who wrote 'Childhood'?",
        "options": ["Markus Natten", "Shirley Toulson", "Walt Whitman", "R.C. Shukla"],
        "answer": "Markus Natten"
      },
      {
        "question": "What does the grandmother feed the sparrows in 'The Portrait of a Lady'?",
        "options": ["Rice", "Wheat", "Biscuits", "Crumbs of bread"],
        "answer": "Crumbs of bread"
      }
    ],
    "Medium": [
      {
        "question": "What do the children do when the grandmother dies in 'The Portrait of a Lady'?",
        "options": ["Cry", "Celebrate", "Remain silent", "Pray"],
        "answer": "Remain silent"
      },
      {
        "question": "What is the poetic device used in 'A Photograph'?",
        "options": ["Alliteration", "Metaphor", "Simile", "Personification"],
        "answer": "Personification"
      },
      {
        "question": "What happened to the ship in 'We're Not Afraid to Die'?",
        "options": ["It hit an iceberg", "It capsized", "It was damaged in a storm", "It sank completely"],
        "answer": "It was damaged in a storm"
      },
      {
        "question": "How old was the poet’s mother in 'A Photograph' when the picture was taken?",
        "options": ["Twelve", "Fourteen", "Ten", "Eighteen"],
        "answer": "Twelve"
      },
      {
        "question": "Who is the author of 'The Ailing Planet: The Green Movement's Role'?",
        "options": ["Nani Palkhivala", "A.P.J. Abdul Kalam", "Amartya Sen", "Khushwant Singh"],
        "answer": "Nani Palkhivala"
      },
      {
        "question": "In 'Discovering Tut', where was Tutankhamun’s body found?",
        "options": ["Pyramid", "Underground chamber", "Desert", "River bank"],
        "answer": "Underground chamber"
      },
      {
        "question": "In 'The Adventure', who is Professor Gaitonde?",
        "options": ["Historian", "Doctor", "Scientist", "Lawyer"],
        "answer": "Historian"
      },
      {
        "question": "In 'The Address', who is the narrator?",
        "options": ["A young girl", "A postman", "A teacher", "A soldier"],
        "answer": "A young girl"
      },
      {
        "question": "Who is the author of 'Ranga's Marriage'?",
        "options": ["Masti Venkatesha Iyengar", "R.K. Narayan", "Ruskin Bond", "Mulk Raj Anand"],
        "answer": "Masti Venkatesha Iyengar"
      },
      {
        "question": "What does the rain say it rises from in 'The Voice of the Rain'?",
        "options": ["The sea", "The land and bottomless sea", "Mountains", "The sky"],
        "answer": "The land and bottomless sea"
      }
    ],
    "Hard": [
      {
        "question": "What type of poem is 'A Photograph'?",
        "options": ["Elegy", "Ballad", "Sonnet", "Ode"],
        "answer": "Elegy"
      },
      {
        "question": "What does the poem 'Childhood' explore?",
        "options": ["Loss of innocence", "Love for nature", "War", "Loneliness"],
        "answer": "Loss of innocence"
      },
      {
        "question": "What is the setting of the story 'The Address'?",
        "options": ["Post-war Netherlands", "India", "Germany", "France"],
        "answer": "Post-war Netherlands"
      },
      {
        "question": "What does the phrase 'The sea holiday was her past, mine is her laughter' signify in 'A Photograph'?",
        "options": ["Different generations' memories", "Time travel", "Childhood dreams", "Nature’s beauty"],
        "answer": "Different generations' memories"
      },
      {
        "question": "What literary device is used in 'The Voice of the Rain' to give rain human qualities?",
        "options": ["Personification", "Hyperbole", "Irony", "Onomatopoeia"],
        "answer": "Personification"
      },
      {
        "question": "In 'We're Not Afraid to Die', who showed extraordinary courage despite injury?",
        "options": ["Suzanne", "Jonathan", "The father", "The crewman"],
        "answer": "Suzanne"
      },
      {
        "question": "What is the main concern of 'The Ailing Planet' article?",
        "options": ["Environmental degradation", "Politics", "Technology", "Economy"],
        "answer": "Environmental degradation"
      },
      {
        "question": "Who discovered Tutankhamun’s tomb?",
        "options": ["Howard Carter", "Napoleon", "Lord Carnarvon", "John Carter"],
        "answer": "Howard Carter"
      },
      {
        "question": "In 'The Adventure', which battle did India win according to the alternative history?",
        "options": ["Battle of Panipat", "Battle of Plassey", "Battle of Waterloo", "Battle of Buxar"],
        "answer": "Battle of Panipat"
      },
      {
        "question": "What is the tone of the poem 'A Photograph'?",
        "options": ["Nostalgic", "Humorous", "Angry", "Optimistic"],
        "answer": "Nostalgic"
      }
    ]
  },
  "Hindi": {
    "Easy": [
      {
        "question": "'पुष्य पर्व' किस रचना का अंश है?",
        "options": ["कविता के बहाने", "पतंग", "गजल", "राजा का बाजा"],
        "answer": "कविता के बहाने"
      },
      {
        "question": "'भारत माता' कविता के रचयिता कौन हैं?",
        "options": ["महादेवी वर्मा", "सुमित्रानंदन पंत", "मैथिलीशरण गुप्त", "माखनलाल चतुर्वेदी"],
        "answer": "सुमित्रानंदन पंत"
      },
      {
        "question": "'मीठे बोल' किस अध्याय में वर्णित हैं?",
        "options": ["नमक का दरोगा", "सपनों के से दिन", "जामुन का पेड़", "ल्हासा की ओर"],
        "answer": "नमक का दरोगा"
      },
      {
        "question": "‘गजल’ किस विधा से संबंधित है?",
        "options": ["निबंध", "कहानी", "कविता", "गीत"],
        "answer": "कविता"
      },
      {
        "question": "‘जामुन का पेड़’ पाठ के लेखक कौन हैं?",
        "options": ["रामवृक्ष बेनीपुरी", "हैरी एस्टेलिन", "कमलेश्वर", "राही मासूम रज़ा"],
        "answer": "कमलेश्वर"
      },
      {
        "question": "'राजा का बाजा' कविता किसने लिखी है?",
        "options": ["केदारनाथ अग्रवाल", "रघुवीर सहाय", "धूमिल", "शमशेर बहादुर सिंह"],
        "answer": "केदारनाथ अग्रवाल"
      },
      {
        "question": "‘पतंग’ कविता का मुख्य विषय क्या है?",
        "options": ["बचपन की यादें", "प्रकृति", "मनुष्य का संघर्ष", "उत्सव"],
        "answer": "बचपन की यादें"
      },
      {
        "question": "'ल्हासा की ओर' यात्रा वृतांत है –",
        "options": ["लेह का", "तिब्बत का", "नेपाल का", "चीन का"],
        "answer": "तिब्बत का"
      },
      {
        "question": "'गुलाब सिंह' किस कहानी का पात्र है?",
        "options": ["गुलाबो", "सपनों के से दिन", "नमक का दरोगा", "ग्लास"],
        "answer": "नमक का दरोगा"
      },
      {
        "question": "'सपनों के से दिन' किस लेखक की आत्मकथा है?",
        "options": ["हरिशंकर परसाई", "नंदकिशोर आचार्य", "नरेश मेहता", "निराला"],
        "answer": "नंदकिशोर आचार्य"
      }
    ],
    "Medium": [
      {
        "question": "'गजल' कविता में किस प्रकार की पीड़ा व्यक्त की गई है?",
        "options": ["देशभक्ति", "प्रेम", "राजनीतिक", "सामाजिक अन्याय"],
        "answer": "सामाजिक अन्याय"
      },
      {
        "question": "'ध्वनि' कविता के रचनाकार कौन हैं?",
        "options": ["रघुवीर सहाय", "धूमिल", "अज्ञेय", "केदारनाथ सिंह"],
        "answer": "अज्ञेय"
      },
      {
        "question": "‘नमक का दरोगा’ किस लेखक की रचना है?",
        "options": ["मुंशी प्रेमचंद", "निराला", "रामवृक्ष बेनीपुरी", "कमलेश्वर"],
        "answer": "मुंशी प्रेमचंद"
      },
      {
        "question": "'भारत माता' कविता में कौन-सा रूप नहीं है?",
        "options": ["धरा", "नारी", "पर्वत", "ताजमहल"],
        "answer": "ताजमहल"
      },
      {
        "question": "'अतीत में दबे पाँव' कविता किसकी रचना है?",
        "options": ["रघुवीर सहाय", "मुक्तिबोध", "धूमिल", "शमशेर बहादुर सिंह"],
        "answer": "मुक्तिबोध"
      },
      {
        "question": "'ग्राम श्री' कविता किस ग्रंथ से ली गई है?",
        "options": ["गीतांजलि", "कामायनी", "पल्लव", "उर्वशी"],
        "answer": "पल्लव"
      },
      {
        "question": "‘ल्हासा की ओर’ पाठ में लेखक कौन है?",
        "options": ["राहुल सांकृत्यायन", "बनारसीदास चतुर्वेदी", "निराला", "प्रेमचंद"],
        "answer": "राहुल सांकृत्यायन"
      },
      {
        "question": "‘जामुन का पेड़’ में न्याय व्यवस्था को क्या दिखाया गया है?",
        "options": ["उचित", "जटिल और अक्षम", "मजबूत", "भरोसेमंद"],
        "answer": "जटिल और अक्षम"
      },
      {
        "question": "'गजल' कविता में कौन-सी विधा की विशेषता है?",
        "options": ["तुकांतता", "छंदमुक्तता", "प्रबोधन", "भावनात्मकता"],
        "answer": "तुकांतता"
      },
      {
        "question": "'राजा का बाजा' कविता में क्या प्रतीक बनकर आता है?",
        "options": ["बाजा", "राजा", "गरीब", "क्रांति"],
        "answer": "बाजा"
      }
    ],
    "Hard": [
      {
        "question": "'अतीत में दबे पाँव' कविता में किसकी खोज की गई है?",
        "options": ["राजनीति की", "बचपन की", "अतीत की स्मृतियों की", "विज्ञान की"],
        "answer": "अतीत की स्मृतियों की"
      },
      {
        "question": "'नमक का दरोगा' में कलक्टर की भूमिका क्या दर्शाती है?",
        "options": ["ईमानदारी", "भ्रष्टाचार", "लोकतंत्र", "अनुशासन"],
        "answer": "भ्रष्टाचार"
      },
      {
        "question": "'ध्वनि' कविता में किसकी चर्चा है?",
        "options": ["प्रेम की", "राजनीति की", "आत्मा की आवाज़ की", "प्रकृति की"],
        "answer": "आत्मा की आवाज़ की"
      },
      {
        "question": "‘सपनों के से दिन’ पाठ का स्वरूप क्या है?",
        "options": ["कहानी", "यात्रावृत्तांत", "आत्मकथा", "डायरी"],
        "answer": "आत्मकथा"
      },
      {
        "question": "'ग्राम श्री' कविता में किस चीज़ का सौंदर्य वर्णन है?",
        "options": ["नगर", "वन", "ग्राम्य जीवन", "नदी"],
        "answer": "ग्राम्य जीवन"
      },
      {
        "question": "‘राजा का बाजा’ कविता में किस सामाजिक समस्या पर व्यंग्य है?",
        "options": ["गरीबी", "शिक्षा", "जातिवाद", "शोषण"],
        "answer": "शोषण"
      },
      {
        "question": "'जामुन का पेड़' कहानी में किसके द्वारा केस लड़ा गया?",
        "options": ["लेखक", "माली", "बड़ा बाबू", "किसान"],
        "answer": "बड़ा बाबू"
      },
      {
        "question": "'भारत माता' कविता में कौन-सी छवि प्रमुख है?",
        "options": ["मंदिर", "युद्धभूमि", "माँ", "पर्वत"],
        "answer": "माँ"
      },
      {
        "question": "‘ल्हासा की ओर’ में लेखक ने क्या दर्शाया है?",
        "options": ["युद्ध का वर्णन", "धार्मिकता", "तिब्बत की यात्रा", "भारतीय संस्कृति"],
        "answer": "तिब्बत की यात्रा"
      },
      {
        "question": "'ध्वनि' कविता में 'सुनने वाला' कौन है?",
        "options": ["ईश्वर", "आम आदमी", "कवि", "राजा"],
        "answer": "कवि"
      }
    ]
  },
  "Mathematics": {
    "Easy": [
      {
        "question": "What is the cardinality of set A = {2, 4, 6, 8}?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
      },
      {
        "question": "Which of the following is a null set?",
        "options": ["{0}", "{}", "{∅}", "{1}"],
        "answer": "{}"
      },
      {
        "question": "What is sin(90°)?",
        "options": ["0", "1", "-1", "0.5"],
        "answer": "1"
      },
      {
        "question": "The value of cos(0°) is:",
        "options": ["1", "0", "-1", "2"],
        "answer": "1"
      },
      {
        "question": "i² equals to:",
        "options": ["0", "1", "-1", "2"],
        "answer": "-1"
      },
      {
        "question": "Which of the following is a rational number?",
        "options": ["√2", "π", "1/2", "√3"],
        "answer": "1/2"
      },
      {
        "question": "Which quadrant does the point (−3, 2) lie in?",
        "options": ["I", "II", "III", "IV"],
        "answer": "II"
      },
      {
        "question": "The degree of polynomial x³ + 2x² + 3x + 4 is:",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
      },
      {
        "question": "The probability of getting head in a fair coin toss is:",
        "options": ["0", "1", "1/2", "2"],
        "answer": "1/2"
      },
      {
        "question": "The solution set of x < 5 is:",
        "options": ["(5, ∞)", "(−∞, 5)", "[5, ∞)", "(−∞, 5]"],
        "answer": "(−∞, 5)"
      }
    ],
    "Medium": [
      {
        "question": "If A = {1, 2}, B = {2, 3}, then A ∩ B is:",
        "options": ["{1}", "{2}", "{3}", "{1, 2}"],
        "answer": "{2}"
      },
      {
        "question": "The domain of y = √(x − 2) is:",
        "options": ["x ≥ 2", "x > 0", "x < 2", "x ≠ 2"],
        "answer": "x ≥ 2"
      },
      {
        "question": "cos²θ + sin²θ equals to:",
        "options": ["0", "1", "2", "undefined"],
        "answer": "1"
      },
      {
        "question": "Which of the following is an irrational number?",
        "options": ["0.25", "1/2", "√3", "2"],
        "answer": "√3"
      },
      {
        "question": "Which of the following is a complex number?",
        "options": ["3", "2i", "√5", "π"],
        "answer": "2i"
      },
      {
        "question": "Slope of line y = 3x + 5 is:",
        "options": ["3", "5", "1", "-3"],
        "answer": "3"
      },
      {
        "question": "The solution of inequality 3x − 4 < 5 is:",
        "options": ["x < 3", "x > 3", "x = 3", "x ≤ 3"],
        "answer": "x < 3"
      },
      {
        "question": "If a die is thrown once, probability of getting odd number is:",
        "options": ["1/2", "1/3", "2/3", "1/6"],
        "answer": "1/2"
      },
      {
        "question": "If z = 3 + 4i, then |z| equals:",
        "options": ["5", "7", "1", "2"],
        "answer": "5"
      },
      {
        "question": "The distance between points (0, 0) and (3, 4) is:",
        "options": ["5", "6", "4", "7"],
        "answer": "5"
      }
    ],
    "Hard": [
      {
        "question": "tan A + cot A equals minimum when A is:",
        "options": ["30°", "45°", "60°", "90°"],
        "answer": "45°"
      },
      {
        "question": "If f(x) = x² − 4x + 7, then f(2) is:",
        "options": ["3", "7", "2", "1"],
        "answer": "3"
      },
      {
        "question": "The sum of first n natural numbers is:",
        "options": ["n(n−1)/2", "n²", "n(n+1)/2", "2n"],
        "answer": "n(n+1)/2"
      },
      {
        "question": "The straight line x + 2y = 6 intersects the y-axis at:",
        "options": ["(0, 3)", "(6, 0)", "(0, −3)", "(2, 2)"],
        "answer": "(0, 3)"
      },
      {
        "question": "A set containing all real numbers except 0 is:",
        "options": ["R", "R−{0}", "Z", "Q"],
        "answer": "R−{0}"
      },
      {
        "question": "Which of the following is not a function?",
        "options": ["f(x) = x", "f(x) = √x", "f(x) = 1/x", "f(x) = ±x"],
        "answer": "f(x) = ±x"
      },
      {
        "question": "The number of subsets of set A = {a, b, c} is:",
        "options": ["3", "6", "8", "9"],
        "answer": "8"
      },
      {
        "question": "If tan A = 1, then angle A is:",
        "options": ["30°", "45°", "60°", "90°"],
        "answer": "45°"
      },
      {
        "question": "Equation of line with slope 2 and passing through (1,2):",
        "options": ["y = 2x", "y = 2x + 1", "y = 2x + 0", "y = 2x + 2"],
        "answer": "y = 2x"
      },
      {
        "question": "The range of function f(x) = x² is:",
        "options": ["R", "R+", "[0, ∞)", "(-∞, ∞)"],
        "answer": "[0, ∞)"
      }
    ]
  },
  "Physics": {
    "Easy": [
      {"question": "What is the SI unit of force?", "options": ["Joule", "Pascal", "Newton", "Watt"], "answer": "Newton"},
      {"question": "Which physical quantity is measured in meters per second (m/s)?", "options": ["Acceleration", "Velocity", "Force", "Work"], "answer": "Velocity"},
      {"question": "What type of quantity is displacement?", "options": ["Scalar", "Vector", "Dimensionless", "None"], "answer": "Vector"},
      {"question": "Name the force that opposes motion between two surfaces.", "options": ["Friction", "Magnetism", "Tension", "Gravity"], "answer": "Friction"},
      {"question": "What is the acceleration due to gravity on Earth?", "options": ["8.9 m/s²", "9.8 m/s²", "10 m/s²", "9 m/s²"], "answer": "9.8 m/s²"},
      {"question": "Which of the following is a scalar quantity?", "options": ["Velocity", "Acceleration", "Force", "Speed"], "answer": "Speed"},
      {"question": "What is the SI unit of energy?", "options": ["Watt", "Joule", "Newton", "Ohm"], "answer": "Joule"},
      {"question": "What is the direction of centripetal force?", "options": ["Outward", "Tangential", "Inward", "Random"], "answer": "Inward"},
      {"question": "Which law is F = ma associated with?", "options": ["Newton’s First Law", "Newton’s Second Law", "Newton’s Third Law", "Hooke’s Law"], "answer": "Newton’s Second Law"},
      {"question": "Which instrument is used to measure mass?", "options": ["Spring balance", "Thermometer", "Barometer", "Balance scale"], "answer": "Balance scale"}
    ],
    "Medium": [
      {"question": "What is the dimensional formula of work?", "options": ["[MLT^-2]", "[ML^2T^-2]", "[ML^2T^-1]", "[M^2L^2T^-2]"], "answer": "[ML^2T^-2]"},
      {"question": "Which of the following quantities has no direction?", "options": ["Displacement", "Velocity", "Acceleration", "Distance"], "answer": "Distance"},
      {"question": "Which law states that for every action, there is an equal and opposite reaction?", "options": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Hooke’s Law"], "answer": "Newton's Third Law"},
      {"question": "Which energy is associated with motion?", "options": ["Potential energy", "Thermal energy", "Kinetic energy", "Chemical energy"], "answer": "Kinetic energy"},
      {"question": "What is the work done when a body moves in a circular path?", "options": ["Zero", "Maximum", "Negative", "Positive"], "answer": "Zero"},
      {"question": "What is the angle between force and displacement in case of maximum work?", "options": ["0°", "45°", "90°", "180°"], "answer": "0°"},
      {"question": "Which quantity is conserved in an elastic collision?", "options": ["Only momentum", "Only energy", "Momentum and kinetic energy", "Only potential energy"], "answer": "Momentum and kinetic energy"},
      {"question": "Which formula gives the centripetal force?", "options": ["mv", "mv²/r", "mr²", "v²r/m"], "answer": "mv²/r"},
      {"question": "Which of the following is not a fundamental unit?", "options": ["Second", "Meter", "Gram", "Ampere"], "answer": "Gram"},
      {"question": "Which of these represents a derived quantity?", "options": ["Mass", "Length", "Time", "Force"], "answer": "Force"}
    ],
    "Hard": [
      {"question": "Which of the following represents the correct equation of motion under gravity?", "options": ["s = ut + 1/2gt²", "s = ut + gt²", "s = ut - 1/2gt²", "s = u² + 2gs"], "answer": "s = ut + 1/2gt²"},
      {"question": "What is the escape velocity from Earth’s surface?", "options": ["9.8 m/s", "11.2 km/s", "7.9 km/s", "22.4 km/s"], "answer": "11.2 km/s"},
      {"question": "Moment of inertia of a solid sphere about its diameter is?", "options": ["(2/5)MR²", "(1/2)MR²", "(3/5)MR²", "(5/2)MR²"], "answer": "(2/5)MR²"},
      {"question": "In SHM, acceleration is proportional to:", "options": ["Velocity", "Displacement", "Time", "Mass"], "answer": "Displacement"},
      {"question": "Which of the following quantities has the unit kg·m²/s²?", "options": ["Work", "Momentum", "Power", "Pressure"], "answer": "Work"},
      {"question": "Which law governs the motion of planets around the sun?", "options": ["Newton’s Laws", "Kepler’s Laws", "Ohm’s Law", "Hooke’s Law"], "answer": "Kepler’s Laws"},
      {"question": "The potential energy of a spring is given by?", "options": ["1/2 kx²", "kx", "k/x", "1/2 mv²"], "answer": "1/2 kx²"},
      {"question": "What is the time period of a simple pendulum dependent on?", "options": ["Mass", "Amplitude", "Length", "Displacement"], "answer": "Length"},
      {"question": "Which unit is used for angular momentum?", "options": ["kg m²/s", "kg m/s²", "kg/m²", "kg m/s"], "answer": "kg m²/s"},
      {"question": "What is the relation between linear and angular velocity?", "options": ["v = rω", "v = ω/r", "v = r/ω", "v = ω²r"], "answer": "v = rω"}
    ]
  },
  "Chemistry": {
    "Easy": [
      {"question": "What is the atomic number of Carbon?", "options": ["6", "12", "14", "8"], "answer": "6"},
      {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Osmium", "Zinc"], "answer": "Oxygen"},
      {"question": "What is the formula of water?", "options": ["H2O", "CO2", "O2", "H2"], "answer": "H2O"},
      {"question": "Which state of matter has a fixed shape and volume?", "options": ["Solid", "Liquid", "Gas", "Plasma"], "answer": "Solid"},
      {"question": "What is the charge of a proton?", "options": ["+1", "-1", "0", "+2"], "answer": "+1"},
      {"question": "Which particle has no electric charge?", "options": ["Electron", "Proton", "Neutron", "Positron"], "answer": "Neutron"},
      {"question": "Which gas is essential for respiration?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Oxygen"},
      {"question": "What is the chemical formula of ammonia?", "options": ["NH3", "CH4", "H2O", "CO2"], "answer": "NH3"},
      {"question": "Which is the lightest element?", "options": ["Hydrogen", "Helium", "Oxygen", "Carbon"], "answer": "Hydrogen"},
      {"question": "What is the basic unit of an element?", "options": ["Atom", "Molecule", "Ion", "Electron"], "answer": "Atom"}
    ],
    "Medium": [
      {"question": "What is the valency of oxygen?", "options": ["1", "2", "3", "4"], "answer": "2"},
      {"question": "Which type of bond is formed by sharing of electrons?", "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "answer": "Covalent"},
      {"question": "What is the molecular formula of glucose?", "options": ["C6H12O6", "C2H5OH", "CH4", "CO2"], "answer": "C6H12O6"},
      {"question": "Which gas is released when an acid reacts with a metal?", "options": ["Hydrogen", "Oxygen", "Carbon Dioxide", "Nitrogen"], "answer": "Hydrogen"},
      {"question": "Which is an example of an ionic compound?", "options": ["NaCl", "H2O", "CH4", "CO2"], "answer": "NaCl"},
      {"question": "What is the electronic configuration of Sodium (Na)?", "options": ["2,8,1", "2,8,2", "2,6", "2,7,1"], "answer": "2,8,1"},
      {"question": "Which element is known as the 'King of Chemicals'?", "options": ["Sulfuric Acid", "Hydrochloric Acid", "Nitric Acid", "Acetic Acid"], "answer": "Sulfuric Acid"},
      {"question": "What is the oxidation state of Carbon in CO2?", "options": ["+4", "-4", "+2", "-2"], "answer": "+4"},
      {"question": "What is the shape of a methane molecule?", "options": ["Tetrahedral", "Linear", "Trigonal Planar", "Bent"], "answer": "Tetrahedral"},
      {"question": "What type of compound is CaCO3?", "options": ["Salt", "Acid", "Base", "Oxide"], "answer": "Salt"}
    ],
    "Hard": [
      {"question": "What is the hybridization of Carbon in ethene (C2H4)?", "options": ["sp2", "sp3", "sp", "sp3d"], "answer": "sp2"},
      {"question": "Which law states that 'mass is neither created nor destroyed'?", "options": ["Law of Conservation of Mass", "Law of Definite Proportion", "Boyle’s Law", "Avogadro’s Law"], "answer": "Law of Conservation of Mass"},
      {"question": "What is the geometry of BF3 molecule?", "options": ["Trigonal Planar", "Tetrahedral", "Linear", "Bent"], "answer": "Trigonal Planar"},
      {"question": "Which element has the highest electronegativity?", "options": ["Fluorine", "Oxygen", "Nitrogen", "Chlorine"], "answer": "Fluorine"},
      {"question": "What is the formula of the compound formed when aluminum reacts with oxygen?", "options": ["Al2O3", "AlO", "AlO2", "Al3O2"], "answer": "Al2O3"},
      {"question": "What is the shape of water molecule according to VSEPR theory?", "options": ["Bent", "Linear", "Trigonal Planar", "Tetrahedral"], "answer": "Bent"},
      {"question": "What is the order of increasing atomic size in the following: N, O, F?", "options": ["F < O < N", "N < O < F", "O < F < N", "F < N < O"], "answer": "F < O < N"},
      {"question": "What is the term for the energy required to remove an electron from an atom?", "options": ["Ionization Energy", "Electron Affinity", "Electronegativity", "Atomic Radius"], "answer": "Ionization Energy"},
      {"question": "What is the molar mass of CaCO3?", "options": ["100 g/mol", "50 g/mol", "200 g/mol", "150 g/mol"], "answer": "100 g/mol"},
      {"question": "Which of the following is a polar molecule?", "options": ["NH3", "CO2", "BF3", "CH4"], "answer": "NH3"}
    ]
  },
  "Biology": {
    "Easy": [
      {"question": "What is the basic unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "answer": "Cell"},
      {"question": "Which organelle is known as the powerhouse of the cell?", "options": ["Ribosome", "Mitochondria", "Nucleus", "Chloroplast"], "answer": "Mitochondria"},
      {"question": "What pigment is responsible for photosynthesis?", "options": ["Chlorophyll", "Carotene", "Xanthophyll", "Hemoglobin"], "answer": "Chlorophyll"},
      {"question": "Which blood group is called the universal donor?", "options": ["A", "B", "AB", "O"], "answer": "O"},
      {"question": "What is the process by which plants make their food?", "options": ["Respiration", "Photosynthesis", "Transpiration", "Digestion"], "answer": "Photosynthesis"},
      {"question": "What is the main component of the cell wall in plants?", "options": ["Cellulose", "Lignin", "Chitin", "Protein"], "answer": "Cellulose"},
      {"question": "Which part of the plant transports water?", "options": ["Phloem", "Xylem", "Stomata", "Root hair"], "answer": "Xylem"},
      {"question": "Which system controls hormones in the human body?", "options": ["Nervous system", "Circulatory system", "Endocrine system", "Digestive system"], "answer": "Endocrine system"},
      {"question": "Where does fertilization occur in human females?", "options": ["Uterus", "Ovary", "Fallopian tube", "Vagina"], "answer": "Fallopian tube"},
      {"question": "What is the genetic material in most living organisms?", "options": ["RNA", "Protein", "DNA", "Lipid"], "answer": "DNA"}
    ],
    "Medium": [
      {"question": "Who discovered the structure of DNA?", "options": ["Watson and Crick", "Gregor Mendel", "Charles Darwin", "Louis Pasteur"], "answer": "Watson and Crick"},
      {"question": "What is the term for the division of the cytoplasm during cell division?", "options": ["Mitosis", "Meiosis", "Cytokinesis", "Interphase"], "answer": "Cytokinesis"},
      {"question": "Which macromolecule is primarily responsible for storing genetic information?", "options": ["Carbohydrates", "Lipids", "Nucleic acids", "Proteins"], "answer": "Nucleic acids"},
      {"question": "Which blood cells help in fighting infections?", "options": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "White blood cells"},
      {"question": "What type of RNA carries amino acids to the ribosome?", "options": ["mRNA", "tRNA", "rRNA", "snRNA"], "answer": "tRNA"},
      {"question": "Which vitamin is produced by skin on exposure to sunlight?", "options": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
      {"question": "What is the name of the process in which green plants lose water vapor?", "options": ["Transpiration", "Photosynthesis", "Respiration", "Osmosis"], "answer": "Transpiration"},
      {"question": "Which organ in human body produces insulin?", "options": ["Liver", "Pancreas", "Kidney", "Spleen"], "answer": "Pancreas"},
      {"question": "What is the site of protein synthesis in a cell?", "options": ["Mitochondria", "Ribosome", "Nucleus", "Golgi apparatus"], "answer": "Ribosome"},
      {"question": "What is the function of hemoglobin?", "options": ["Transport oxygen", "Digest food", "Fight infection", "Produce hormones"], "answer": "Transport oxygen"}
    ],
    "Hard": [
      {"question": "Which phase of mitosis involves the alignment of chromosomes at the cell equator?", "options": ["Prophase", "Metaphase", "Anaphase", "Telophase"], "answer": "Metaphase"},
      {"question": "What is the name of the theory that explains the origin of eukaryotic cells?", "options": ["Endosymbiotic theory", "Cell theory", "Theory of evolution", "Germ theory"], "answer": "Endosymbiotic theory"},
      {"question": "Which enzyme is responsible for unwinding the DNA helix during replication?", "options": ["DNA polymerase", "Helicase", "Ligase", "Primase"], "answer": "Helicase"},
      {"question": "Which of the following is a heterotrophic mode of nutrition?", "options": ["Photosynthesis", "Chemosynthesis", "Parasitism", "Autotrophy"], "answer": "Parasitism"},
      {"question": "What is the term for programmed cell death?", "options": ["Necrosis", "Apoptosis", "Mitosis", "Meiosis"], "answer": "Apoptosis"},
      {"question": "Which pigment is found in red blood cells?", "options": ["Chlorophyll", "Hemoglobin", "Myoglobin", "Carotene"], "answer": "Hemoglobin"},
      {"question": "What is the functional unit of the kidney?", "options": ["Neuron", "Nephron", "Alveoli", "Osteon"], "answer": "Nephron"},
      {"question": "Which hormone regulates the sleep-wake cycle?", "options": ["Melatonin", "Insulin", "Adrenaline", "Thyroxine"], "answer": "Melatonin"},
      {"question": "In DNA, adenine pairs with which base?", "options": ["Thymine", "Cytosine", "Guanine", "Uracil"], "answer": "Thymine"},
      {"question": "Which process results in the formation of gametes?", "options": ["Mitosis", "Meiosis", "Binary fission", "Budding"], "answer": "Meiosis"}
    ]
  },
  "Accountancy": {
    "Easy": [
      {"question": "What is the accounting equation?", "options": ["Assets = Liabilities + Capital", "Assets = Capital - Liabilities", "Capital = Assets + Liabilities", "Assets = Liabilities - Capital"], "answer": "Assets = Liabilities + Capital"},
      {"question": "Which of the following is a tangible asset?", "options": ["Goodwill", "Trademark", "Building", "Patent"], "answer": "Building"},
      {"question": "What is the primary purpose of accounting?", "options": ["To calculate tax", "To maintain financial records", "To prepare budgets", "To audit companies"], "answer": "To maintain financial records"},
      {"question": "What does 'liability' represent in accounting?", "options": ["Owner’s claim", "Creditors’ claim", "Assets owned", "Profit earned"], "answer": "Creditors’ claim"},
      {"question": "Which financial statement shows the financial position of a business?", "options": ["Profit and Loss Account", "Balance Sheet", "Cash Flow Statement", "Trial Balance"], "answer": "Balance Sheet"},
      {"question": "What is the accounting period usually called?", "options": ["Financial year", "Calendar year", "Fiscal period", "Audit period"], "answer": "Financial year"},
      {"question": "What is capital?", "options": ["Owner’s investment in the business", "Borrowed funds", "Company’s income", "Expenses"], "answer": "Owner’s investment in the business"},
      {"question": "What is a journal in accounting?", "options": ["Book of original entry", "Final accounts", "Trial balance", "Ledger"], "answer": "Book of original entry"},
      {"question": "Which account type increases on the debit side?", "options": ["Liabilities", "Assets", "Capital", "Income"], "answer": "Assets"},
      {"question": "What does debit side in accounting signify?", "options": ["Expenses and Assets", "Income and Liabilities", "Capital and Income", "Liabilities and Expenses"], "answer": "Expenses and Assets"}
    ],
    "Medium": [
      {"question": "Which document is used to record cash transactions?", "options": ["Cash Book", "Journal", "Ledger", "Trial Balance"], "answer": "Cash Book"},
      {"question": "What is 'Trial Balance'?", "options": ["A statement showing final profit", "A list of ledger balances", "A financial statement", "A balance sheet"], "answer": "A list of ledger balances"},
      {"question": "What is meant by 'accrual basis' of accounting?", "options": ["Recording transactions when cash is received or paid", "Recording transactions when they occur", "Recording only cash transactions", "Recording only credit transactions"], "answer": "Recording transactions when they occur"},
      {"question": "What is a ledger in accounting?", "options": ["A book of final accounts", "A book containing journal entries", "A book showing account balances", "A list of creditors"], "answer": "A book showing account balances"},
      {"question": "Which of the following is a capital expenditure?", "options": ["Purchase of furniture", "Payment of electricity bill", "Salary paid", "Rent paid"], "answer": "Purchase of furniture"},
      {"question": "What is 'depreciation'?", "options": ["Increase in asset value", "Decrease in asset value", "Revenue income", "Owner’s capital"], "answer": "Decrease in asset value"},
      {"question": "What does a 'balance sheet' show?", "options": ["Revenue and expenses", "Assets and liabilities", "Cash inflows", "Profit earned"], "answer": "Assets and liabilities"},
      {"question": "What is a 'contra entry'?", "options": ["Entry in both cash and bank columns", "Entry in ledger only", "Entry in journal only", "Entry involving creditors"], "answer": "Entry in both cash and bank columns"},
      {"question": "Which account is credited when goods are sold on credit?", "options": ["Sales Account", "Purchases Account", "Debtors Account", "Cash Account"], "answer": "Sales Account"},
      {"question": "What is 'capital expenditure'?", "options": ["Expenditure on fixed assets", "Expenditure on day-to-day expenses", "Payment of salaries", "Payment of rent"], "answer": "Expenditure on fixed assets"}
    ],
    "Hard": [
      {"question": "Which concept assumes that a business will continue to operate indefinitely?", "options": ["Going concern", "Matching concept", "Accrual concept", "Conservatism"], "answer": "Going concern"},
      {"question": "What is the purpose of 'provision for doubtful debts'?", "options": ["To write off bad debts", "To estimate uncollectible debts", "To record sales", "To calculate profit"], "answer": "To estimate uncollectible debts"},
      {"question": "What is the meaning of 'double entry' system?", "options": ["Every transaction affects two accounts", "Every transaction is recorded once", "Transactions are recorded only in ledger", "Transactions are recorded only in cash book"], "answer": "Every transaction affects two accounts"},
      {"question": "What is 'consistency concept' in accounting?", "options": ["Using same accounting principles over time", "Changing methods frequently", "Ignoring expenses", "Ignoring revenues"], "answer": "Using same accounting principles over time"},
      {"question": "Which account is debited when machinery is purchased for cash?", "options": ["Machinery account", "Cash account", "Purchases account", "Capital account"], "answer": "Machinery account"},
      {"question": "What is the effect of purchase return on the purchase account?", "options": ["Increase", "Decrease", "No effect", "Depends on situation"], "answer": "Decrease"},
      {"question": "Which financial statement is prepared first?", "options": ["Balance Sheet", "Profit and Loss Account", "Trial Balance", "Cash Flow Statement"], "answer": "Profit and Loss Account"},
      {"question": "Which principle states that revenue and expenses must be matched?", "options": ["Matching principle", "Conservatism", "Going concern", "Historical cost"], "answer": "Matching principle"},
      {"question": "What is 'capital withdrawal'?", "options": ["Owner taking money from business", "Owner investing money in business", "Business borrowing money", "Business paying expenses"], "answer": "Owner taking money from business"},
      {"question": "Which account is credited when a debtor pays the amount owed?", "options": ["Debtors Account", "Cash Account", "Sales Account", "Purchases Account"], "answer": "Cash Account"}
    ]
  },
  "Business Studies": {
    "Easy": [
      {"question": "What is business?", "options": ["An economic activity", "A leisure activity", "A hobby", "A charity"], "answer": "An economic activity"},
      {"question": "Who is an entrepreneur?", "options": ["A person who starts a business", "A person who invests money in stocks", "A person who buys goods", "A government official"], "answer": "A person who starts a business"},
      {"question": "What is the primary objective of business?", "options": ["Profit earning", "Entertainment", "Social service", "Employment"], "answer": "Profit earning"},
      {"question": "Which of these is a service business?", "options": ["Banking", "Manufacturing", "Farming", "Mining"], "answer": "Banking"},
      {"question": "What does ‘trade’ mean?", "options": ["Buying and selling goods", "Manufacturing goods", "Advertising goods", "Consuming goods"], "answer": "Buying and selling goods"},
      {"question": "Which of the following is a factor of production?", "options": ["Capital", "Demand", "Price", "Profit"], "answer": "Capital"},
      {"question": "What is meant by ‘commerce’?", "options": ["All activities that facilitate trade", "Only buying goods", "Only selling goods", "Only manufacturing goods"], "answer": "All activities that facilitate trade"},
      {"question": "What is ‘industry’?", "options": ["Production of goods and services", "Buying goods", "Selling goods", "Advertising goods"], "answer": "Production of goods and services"},
      {"question": "Who regulates the business environment?", "options": ["Government", "Customers", "Employees", "Competitors"], "answer": "Government"},
      {"question": "What is a ‘producer’?", "options": ["Person who makes goods or services", "Person who sells goods", "Person who buys goods", "Person who manages business"], "answer": "Person who makes goods or services"}
    ],
    "Medium": [
      {"question": "What is ‘risk’ in business?", "options": ["Possibility of loss", "Profit earned", "Salary paid", "Goods produced"], "answer": "Possibility of loss"},
      {"question": "Which of the following is a characteristic of business?", "options": ["Economic activity", "Non-economic activity", "Leisure activity", "Hobby"], "answer": "Economic activity"},
      {"question": "What does ‘capital’ refer to in business?", "options": ["Money invested in business", "Goods produced", "Goods sold", "Profit earned"], "answer": "Money invested in business"},
      {"question": "What is ‘marketing’?", "options": ["Selling goods and services", "Manufacturing goods", "Buying goods", "Advertising only"], "answer": "Selling goods and services"},
      {"question": "Which of these is an example of ‘wholesale trade’?", "options": ["Selling goods in bulk to retailers", "Selling goods to customers", "Manufacturing goods", "Advertising goods"], "answer": "Selling goods in bulk to retailers"},
      {"question": "What is ‘business ethics’?", "options": ["Moral principles in business", "Business laws", "Profit earning methods", "Marketing techniques"], "answer": "Moral principles in business"},
      {"question": "What is ‘social responsibility’ of business?", "options": ["Obligation towards society", "Only profit earning", "Advertising products", "Selling goods"], "answer": "Obligation towards society"},
      {"question": "Which is a ‘secondary industry’?", "options": ["Manufacturing", "Agriculture", "Mining", "Fishing"], "answer": "Manufacturing"},
      {"question": "What is ‘capital market’?", "options": ["Market for long-term funds", "Market for daily goods", "Market for labor", "Market for raw materials"], "answer": "Market for long-term funds"},
      {"question": "Which form of business has unlimited liability?", "options": ["Sole proprietorship", "Private limited company", "Public limited company", "Partnership"], "answer": "Sole proprietorship"}
    ],
    "Hard": [
      {"question": "What is ‘limited liability’?", "options": ["Liability limited to amount invested", "Unlimited responsibility", "No responsibility", "Liability for others' debts"], "answer": "Liability limited to amount invested"},
      {"question": "Which document is required to start a partnership firm?", "options": ["Partnership deed", "Memorandum of Association", "Articles of Association", "Share certificate"], "answer": "Partnership deed"},
      {"question": "What is ‘joint stock company’?", "options": ["Company owned by shareholders", "Company owned by government", "Company owned by single person", "Company owned by employees"], "answer": "Company owned by shareholders"},
      {"question": "What is the meaning of ‘dividend’?", "options": ["Share of profits to shareholders", "Salary to employees", "Capital invested", "Loan taken"], "answer": "Share of profits to shareholders"},
      {"question": "Which body manages a public limited company?", "options": ["Board of Directors", "Government", "Shareholders", "Auditors"], "answer": "Board of Directors"},
      {"question": "What is ‘merger’ in business?", "options": ["Combination of two companies", "Selling goods", "Buying goods", "Manufacturing products"], "answer": "Combination of two companies"},
      {"question": "What is ‘franchise’?", "options": ["Right to use brand name", "Type of partnership", "Loan given to business", "Type of company"], "answer": "Right to use brand name"},
      {"question": "What is ‘working capital’?", "options": ["Capital for daily operations", "Capital invested in fixed assets", "Profit earned", "Loan taken"], "answer": "Capital for daily operations"},
      {"question": "What is ‘public enterprise’?", "options": ["Business owned by government", "Business owned by private individuals", "Partnership firm", "Sole proprietorship"], "answer": "Business owned by government"},
      {"question": "What is ‘business environment’?", "options": ["All external factors affecting business", "Only customers", "Only government policies", "Only employees"], "answer": "All external factors affecting business"}
    ]
  },
  "Economics": {
    "Easy": [
      {"question": "What is Economics?", "options": ["Study of production and consumption", "Study of plants", "Study of history", "Study of language"], "answer": "Study of production and consumption"},
      {"question": "What is a need?", "options": ["Basic requirement for survival", "Luxury item", "Non-essential item", "Toy"], "answer": "Basic requirement for survival"},
      {"question": "What does GDP stand for?", "options": ["Gross Domestic Product", "General Domestic Price", "Gross Domestic Profit", "General Demand Product"], "answer": "Gross Domestic Product"},
      {"question": "Who is a consumer?", "options": ["One who uses goods and services", "One who produces goods", "One who sells goods", "One who buys goods only"], "answer": "One who uses goods and services"},
      {"question": "What is ‘scarcity’?", "options": ["Limited availability of resources", "Unlimited resources", "Surplus goods", "Abundance of resources"], "answer": "Limited availability of resources"},
      {"question": "Which sector deals with farming?", "options": ["Primary sector", "Secondary sector", "Tertiary sector", "Quaternary sector"], "answer": "Primary sector"},
      {"question": "What is ‘demand’?", "options": ["Willingness and ability to buy", "Willingness to sell", "Ability to produce", "Ability to save money"], "answer": "Willingness and ability to buy"},
      {"question": "What is ‘supply’?", "options": ["Quantity of goods available for sale", "Quantity of goods demanded", "Price of goods", "Cost of goods"], "answer": "Quantity of goods available for sale"},
      {"question": "What is a ‘producer’?", "options": ["Person who makes goods or services", "Person who buys goods", "Person who sells goods", "Person who uses goods"], "answer": "Person who makes goods or services"},
      {"question": "What is a ‘market’?", "options": ["Place where buyers and sellers meet", "Place where goods are produced", "Place where goods are stored", "Place where goods are discarded"], "answer": "Place where buyers and sellers meet"}
    ],
    "Medium": [
      {"question": "What is ‘opportunity cost’?", "options": ["Next best alternative foregone", "Total cost of production", "Cost of machinery", "Price of goods"], "answer": "Next best alternative foregone"},
      {"question": "What does ‘elasticity of demand’ measure?", "options": ["Responsiveness of demand to price change", "Total demand", "Supply of goods", "Price of goods"], "answer": "Responsiveness of demand to price change"},
      {"question": "Which institution regulates money supply in India?", "options": ["Reserve Bank of India", "State Bank of India", "Ministry of Finance", "Income Tax Department"], "answer": "Reserve Bank of India"},
      {"question": "What is ‘public distribution system’?", "options": ["System to provide essential goods at subsidized rates", "Private business system", "Online shopping system", "Export system"], "answer": "System to provide essential goods at subsidized rates"},
      {"question": "Which sector includes manufacturing industries?", "options": ["Secondary sector", "Primary sector", "Tertiary sector", "Quaternary sector"], "answer": "Secondary sector"},
      {"question": "What is ‘per capita income’?", "options": ["Average income per person", "Total income of a country", "Income of government", "Income of companies"], "answer": "Average income per person"},
      {"question": "What is ‘money’?", "options": ["Medium of exchange", "Goods and services", "Bank deposit", "Wealth"], "answer": "Medium of exchange"},
      {"question": "Which of the following is a direct tax?", "options": ["Income tax", "GST", "Excise duty", "Custom duty"], "answer": "Income tax"},
      {"question": "What is the function of ‘demand curve’?", "options": ["Shows relationship between price and quantity demanded", "Shows total production", "Shows supply details", "Shows consumer preferences"], "answer": "Shows relationship between price and quantity demanded"},
      {"question": "Which is an example of ‘tertiary sector’?", "options": ["Banking", "Farming", "Manufacturing", "Mining"], "answer": "Banking"}
    ],
    "Hard": [
      {"question": "What is ‘GDP deflator’?", "options": ["Measure of price level", "Measure of GDP growth", "Measure of income", "Measure of demand"], "answer": "Measure of price level"},
      {"question": "What is ‘market equilibrium’?", "options": ["Point where demand equals supply", "Maximum price", "Minimum price", "Government fixed price"], "answer": "Point where demand equals supply"},
      {"question": "What is ‘inflation’?", "options": ["Rise in general price level", "Fall in prices", "Stable prices", "Government subsidy"], "answer": "Rise in general price level"},
      {"question": "What is ‘budget deficit’?", "options": ["Expenditure exceeds revenue", "Revenue exceeds expenditure", "Balanced budget", "Government saving"], "answer": "Expenditure exceeds revenue"},
      {"question": "What is ‘monetary policy’?", "options": ["Control of money supply by RBI", "Government budget plan", "Tax policy", "Trade policy"], "answer": "Control of money supply by RBI"},
      {"question": "What is the ‘Human Development Index’ (HDI)?", "options": ["Composite index of health, education, and income", "Measure of GDP only", "Measure of poverty", "Measure of inflation"], "answer": "Composite index of health, education, and income"},
      {"question": "What is ‘aggregate demand’?", "options": ["Total demand in the economy", "Demand of a single product", "Demand for exports", "Demand for imports"], "answer": "Total demand in the economy"},
      {"question": "What is the meaning of ‘fiscal policy’?", "options": ["Government’s policy on taxation and spending", "Policy on money supply", "Trade policy", "Price control"], "answer": "Government’s policy on taxation and spending"},
      {"question": "Which of these is a non-renewable resource?", "options": ["Coal", "Solar energy", "Wind energy", "Water"], "answer": "Coal"},
      {"question": "What is ‘Human Capital’?", "options": ["Skills and abilities of people", "Natural resources", "Physical capital", "Money invested"], "answer": "Skills and abilities of people"}
    ]
  },
  "History": {
    "Easy": [
      {"question": "Who was the founder of the Maurya Empire?", "options": ["Chandragupta Maurya", "Ashoka", "Bindusara", "Harshavardhana"], "answer": "Chandragupta Maurya"},
      {"question": "Which ancient Indian text is known as the 'Book of Knowledge'?", "options": ["Vedas", "Upanishads", "Mahabharata", "Ramayana"], "answer": "Vedas"},
      {"question": "Which city was the capital of the Gupta Empire?", "options": ["Pataliputra", "Taxila", "Ujjain", "Kannauj"], "answer": "Pataliputra"},
      {"question": "Who was the last ruler of the Mughal Empire?", "options": ["Bahadur Shah Zafar", "Aurangzeb", "Shah Jahan", "Akbar"], "answer": "Bahadur Shah Zafar"},
      {"question": "Which empire is famous for its rock-cut caves at Ajanta?", "options": ["Satavahana", "Gupta", "Maurya", "Chola"], "answer": "Satavahana"},
      {"question": "The Harappan civilization is also known as?", "options": ["Indus Valley Civilization", "Mesopotamian Civilization", "Egyptian Civilization", "Mayan Civilization"], "answer": "Indus Valley Civilization"},
      {"question": "The Battle of Plassey was fought in which year?", "options": ["1757", "1764", "1857", "1776"], "answer": "1757"},
      {"question": "Who wrote the book 'Arthashastra'?", "options": ["Chanakya", "Kautilya", "Megasthenes", "Brahmagupta"], "answer": "Chanakya"},
      {"question": "Which river was important for the Harappan Civilization?", "options": ["Indus", "Ganga", "Yamuna", "Brahmaputra"], "answer": "Indus"},
      {"question": "The Qutub Minar is located in which city?", "options": ["Delhi", "Agra", "Jaipur", "Lucknow"], "answer": "Delhi"}
    ],
    "Medium": [
      {"question": "Who was the ruler during the peak of the Gupta Empire?", "options": ["Chandragupta I", "Samudragupta", "Skandagupta", "Harsha"], "answer": "Samudragupta"},
      {"question": "The Arthashastra deals mainly with?", "options": ["Politics and administration", "Religion", "Philosophy", "Astronomy"], "answer": "Politics and administration"},
      {"question": "Which was the main language of administration during the Mauryan Empire?", "options": ["Prakrit", "Sanskrit", "Persian", "Greek"], "answer": "Prakrit"},
      {"question": "Who was the founder of the Chola dynasty?", "options": ["Vijayalaya", "Raja Raja Chola", "Karikala", "Rajendra Chola"], "answer": "Vijayalaya"},
      {"question": "The temple at Brihadeshwara was built by which Chola ruler?", "options": ["Raja Raja Chola I", "Rajendra Chola I", "Vijayalaya", "Karikala"], "answer": "Raja Raja Chola I"},
      {"question": "Which Mughal emperor built the Taj Mahal?", "options": ["Shah Jahan", "Akbar", "Aurangzeb", "Humayun"], "answer": "Shah Jahan"},
      {"question": "The Bhakti movement was mainly associated with?", "options": ["Devotion to God", "Political reforms", "Trade expansion", "Scientific progress"], "answer": "Devotion to God"},
      {"question": "Which European traveler wrote about the Indian king 'Chandra Gupta'?", "options": ["Megasthenes", "Marco Polo", "Ibn Battuta", "Vasco da Gama"], "answer": "Megasthenes"},
      {"question": "The Indus Valley Civilization is known for?", "options": ["Urban planning", "Nomadic lifestyle", "Tribal warfare", "Agrarian society"], "answer": "Urban planning"},
      {"question": "Who was the prominent ruler of the Vijayanagara Empire?", "options": ["Krishnadevaraya", "Harihara", "Deva Raya", "Bukkaraya"], "answer": "Krishnadevaraya"}
    ],
    "Hard": [
      {"question": "What was the main purpose of the Ashokan edicts?", "options": ["To spread Dharma and moral law", "To announce war", "To collect taxes", "To establish trade routes"], "answer": "To spread Dharma and moral law"},
      {"question": "The Gupta period is often called the 'Golden Age' because of?", "options": ["Advances in art, science and literature", "Military conquest", "Trade expansion", "Religious reforms"], "answer": "Advances in art, science and literature"},
      {"question": "Who were the Sangam poets?", "options": ["Ancient Tamil poets", "Sanskrit poets", "Persian poets", "Arabic poets"], "answer": "Ancient Tamil poets"},
      {"question": "Which dynasty controlled the Deccan region during the 6th century?", "options": ["Chalukyas", "Guptas", "Mughals", "Mauryas"], "answer": "Chalukyas"},
      {"question": "The main source of information about the Harappan Civilization comes from?", "options": ["Archaeological excavations", "Ancient texts", "Foreign travelers' accounts", "Oral traditions"], "answer": "Archaeological excavations"},
      {"question": "The Vijayanagara Empire was established to resist which invading power?", "options": ["Delhi Sultanate", "Mughals", "Portuguese", "British"], "answer": "Delhi Sultanate"},
      {"question": "What was the role of 'Nagarams' in South Indian society?", "options": ["Urban settlements", "Religious institutions", "Military camps", "Trade centers"], "answer": "Urban settlements"},
      {"question": "The Battle of Panipat (1526) marked the beginning of which empire?", "options": ["Mughal Empire", "Maratha Empire", "Delhi Sultanate", "British Empire"], "answer": "Mughal Empire"},
      {"question": "Who was the author of the 'Rajatarangini'?", "options": ["Kalhana", "Banabhatta", "Vishnu Sharma", "Bhasa"], "answer": "Kalhana"},
      {"question": "Which Sultan introduced the 'Iqta' system in India?", "options": ["Iltutmish", "Alauddin Khilji", "Muhammad bin Tughlaq", "Balban"], "answer": "Iltutmish"}
    ]
  },
  "Political Science": {
    "Easy": [
      {"question": "What is the primary function of the Constitution?", "options": ["To lay down the rules of government", "To collect taxes", "To declare war", "To organize sports"], "answer": "To lay down the rules of government"},
      {"question": "Which part of the Indian Constitution deals with Fundamental Rights?", "options": ["Part III", "Part I", "Part II", "Part IV"], "answer": "Part III"},
      {"question": "Who was the Chairman of the Drafting Committee of the Indian Constitution?", "options": ["Dr. B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel"], "answer": "Dr. B.R. Ambedkar"},
      {"question": "How many Fundamental Rights are there in the Indian Constitution?", "options": ["6", "5", "7", "4"], "answer": "6"},
      {"question": "The President of India is elected by?", "options": ["Electoral College", "Direct voting by people", "Prime Minister", "Supreme Court"], "answer": "Electoral College"},
      {"question": "Which body is responsible for making laws in India?", "options": ["Parliament", "Supreme Court", "President", "Election Commission"], "answer": "Parliament"},
      {"question": "What is the term of Lok Sabha?", "options": ["5 years", "6 years", "4 years", "3 years"], "answer": "5 years"},
      {"question": "Who appoints the Prime Minister of India?", "options": ["President", "Chief Justice", "Lok Sabha Speaker", "Home Minister"], "answer": "President"},
      {"question": "Which article of the Constitution provides for the Right to Equality?", "options": ["Article 14", "Article 19", "Article 21", "Article 32"], "answer": "Article 14"},
      {"question": "The Directive Principles of State Policy are found in which Part of the Constitution?", "options": ["Part IV", "Part III", "Part II", "Part I"], "answer": "Part IV"}
    ],
    "Medium": [
      {"question": "What is the minimum age required to become the President of India?", "options": ["35 years", "30 years", "25 years", "40 years"], "answer": "35 years"},
      {"question": "The system of government in India is?", "options": ["Parliamentary", "Presidential", "Monarchy", "Dictatorship"], "answer": "Parliamentary"},
      {"question": "Which article of the Constitution deals with the emergency provisions?", "options": ["Article 352", "Article 370", "Article 19", "Article 21"], "answer": "Article 352"},
      {"question": "Who can dissolve the Lok Sabha?", "options": ["President", "Prime Minister", "Supreme Court", "Speaker"], "answer": "President"},
      {"question": "The Rajya Sabha is also called?", "options": ["Council of States", "House of People", "Legislative Assembly", "Parliament"], "answer": "Council of States"},
      {"question": "Which of the following is NOT a Fundamental Right?", "options": ["Right to Property", "Right to Freedom", "Right to Equality", "Right to Constitutional Remedies"], "answer": "Right to Property"},
      {"question": "The Indian Constitution is adopted on which date?", "options": ["26th January 1950", "15th August 1947", "26th November 1949", "15th January 1950"], "answer": "26th January 1950"},
      {"question": "Who is the head of the Union Judiciary in India?", "options": ["Chief Justice of India", "Attorney General", "President", "Prime Minister"], "answer": "Chief Justice of India"},
      {"question": "What does 'bicameral legislature' mean?", "options": ["Two houses", "Single house", "Three houses", "Four houses"], "answer": "Two houses"},
      {"question": "Which Article guarantees Freedom of Speech and Expression?", "options": ["Article 19", "Article 21", "Article 14", "Article 15"], "answer": "Article 19"}
    ],
    "Hard": [
      {"question": "Which article of the Indian Constitution provides for the amendment procedure?", "options": ["Article 368", "Article 370", "Article 352", "Article 356"], "answer": "Article 368"},
      {"question": "The basic structure doctrine was propounded in which case?", "options": ["Kesavananda Bharati Case", "Golaknath Case", "Maneka Gandhi Case", "Minerva Mills Case"], "answer": "Kesavananda Bharati Case"},
      {"question": "Which constitutional amendment introduced the Goods and Services Tax (GST)?", "options": ["101st Amendment", "42nd Amendment", "44th Amendment", "73rd Amendment"], "answer": "101st Amendment"},
      {"question": "The impeachment of the President of India is governed by which article?", "options": ["Article 61", "Article 56", "Article 58", "Article 62"], "answer": "Article 61"},
      {"question": "Which of the following is NOT a feature of the Indian Constitution?", "options": ["Unitary in nature", "Federal in nature", "Parliamentary system", "Secular state"], "answer": "Unitary in nature"},
      {"question": "The Sarkaria Commission dealt with which issue?", "options": ["Centre-State Relations", "Judicial reforms", "Election reforms", "Economic reforms"], "answer": "Centre-State Relations"},
      {"question": "Which Article provides for the establishment of the Finance Commission?", "options": ["Article 280", "Article 300", "Article 275", "Article 256"], "answer": "Article 280"},
      {"question": "The Rajya Sabha members are elected for a term of?", "options": ["6 years", "5 years", "4 years", "3 years"], "answer": "6 years"},
      {"question": "Who has the power to appoint the Governor of a state?", "options": ["President of India", "Prime Minister", "Chief Minister", "Chief Justice of the State High Court"], "answer": "President of India"},
      {"question": "Which Article deals with the suspension of Fundamental Rights during an emergency?", "options": ["Article 358", "Article 352", "Article 360", "Article 370"], "answer": "Article 358"}
    ]
  },
  "Geography": {
    "Easy": [
      {"question": "Which is the closest planet to Earth?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Venus"},
      {"question": "Which layer of the Earth lies just below the crust?", "options": ["Mantle", "Core", "Lithosphere", "Asthenosphere"], "answer": "Mantle"},
      {"question": "What is the shape of the Earth?", "options": ["Geoid", "Circle", "Flat", "Cone"], "answer": "Geoid"},
      {"question": "Which gas is most abundant in the Earth's atmosphere?", "options": ["Nitrogen", "Oxygen", "Carbon dioxide", "Hydrogen"], "answer": "Nitrogen"},
      {"question": "Which is the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": "Nile"},
      {"question": "Which imaginary line divides the Earth into the Northern and Southern Hemisphere?", "options": ["Equator", "Prime Meridian", "Tropic of Cancer", "Arctic Circle"], "answer": "Equator"},
      {"question": "Which landform is formed by river deposition?", "options": ["Delta", "Valley", "Plateau", "Hill"], "answer": "Delta"},
      {"question": "Which instrument is used to measure earthquakes?", "options": ["Seismograph", "Barometer", "Thermometer", "Anemometer"], "answer": "Seismograph"},
      {"question": "What is the study of weather called?", "options": ["Meteorology", "Geology", "Climatology", "Astronomy"], "answer": "Meteorology"},
      {"question": "Which is the largest continent in the world?", "options": ["Asia", "Africa", "Europe", "North America"], "answer": "Asia"}
    ],
    "Medium": [
      {"question": "The theory of plate tectonics explains the movement of?", "options": ["Lithospheric plates", "Ocean currents", "Air masses", "Tides"], "answer": "Lithospheric plates"},
      {"question": "Which rock is formed from molten magma?", "options": ["Igneous", "Sedimentary", "Metamorphic", "Fossil"], "answer": "Igneous"},
      {"question": "Which type of rainfall occurs due to mountains?", "options": ["Orographic rainfall", "Convectional rainfall", "Cyclonic rainfall", "Monsoon rainfall"], "answer": "Orographic rainfall"},
      {"question": "Which current is a cold ocean current?", "options": ["Humboldt Current", "Gulf Stream", "Kuroshio Current", "Agulhas Current"], "answer": "Humboldt Current"},
      {"question": "Which layer of the atmosphere contains the ozone layer?", "options": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"], "answer": "Stratosphere"},
      {"question": "Which scale measures the intensity of earthquakes?", "options": ["Richter Scale", "Beaufort Scale", "Mercalli Scale", "Mohs Scale"], "answer": "Richter Scale"},
      {"question": "The Earth rotates from?", "options": ["West to East", "East to West", "North to South", "South to North"], "answer": "West to East"},
      {"question": "The Tropic of Cancer passes through which Indian state?", "options": ["Rajasthan", "Gujarat", "Kerala", "Punjab"], "answer": "Gujarat"},
      {"question": "Which part of the Earth is called the 'core'?", "options": ["Innermost layer", "Outer crust", "Mantle", "Hydrosphere"], "answer": "Innermost layer"},
      {"question": "Weathering is the process of?", "options": ["Breaking down rocks", "Moving tectonic plates", "Volcano formation", "Cloud formation"], "answer": "Breaking down rocks"}
    ],
    "Hard": [
      {"question": "Which scientist proposed the Continental Drift Theory?", "options": ["Alfred Wegener", "Darwin", "Newton", "Galileo"], "answer": "Alfred Wegener"},
      {"question": "Which type of rock is formed due to intense heat and pressure?", "options": ["Metamorphic", "Igneous", "Sedimentary", "Volcanic"], "answer": "Metamorphic"},
      {"question": "The Pacific Ring of Fire is associated with?", "options": ["Earthquakes and Volcanoes", "Tornadoes", "Cyclones", "Floods"], "answer": "Earthquakes and Volcanoes"},
      {"question": "The vertical rays of the Sun are received between which latitudes?", "options": ["Tropic of Cancer and Tropic of Capricorn", "Equator and Arctic Circle", "Tropic of Cancer and Arctic Circle", "Equator and Antarctic Circle"], "answer": "Tropic of Cancer and Tropic of Capricorn"},
      {"question": "Which factor does NOT influence the distribution of temperature?", "options": ["Soil color", "Latitude", "Altitude", "Ocean currents"], "answer": "Soil color"},
      {"question": "Which layer of the atmosphere has the highest temperature?", "options": ["Thermosphere", "Troposphere", "Stratosphere", "Mesosphere"], "answer": "Thermosphere"},
      {"question": "What is the name of the boundary between the crust and the mantle?", "options": ["Mohorovicic Discontinuity", "Gutenberg Discontinuity", "Convection Zone", "Asthenosphere"], "answer": "Mohorovicic Discontinuity"},
      {"question": "Which movement causes the folding of Earth's crust?", "options": ["Endogenic forces", "Exogenic forces", "Plate cooling", "River erosion"], "answer": "Endogenic forces"},
      {"question": "Which type of volcano erupts frequently but mildly?", "options": ["Shield volcano", "Composite volcano", "Cinder cone", "Caldera"], "answer": "Shield volcano"},
      {"question": "What is the average salinity of ocean water?", "options": ["35 parts per thousand", "50 parts per thousand", "15 parts per thousand", "10 parts per thousand"], "answer": "35 parts per thousand"}
    ]
  },
  "IP": {
    "Easy": [
      {"question": "Which of the following is an input device?", "options": ["Keyboard", "Monitor", "Speaker", "Printer"], "answer": "Keyboard"},
      {"question": "Which of the following is a valid variable name in Python?", "options": ["my_name", "1name", "my-name", "my name"], "answer": "my_name"},
      {"question": "Which of these is a Python data type?", "options": ["int", "char", "byte", "double"], "answer": "int"},
      {"question": "What is the output of: print(2 + 3 * 4)?", "options": ["14", "20", "24", "18"], "answer": "14"},
      {"question": "Which of these is used to take input in Python?", "options": ["input()", "scan()", "get()", "cin"], "answer": "input()"},
      {"question": "Which keyword is used for defining a function in Python?", "options": ["def", "func", "define", "function"], "answer": "def"},
      {"question": "What does RAM stand for?", "options": ["Random Access Memory", "Read Access Memory", "Run Access Machine", "None of these"], "answer": "Random Access Memory"},
      {"question": "Which of the following is NOT a programming language?", "options": ["Python", "HTML", "Java", "C++"], "answer": "HTML"},
      {"question": "Which function is used to find length of a list in Python?", "options": ["len()", "length()", "size()", "count()"], "answer": "len()"},
      {"question": "Which of the following is a logical operator in Python?", "options": ["and", "plus", "not equal", "mod"], "answer": "and"}
    ],
    "Medium": [
      {"question": "Which symbol is used for comments in Python?", "options": ["#", "//", "/*", "--"], "answer": "#"},
      {"question": "Which Python function converts a string to an integer?", "options": ["int()", "str()", "float()", "chr()"], "answer": "int()"},
      {"question": "What is the result of: len('Information')?", "options": ["11", "12", "10", "13"], "answer": "11"},
      {"question": "Which loop runs at least once even if the condition is false in other languages (not Python)?", "options": ["do-while", "for", "while", "none"], "answer": "do-while"},
      {"question": "In Python, a list is enclosed within?", "options": ["[ ]", "{ }", "( )", "< >"], "answer": "[ ]"},
      {"question": "What is the index of 'b' in the string 'abc'?", "options": ["1", "2", "0", "-1"], "answer": "1"},
      {"question": "Which of the following is a Python keyword?", "options": ["elif", "define", "integer", "loop"], "answer": "elif"},
      {"question": "Which of the following is used to represent missing values in a DataFrame?", "options": ["NaN", "None", "Zero", "Null"], "answer": "NaN"},
      {"question": "Which method is used to read a CSV file in Pandas?", "options": ["read_csv()", "load_csv()", "open_csv()", "get_csv()"], "answer": "read_csv()"},
      {"question": "Which of these is used to import Pandas in Python?", "options": ["import pandas as pd", "include pandas", "load pandas", "import panda"], "answer": "import pandas as pd"}
    ],
    "Hard": [
      {"question": "Which function is used to get the first 5 rows of a DataFrame?", "options": ["head()", "top()", "first()", "start()"], "answer": "head()"},
      {"question": "Which function is used to find missing values in Pandas?", "options": ["isnull()", "missing()", "checknull()", "null()"], "answer": "isnull()"},
      {"question": "Which data structure is used for labelled 1D data in Pandas?", "options": ["Series", "List", "Tuple", "Array"], "answer": "Series"},
      {"question": "Which command displays the structure of a DataFrame?", "options": ["info()", "describe()", "structure()", "shape()"], "answer": "info()"},
      {"question": "Which method is used to combine two DataFrames by rows?", "options": ["concat()", "merge()", "append()", "join()"], "answer": "concat()"},
      {"question": "Which operator is used for exponentiation in Python?", "options": ["**", "^", "^^", "//"], "answer": "**"},
      {"question": "What does CSV stand for?", "options": ["Comma Separated Values", "Code Storage Version", "Character Separated Values", "Central Storage Volume"], "answer": "Comma Separated Values"},
      {"question": "Which function returns summary statistics of numerical columns?", "options": ["describe()", "summary()", "stats()", "details()"], "answer": "describe()"},
      {"question": "Which Python library is used for data visualization?", "options": ["Matplotlib", "NumPy", "Seaborn", "Pandas"], "answer": "Matplotlib"},
      {"question": "What is the extension of Python files?", "options": [".py", ".pt", ".p", ".python"], "answer": ".py"}
    ]
  },
  "Physical Education": {
    "Easy": [
      {"question": "What is the full form of BMI?", "options": ["Body Mass Index", "Body Muscle Index", "Body Movement Indicator", "Basic Mass Index"], "answer": "Body Mass Index"},
      {"question": "Which component is related to the ability of the heart and lungs to supply oxygen?", "options": ["Cardiovascular Endurance", "Muscular Strength", "Flexibility", "Agility"], "answer": "Cardiovascular Endurance"},
      {"question": "Which vitamin is also called the sunshine vitamin?", "options": ["Vitamin D", "Vitamin C", "Vitamin A", "Vitamin B12"], "answer": "Vitamin D"},
      {"question": "Which mineral is important for strong bones?", "options": ["Calcium", "Iron", "Zinc", "Iodine"], "answer": "Calcium"},
      {"question": "Yoga originated in which country?", "options": ["India", "China", "Greece", "Japan"], "answer": "India"},
      {"question": "Which asana is best for improving concentration?", "options": ["Vrikshasana", "Bhujangasana", "Savasana", "Paschimottanasana"], "answer": "Vrikshasana"},
      {"question": "What is the normal blood pressure level?", "options": ["120/80 mmHg", "100/60 mmHg", "130/90 mmHg", "110/70 mmHg"], "answer": "120/80 mmHg"},
      {"question": "The capacity to do work is called?", "options": ["Energy", "Power", "Speed", "Strength"], "answer": "Energy"},
      {"question": "Which nutrient is the main source of energy?", "options": ["Carbohydrates", "Proteins", "Vitamins", "Fats"], "answer": "Carbohydrates"},
      {"question": "The ability to move joints easily is called?", "options": ["Flexibility", "Endurance", "Speed", "Agility"], "answer": "Flexibility"}
    ],
    "Medium": [
      {"question": "Which test is used to measure agility?", "options": ["Illinois Agility Test", "Sit and Reach", "Push-up Test", "Beep Test"], "answer": "Illinois Agility Test"},
      {"question": "Which component of fitness is measured by 'Sit and Reach' test?", "options": ["Flexibility", "Speed", "Strength", "Coordination"], "answer": "Flexibility"},
      {"question": "Which disorder is caused due to deficiency of calcium?", "options": ["Osteoporosis", "Scurvy", "Rickets", "Goiter"], "answer": "Osteoporosis"},
      {"question": "Which method is best for measuring height?", "options": ["Stadiometer", "Tape", "Scale", "Balance"], "answer": "Stadiometer"},
      {"question": "Which asana is helpful in relieving stress?", "options": ["Savasana", "Tadasana", "Vajrasana", "Halasana"], "answer": "Savasana"},
      {"question": "What does the term 'warming up' refer to?", "options": ["Light exercise before main workout", "Final sprint", "Rest after exercise", "Stretching during sleep"], "answer": "Light exercise before main workout"},
      {"question": "Which component improves by long-distance running?", "options": ["Cardiovascular Endurance", "Strength", "Flexibility", "Speed"], "answer": "Cardiovascular Endurance"},
      {"question": "Which nutrient is known as body-building food?", "options": ["Proteins", "Fats", "Vitamins", "Carbohydrates"], "answer": "Proteins"},
      {"question": "What is the term for the ability to quickly change direction?", "options": ["Agility", "Balance", "Coordination", "Reaction time"], "answer": "Agility"},
      {"question": "In yoga, which posture is called the Cobra Pose?", "options": ["Bhujangasana", "Tadasana", "Dhanurasana", "Halasana"], "answer": "Bhujangasana"}
    ],
    "Hard": [
      {"question": "Which law of learning states that practice leads to improvement?", "options": ["Law of Exercise", "Law of Readiness", "Law of Effect", "Law of Repetition"], "answer": "Law of Exercise"},
      {"question": "Which vitamin deficiency causes night blindness?", "options": ["Vitamin A", "Vitamin D", "Vitamin C", "Vitamin B12"], "answer": "Vitamin A"},
      {"question": "Which test measures cardiovascular fitness in children?", "options": ["Harvard Step Test", "Beep Test", "Sit and Reach", "Cooper Test"], "answer": "Beep Test"},
      {"question": "Which component is tested by the 'Standing Broad Jump'?", "options": ["Explosive leg strength", "Agility", "Flexibility", "Cardio endurance"], "answer": "Explosive leg strength"},
      {"question": "What is the main cause of postural deformities?", "options": ["Improper posture", "Excess calcium", "Regular exercise", "Genetics only"], "answer": "Improper posture"},
      {"question": "Which asana helps improve digestion?", "options": ["Pavanamuktasana", "Tadasana", "Bhujangasana", "Vrikshasana"], "answer": "Pavanamuktasana"},
      {"question": "Flat foot is a type of?", "options": ["Postural deformity", "Nutrient deficiency", "Fitness component", "Exercise method"], "answer": "Postural deformity"},
      {"question": "Which factor affects physical fitness the most?", "options": ["Lifestyle", "Language", "Religion", "Color"], "answer": "Lifestyle"},
      {"question": "What is the recommended intake of water per day for an average adult?", "options": ["2 to 3 litres", "5 litres", "1 litre", "10 litres"], "answer": "2 to 3 litres"},
      {"question": "What is the term for rapid heartbeat?", "options": ["Tachycardia", "Bradycardia", "Cardiofitness", "Hypertension"], "answer": "Tachycardia"}
    ]
  }
},
"12": {
  "English": {
    "Easy": [
      {"question": "Who is the author of 'The Last Lesson'?", "options": ["Alphonse Daudet", "M. Hamel", "Franz", "Douglas"], "answer": "Alphonse Daudet"},
      {"question": "What is the central theme of 'My Mother at Sixty-six'?", "options": ["Aging and mortality", "Childhood memories", "Nature's beauty", "Separation"], "answer": "Aging and mortality"},
      {"question": "In 'Lost Spring', what does Anees Jung talk about?", "options": ["Child labor and poverty", "Education", "Festivals", "Love and family"], "answer": "Child labor and poverty"},
      {"question": "What does the poem 'Keeping Quiet' emphasize?", "options": ["Peace and introspection", "War", "Revenge", "Love"], "answer": "Peace and introspection"},
      {"question": "What is Kamala Das afraid of in 'My Mother at Sixty-six'?", "options": ["Losing her mother", "Traffic", "Aging", "Being alone"], "answer": "Losing her mother"},
      {"question": "Who wrote the poem 'A Thing of Beauty'?", "options": ["John Keats", "Robert Frost", "Pablo Neruda", "William Blake"], "answer": "John Keats"},
      {"question": "Where is Coorg located?", "options": ["Karnataka", "Kerala", "Tamil Nadu", "Goa"], "answer": "Karnataka"},
      {"question": "Who is the protagonist in 'Deep Water'?", "options": ["William Douglas", "Franz", "M. Hamel", "Valli"], "answer": "William Douglas"},
      {"question": "Which subject was most dear to M. Hamel?", "options": ["French", "English", "History", "Science"], "answer": "French"},
      {"question": "Who wrote 'The Rattrap'?", "options": ["Selma Lagerlöf", "John Keats", "Alphonse Daudet", "Zitkala-Sa"], "answer": "Selma Lagerlöf"}
    ],
    "Medium": [
      {"question": "In 'The Rattrap', what did the peddler believe about the world?", "options": ["It is a big rattrap", "It is heaven", "It is a journey", "It is peaceful"], "answer": "It is a big rattrap"},
      {"question": "In 'Indigo', what did Gandhi prove?", "options": ["The power of non-violence", "The power of money", "The need for war", "The importance of science"], "answer": "The power of non-violence"},
      {"question": "In 'Aunt Jennifer's Tigers', what do the tigers symbolize?", "options": ["Freedom and strength", "Fear", "Family", "Money"], "answer": "Freedom and strength"},
      {"question": "In 'Poets and Pancakes', which studio is mentioned?", "options": ["Gemini Studios", "R.K. Studios", "Filmistan", "Annapurna Studio"], "answer": "Gemini Studios"},
      {"question": "What does the poem 'An Elementary School Classroom in a Slum' highlight?", "options": ["Inequality in education", "Sports", "Discipline", "Technology"], "answer": "Inequality in education"},
      {"question": "Who is the author of 'The Third Level'?", "options": ["Jack Finney", "Shirley Toulson", "Stephen Leacock", "William Wordsworth"], "answer": "Jack Finney"},
      {"question": "In 'On the Face of It', Derry suffers from?", "options": ["Acid burn", "Paralysis", "Blindness", "Deafness"], "answer": "Acid burn"},
      {"question": "Who was Rajkumar Shukla?", "options": ["A poor sharecropper", "A British officer", "A lawyer", "A teacher"], "answer": "A poor sharecropper"},
      {"question": "What did the peddler steal in 'The Rattrap'?", "options": ["Thirty kronor", "Food", "Shoes", "Gold"], "answer": "Thirty kronor"},
      {"question": "Who helps Douglas overcome his fear in 'Deep Water'?", "options": ["A swimming instructor", "His father", "His friend", "His teacher"], "answer": "A swimming instructor"}
    ],
    "Hard": [
      {"question": "In 'The Enemy', what does Dr. Sadao finally do with the American prisoner?", "options": ["Helps him escape", "Hands him to police", "Kills him", "Keeps him"], "answer": "Helps him escape"},
      {"question": "What theme does 'Should Wizard Hit Mommy?' explore?", "options": ["Parenting vs fantasy", "Science", "Courage", "Politics"], "answer": "Parenting vs fantasy"},
      {"question": "What does the poem 'A Roadside Stand' criticize?", "options": ["Neglect of rural people", "Urban beauty", "Weather", "Modern technology"], "answer": "Neglect of rural people"},
      {"question": "In 'Evans Tries an O-Level', what was Evans known as?", "options": ["The break expert", "The Greek master", "The criminal", "The philosopher"], "answer": "The break expert"},
      {"question": "What did Zitkala-Sa dislike at the boarding school?", "options": ["Hair being cut", "Food", "Lessons", "Dress code"], "answer": "Hair being cut"},
      {"question": "Why was Gandhi's visit to Champaran historic?", "options": ["It started a civil disobedience movement", "It was his first satyagraha", "He met Nehru there", "He resigned politics"], "answer": "It was his first satyagraha"},
      {"question": "What does the phrase 'thumbprints on his windpipe' mean in 'The Interview'?", "options": ["Suppression", "Freedom", "Music", "Health"], "answer": "Suppression"},
      {"question": "What is the tone of the poem 'Keeping Quiet'?", "options": ["Calm and reflective", "Aggressive", "Sad", "Happy"], "answer": "Calm and reflective"},
      {"question": "In 'The Tiger King', why was the king cursed?", "options": ["For killing tigers", "For breaking a promise", "For insulting a saint", "For being arrogant"], "answer": "For killing tigers"},
      {"question": "In 'The Third Level', what does the 3rd level symbolize?", "options": ["Escape from reality", "A trap", "Success", "Anger"], "answer": "Escape from reality"}
    ]
  },
  "Hindi": {
    "Easy": [
      {"question": "'अतीत में दबे पाँव' कहानी के लेखक कौन हैं?", "options": ["कृष्णा सोबती", "मुक्तिबोध", "मन्नू भंडारी", "गजानन माधव मुक्तिबोध"], "answer": "कृष्णा सोबती"},
      {"question": "'पतंग' कविता किसने लिखी है?", "options": ["केदारनाथ अग्रवाल", "मुक्तिबोध", "अज्ञेय", "धर्मवीर भारती"], "answer": "केदारनाथ अग्रवाल"},
      {"question": "'शेख़ सादी' कौन थे?", "options": ["ईरानी सूफ़ी लेखक", "भारतीय संत", "हिंदी कवि", "दक्षिण भारत के राजा"], "answer": "ईरानी सूफ़ी लेखक"},
      {"question": "'मैं क्यों लिखता हूँ' पाठ में लेखक का नाम क्या है?", "options": ["हरिशंकर परसाई", "धर्मवीर भारती", "कन्हैयालाल मिश्र", "कन्हैयालाल वाजपेयी"], "answer": "धर्मवीर भारती"},
      {"question": "'जैसे को तैसा' कहानी में पात्र कौन-कौन से हैं?", "options": ["रामलाल और गिरधारी", "बाबू और मुंशी", "श्यामलाल और गफूर", "सीता और राधा"], "answer": "रामलाल और गिरधारी"},
      {"question": "'तितली' कहानी में तितली का प्रतीक क्या है?", "options": ["स्वतंत्रता", "भय", "धन", "लालच"], "answer": "स्वतंत्रता"},
      {"question": "‘रजनी’ पाठ में किसका वर्णन है?", "options": ["एक ग्रामीण स्त्री का", "एक शिक्षिका का", "एक लेखिका का", "एक युवा लड़की का"], "answer": "एक शिक्षिका का"},
      {"question": "‘ग़ज़ल’ किस विधा से संबंधित है?", "options": ["उर्दू काव्य", "नाटक", "उपन्यास", "लेख"], "answer": "उर्दू काव्य"},
      {"question": "‘कविता के बहाने’ किसकी रचना है?", "options": ["कुंवर नारायण", "मुक्तिबोध", "केदारनाथ सिंह", "अज्ञेय"], "answer": "कुंवर नारायण"},
      {"question": "'दुष्यंत कुमार' किस विधा के रचनाकार हैं?", "options": ["ग़ज़ल", "नाटक", "लेख", "उपन्यास"], "answer": "ग़ज़ल"}
    ],
    "Medium": [
      {"question": "'कविता के बहाने' में लेखक किस विषय पर बात करता है?", "options": ["कविता की आवश्यकता और समाज", "धन की महत्ता", "राजनीति", "भाषा का विकास"], "answer": "कविता की आवश्यकता और समाज"},
      {"question": "'शिकार' पाठ में प्रमुख विषय क्या है?", "options": ["राजा का साहस", "नारी शक्ति", "सामाजिक विसंगतियाँ", "प्रकृति का सौंदर्य"], "answer": "सामाजिक विसंगतियाँ"},
      {"question": "'ग़ज़ल' में मुख्य भाव क्या होता है?", "options": ["प्रेम और पीड़ा", "क्रोध", "प्रकृति", "न्याय"], "answer": "प्रेम और पीड़ा"},
      {"question": "'आलो आंधारि' में किसके संघर्ष का चित्रण है?", "options": ["बेबसी में जी रही लड़की", "राजा", "पुजारी", "सैनिक"], "answer": "बेबसी में जी रही लड़की"},
      {"question": "'चाँदनी बेगम' उपन्यास किसने लिखा?", "options": ["इस्मत चुगताई", "अमृता प्रीतम", "प्रेमचंद", "भीष्म साहनी"], "answer": "इस्मत चुगताई"},
      {"question": "'एक लेखक की डायरी' में लेखक ने क्या उजागर किया है?", "options": ["लेखक का आत्मसंघर्ष", "राजनीतिक संकट", "धार्मिक कट्टरता", "यात्रा वृतांत"], "answer": "लेखक का आत्मसंघर्ष"},
      {"question": "'मुक्तिबोध' कौन-सी कविता विधा से संबंधित हैं?", "options": ["नवलेखन", "छायावाद", "प्रगतिवाद", "रीतिकाल"], "answer": "नवलेखन"},
      {"question": "'आम आदमी और सिर' पाठ में लेखक ने किस बात की आलोचना की है?", "options": ["राजनीतिक व्यवस्था", "पुलिस व्यवस्था", "सामाजिक असमानता", "शिक्षा प्रणाली"], "answer": "राजनीतिक व्यवस्था"},
      {"question": "'पतंग' कविता में पतंग किसका प्रतीक है?", "options": ["बालपन की आकांक्षा", "धन", "ज्ञान", "समाज"], "answer": "बालपन की आकांक्षा"},
      {"question": "'शेख़ सादी' पाठ से हमें क्या सीख मिलती है?", "options": ["सच्चाई और नैतिकता", "धन संचय", "राजनीति", "युद्ध नीति"], "answer": "सच्चाई और नैतिकता"}
    ],
    "Hard": [
      {"question": "'कविता के बहाने' में कौन-सी बात प्रमुख रूप से उठाई गई है?", "options": ["कविता का सामाजिक उत्तरदायित्व", "कविता का सौंदर्य", "रूपक की शैली", "व्यक्तिवादी दृष्टिकोण"], "answer": "कविता का सामाजिक उत्तरदायित्व"},
      {"question": "'आलो आंधारि' आत्मकथा में किसका चित्रण है?", "options": ["बेबी हालदार", "मन्नू भंडारी", "ताराशंकर बंधोपाध्याय", "कृष्णा सोबती"], "answer": "बेबी हालदार"},
      {"question": "'ग़ज़ल' विधा का प्रमुख शिल्प तत्त्व क्या होता है?", "options": ["मतला और मकता", "पात्र और कथानक", "संदर्भ और भाव", "लय और ताल"], "answer": "मतला और मकता"},
      {"question": "'अतीत में दबे पाँव' पाठ में विभाजन के किस पहलू को दर्शाया गया है?", "options": ["मानवता का विनाश", "राजनीतिक लाभ", "भाषा विवाद", "धार्मिक कट्टरता"], "answer": "मानवता का विनाश"},
      {"question": "'रजनी' पाठ में नारी शिक्षा को किस रूप में देखा गया है?", "options": ["सशक्तिकरण के माध्यम", "परंपरा का अंश", "अनुशासन", "साहित्य का हिस्सा"], "answer": "सशक्तिकरण के माध्यम"},
      {"question": "'दुष्यंत कुमार' की ग़ज़लें किस आंदोलन से जुड़ी मानी जाती हैं?", "options": ["नवगीत आंदोलन", "प्रयोगवाद", "जनकवि आंदोलन", "जनकथा आंदोलन"], "answer": "जनकवि आंदोलन"},
      {"question": "'एक लेखक की डायरी' पाठ में लेखक ने किन समस्याओं पर ध्यान दिया है?", "options": ["साहित्य और समाज की दूरी", "प्रकृति का वर्णन", "युद्ध नीति", "राजनीतिक व्यवस्था"], "answer": "साहित्य और समाज की दूरी"},
      {"question": "'जैसे को तैसा' कहानी में किस सामाजिक समस्या पर चोट की गई है?", "options": ["पाखंड", "अशिक्षा", "गरीबी", "धार्मिक कट्टरता"], "answer": "पाखंड"},
      {"question": "'तितली' कहानी का अंत किस बात को दर्शाता है?", "options": ["मन की स्वतंत्रता", "मृत्यु", "क्रोध", "लालच"], "answer": "मन की स्वतंत्रता"},
      {"question": "'आम आदमी और सिर' पाठ किस शैली में लिखा गया है?", "options": ["व्यंग्य", "काव्य", "नाटक", "लेख"], "answer": "व्यंग्य"}
    ]
  },
  "Physics": {
    "Easy": [
      {"question": "Coulomb's law deals with which type of force?", "options": ["Electrostatic", "Magnetic", "Gravitational", "Nuclear"], "answer": "Electrostatic"},
      {"question": "SI unit of electric charge is?", "options": ["Coulomb", "Volt", "Ohm", "Ampere"], "answer": "Coulomb"},
      {"question": "Which device converts AC to DC?", "options": ["Rectifier", "Transformer", "Inductor", "Capacitor"], "answer": "Rectifier"},
      {"question": "The electric field inside a conductor is?", "options": ["Zero", "Infinite", "Constant", "Variable"], "answer": "Zero"},
      {"question": "Which quantity is conserved in all collisions?", "options": ["Momentum", "Kinetic Energy", "Force", "Velocity"], "answer": "Momentum"},
      {"question": "Which law is used to find magnetic field due to current?", "options": ["Biot–Savart Law", "Ohm's Law", "Faraday's Law", "Lenz's Law"], "answer": "Biot–Savart Law"},
      {"question": "The SI unit of magnetic flux is?", "options": ["Weber", "Tesla", "Henry", "Ampere"], "answer": "Weber"},
      {"question": "Which of the following is a scalar quantity?", "options": ["Electric potential", "Magnetic field", "Electric field", "Current"], "answer": "Electric potential"},
      {"question": "Ammeter is always connected in?", "options": ["Series", "Parallel", "Both", "None"], "answer": "Series"},
      {"question": "What is the value of 1 microfarad in Farads?", "options": ["10^-6 F", "10^6 F", "10^-3 F", "10^-9 F"], "answer": "10^-6 F"}
    ],
    "Medium": [
      {"question": "Kirchhoff's Voltage Law is based on which principle?", "options": ["Conservation of energy", "Conservation of charge", "Ohm’s law", "Coulomb's law"], "answer": "Conservation of energy"},
      {"question": "Which of the following does not affect the capacitance of a capacitor?", "options": ["Voltage", "Area of plates", "Distance between plates", "Dielectric constant"], "answer": "Voltage"},
      {"question": "The energy stored in a capacitor is given by?", "options": ["½CV²", "CV", "C/V", "½QV"], "answer": "½CV²"},
      {"question": "In Lenz’s law, the induced EMF always?", "options": ["Opposes the cause producing it", "Supports the magnetic field", "Is constant", "Increases current"], "answer": "Opposes the cause producing it"},
      {"question": "The direction of magnetic field around a current-carrying wire is given by?", "options": ["Right-hand thumb rule", "Fleming’s left-hand rule", "Lenz’s law", "Faraday’s law"], "answer": "Right-hand thumb rule"},
      {"question": "Self-inductance of a coil depends on?", "options": ["Number of turns", "Core material", "Area of cross-section", "All of the above"], "answer": "All of the above"},
      {"question": "Power factor in an AC circuit is given by?", "options": ["cos ϕ", "sin ϕ", "tan ϕ", "cot ϕ"], "answer": "cos ϕ"},
      {"question": "Which electromagnetic wave has the shortest wavelength?", "options": ["Gamma rays", "X-rays", "UV rays", "Radio waves"], "answer": "Gamma rays"},
      {"question": "The lens which is thicker at the center is called?", "options": ["Convex lens", "Concave lens", "Plano-concave", "Cylindrical lens"], "answer": "Convex lens"},
      {"question": "In Young’s double-slit experiment, fringe width is proportional to?", "options": ["Wavelength", "Inverse of slit distance", "Square of slit distance", "Frequency"], "answer": "Wavelength"}
    ],
    "Hard": [
      {"question": "In an LCR series circuit at resonance, the current is?", "options": ["Maximum", "Minimum", "Zero", "Infinity"], "answer": "Maximum"},
      {"question": "The radius of the nth orbit in hydrogen atom is proportional to?", "options": ["n²", "n", "1/n", "1/n²"], "answer": "n²"},
      {"question": "Critical angle for total internal reflection occurs when light goes from?", "options": ["Denser to rarer medium", "Rarer to denser medium", "Air to vacuum", "Vacuum to glass"], "answer": "Denser to rarer medium"},
      {"question": "Photoelectric effect proves which nature of light?", "options": ["Particle nature", "Wave nature", "Dual nature", "Reflective nature"], "answer": "Particle nature"},
      {"question": "Which of the following has the highest energy?", "options": ["X-rays", "Ultraviolet", "Microwaves", "Infrared"], "answer": "X-rays"},
      {"question": "Binding energy per nucleon is maximum for which element?", "options": ["Iron (Fe)", "Uranium (U)", "Helium (He)", "Hydrogen (H)"], "answer": "Iron (Fe)"},
      {"question": "De Broglie wavelength is inversely proportional to?", "options": ["Momentum", "Velocity", "Frequency", "Energy"], "answer": "Momentum"},
      {"question": "Which of the following nuclei is most stable?", "options": ["Fe-56", "U-238", "He-4", "C-12"], "answer": "Fe-56"},
      {"question": "Mass defect is the difference between?", "options": ["Mass of nucleons and nucleus", "Mass of proton and neutron", "Mass of neutron and electron", "Atomic mass and molar mass"], "answer": "Mass of nucleons and nucleus"},
      {"question": "In semiconductors, the energy gap is typically?", "options": ["1 eV", "10 eV", "0.01 eV", "5 eV"], "answer": "1 eV"}
    ]
  },
  "Chemistry": {
    "Easy": [
      {"question": "Which element has the atomic number 17?", "options": ["Chlorine", "Fluorine", "Oxygen", "Nitrogen"], "answer": "Chlorine"},
      {"question": "Which of the following is a noble gas?", "options": ["Neon", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Neon"},
      {"question": "The molecular formula of methane is?", "options": ["CH4", "C2H6", "C3H8", "CH3OH"], "answer": "CH4"},
      {"question": "Which acid is present in vinegar?", "options": ["Acetic acid", "Citric acid", "Hydrochloric acid", "Sulphuric acid"], "answer": "Acetic acid"},
      {"question": "Which gas is evolved when zinc reacts with HCl?", "options": ["Hydrogen", "Oxygen", "Nitrogen", "Carbon dioxide"], "answer": "Hydrogen"},
      {"question": "The functional group in alcohols is?", "options": ["–OH", "–COOH", "–CHO", "–NH2"], "answer": "–OH"},
      {"question": "Which compound is used in dry cleaning?", "options": ["Carbon tetrachloride", "Methanol", "Acetone", "Benzene"], "answer": "Carbon tetrachloride"},
      {"question": "Which metal is liquid at room temperature?", "options": ["Mercury", "Sodium", "Lead", "Aluminium"], "answer": "Mercury"},
      {"question": "The number of covalent bonds in methane is?", "options": ["4", "2", "1", "3"], "answer": "4"},
      {"question": "Which of these is an exothermic reaction?", "options": ["Combustion of methane", "Photosynthesis", "Melting of ice", "Evaporation of water"], "answer": "Combustion of methane"}
    ],
    "Medium": [
      {"question": "Which of the following has a tetrahedral geometry?", "options": ["CH4", "NH3", "H2O", "CO2"], "answer": "CH4"},
      {"question": "IUPAC name of CH3–CH2–OH is?", "options": ["Ethanol", "Methanol", "Propanol", "Ethanoic acid"], "answer": "Ethanol"},
      {"question": "Which metal is extracted by electrolytic reduction?", "options": ["Aluminium", "Iron", "Zinc", "Copper"], "answer": "Aluminium"},
      {"question": "The pH of a neutral solution is?", "options": ["7", "5", "3", "9"], "answer": "7"},
      {"question": "Which compound shows geometrical isomerism?", "options": ["But-2-ene", "Ethane", "Propane", "Methane"], "answer": "But-2-ene"},
      {"question": "Which reagent is used for the test of aldehydes?", "options": ["Tollen's reagent", "Fehling's solution", "Baeyer's reagent", "Benedict's solution"], "answer": "Tollen's reagent"},
      {"question": "Which of the following is not a green house gas?", "options": ["O2", "CO2", "CH4", "N2O"], "answer": "O2"},
      {"question": "Which ion is responsible for hardness of water?", "options": ["Ca²⁺", "Na⁺", "K⁺", "H⁺"], "answer": "Ca²⁺"},
      {"question": "Which one of the following is a non-electrolyte?", "options": ["Glucose", "NaCl", "HCl", "KOH"], "answer": "Glucose"},
      {"question": "Which is the correct order of reactivity of halogens?", "options": ["F2 > Cl2 > Br2 > I2", "Cl2 > F2 > I2 > Br2", "I2 > Br2 > Cl2 > F2", "Br2 > I2 > F2 > Cl2"], "answer": "F2 > Cl2 > Br2 > I2"}
    ],
    "Hard": [
      {"question": "Which of the following has the highest boiling point?", "options": ["H2O", "H2S", "H2Se", "H2Te"], "answer": "H2O"},
      {"question": "Which of the following is a non-biodegradable pollutant?", "options": ["DDT", "Cow dung", "Vegetable waste", "Paper"], "answer": "DDT"},
      {"question": "Which of the following will show +I effect?", "options": ["–CH3", "–COOH", "–NO2", "–CN"], "answer": "–CH3"},
      {"question": "Which of the following is an example of a zwitterion?", "options": ["Amino acid", "Ethanol", "Benzoic acid", "Methane"], "answer": "Amino acid"},
      {"question": "Which vitamin is synthesized from cholesterol?", "options": ["Vitamin D", "Vitamin A", "Vitamin B", "Vitamin C"], "answer": "Vitamin D"},
      {"question": "Which compound shows optical isomerism?", "options": ["Lactic acid", "Acetic acid", "Methanol", "Formaldehyde"], "answer": "Lactic acid"},
      {"question": "The major product of dehydration of alcohol is?", "options": ["Alkene", "Aldehyde", "Carboxylic acid", "Ketone"], "answer": "Alkene"},
      {"question": "Which of the following undergoes SN1 reaction fastest?", "options": ["Tertiary alkyl halide", "Primary alkyl halide", "Secondary alkyl halide", "Methyl halide"], "answer": "Tertiary alkyl halide"},
      {"question": "Which one of the following is a chelating ligand?", "options": ["EDTA", "Cl⁻", "CN⁻", "NH3"], "answer": "EDTA"},
      {"question": "Which of the following complexes shows optical isomerism?", "options": ["[Co(en)3]³⁺", "[Ni(CN)4]²⁻", "[Cu(NH3)4]²⁺", "[PtCl4]²⁻"], "answer": "[Co(en)3]³⁺"}
    ]
  },
  "Mathematics": {
    "Easy": [
      {"question": "What is the derivative of sin(x)?", "options": ["cos(x)", "-cos(x)", "-sin(x)", "tan(x)"], "answer": "cos(x)"},
      {"question": "The value of cos(0°) is?", "options": ["1", "0", "-1", "√3"], "answer": "1"},
      {"question": "What is the integration of 1/x dx?", "options": ["ln|x| + C", "x + C", "1/x + C", "x² + C"], "answer": "ln|x| + C"},
      {"question": "What is the determinant of a 2x2 matrix [[1,2],[3,4]]?", "options": ["-2", "10", "2", "0"], "answer": "-2"},
      {"question": "If A = {1, 2, 3}, then the number of subsets of A is?", "options": ["8", "6", "3", "4"], "answer": "8"},
      {"question": "The angle between the vectors a = i and b = j is?", "options": ["90°", "0°", "180°", "45°"], "answer": "90°"},
      {"question": "If A is a square matrix of order 3, then det(A) is a?", "options": ["Scalar", "Vector", "Matrix", "Identity"], "answer": "Scalar"},
      {"question": "The range of sin(x) is?", "options": ["[-1, 1]", "[0, ∞)", "(-∞, ∞)", "[0, 1]"], "answer": "[-1, 1]"},
      {"question": "What is the slope of a line parallel to x-axis?", "options": ["0", "1", "∞", "-1"], "answer": "0"},
      {"question": "The value of (a + b)² is?", "options": ["a² + 2ab + b²", "a² - 2ab + b²", "a² + b²", "ab + b²"], "answer": "a² + 2ab + b²"}
    ],
    "Medium": [
      {"question": "If y = x² + 2x, then dy/dx is?", "options": ["2x + 2", "2x", "x + 2", "x² + 2x"], "answer": "2x + 2"},
      {"question": "If A and B are two events, then P(A ∪ B) equals?", "options": ["P(A) + P(B) − P(A ∩ B)", "P(A) × P(B)", "P(A) + P(B)", "P(A ∩ B)"], "answer": "P(A) + P(B) − P(A ∩ B)"},
      {"question": "The number of all possible 3-digit numbers is?", "options": ["900", "1000", "899", "999"], "answer": "900"},
      {"question": "The derivative of tan(x) is?", "options": ["sec²(x)", "tan(x)", "sin(x)", "cos(x)"], "answer": "sec²(x)"},
      {"question": "Area under the curve y = x between x = 0 and x = 2 is?", "options": ["2", "4", "1", "3"], "answer": "2"},
      {"question": "A vector perpendicular to both i + j and j + k is?", "options": ["i − j + k", "i + j − k", "i − k", "j + k"], "answer": "i − j + k"},
      {"question": "The probability of getting head in one coin toss is?", "options": ["1/2", "1/3", "1", "0"], "answer": "1/2"},
      {"question": "If A = [[2, 0], [0, 3]], then trace(A) is?", "options": ["5", "6", "2", "3"], "answer": "5"},
      {"question": "What is the inverse of a 2x2 identity matrix?", "options": ["Itself", "Zero matrix", "Transpose", "None"], "answer": "Itself"},
      {"question": "Which of the following is a continuous function?", "options": ["f(x) = x²", "f(x) = 1/x", "f(x) = |x|", "f(x) = [x]"], "answer": "f(x) = x²"}
    ],
    "Hard": [
      {"question": "If ∫(x² + 2x + 1) dx = ?", "options": ["(x³/3) + x² + x + C", "x² + x + C", "(x²/2) + 2x + C", "x³ + x² + 1 + C"], "answer": "(x³/3) + x² + x + C"},
      {"question": "If A is a non-singular matrix, then A⁻¹ exists only if?", "options": ["det(A) ≠ 0", "det(A) = 0", "A is symmetric", "A is skew-symmetric"], "answer": "det(A) ≠ 0"},
      {"question": "What is the value of lim(x→0) (sinx)/x?", "options": ["1", "0", "∞", "Does not exist"], "answer": "1"},
      {"question": "If the vectors a and b are perpendicular, then a·b is?", "options": ["0", "1", "a + b", "a × b"], "answer": "0"},
      {"question": "The general solution of dy/dx = y is?", "options": ["y = Ce^x", "y = x²", "y = sinx", "y = e^(1/x)"], "answer": "y = Ce^x"},
      {"question": "The angle between two lines having slopes m₁ and m₂ is given by?", "options": ["tan⁻¹|(m₁−m₂)/(1+m₁m₂)|", "m₁ + m₂", "m₁ × m₂", "m₁/m₂"], "answer": "tan⁻¹|(m₁−m₂)/(1+m₁m₂)|"},
      {"question": "Which of the following is a bijective function?", "options": ["f(x)=x³", "f(x)=x²", "f(x)=|x|", "f(x)=[x]"], "answer": "f(x)=x³"},
      {"question": "If X is a binomial variable with n=5, p=0.5, then E(X) = ?", "options": ["2.5", "5", "1", "0.5"], "answer": "2.5"},
      {"question": "If the angle between two vectors is 90°, then their dot product is?", "options": ["0", "1", "−1", "∞"], "answer": "0"},
      {"question": "What is the solution of the differential equation dy/dx = x²y?", "options": ["y = Ce^(x³/3)", "y = x² + C", "y = ln(x)", "y = x³/3 + C"], "answer": "y = Ce^(x³/3)"}
    ]
  },
  "Biology": {
    "Easy": [
      {"question": "Which process forms gametes?", "options": ["Meiosis", "Mitosis", "Fertilization", "Cloning"], "answer": "Meiosis"},
      {"question": "Which hormone is responsible for milk production?", "options": ["Prolactin", "Oxytocin", "Estrogen", "Progesterone"], "answer": "Prolactin"},
      {"question": "What is the genetic material in most organisms?", "options": ["DNA", "RNA", "Protein", "Enzyme"], "answer": "DNA"},
      {"question": "Which part of the flower develops into fruit?", "options": ["Ovary", "Petal", "Anther", "Style"], "answer": "Ovary"},
      {"question": "What is the full form of AIDS?", "options": ["Acquired Immuno Deficiency Syndrome", "Automatic Immune Deficiency System", "Advanced Immune Disease Syndrome", "Auto Immune Deficiency Syndrome"], "answer": "Acquired Immuno Deficiency Syndrome"},
      {"question": "Mendel is known as the father of?", "options": ["Genetics", "Biology", "Anatomy", "Botany"], "answer": "Genetics"},
      {"question": "Which organ produces insulin?", "options": ["Pancreas", "Liver", "Heart", "Kidney"], "answer": "Pancreas"},
      {"question": "Which vitamin is synthesized in the skin by sunlight?", "options": ["Vitamin D", "Vitamin A", "Vitamin C", "Vitamin K"], "answer": "Vitamin D"},
      {"question": "Which is the largest cell in the human body?", "options": ["Ovum", "Neuron", "Muscle cell", "RBC"], "answer": "Ovum"},
      {"question": "Who discovered the double helix model of DNA?", "options": ["Watson and Crick", "Mendel", "Pasteur", "Darwin"], "answer": "Watson and Crick"}
    ],
    "Medium": [
      {"question": "Which gene causes cancer?", "options": ["Oncogene", "Homeobox gene", "Regulatory gene", "Structural gene"], "answer": "Oncogene"},
      {"question": "Which enzyme joins Okazaki fragments?", "options": ["DNA ligase", "DNA polymerase", "Helicase", "Topoisomerase"], "answer": "DNA ligase"},
      {"question": "Which organelle is responsible for photosynthesis?", "options": ["Chloroplast", "Mitochondria", "Ribosome", "Nucleus"], "answer": "Chloroplast"},
      {"question": "Which immunoglobulin is found in mother's milk?", "options": ["IgA", "IgG", "IgM", "IgE"], "answer": "IgA"},
      {"question": "Test tube baby technique is called?", "options": ["IVF", "IUI", "Surrogacy", "ZIFT"], "answer": "IVF"},
      {"question": "Which part of the neuron receives impulses?", "options": ["Dendrites", "Axon", "Node of Ranvier", "Synapse"], "answer": "Dendrites"},
      {"question": "What is the cause of Down syndrome?", "options": ["Trisomy of chromosome 21", "Monosomy X", "Trisomy 18", "Deletion of chromosome 5"], "answer": "Trisomy of chromosome 21"},
      {"question": "Which scientist proposed Natural Selection?", "options": ["Charles Darwin", "Lamarck", "Mendel", "Pasteur"], "answer": "Charles Darwin"},
      {"question": "Bt cotton is a genetically modified crop resistant to?", "options": ["Insects", "Fungi", "Weeds", "Virus"], "answer": "Insects"},
      {"question": "What is the role of biofertilizers?", "options": ["Enhance soil fertility", "Kill pests", "Increase water absorption", "Act as hormones"], "answer": "Enhance soil fertility"}
    ],
    "Hard": [
      {"question": "Which part of the brain regulates temperature?", "options": ["Hypothalamus", "Cerebrum", "Cerebellum", "Medulla"], "answer": "Hypothalamus"},
      {"question": "What is the function of restriction enzymes?", "options": ["Cut DNA at specific sequences", "Join DNA strands", "Copy DNA", "Stabilize RNA"], "answer": "Cut DNA at specific sequences"},
      {"question": "What is the genotype ratio in a monohybrid cross?", "options": ["1:2:1", "3:1", "9:3:3:1", "2:1"], "answer": "1:2:1"},
      {"question": "In Hardy-Weinberg equilibrium, p² + 2pq + q² = ?", "options": ["1", "0", "2", "∞"], "answer": "1"},
      {"question": "Which hormone is produced by the placenta?", "options": ["hCG", "FSH", "LH", "Testosterone"], "answer": "hCG"},
      {"question": "Apical dominance in plants is controlled by?", "options": ["Auxin", "Cytokinin", "Ethylene", "Gibberellin"], "answer": "Auxin"},
      {"question": "Which technique is used to amplify DNA?", "options": ["PCR", "ELISA", "Gel electrophoresis", "Blotting"], "answer": "PCR"},
      {"question": "Which human chromosome has the most genes?", "options": ["Chromosome 1", "Chromosome 21", "X chromosome", "Y chromosome"], "answer": "Chromosome 1"},
      {"question": "Which plant is used in the study of genetics?", "options": ["Pea plant", "Wheat", "Rice", "Sunflower"], "answer": "Pea plant"},
      {"question": "In which stage of meiosis does crossing over occur?", "options": ["Prophase I", "Metaphase I", "Anaphase I", "Telophase I"], "answer": "Prophase I"}
    ]
  },
  "Accountancy": {
    "Easy": [
      {"question": "Which account is affected when capital is introduced in the business?", "options": ["Capital Account", "Cash Account", "Drawings Account", "Sales Account"], "answer": "Capital Account"},
      {"question": "Partnership is governed by which Act?", "options": ["Indian Partnership Act, 1932", "Companies Act, 2013", "Contract Act, 1872", "Income Tax Act"], "answer": "Indian Partnership Act, 1932"},
      {"question": "What is the minimum number of partners in a partnership firm?", "options": ["2", "1", "3", "7"], "answer": "2"},
      {"question": "Goodwill is classified as which type of asset?", "options": ["Intangible Asset", "Fixed Asset", "Current Asset", "Fictitious Asset"], "answer": "Intangible Asset"},
      {"question": "Which statement shows the financial position of a business?", "options": ["Balance Sheet", "Trial Balance", "Ledger", "Cash Book"], "answer": "Balance Sheet"},
      {"question": "What is the nature of a Drawings Account?", "options": ["Personal", "Nominal", "Real", "Revenue"], "answer": "Personal"},
      {"question": "The portion of profit distributed among partners is called?", "options": ["Profit Share", "Remuneration", "Salary", "Drawings"], "answer": "Profit Share"},
      {"question": "Which account is prepared at the time of admission of a partner?", "options": ["Revaluation Account", "Profit & Loss Account", "Capital Account", "Cash Account"], "answer": "Revaluation Account"},
      {"question": "What is the full form of DR in accounting?", "options": ["Debit", "Drawing", "Deposit Receipt", "Deferred Revenue"], "answer": "Debit"},
      {"question": "Which side of the Capital Account is increased?", "options": ["Credit", "Debit", "Both", "None"], "answer": "Credit"}
    ],
    "Medium": [
      {"question": "Which method is used for calculating sacrificing ratio?", "options": ["Old Ratio – New Ratio", "New Ratio – Old Ratio", "New Ratio × Old Ratio", "Old Ratio + New Ratio"], "answer": "Old Ratio – New Ratio"},
      {"question": "When a partner retires, goodwill is credited to?", "options": ["All partners in gaining ratio", "Retiring partner only", "Old partners equally", "Capital Account only"], "answer": "All partners in gaining ratio"},
      {"question": "In dissolution, realisation account is prepared to?", "options": ["Calculate profit or loss on sale of assets", "Distribute capital", "Adjust reserves", "Record drawings"], "answer": "Calculate profit or loss on sale of assets"},
      {"question": "On admission, unrecorded liability is?", "options": ["Debited to Revaluation Account", "Credited to Revaluation Account", "Debited to Partner’s Capital", "Credited to Goodwill Account"], "answer": "Credited to Revaluation Account"},
      {"question": "Which is not shown in a Cash Flow Statement?", "options": ["Credit Sales", "Cash Sales", "Depreciation", "Dividend Paid"], "answer": "Credit Sales"},
      {"question": "What is the objective of ratio analysis?", "options": ["Assess financial performance", "Calculate taxes", "Maintain cash book", "Find errors"], "answer": "Assess financial performance"},
      {"question": "Which account is affected by revaluation of assets?", "options": ["Revaluation Account", "Capital Account", "Cash Account", "Trading Account"], "answer": "Revaluation Account"},
      {"question": "Which account is debited when share application money is received?", "options": ["Bank Account", "Share Capital", "Calls-in-Arrears", "Securities Premium"], "answer": "Bank Account"},
      {"question": "Which section of Cash Flow covers issue of shares?", "options": ["Financing Activities", "Investing Activities", "Operating Activities", "All of these"], "answer": "Financing Activities"},
      {"question": "What is the formula for Current Ratio?", "options": ["Current Assets / Current Liabilities", "Current Liabilities / Current Assets", "Total Assets / Total Liabilities", "Quick Assets / Current Liabilities"], "answer": "Current Assets / Current Liabilities"}
    ],
    "Hard": [
      {"question": "Which ratio shows the relationship between net profit and revenue?", "options": ["Net Profit Ratio", "Gross Profit Ratio", "Operating Ratio", "Current Ratio"], "answer": "Net Profit Ratio"},
      {"question": "Contingent liabilities are shown?", "options": ["In notes to accounts", "In balance sheet", "In P&L account", "In cash flow"], "answer": "In notes to accounts"},
      {"question": "Which is deducted from Gross Profit to calculate Operating Profit?", "options": ["Operating Expenses", "Indirect Incomes", "Depreciation", "Cost of Goods Sold"], "answer": "Operating Expenses"},
      {"question": "Debenture Redemption Reserve is created from?", "options": ["Profit", "Capital", "Loan", "Cash"], "answer": "Profit"},
      {"question": "Which schedule of Company’s Balance Sheet shows Non-Current Liabilities?", "options": ["Schedule III", "Schedule II", "Schedule I", "None"], "answer": "Schedule III"},
      {"question": "Which activity is purchase of fixed asset in Cash Flow?", "options": ["Investing", "Financing", "Operating", "Non-cash"], "answer": "Investing"},
      {"question": "If goodwill is privately paid, it is?", "options": ["Not recorded in books", "Credited to capital", "Debited to revaluation", "Credited to goodwill"], "answer": "Not recorded in books"},
      {"question": "A rise in Current Ratio indicates?", "options": ["Improved short-term solvency", "Decline in profitability", "Fall in liquidity", "High risk"], "answer": "Improved short-term solvency"},
      {"question": "Cash from operating activities is calculated using?", "options": ["Cash Flow Statement", "Balance Sheet", "Ledger", "Ratio analysis"], "answer": "Cash Flow Statement"},
      {"question": "Preliminary expenses written off appear in Cash Flow under?", "options": ["Operating Activities", "Financing Activities", "Investing Activities", "Not shown"], "answer": "Operating Activities"}
    ]
  },
  "Business Studies": {
    "Easy": [
      {"question": "Which function of management is concerned with grouping activities?", "options": ["Organising", "Planning", "Controlling", "Directing"], "answer": "Organising"},
      {"question": "Who is known as the father of scientific management?", "options": ["F.W. Taylor", "Henry Fayol", "Elton Mayo", "Peter Drucker"], "answer": "F.W. Taylor"},
      {"question": "Which level of management is responsible for implementing plans?", "options": ["Middle-level", "Top-level", "Lower-level", "None"], "answer": "Middle-level"},
      {"question": "What is the first function of management?", "options": ["Planning", "Organising", "Controlling", "Staffing"], "answer": "Planning"},
      {"question": "Which principle of management suggests 'one boss for one employee'?", "options": ["Unity of Command", "Scalar Chain", "Order", "Authority and Responsibility"], "answer": "Unity of Command"},
      {"question": "Which document is issued by a company to invite public to invest?", "options": ["Prospectus", "Certificate of Incorporation", "MOA", "AOA"], "answer": "Prospectus"},
      {"question": "Which motivation theory was developed by Maslow?", "options": ["Hierarchy of Needs", "Equity Theory", "Two-Factor Theory", "X and Y Theory"], "answer": "Hierarchy of Needs"},
      {"question": "Which marketing element includes activities like advertising and sales?", "options": ["Promotion", "Price", "Product", "Place"], "answer": "Promotion"},
      {"question": "What is the time span of operational planning?", "options": ["Short-term", "Long-term", "Very long-term", "None"], "answer": "Short-term"},
      {"question": "Which function of management ensures that actual performance matches plans?", "options": ["Controlling", "Organising", "Planning", "Staffing"], "answer": "Controlling"}
    ],
    "Medium": [
      {"question": "Which financial decision affects both profitability and liquidity?", "options": ["Working Capital Decision", "Investment Decision", "Dividend Decision", "None"], "answer": "Working Capital Decision"},
      {"question": "Delegation does not include which of the following?", "options": ["Decentralisation", "Responsibility", "Authority", "Accountability"], "answer": "Decentralisation"},
      {"question": "Which document defines the objectives of a company?", "options": ["Memorandum of Association", "Articles of Association", "Prospectus", "Certificate of Incorporation"], "answer": "Memorandum of Association"},
      {"question": "What is the process of recruiting employees from within the organisation?", "options": ["Internal Source", "External Source", "Outsourcing", "Offshoring"], "answer": "Internal Source"},
      {"question": "Which of the following is a feature of planning?", "options": ["Planning is futuristic", "Planning increases rigidity", "Planning is pervasive", "All of these"], "answer": "All of these"},
      {"question": "Which leadership style gives complete freedom to subordinates?", "options": ["Laissez-Faire", "Autocratic", "Democratic", "Transformational"], "answer": "Laissez-Faire"},
      {"question": "Which type of organisational structure is based on functions?", "options": ["Functional Structure", "Divisional Structure", "Matrix Structure", "Project Structure"], "answer": "Functional Structure"},
      {"question": "Which factor does not affect the working capital requirement?", "options": ["Nature of business", "Production cycle", "Cash flow position", "Price of land"], "answer": "Price of land"},
      {"question": "Which component of marketing mix is most flexible?", "options": ["Price", "Product", "Place", "Promotion"], "answer": "Price"},
      {"question": "Which term means giving more autonomy to lower levels?", "options": ["Decentralisation", "Centralisation", "Delegation", "Coordination"], "answer": "Decentralisation"}
    ],
    "Hard": [
      {"question": "SEBI was established in which year?", "options": ["1992", "1988", "1991", "1995"], "answer": "1992"},
      {"question": "Which of the following is not a function of SEBI?", "options": ["Appointing RBI Governor", "Regulating Stock Market", "Protecting investor interest", "Promoting fair practices"], "answer": "Appointing RBI Governor"},
      {"question": "Which financial market deals in existing securities?", "options": ["Secondary Market", "Primary Market", "Money Market", "Capital Market"], "answer": "Secondary Market"},
      {"question": "Which type of plan has a wider scope and longer time horizon?", "options": ["Strategy", "Policy", "Rule", "Method"], "answer": "Strategy"},
      {"question": "The 'Principle of Espirit de Corps' is concerned with?", "options": ["Team Spirit", "Discipline", "Equity", "Stability"], "answer": "Team Spirit"},
      {"question": "Which consumer right allows you to get relief against unfair practices?", "options": ["Right to Redressal", "Right to Choose", "Right to Be Heard", "Right to Information"], "answer": "Right to Redressal"},
      {"question": "In staffing, the process of introducing a new employee to the organisation is?", "options": ["Orientation", "Selection", "Recruitment", "Placement"], "answer": "Orientation"},
      {"question": "What is the full form of NSE?", "options": ["National Stock Exchange", "New Stock Entity", "National Sales Exchange", "None of these"], "answer": "National Stock Exchange"},
      {"question": "Which financial statement provides information about liquidity?", "options": ["Cash Flow Statement", "Balance Sheet", "Profit & Loss Account", "Trial Balance"], "answer": "Cash Flow Statement"},
      {"question": "The principle of 'Order' implies?", "options": ["Right person at the right job", "Obedience", "Stability", "Discipline"], "answer": "Right person at the right job"}
    ]
  },
  "Economics": {
    "Easy": [
      {"question": "Which of the following is a central problem of an economy?", "options": ["What to produce", "Where to produce", "Who will govern", "None of these"], "answer": "What to produce"},
      {"question": "National Income is the sum total of?", "options": ["Factor incomes", "Transfer payments", "Subsidies", "All types of income"], "answer": "Factor incomes"},
      {"question": "GDP at market price includes?", "options": ["Indirect taxes", "Subsidies", "Depreciation", "Both A and B"], "answer": "Both A and B"},
      {"question": "Which sector contributes the most to India's GDP?", "options": ["Service sector", "Agriculture", "Industrial sector", "Mining"], "answer": "Service sector"},
      {"question": "Which of the following is a component of Aggregate Demand?", "options": ["Consumption", "Investment", "Government expenditure", "All of these"], "answer": "All of these"},
      {"question": "What does CPI measure?", "options": ["Inflation for consumers", "Wages", "Exports", "GDP"], "answer": "Inflation for consumers"},
      {"question": "When Exports > Imports, it is called?", "options": ["Trade surplus", "Trade deficit", "BOP crisis", "Capital inflow"], "answer": "Trade surplus"},
      {"question": "Which of these is a leakage in the circular flow of income?", "options": ["Saving", "Investment", "Consumption", "Government spending"], "answer": "Saving"},
      {"question": "Which organisation calculates National Income in India?", "options": ["NSO", "RBI", "SEBI", "NABARD"], "answer": "NSO"},
      {"question": "The formula for GDP Deflator is?", "options": ["(Nominal GDP / Real GDP) × 100", "Nominal GDP - Real GDP", "CPI × 100", "WPI + CPI"], "answer": "(Nominal GDP / Real GDP) × 100"}
    ],
    "Medium": [
      {"question": "Real GDP is measured at?", "options": ["Constant prices", "Current prices", "Market prices", "Factor cost"], "answer": "Constant prices"},
      {"question": "What is autonomous consumption?", "options": ["Consumption when income is zero", "Income-dependent consumption", "Business investment", "Government spending"], "answer": "Consumption when income is zero"},
      {"question": "If MPC = 0.8, then the value of multiplier is?", "options": ["5", "2", "4", "8"], "answer": "5"},
      {"question": "Which curve is upward sloping in the Keynesian model?", "options": ["Aggregate Supply", "Aggregate Demand", "Consumption", "Saving"], "answer": "Aggregate Supply"},
      {"question": "Which item is not included in the capital account of BOP?", "options": ["Exports", "FDI", "External borrowings", "NRI deposits"], "answer": "Exports"},
      {"question": "Revenue deficit arises when?", "options": ["Revenue expenditure > Revenue receipts", "Capital receipts > Capital expenditure", "Total expenditure < Total receipts", "None"], "answer": "Revenue expenditure > Revenue receipts"},
      {"question": "Which of the following is a direct tax?", "options": ["Income Tax", "GST", "Customs duty", "Excise duty"], "answer": "Income Tax"},
      {"question": "Which measure is used to correct excess demand?", "options": ["Increase CRR", "Decrease tax", "Increase spending", "Reduce interest rates"], "answer": "Increase CRR"},
      {"question": "The situation where saving exceeds investment leads to?", "options": ["Deflationary gap", "Inflationary gap", "BOP surplus", "Budget deficit"], "answer": "Deflationary gap"},
      {"question": "Which of the following is not a function of money?", "options": ["Price control", "Store of value", "Unit of account", "Medium of exchange"], "answer": "Price control"}
    ],
    "Hard": [
      {"question": "What is the relationship between MPS and MPC?", "options": ["MPC + MPS = 1", "MPC - MPS = 1", "MPS × MPC = 1", "MPS = MPC"], "answer": "MPC + MPS = 1"},
      {"question": "Which of the following is a qualitative credit control measure?", "options": ["Moral suasion", "CRR", "Bank rate", "Repo rate"], "answer": "Moral suasion"},
      {"question": "Which of the following is not included in domestic income?", "options": ["Net factor income from abroad", "Operating surplus", "Compensation of employees", "Mixed income"], "answer": "Net factor income from abroad"},
      {"question": "Balanced budget multiplier is always equal to?", "options": ["1", "0", ">1", "<1"], "answer": "1"},
      {"question": "Which of the following is not a component of compensation of employees?", "options": ["Interest on loan", "Wages in cash", "Social security", "Bonuses"], "answer": "Interest on loan"},
      {"question": "An increase in investment leads to increase in output due to?", "options": ["Multiplier effect", "Inflation", "Substitution effect", "Law of diminishing returns"], "answer": "Multiplier effect"},
      {"question": "Which of the following is not a method of calculating national income?", "options": ["Inventory method", "Income method", "Expenditure method", "Production method"], "answer": "Inventory method"},
      {"question": "When is a good considered intermediate?", "options": ["Used in production of final good", "Consumed directly", "Sold to households", "Exported"], "answer": "Used in production of final good"},
      {"question": "Which body manages fiscal policy in India?", "options": ["Government of India", "RBI", "SEBI", "NITI Aayog"], "answer": "Government of India"},
      {"question": "Which situation represents full employment equilibrium?", "options": ["Aggregate demand = Aggregate supply at full employment", "Saving = Investment", "Imports = Exports", "Govt. expenditure = Tax revenue"], "answer": "Aggregate demand = Aggregate supply at full employment"}
    ]
  },
  "Political Science": {
    "Easy": [
      {"question": "Which article of the Indian Constitution defines the Union and its territory?", "options": ["Article 1", "Article 14", "Article 19", "Article 21"], "answer": "Article 1"},
      {"question": "Who is the head of the State in India?", "options": ["President", "Prime Minister", "Governor", "Chief Justice"], "answer": "President"},
      {"question": "What type of government does India have?", "options": ["Parliamentary democracy", "Presidential democracy", "Monarchy", "Military dictatorship"], "answer": "Parliamentary democracy"},
      {"question": "Which body is the highest law-making body in India?", "options": ["Parliament", "Supreme Court", "Rajya Sabha", "Lok Sabha"], "answer": "Parliament"},
      {"question": "How many members are nominated to the Rajya Sabha by the President?", "options": ["12", "10", "15", "20"], "answer": "12"},
      {"question": "Who appoints the Chief Justice of India?", "options": ["President", "Prime Minister", "Parliament", "Supreme Court"], "answer": "President"},
      {"question": "What is the minimum age to become the President of India?", "options": ["35 years", "30 years", "25 years", "40 years"], "answer": "35 years"},
      {"question": "Who presides over the meetings of the Lok Sabha?", "options": ["Speaker", "President", "Prime Minister", "Deputy Speaker"], "answer": "Speaker"},
      {"question": "What is the term of the Lok Sabha?", "options": ["5 years", "6 years", "4 years", "3 years"], "answer": "5 years"},
      {"question": "Which part of the Constitution deals with Fundamental Rights?", "options": ["Part III", "Part IV", "Part II", "Part VI"], "answer": "Part III"}
    ],
    "Medium": [
      {"question": "Which amendment introduced the Goods and Services Tax (GST)?", "options": ["101st Amendment", "42nd Amendment", "44th Amendment", "73rd Amendment"], "answer": "101st Amendment"},
      {"question": "What is the minimum age to become a Member of Lok Sabha?", "options": ["25 years", "30 years", "35 years", "40 years"], "answer": "25 years"},
      {"question": "Which article provides for the Right to Constitutional Remedies?", "options": ["Article 32", "Article 21", "Article 19", "Article 14"], "answer": "Article 32"},
      {"question": "Which body recommends the allocation of seats in the Lok Sabha to various states?", "options": ["Delimitation Commission", "Election Commission", "Supreme Court", "Parliament"], "answer": "Delimitation Commission"},
      {"question": "Who has the power to dissolve the Lok Sabha?", "options": ["President", "Prime Minister", "Supreme Court", "Parliament"], "answer": "President"},
      {"question": "What is the maximum strength of the Lok Sabha as per the Constitution?", "options": ["552", "545", "530", "560"], "answer": "552"},
      {"question": "Which Fundamental Right is known as the 'heart and soul' of the Indian Constitution?", "options": ["Right to Constitutional Remedies", "Right to Equality", "Right to Freedom", "Right against Exploitation"], "answer": "Right to Constitutional Remedies"},
      {"question": "Who can promulgate ordinances when Parliament is not in session?", "options": ["President", "Prime Minister", "Cabinet", "Chief Justice"], "answer": "President"},
      {"question": "Which article deals with the Directive Principles of State Policy?", "options": ["Part IV", "Part III", "Part V", "Part VI"], "answer": "Part IV"},
      {"question": "Which of the following is NOT a feature of Indian Federalism?", "options": ["Division of powers", "Single citizenship", "Double citizenship", "Independent judiciary"], "answer": "Double citizenship"}
    ],
    "Hard": [
      {"question": "Which case is famous for the Basic Structure doctrine of the Constitution?", "options": ["Kesavananda Bharati", "Golaknath", "Maneka Gandhi", "Minerva Mills"], "answer": "Kesavananda Bharati"},
      {"question": "Who was the first Deputy Prime Minister of India?", "options": ["Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Lal Bahadur Shastri", "Rajendra Prasad"], "answer": "Sardar Vallabhbhai Patel"},
      {"question": "Which article of the Constitution deals with Emergency Provisions?", "options": ["Article 352", "Article 370", "Article 356", "Article 365"], "answer": "Article 352"},
      {"question": "Which schedule of the Constitution deals with the allocation of powers and responsibilities between Union and States?", "options": ["7th Schedule", "5th Schedule", "6th Schedule", "4th Schedule"], "answer": "7th Schedule"},
      {"question": "Who appoints the Governors of the States?", "options": ["President", "Prime Minister", "Chief Minister", "Parliament"], "answer": "President"},
      {"question": "What is the tenure of a member of the Rajya Sabha?", "options": ["6 years", "5 years", "4 years", "3 years"], "answer": "6 years"},
      {"question": "Which article allows the Parliament to amend the Constitution?", "options": ["Article 368", "Article 356", "Article 370", "Article 352"], "answer": "Article 368"},
      {"question": "The principle of Separation of Powers was given by?", "options": ["Montesquieu", "Rousseau", "Locke", "Hobbes"], "answer": "Montesquieu"},
      {"question": "Which amendment gave constitutional status to Panchayati Raj Institutions?", "options": ["73rd Amendment", "42nd Amendment", "44th Amendment", "52nd Amendment"], "answer": "73rd Amendment"},
      {"question": "Which writ means 'to produce the body' before the court?", "options": ["Habeas Corpus", "Mandamus", "Prohibition", "Certiorari"], "answer": "Habeas Corpus"}
    ]
  },
  "Geography": {
    "Easy": [
      {"question": "Which one of the following is the largest continent by area?", "options": ["Asia", "Africa", "Europe", "Australia"], "answer": "Asia"},
      {"question": "What is the capital of India?", "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "New Delhi"},
      {"question": "Which soil type is most suitable for rice cultivation?", "options": ["Alluvial soil", "Red soil", "Black soil", "Laterite soil"], "answer": "Alluvial soil"},
      {"question": "Which ocean is the largest in the world?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},
      {"question": "Which is the longest river in India?", "options": ["Ganga", "Yamuna", "Brahmaputra", "Godavari"], "answer": "Ganga"},
      {"question": "Which mountain range forms the northern boundary of India?", "options": ["Himalayas", "Aravallis", "Vindhyas", "Satpuras"], "answer": "Himalayas"},
      {"question": "What is the main cause of earthquakes?", "options": ["Movement of tectonic plates", "Heavy rainfall", "Volcanic eruption", "Wind erosion"], "answer": "Movement of tectonic plates"},
      {"question": "Which of the following is a cold desert?", "options": ["Ladakh", "Thar", "Kutch", "Rann of Kachchh"], "answer": "Ladakh"},
      {"question": "Which crop is known as the ‘King of Spices’?", "options": ["Pepper", "Cardamom", "Clove", "Cinnamon"], "answer": "Pepper"},
      {"question": "Which type of climate does India have?", "options": ["Tropical monsoon", "Mediterranean", "Desert", "Temperate"], "answer": "Tropical monsoon"}
    ],
    "Medium": [
      {"question": "Which soil is called ‘Regur’ soil?", "options": ["Black soil", "Red soil", "Alluvial soil", "Laterite soil"], "answer": "Black soil"},
      {"question": "Which state in India receives the highest rainfall?", "options": ["Meghalaya", "Kerala", "Assam", "West Bengal"], "answer": "Meghalaya"},
      {"question": "The Deccan Plateau is made up of which type of rock?", "options": ["Igneous rock", "Sedimentary rock", "Metamorphic rock", "Alluvial rock"], "answer": "Igneous rock"},
      {"question": "Which of the following rivers does NOT flow into the Bay of Bengal?", "options": ["Narmada", "Godavari", "Mahanadi", "Krishna"], "answer": "Narmada"},
      {"question": "Which type of vegetation is found in the tropical rainforests of India?", "options": ["Evergreen", "Deciduous", "Coniferous", "Scrub"], "answer": "Evergreen"},
      {"question": "The term 'El Niño' is associated with which natural phenomenon?", "options": ["Ocean currents", "Earthquakes", "Volcanic eruptions", "Cyclones"], "answer": "Ocean currents"},
      {"question": "Which state is the largest producer of tea in India?", "options": ["Assam", "West Bengal", "Kerala", "Tamil Nadu"], "answer": "Assam"},
      {"question": "Which city is known as the ‘Salt City’ of India?", "options": ["Bhavnagar", "Kutch", "Gandhinagar", "Surat"], "answer": "Bhavnagar"},
      {"question": "Which of these is a cold ocean current?", "options": ["California current", "Gulf Stream", "Kuroshio current", "Brazil current"], "answer": "California current"},
      {"question": "The Thar Desert is located in which Indian state?", "options": ["Rajasthan", "Gujarat", "Haryana", "Punjab"], "answer": "Rajasthan"}
    ],
    "Hard": [
      {"question": "Which of the following is NOT a part of the Himalayas?", "options": ["Pir Panjal", "Zaskar", "Vindhya", "Karakoram"], "answer": "Vindhya"},
      {"question": "Which river originates from Amarkantak?", "options": ["Narmada", "Tungabhadra", "Godavari", "Mahanadi"], "answer": "Narmada"},
      {"question": "Which soil is rich in iron and aluminium but poor in nitrogen and phosphorus?", "options": ["Laterite soil", "Alluvial soil", "Black soil", "Red soil"], "answer": "Laterite soil"},
      {"question": "The Western Ghats are older than the Himalayas because they belong to which geological period?", "options": ["Precambrian", "Tertiary", "Quaternary", "Secondary"], "answer": "Precambrian"},
      {"question": "Which Indian state has the highest forest cover?", "options": ["Madhya Pradesh", "Arunachal Pradesh", "Maharashtra", "Odisha"], "answer": "Madhya Pradesh"},
      {"question": "Which river basin covers parts of three states and drains into the Arabian Sea?", "options": ["Tapi", "Ganga", "Brahmaputra", "Godavari"], "answer": "Tapi"},
      {"question": "Which of these minerals is NOT commonly found in the Indian subcontinent?", "options": ["Bauxite", "Gold", "Diamond", "Quartz"], "answer": "Quartz"},
      {"question": "Which tectonic plate is the Indian plate colliding with?", "options": ["Eurasian Plate", "African Plate", "Pacific Plate", "Australian Plate"], "answer": "Eurasian Plate"},
      {"question": "Which of the following lakes is a saltwater lake?", "options": ["Chilika Lake", "Dal Lake", "Wular Lake", "Pulicat Lake"], "answer": "Chilika Lake"},
      {"question": "Which of the following is NOT an example of a metamorphic rock?", "options": ["Marble", "Slate", "Granite", "Gneiss"], "answer": "Granite"}
    ]
  },
  "Sociology": {
    "Easy": [
      {"question": "What is sociology?", "options": ["Study of society", "Study of animals", "Study of plants", "Study of stars"], "answer": "Study of society"},
      {"question": "Who is known as the father of sociology?", "options": ["Auguste Comte", "Karl Marx", "Emile Durkheim", "Max Weber"], "answer": "Auguste Comte"},
      {"question": "Which term refers to the learned behavior of people in society?", "options": ["Culture", "Biology", "Instinct", "Nature"], "answer": "Culture"},
      {"question": "What is socialization?", "options": ["Learning social norms", "Eating food", "Sleeping", "Breathing"], "answer": "Learning social norms"},
      {"question": "Which institution is responsible for primary socialization?", "options": ["Family", "School", "Media", "Government"], "answer": "Family"},
      {"question": "What does 'norms' mean in sociology?", "options": ["Rules of society", "Random behavior", "Food habits", "Weather patterns"], "answer": "Rules of society"},
      {"question": "Which of the following is a formal social institution?", "options": ["School", "Friendship", "Family", "Language"], "answer": "School"},
      {"question": "What is the term for a group of people living in the same area?", "options": ["Community", "Family", "Class", "Caste"], "answer": "Community"},
      {"question": "Who studied the concept of 'class conflict'?", "options": ["Karl Marx", "Emile Durkheim", "Max Weber", "Herbert Spencer"], "answer": "Karl Marx"},
      {"question": "What is social change?", "options": ["Change in society", "Change in weather", "Change in culture", "Change in language"], "answer": "Change in society"}
    ],
    "Medium": [
      {"question": "Which term describes the division of society based on economic status?", "options": ["Social class", "Caste", "Race", "Ethnicity"], "answer": "Social class"},
      {"question": "What is 'patriarchy'?", "options": ["Male dominated society", "Female dominated society", "Child dominated society", "Elder dominated society"], "answer": "Male dominated society"},
      {"question": "Who introduced the concept of ‘Verstehen’ in sociology?", "options": ["Max Weber", "Karl Marx", "Emile Durkheim", "Auguste Comte"], "answer": "Max Weber"},
      {"question": "What is ‘anomie’ according to Durkheim?", "options": ["Breakdown of social norms", "Social harmony", "Family bonding", "Religious faith"], "answer": "Breakdown of social norms"},
      {"question": "Which of these is NOT a characteristic of caste system?", "options": ["Hereditary", "Endogamy", "Social mobility", "Purity and pollution"], "answer": "Social mobility"},
      {"question": "What is ‘social mobility’?", "options": ["Movement between social classes", "Movement of animals", "Economic growth", "Migration"], "answer": "Movement between social classes"},
      {"question": "What type of solidarity exists in traditional societies?", "options": ["Mechanical solidarity", "Organic solidarity", "Cultural solidarity", "Political solidarity"], "answer": "Mechanical solidarity"},
      {"question": "Which sociologist studied suicide?", "options": ["Emile Durkheim", "Karl Marx", "Max Weber", "Herbert Spencer"], "answer": "Emile Durkheim"},
      {"question": "What is ‘ethnocentrism’?", "options": ["Belief in superiority of one’s own culture", "Acceptance of all cultures", "Ignoring cultures", "Studying other cultures"], "answer": "Belief in superiority of one’s own culture"},
      {"question": "What is the primary focus of ‘functionalism’ in sociology?", "options": ["Society as a system of interrelated parts", "Class conflict", "Individual freedom", "Social change"], "answer": "Society as a system of interrelated parts"}
    ],
    "Hard": [
      {"question": "What is the ‘proletariat’ according to Karl Marx?", "options": ["Working class", "Capitalist class", "Landowners", "Politicians"], "answer": "Working class"},
      {"question": "Which sociologist introduced the concept of ‘ideal type’?", "options": ["Max Weber", "Emile Durkheim", "Karl Marx", "Talcott Parsons"], "answer": "Max Weber"},
      {"question": "What does ‘bureaucracy’ refer to?", "options": ["Formal organizational structure", "Family system", "Economic system", "Political party"], "answer": "Formal organizational structure"},
      {"question": "Which theory emphasizes the role of language and symbols in social interaction?", "options": ["Symbolic interactionism", "Structural functionalism", "Conflict theory", "Feminist theory"], "answer": "Symbolic interactionism"},
      {"question": "What is ‘social stratification’?", "options": ["Hierarchical arrangement of social groups", "Random grouping", "Cultural mixing", "Political alliance"], "answer": "Hierarchical arrangement of social groups"},
      {"question": "Who developed the ‘structural functionalism’ theory?", "options": ["Talcott Parsons", "Karl Marx", "Max Weber", "Emile Durkheim"], "answer": "Talcott Parsons"},
      {"question": "What does ‘alienation’ mean in Marxist theory?", "options": ["Separation from work and its products", "Social integration", "Economic success", "Political power"], "answer": "Separation from work and its products"},
      {"question": "What is ‘patrilineal descent’?", "options": ["Lineage traced through father", "Lineage traced through mother", "No lineage", "Mixed lineage"], "answer": "Lineage traced through father"},
      {"question": "What is the main theme of feminist theory?", "options": ["Gender inequality", "Class conflict", "Religious beliefs", "Economic development"], "answer": "Gender inequality"},
      {"question": "Which concept describes the process by which cultural traits spread from one society to another?", "options": ["Cultural diffusion", "Assimilation", "Acculturation", "Socialization"], "answer": "Cultural diffusion"}
    ]
  },
  "Psychology": {
    "Easy": [
      {"question": "What is Psychology?", "options": ["Study of mind and behavior", "Study of plants", "Study of stars", "Study of machines"], "answer": "Study of mind and behavior"},
      {"question": "Who is known as the father of Psychology?", "options": ["Wilhelm Wundt", "Sigmund Freud", "B.F. Skinner", "Jean Piaget"], "answer": "Wilhelm Wundt"},
      {"question": "What does 'cognition' refer to?", "options": ["Mental processes like thinking and memory", "Physical movement", "Eating habits", "Sleeping patterns"], "answer": "Mental processes like thinking and memory"},
      {"question": "What is 'learning' in Psychology?", "options": ["Permanent change in behavior due to experience", "Temporary mood change", "Biological growth", "Sleeping"], "answer": "Permanent change in behavior due to experience"},
      {"question": "Who proposed the theory of Classical Conditioning?", "options": ["Ivan Pavlov", "B.F. Skinner", "Jean Piaget", "Sigmund Freud"], "answer": "Ivan Pavlov"},
      {"question": "What is ‘intelligence’?", "options": ["Ability to learn and solve problems", "Physical strength", "Height", "Speed"], "answer": "Ability to learn and solve problems"},
      {"question": "What is the primary focus of developmental psychology?", "options": ["Human growth and development", "Plants growth", "Animal behavior", "Weather changes"], "answer": "Human growth and development"},
      {"question": "What is 'motivation'?", "options": ["Process that initiates and directs behavior", "Eating food", "Sleeping", "Walking"], "answer": "Process that initiates and directs behavior"},
      {"question": "Who developed the Psychoanalytic theory?", "options": ["Sigmund Freud", "Wilhelm Wundt", "Ivan Pavlov", "B.F. Skinner"], "answer": "Sigmund Freud"},
      {"question": "What is ‘perception’?", "options": ["Process of organizing sensory information", "Sleeping", "Eating", "Running"], "answer": "Process of organizing sensory information"}
    ],
    "Medium": [
      {"question": "What are the three components of attitude?", "options": ["Cognitive, affective, behavioral", "Physical, mental, emotional", "Positive, negative, neutral", "Happy, sad, angry"], "answer": "Cognitive, affective, behavioral"},
      {"question": "Which stage in Piaget’s theory involves logical thinking about concrete events?", "options": ["Concrete operational", "Sensorimotor", "Formal operational", "Preoperational"], "answer": "Concrete operational"},
      {"question": "What does ‘observational learning’ mean?", "options": ["Learning by watching others", "Learning by trial and error", "Learning by punishment", "Learning by reinforcement"], "answer": "Learning by watching others"},
      {"question": "What is ‘memory’?", "options": ["Process of encoding, storing, and retrieving information", "Forgetting information", "Sleeping", "Physical activity"], "answer": "Process of encoding, storing, and retrieving information"},
      {"question": "Who proposed the hierarchy of needs?", "options": ["Abraham Maslow", "Carl Rogers", "B.F. Skinner", "Jean Piaget"], "answer": "Abraham Maslow"},
      {"question": "What is the main focus of humanistic psychology?", "options": ["Human potential and self-actualization", "Behavioral conditioning", "Psychoanalysis", "Cognitive development"], "answer": "Human potential and self-actualization"},
      {"question": "What does ‘defense mechanism’ do?", "options": ["Protects ego from anxiety", "Causes anxiety", "Increases motivation", "Improves memory"], "answer": "Protects ego from anxiety"},
      {"question": "Which part of the brain controls voluntary movements?", "options": ["Motor cortex", "Occipital lobe", "Temporal lobe", "Cerebellum"], "answer": "Motor cortex"},
      {"question": "What is the term for the tendency to remember the first and last items in a list better?", "options": ["Serial position effect", "Recency effect", "Primacy effect", "Chunking"], "answer": "Serial position effect"},
      {"question": "What is ‘personality’?", "options": ["Unique and consistent patterns of behavior and thoughts", "Temporary mood", "Physical appearance", "Height"], "answer": "Unique and consistent patterns of behavior and thoughts"}
    ],
    "Hard": [
      {"question": "What is the ‘id’ in Freud’s personality theory?", "options": ["Primitive and instinctual part", "Rational part", "Moral conscience", "Social self"], "answer": "Primitive and instinctual part"},
      {"question": "What is ‘operant conditioning’?", "options": ["Learning through consequences of behavior", "Learning by association", "Learning by observation", "Innate learning"], "answer": "Learning through consequences of behavior"},
      {"question": "Which test is commonly used to assess intelligence?", "options": ["IQ test", "Rorschach test", "TAT", "MMPI"], "answer": "IQ test"},
      {"question": "What is ‘cognitive dissonance’?", "options": ["Mental discomfort from holding contradictory beliefs", "Feeling happy", "Good memory", "Lack of motivation"], "answer": "Mental discomfort from holding contradictory beliefs"},
      {"question": "Who developed the stages of psychosocial development?", "options": ["Erik Erikson", "Jean Piaget", "Sigmund Freud", "B.F. Skinner"], "answer": "Erik Erikson"},
      {"question": "What is the main idea of the ‘Gestalt’ psychology?", "options": ["The whole is greater than the sum of its parts", "Learning by conditioning", "Psychoanalysis", "Behaviorism"], "answer": "The whole is greater than the sum of its parts"},
      {"question": "What is ‘schema’ in cognitive psychology?", "options": ["Mental framework for organizing information", "Memory loss", "Physical reflex", "Emotional response"], "answer": "Mental framework for organizing information"},
      {"question": "Which part of the brain is involved in emotions?", "options": ["Limbic system", "Cerebellum", "Occipital lobe", "Parietal lobe"], "answer": "Limbic system"},
      {"question": "What is ‘learned helplessness’?", "options": ["Condition where a person feels unable to control events", "High motivation", "Good memory", "Positive reinforcement"], "answer": "Condition where a person feels unable to control events"},
      {"question": "Which psychologist is associated with the ‘Little Albert’ experiment?", "options": ["John B. Watson", "B.F. Skinner", "Ivan Pavlov", "Carl Rogers"], "answer": "John B. Watson"}
    ]
  },
  "Geography": {
    "Easy": [
      {"question": "Which is the longest river in India?", "options": ["Ganga", "Yamuna", "Godavari", "Brahmaputra"], "answer": "Ganga"},
      {"question": "The Tropic of Cancer passes through which Indian state?", "options": ["Madhya Pradesh", "Rajasthan", "Gujarat", "Assam"], "answer": "Rajasthan"},
      {"question": "What type of climate does India mostly have?", "options": ["Tropical", "Arctic", "Desert", "Temperate"], "answer": "Tropical"},
      {"question": "Which is the highest peak in India?", "options": ["Kanchenjunga", "Nanda Devi", "Mount Everest", "Annapurna"], "answer": "Kanchenjunga"},
      {"question": "Which ocean lies to the south of India?", "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "answer": "Indian Ocean"},
      {"question": "What is the primary source of the Ganga river?", "options": ["Gangotri Glacier", "Yamunotri Glacier", "Pindari Glacier", "Siachen Glacier"], "answer": "Gangotri Glacier"},
      {"question": "Which of these is a major desert in India?", "options": ["Thar Desert", "Sahara Desert", "Gobi Desert", "Kalahari Desert"], "answer": "Thar Desert"},
      {"question": "The Western Ghats are located along which coast?", "options": ["West coast", "East coast", "North coast", "South coast"], "answer": "West coast"},
      {"question": "Which is the largest delta in India?", "options": ["Sundarbans", "Godavari", "Mahanadi", "Krishna"], "answer": "Sundarbans"},
      {"question": "Which soil type is found mostly in the river valleys and delta regions?", "options": ["Alluvial soil", "Black soil", "Red soil", "Laterite soil"], "answer": "Alluvial soil"}
    ],
    "Medium": [
      {"question": "Which of the following rivers does NOT originate from the Himalayas?", "options": ["Mahanadi", "Ganga", "Yamuna", "Saraswati"], "answer": "Mahanadi"},
      {"question": "The Deccan Plateau is mainly composed of which rock type?", "options": ["Basalt", "Granite", "Limestone", "Sandstone"], "answer": "Basalt"},
      {"question": "Which wind is responsible for the Indian monsoon?", "options": ["Southwest monsoon", "Northeast monsoon", "Western disturbances", "Trade winds"], "answer": "Southwest monsoon"},
      {"question": "Which crop is predominantly grown in black soil regions?", "options": ["Cotton", "Wheat", "Rice", "Sugarcane"], "answer": "Cotton"},
      {"question": "Which mountain range separates India from China?", "options": ["Himalayas", "Aravalli", "Vindhya", "Satpura"], "answer": "Himalayas"},
      {"question": "The Thar Desert is primarily spread across which two Indian states?", "options": ["Rajasthan and Gujarat", "Rajasthan and Punjab", "Punjab and Haryana", "Maharashtra and Gujarat"], "answer": "Rajasthan and Gujarat"},
      {"question": "Which of the following is NOT a major port in India?", "options": ["Mumbai", "Kolkata", "Chennai", "Hyderabad"], "answer": "Hyderabad"},
      {"question": "Which part of India receives the highest rainfall?", "options": ["Cherrapunji", "Delhi", "Jaipur", "Mumbai"], "answer": "Cherrapunji"},
      {"question": "Which of the following is the main reason for the formation of the Western Ghats?", "options": ["Volcanic activity", "Tectonic uplift", "Erosion", "Sedimentation"], "answer": "Tectonic uplift"},
      {"question": "Which soil is known as 'Regur' soil?", "options": ["Black soil", "Alluvial soil", "Red soil", "Laterite soil"], "answer": "Black soil"}
    ],
    "Hard": [
      {"question": "What causes the seasonal reversal of winds in India?", "options": ["Differential heating of land and sea", "Earth's rotation", "Mountain barriers", "Tidal forces"], "answer": "Differential heating of land and sea"},
      {"question": "Which geological era saw the formation of the Himalayas?", "options": ["Tertiary", "Secondary", "Primary", "Quaternary"], "answer": "Tertiary"},
      {"question": "Which of the following is a major factor influencing soil formation in India?", "options": ["Climate", "Latitude", "Longitude", "Altitude"], "answer": "Climate"},
      {"question": "What is the term for the rain-bearing winds that blow from the Bay of Bengal during the retreating monsoon?", "options": ["Northeast monsoon", "Southwest monsoon", "Western disturbances", "Trade winds"], "answer": "Northeast monsoon"},
      {"question": "Which Indian state has the largest area under forest cover?", "options": ["Madhya Pradesh", "Maharashtra", "Arunachal Pradesh", "Uttarakhand"], "answer": "Madhya Pradesh"},
      {"question": "Which rock type is most commonly found in the Peninsular Plateau?", "options": ["Igneous and metamorphic", "Sedimentary", "Volcanic", "Alluvial"], "answer": "Igneous and metamorphic"},
      {"question": "Which river system in India is considered the oldest?", "options": ["Narmada", "Ganga", "Yamuna", "Godavari"], "answer": "Narmada"},
      {"question": "What is the main reason for the fertility of alluvial soil?", "options": ["Presence of fine particles and minerals", "High sand content", "Low moisture retention", "High acidity"], "answer": "Presence of fine particles and minerals"},
      {"question": "Which type of farming is practiced in the Himalayan region?", "options": ["Terrace farming", "Shifting cultivation", "Commercial farming", "Plantation farming"], "answer": "Terrace farming"},
      {"question": "Which climatic region of India is characterized by hot and dry summers and mild winters?", "options": ["Tropical desert", "Tropical wet", "Temperate", "Mountain"], "answer": "Tropical desert"}
    ]
  },
  "Political Science": {
    "Easy": [
      {"question": "Which body is the guardian of the Indian Constitution?", "options": ["Supreme Court", "Parliament", "President", "Prime Minister"], "answer": "Supreme Court"},
      {"question": "India adopted its Constitution on?", "options": ["26 January 1950", "15 August 1947", "2 October 1949", "26 November 1950"], "answer": "26 January 1950"},
      {"question": "Which event led to the declaration of Emergency in 1975?", "options": ["Allahabad High Court judgment", "War with Pakistan", "Economic crisis", "Parliament deadlock"], "answer": "Allahabad High Court judgment"},
      {"question": "Which country follows the policy of non-alignment with military blocs?", "options": ["India", "USA", "Russia", "China"], "answer": "India"},
      {"question": "Who was the first Prime Minister of independent India?", "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhash Chandra Bose"], "answer": "Jawaharlal Nehru"},
      {"question": "What does the term 'coalition government' mean?", "options": ["Alliance of parties", "Single-party rule", "Military rule", "Judicial government"], "answer": "Alliance of parties"},
      {"question": "The Panchayati Raj system was introduced through which amendment?", "options": ["73rd", "42nd", "44th", "86th"], "answer": "73rd"},
      {"question": "Who appoints the Chief Election Commissioner?", "options": ["President", "Prime Minister", "Parliament", "Supreme Court"], "answer": "President"},
      {"question": "Which organization was formed in 1945 to promote peace?", "options": ["UNO", "NATO", "SEATO", "SAARC"], "answer": "UNO"},
      {"question": "Which article of the Indian Constitution deals with Fundamental Rights?", "options": ["Article 12 to 35", "Article 36 to 51", "Article 1 to 11", "Article 51 to 60"], "answer": "Article 12 to 35"}
    ],
    "Medium": [
      {"question": "Who led the Chipko Movement in the 1970s?", "options": ["Sunderlal Bahuguna", "Medha Patkar", "Anna Hazare", "Vinoba Bhave"], "answer": "Sunderlal Bahuguna"},
      {"question": "Which party emerged as a national alternative to Congress in 1977?", "options": ["Janata Party", "BJP", "Left Front", "DMK"], "answer": "Janata Party"},
      {"question": "Which Indian Prime Minister signed the Shimla Agreement in 1972?", "options": ["Indira Gandhi", "Rajiv Gandhi", "Morarji Desai", "Narasimha Rao"], "answer": "Indira Gandhi"},
      {"question": "What does NAM stand for?", "options": ["Non-Aligned Movement", "National Armed Movement", "Non-Aggression Movement", "National Alliance for Media"], "answer": "Non-Aligned Movement"},
      {"question": "Which region was granted special status under Article 370 (till 2019)?", "options": ["Jammu & Kashmir", "Punjab", "Assam", "Nagaland"], "answer": "Jammu & Kashmir"},
      {"question": "Which body ensures free and fair elections in India?", "options": ["Election Commission", "Supreme Court", "Lok Sabha", "President"], "answer": "Election Commission"},
      {"question": "Who was the main architect of India’s foreign policy after independence?", "options": ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Sardar Patel", "Lal Bahadur Shastri"], "answer": "Jawaharlal Nehru"},
      {"question": "What was the main aim of the Green Revolution?", "options": ["Increase agricultural production", "Promote trade", "Industrialization", "Urbanization"], "answer": "Increase agricultural production"},
      {"question": "Which war led to the creation of Bangladesh in 1971?", "options": ["India-Pakistan War", "India-China War", "Kargil War", "World War II"], "answer": "India-Pakistan War"},
      {"question": "Which movement opposed the Mandal Commission recommendations?", "options": ["Anti-reservation movement", "Narmada Bachao Andolan", "Bhoodan Movement", "Chipko Movement"], "answer": "Anti-reservation movement"}
    ],
    "Hard": [
      {"question": "What is the meaning of 'Bipolar world' in international relations?", "options": ["Two superpowers dominating the world", "Two governments in a country", "Dual citizenship", "Two-party democracy"], "answer": "Two superpowers dominating the world"},
      {"question": "Which international organization replaced GATT in 1995?", "options": ["WTO", "IMF", "World Bank", "UNCTAD"], "answer": "WTO"},
      {"question": "What was the objective of the 'Operation Enduring Freedom' launched by the USA?", "options": ["Combat terrorism in Afghanistan", "Rebuild Iraq", "Destroy nuclear weapons", "Promote democracy"], "answer": "Combat terrorism in Afghanistan"},
      {"question": "Which of the following countries is not a permanent member of the UN Security Council?", "options": ["India", "Russia", "China", "France"], "answer": "India"},
      {"question": "Which economic policy was introduced in India in 1991?", "options": ["Liberalisation, Privatisation, Globalisation (LPG)", "Green Revolution", "Five-Year Plans", "Industrial Policy Resolution"], "answer": "Liberalisation, Privatisation, Globalisation (LPG)"},
      {"question": "Which principle of India’s foreign policy means peaceful coexistence?", "options": ["Panchsheel", "NAM", "SAARC", "Look East"], "answer": "Panchsheel"},
      {"question": "What was the purpose of the Tashkent Agreement?", "options": ["Peace between India and Pakistan (1965 war)", "Nuclear treaty", "Free trade agreement", "Military alliance"], "answer": "Peace between India and Pakistan (1965 war)"},
      {"question": "Who was the first woman Prime Minister of India?", "options": ["Indira Gandhi", "Sarojini Naidu", "Pratibha Patil", "Meira Kumar"], "answer": "Indira Gandhi"},
      {"question": "Which theory of international politics assumes states act in their own interest?", "options": ["Realism", "Idealism", "Constructivism", "Marxism"], "answer": "Realism"},
      {"question": "Which Prime Minister launched the 20-point programme during Emergency?", "options": ["Indira Gandhi", "Rajiv Gandhi", "Morarji Desai", "Lal Bahadur Shastri"], "answer": "Indira Gandhi"}
    ]
  },
  "IP": {
    "Easy": [
      {"question": "Which of the following is a valid Python data type?", "options": ["integer", "number", "character", "digit"], "answer": "integer"},
      {"question": "What does RAM stand for?", "options": ["Random Access Memory", "Read And Modify", "Remote Access Module", "Run Access Mode"], "answer": "Random Access Memory"},
      {"question": "Which symbol is used for comments in Python?", "options": ["#", "//", "/*", "%"], "answer": "#"},
      {"question": "Which operator is used for exponentiation in Python?", "options": ["^", "**", "//", "%%"], "answer": "**"},
      {"question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "define", "fun"], "answer": "def"},
      {"question": "What is the extension of a Python file?", "options": [".py", ".pt", ".python", ".exe"], "answer": ".py"},
      {"question": "Which of the following is not a loop in Python?", "options": ["for", "while", "do-while", "None of these"], "answer": "do-while"},
      {"question": "Which keyword is used to exit a loop?", "options": ["break", "exit", "continue", "stop"], "answer": "break"},
      {"question": "Which method is used to add an element at the end of a list?", "options": ["add()", "append()", "insert()", "push()"], "answer": "append()"},
      {"question": "Which of the following is a valid variable name?", "options": ["my-var", "2value", "value_2", "class"], "answer": "value_2"}
    ],
    "Medium": [
      {"question": "Which data structure uses FIFO method?", "options": ["Stack", "Queue", "Tree", "List"], "answer": "Queue"},
      {"question": "Which keyword is used to handle exceptions in Python?", "options": ["catch", "error", "except", "tryexcept"], "answer": "except"},
      {"question": "What does CSV stand for?", "options": ["Comma Separated Values", "Computer Standard Values", "Column Separator View", "Common Symbol Version"], "answer": "Comma Separated Values"},
      {"question": "Which of the following is used to open a file in read mode?", "options": ["open(file, 'r')", "read(file)", "file.read()", "open('read', file)"], "answer": "open(file, 'r')"},
      {"question": "Which module in Python is used for database connectivity with MySQL?", "options": ["mysql.connector", "pymysql", "dbconnect", "sqlpython"], "answer": "mysql.connector"},
      {"question": "What is the output of: len({'a':1, 'b':2})?", "options": ["2", "1", "3", "0"], "answer": "2"},
      {"question": "Which method is used to fetch all rows from MySQL query result?", "options": ["fetch()", "fetchone()", "fetchall()", "select()"], "answer": "fetchall()"},
      {"question": "Which protocol is used for sending emails?", "options": ["SMTP", "HTTP", "FTP", "POP3"], "answer": "SMTP"},
      {"question": "What is the default port for MySQL?", "options": ["3306", "8080", "1433", "1521"], "answer": "3306"},
      {"question": "Which of these is not a valid data type in SQL?", "options": ["VARCHAR", "INTEGER", "DATE", "STRING"], "answer": "STRING"}
    ],
    "Hard": [
      {"question": "Which method is used to remove a specific item from a list in Python?", "options": ["remove()", "pop()", "delete()", "discard()"], "answer": "remove()"},
      {"question": "Which SQL command is used to modify existing records?", "options": ["UPDATE", "MODIFY", "CHANGE", "ALTER"], "answer": "UPDATE"},
      {"question": "In DBMS, which key uniquely identifies each record?", "options": ["Primary Key", "Foreign Key", "Candidate Key", "Super Key"], "answer": "Primary Key"},
      {"question": "Which Python function returns a sequence of numbers?", "options": ["range()", "number()", "sequence()", "set()"], "answer": "range()"},
      {"question": "Which command is used to view all tables in MySQL?", "options": ["SHOW TABLES;", "DISPLAY TABLES;", "SELECT *;", "TABLES();"], "answer": "SHOW TABLES;"},
      {"question": "Which of the following is not a type of cyber attack?", "options": ["Phishing", "SQL Injection", "DDoS", "JPEG Spoofing"], "answer": "JPEG Spoofing"},
      {"question": "Which term describes a system of interconnected computers?", "options": ["Network", "Server", "Database", "Web"], "answer": "Network"},
      {"question": "Which law relates to data privacy in India?", "options": ["IT Act 2000", "Privacy Act 2015", "Digital Safety Bill", "Cyberlaw 2022"], "answer": "IT Act 2000"},
      {"question": "Which method is used to commit a transaction in Python MySQL?", "options": ["commit()", "save()", "submit()", "apply()"], "answer": "commit()"},
      {"question": "Which part of computer handles all arithmetic and logical operations?", "options": ["ALU", "CU", "RAM", "ROM"], "answer": "ALU"}
    ]
  }
}

}



























































  























































    


    











    
    

