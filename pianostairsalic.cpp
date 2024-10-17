const int ldrPin = A0;      // Photoresistor connected to analog pin A0

void setup() {
  Serial.begin(9600);        // Start serial communication
}

void loop() {
  int ldrValue = analogRead(ldrPin);  // Read the LDR value
  Serial.println(ldrValue);            // Send value to Python
  delay(100);  // Short delay for stability
}


Use os.system(“afplay ” + {AUDIO}) instead of playsound.playsound({AUDIO})

