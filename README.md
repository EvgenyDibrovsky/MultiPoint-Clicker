# MultiPoint Clicker

## Description
**MultiPoint Clicker** is a utility designed to automate clicks in multiple locations across various applications. The clicker simulates multiple human-like clicks, making it versatile for a range of tasks, with an interface and settings that allow easy customization.

### Key Features
1. Supports multiple click points with precise configuration.
2. Natural human click simulation for realistic interactions.
3. Intuitive and user-friendly interface.
4. Customizable clickable area and functional hotkeys.

 
## Installation and Setup

1. **Clone the repository**
   - Open a terminal and run the following command to clone the repository:
     ```sh
     git clone https://github.com/EvgenyDibrovsky/MultiPoint-Clicker.git
     ```

2. **Navigate to the project directory**
   - Change to the cloned repository directory:
     ```sh
     cd MultiPoint-Clicker
     ```

3. **Create and activate a virtual environment (recommended)**
   - Create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```sh
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```sh
       source venv/bin/activate
       ```

4. **Install dependencies**
   - Install the necessary dependencies:
     ```sh
     pip install -r requirements.txt
     ```

5. **Run the application**
   - To launch the application, run the following command:
     ```sh
     python multipoint_clicker.py
     ```

### Running in an IDE

If you prefer using an IDE like PyCharm or VSCode:

1. **Open the project in your IDE**
   - Open your IDE and select the `MultiPoint-Clicker` project directory.

2. **Configure the interpreter**
   - Ensure your IDE is using the virtual environment you created earlier.

3. **Install dependencies in the IDE**
   - Use the IDE terminal or built-in package management tools to install dependencies from `requirements.txt`.

4. **Run the project**
   - Locate the `multipoint_clicker.py` file in the project explorer and run it.

### Compiling to an executable file (optional)

1. **Run PyInstaller**
   - Install PyInstaller if it's not already installed:
     ```sh
     pip install pyinstaller
     ```
   - Generate the executable file:
     ```sh
     pyinstaller multipoint_clicker.spec
     ```

2. **Find the executable**
   - After the build process is complete, the executable will be located in the `dist/multipoint_clicker` directory.

 
### 1. Launching the Application
- Open the MultiPoint Clicker.
- The main window will display several buttons for configuring and controlling the auto clicker.

### 2. Setting Click Points
- Click on each button to set the coordinates for each click point.
- A semi-transparent window will appear, allowing you to select the area where the click should occur.
- Once the points are set, the settings are saved automatically.

### 3. Starting the Auto Clicker
- Click the "Start Clicker" button or use the `Ctrl+Alt+S` hotkey to start.
- To pause or resume the clicker, press `Ctrl+Alt+S` again.

## Gratitude

If this project was helpful, you can support the developer by sending cryptocurrency to one of the wallets below.
 
| Cryptocurrency   | Address                                                                                     | QR Code                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Toncoin (TON)**  | `UQCmxDxpdR9q2cNkynVhRNxSo76qOAzhzu1IepB2VaTWV0gm`                                          | <img width="200" height="200" src="https://github.com/user-attachments/assets/6b24c941-bf20-4ab3-8bf1-8da8cc346511">                    |
| **Tether (USDT)**  | `0x320a80aa5842dab4e8375f426225de6b0a221ed3`                                          | <img width="200" height="200" src="https://github.com/user-attachments/assets/83320e17-e727-4a5a-8651-853dc061c691">                    |
