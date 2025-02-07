# **Code Crisis: 24HR Hackathon**  

## **Mission Briefing**  

Mingo, HCU's beloved mascot, has been trapped in a **glitched virtual snowstorm** inside a rogue AI simulation. To bring Mingo back to campus, your team must **hack into the simulation**, solve cryptographic challenges, map escape routes, and outsmart the AI before it erases Mingo forever.  

Your team will face **multiple security layers, unpredictable AI defenses, and time-sensitive challenges**. Each phase will push your problem-solving, coding, and hacking skills to the limit.  

If you **fail to complete all tasks within 24 hours**, the simulation will lock down permanently.  

---  

## **Phases of the Challenge**  

### **Phase 1: Breaking the AI’s First Defense (Cryptographic Challenge)**  

**GOAL:** Locate where Mingo is trapped by decoding a corrupted distress signal intercepted from the AI.  

**CHALLENGE:** The signal is encoded **not just in a basic Caesar Cipher but also in hexadecimal**. You must **first reverse the hexadecimal encoding**, then shift the decrypted text using a Caesar Cipher, you will have to figure out the shift key.  

**Phase 1 Task:** Write a Python script that:  
1. Reads `message.txt` (which contains encrypted hexadecimal message).  
2. **Converts the hexadecimal string into plaintext**.  
3. Decodes the plaintext using a **Caesar Cipher with a shift of X** to retrieve the final message.
4. Outputs the **name  of Mingo’s first location.**

💡 **Hint:** Use Python's bytes.fromhex() method or a similar function (i.e. look at the codecs Python library) to decode the hexadecimal.

---

### **Phase 2: Hacking the Virtual Map**  

**GOAL:** Visualize where Mingo is trapped inside the AI simulation.  

**CHALLENGE:** The AI has tampered with the map. Some locations are **incorrectly marked, and the real coordinates are off by a few digits**. Your task is to write a script to:  
1. **Validate the coordinates** from Phase 1 using an external API (like OpenStreetMap or Google Maps API). *See the hint for help on how to get the latitude and longitude of the location from Phase 1.*  
2. **Correct any coordinate errors** by cross-checking them with real-world locations.  
3. **Render the correct location on a map** using Folium, Matplotlib, or any other mapping tool.  

💡 **Hint:** Taking the name of the location from Phase 1, you can find the latitude and longitude by going to google.com/maps and dropping a pin (by clicking on the building) and then right clicking to get the location information.

🔹 **Bonus:** Add interactive zoom and a pop-up label explaining the location.  

---

### **Phase 3: AI Logic Firewall (Dynamic Puzzle Solver)**  

**GOAL:** Solve riddles left by the AI to reveal Mingo’s escape route.  

**CHALLENGE:** The AI is **not static**. It generates **randomized riddles** from a provided JSON file. Your script must:  
1. Parse `riddles.json`.  
2. Allow the user to input answers interactively.  
3. If correct, extract the **third letter of each answer**, rearrange them to spell out a word and put it in the given token website (included in the instruction website).  

💡 **Hint:** Implement some form of input consistency. Look at the `riddles.json` file, and see the format of the answers. When taking the user's input, design your script so that every possible answer is normalized/looks the same as the value in the key-value pairs in the `.json` file. *Look at string handling methods in Python.*

💡 **Hint:** The token website code is case sensitive, so "Hello" != "hello". 

🔹 **Bonus:** Implement **Levenshtein Distance** to allow for minor typos in answers.  

---

### **Phase 4: Navigating the Snowstorm (Pathfinding Challenge)**  

**GOAL:** Map out a safe path for Mingo while avoiding **AI-generated obstacles**.  

**CHALLENGE:** The snowstorm is **not static**—it generates new hazards dynamically. Your script must:  
1. Take **two sets of coordinates** (from Phase 2 and Phase 3).  
2. Generate **multiple possible paths** and check for obstacles.  
3. Use **A* (A-star) pathfinding** or another algorithm to **find the safest route**.  
4. Display the optimal path **on a map**.  

🔹 **Bonus:** Animate the path on the map.  

---

### **Phase 5: AI Security Lockdown (Decryption & Reverse Engineering)**  

**GOAL:** The AI has encrypted Mingo’s final escape instructions. You must **decrypt them before time runs out**.  

**CHALLENGE:** The AI has encoded the message as a binary string. Your task is to:  
1. **Read** `decrypt.txt`, which contains the encrypted binary data (e.g., `0100100001100101011011000110110001101111`).  
2. Convert the binary string to ASCII characters to retrieve plaintext instructions.  
3. Display the **decoded rescue instructions** and FIND MINGO!
4. Insert the location of Mingo from his message in the token website. *Remember: the website is case sensitive!*

💡 **Hint:** Use Python’s `int(binary_string, 2)` method to convert binary to integers.

---

### **Phase 6: Final Challenge – The AI Showdown**  

**GOAL:** Use all your previous solutions to execute the **final rescue operation** and bring Mingo back.  

**FINAL TASK:** Write a Python script that:  
✅ **Integrates** all the previous scripts into a single, seamless workflow.  
✅ **Automatically executes** each phase in order.  
✅ **Prints the final decryption result**   
✅ **After getting the Google Form link from the token website, submit your team's answer!**   


🔹 **Bonus:** Implement **error handling** so that if one phase fails, it **doesn’t crash the whole script**—instead, it provides hints on what went wrong.  

---

## **Scoring System**  

Each phase is worth a certain number of points, **but efficiency and creativity will be rewarded**:  
- **Basic completion** of a phase = 10 points.  
- **Optimization (e.g., best algorithm choice, clean code, etc.)** = +5 points.  
- **Advanced features (e.g., interactivity, animations, etc.)** = +10 points.  
- **Creative solutions (e.g., alternative encryption techniques, custom pathfinding algorithms, AI-generated maps)** = +15 points.  

Total possible points: **100+**  

---

## **Rules & Guidelines**  

1. **Collaboration is encouraged, but each team must submit their own unique solutions.**  
2. **Using AI (ChatGPT, Claude, Gemini, etc.) is allowed, but all AI-generated code must be cited in comments.**  
3. **StackOverflow and other online resources are fair game, but copied code must be cited.**  
4. **Suspected AI-generated work without citation will lead to point deductions or disqualification.**  

---

## **Resources**  

- **Caesar & XOR Cipher:** [GeeksforGeeks](https://www.geeksforgeeks.org/xor-cipher/)  
- **Mapping Libraries:** [Python Mapping Libraries](https://medium.com/@alexroz/6-python-libraries-to-make-beautiful-maps-9fb9edb28b27)  
- **Pathfinding Algorithms:** [A* Algorithm in Python](https://www.redblobgames.com/pathfinding/a-star/introduction.html)  
- **Google Maps Finding Lat and Long:** [Google Maps Help](https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop#:~:text=Get%20the%20coordinates%20of%20a,and%20longitude%20in%20decimal%20format.)
- HCU Map (included in the instruction set sent)

---

## **Final Words**  

This isn’t just a coding competition—it’s a **battle against an AI**, a **race against time**, and a **test of creativity**. Will you outsmart the rogue simulation and save Mingo, or will he be lost in the snowstorm forever?  

The clock starts **NOW**. 🚀🔥  

